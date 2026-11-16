"""Export Day 6 pgvector chunks (strategy B) to Day 7 JSON schema + copy corpus pages."""
import json, os, sys, psycopg
try:  # read DATABASE_URL from the git-ignored .env (no secret in code)
    for _l in open(".env", encoding="utf-8"):
        _k, _s, _v = _l.strip().partition("=")
        if _s and not _k.startswith("#"): os.environ.setdefault(_k.strip(), _v.strip())
except FileNotFoundError:
    pass
URL = os.environ.get("DATABASE_URL")
if not URL:
    sys.exit("DATABASE_URL is not set: add DATABASE_URL (the Day-6 PostgreSQL connection string, see the Day-6 starter docker-compose) to your git-ignored .env")
out = sys.argv[1] if len(sys.argv) > 1 else "data/real"
with psycopg.connect(URL) as c:
    rows = c.execute("""SELECT chunk_id, text, document_id, source, page, chapter, chapter_title, printed_page, metadata
                        FROM chunks WHERE strategy='B' ORDER BY page, chunk_id""").fetchall()
chunks = [{"id": r[0], "text": r[1], "source_id": r[2], "source": r[3], "page": r[4],
           "metadata": {"chapter": r[5], "chapter_title": r[6], "printed_page": r[7], "day6_strategy": "B"}} for r in rows]
json.dump(chunks, open(f"{out}/chunks.json", "w"), ensure_ascii=False, indent=1)
print(len(chunks), "chunks")
