"""Build the Advanced-challenge index from the CCDR Vietnam PDF (Vietnamese).
 text  : PyMuPDF text layer, header/footer removed, paragraph-packed chunks (<=1000 chars)
 table/figure : chunks from adv/visual_notes.json (number glyphs of tables are scrambled in the text layer; charts/maps/diagrams are graphics)
Stores vectors in PostgreSQL+pgvector (table adv_chunks), embedding intfloat/multilingual-e5-small (384d)."""
import json, os, re, sys, hashlib, time
import pymupdf, psycopg
PDF = "adv/raw/ccdr_vi.pdf"; DOC = "ccdr-vn-2022"
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from rag.retrievers import DB_URL as DB  # DATABASE_URL comes from the git-ignored .env
CH = [(8, 13, 0, "Giới thiệu và phần mở đầu"), (14, 21, 1, "1. Mô hình phát triển của Việt Nam và những thách thức về khí hậu"),
      (22, 27, 2, "2. Khu vực công và khu vực tư nhân không được chuẩn bị đồng đều"), (28, 47, 3, "3. Thích ứng với biến đổi khí hậu"),
      (48, 75, 4, "4. Giảm thiểu biến đổi khí hậu"), (76, 81, 5, "5. Huy động tài chính"), (82, 90, 6, "6. Kết luận và khuyến nghị"),
      (91, 104, 7, "Phụ lục")]
def chap(p):
    for a, b, n, t in CH:
        if a <= p <= b: return n, t
    return None, None
HEAD = re.compile(r"^(Việt Nam: Báo cáo về Khí hậu và Phát triển\s*\|?|\|?\s*Việt Nam: Báo cáo về Khí hậu và Phát triển|\d{1,3})$")
def paras(t):
    lines = [l.strip() for l in t.split("\n")]
    lines = [l for l in lines if l and not HEAD.match(l)]
    out, cur = [], ""
    for l in lines:  # PDF hard-wraps lines: join; start a new paragraph after a sentence end followed by short line
        cur = (cur + " " + l).strip() if cur else l
        if re.search(r"[.:;!?)\]]$", l) and len(l) < 70: out.append(cur); cur = ""
    if cur: out.append(cur)
    return out
def pack(ps, limit=1000):
    out, cur = [], ""
    for p in ps:
        while len(p) > limit * 1.4:
            cut = p.rfind(". ", 0, limit); cut = cut + 1 if cut > 200 else limit
            if cur: out.append(cur); cur = ""
            out.append(p[:cut].strip()); p = p[cut:].strip()
        if cur and len(cur) + len(p) + 1 > limit: out.append(cur); cur = p
        else: cur = (cur + " " + p).strip()
    if cur: out.append(cur)
    return out
def main(ingest=True):
    doc = pymupdf.open(PDF); chunks, skipped = [], []
    notes = json.load(open("adv/visual_notes.json"))["items"]
    for i, pg in enumerate(doc):
        n = i + 1
        if n < 8: skipped.append({"page": n, "reason": "cover/copyright/table of contents"}); continue
        t = pg.get_text()
        body = pack(paras(t))
        ch, title = chap(n)
        if sum(map(len, body)) < 150: skipped.append({"page": n, "reason": "<150 chars of text (photo/chapter opener/blank)"})
        for k, txt in enumerate(body):
            chunks.append({"id": f"{DOC}:p{n}:t{k}", "text": txt, "source_id": DOC, "source": "ccdr-vi.pdf", "page": n,
                           "metadata": {"chapter": ch, "chapter_title": title, "printed_page": n - 10 if n >= 11 else None, "chunk_type": "text"}})
    for k, it in enumerate(notes):
        ch, title = chap(it["page"])
        head = f"{it['figure_id']}: {it['title']}. "
        parts = pack(re.split(r"(?<=[.;])\s+", it["text"]), limit=900)  # keep each vector within the 512-token window of e5-small
        for j, part in enumerate(parts):
            chunks.append({"id": f"{DOC}:p{it['page']}:{'tb' if it['type']=='table' else 'fg'}{k}" + (f"{'abcdef'[j]}" if len(parts) > 1 else ""), "text": head + part, "source_id": DOC, "source": "ccdr-vi.pdf", "page": it["page"],
                           "metadata": {"chapter": ch, "chapter_title": title, "printed_page": it["page"] - 10, "chunk_type": it["type"], "figure_id": it["figure_id"]}})
    ids = [c["id"] for c in chunks]; assert len(ids) == len(set(ids))
    json.dump(chunks, open("adv/work/chunks.json", "w"), ensure_ascii=False)
    stats = {"chunks": len(chunks), "by_type": {t: sum(c["metadata"]["chunk_type"] == t for c in chunks) for t in ("text", "table", "figure")},
             "mean_chars_text": round(sum(len(c["text"]) for c in chunks if c["metadata"]["chunk_type"] == "text") / max(1, sum(c["metadata"]["chunk_type"] == "text" for c in chunks))),
             "pages_in_pdf": len(doc), "pages_indexed_with_content": len({c["page"] for c in chunks}), "skipped_pages": skipped}
    print(json.dumps({k: v for k, v in stats.items() if k != "skipped_pages"}), "skipped:", [s["page"] for s in skipped])
    if not ingest: return
    from sentence_transformers import SentenceTransformer
    m = SentenceTransformer("intfloat/multilingual-e5-small", device="cpu"); t0 = time.time()
    vecs = m.encode([f"passage: {c['text']}" for c in chunks], batch_size=16, normalize_embeddings=True, show_progress_bar=False)
    stats["embed_seconds"] = round(time.time() - t0, 1)
    with psycopg.connect(DB) as c:
        c.execute("CREATE EXTENSION IF NOT EXISTS vector")
        c.execute("""CREATE TABLE IF NOT EXISTS adv_chunks (chunk_id text PRIMARY KEY, document_id text NOT NULL, page int NOT NULL,
                     chapter int, chunk_type text NOT NULL, text text NOT NULL, metadata jsonb NOT NULL, embedding vector(384) NOT NULL)""")
        c.execute("CREATE INDEX IF NOT EXISTS adv_chunks_filter ON adv_chunks (chapter, chunk_type)")
        with c.transaction():
            c.execute("DELETE FROM adv_chunks WHERE document_id=%s", (DOC,))  # re-ingest replaces; no duplicates
            with c.cursor() as cur:
                cur.executemany("INSERT INTO adv_chunks VALUES (%s,%s,%s,%s,%s,%s,%s,%s::vector)",
                    [(ch["id"], DOC, ch["page"], ch["metadata"]["chapter"], ch["metadata"]["chunk_type"], ch["text"], json.dumps(ch["metadata"], ensure_ascii=False),
                      "[" + ",".join(f"{x:.8f}" for x in v) + "]") for ch, v in zip(chunks, vecs)])
        stats["db_rows"] = c.execute("SELECT count(*) FROM adv_chunks WHERE document_id=%s", (DOC,)).fetchone()[0]
    json.dump(stats, open("adv/index_stats.json", "w"), ensure_ascii=False, indent=1)
    print("ingested", stats["db_rows"], "rows in", stats["embed_seconds"], "s")
if __name__ == "__main__": main(ingest="--no-db" not in sys.argv)
