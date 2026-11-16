"""Three light retrieval methods over the Day-6 index:
  dense  : multilingual-e5-small query embedding -> pgvector cosine (Day-6 PostgreSQL table, strategy B)
  bm25   : pure-python Okapi BM25 over the same chunks (lexical)
  hybrid : Reciprocal Rank Fusion of dense and bm25 rankings
All return dicts: id, text, source_id, source, page, metadata, score, rank (+ per-method ranks for hybrid)."""
from __future__ import annotations
import json, math, os, re
from collections import Counter

def _load_env(path=".env"):  # read DATABASE_URL from the git-ignored .env (no secret in code)
    try:
        for line in open(path, encoding="utf-8"):
            k, sep, v = line.strip().partition("=")
            if sep and not k.startswith("#"): os.environ.setdefault(k.strip(), v.strip())
    except FileNotFoundError:
        pass


_load_env()
DB_URL = os.environ.get("DATABASE_URL")
if not DB_URL:
    raise RuntimeError("DATABASE_URL is not set: copy .env.example to .env and fill in the Day-6 database URL")
STRATEGY = "B"  # Day-6 paragraph chunks (same chunks as strategy C)
STOP = set("a an the of to in on for and or is are was were be by with as at from that this it its which what who how does do did into than then their there these those can may not no".split())


def tok(s: str) -> list[str]:
    return [w for w in re.findall(r"[a-z0-9]+", s.lower()) if w not in STOP]


def _match(ch: dict, filt: dict | None) -> bool:
    return all(ch["metadata"].get(k) == v for k, v in (filt or {}).items())


def load_chunks(path="data/real/chunks.json"):
    return json.load(open(path, encoding="utf-8"))


class BM25:
    name = "bm25"

    def __init__(self, chunks, k1=1.5, b=0.75):
        self.chunks, self.k1, self.b = chunks, k1, b
        self.docs = [Counter(tok(c["text"])) for c in chunks]
        self.len = [sum(d.values()) for d in self.docs]
        self.avg = sum(self.len) / len(self.len)
        df = Counter(t for d in self.docs for t in d)
        n = len(chunks)
        self.idf = {t: math.log(1 + (n - f + .5) / (f + .5)) for t, f in df.items()}

    def search(self, query, top_k=3, filters=None):
        q = tok(query)
        scored = []
        for i, c in enumerate(self.chunks):
            if not _match(c, filters): continue
            d, L, s = self.docs[i], self.len[i], 0.0
            for t in q:
                f = d.get(t, 0)
                if f: s += self.idf[t] * f * (self.k1 + 1) / (f + self.k1 * (1 - self.b + self.b * L / self.avg))
            scored.append((s, i))
        scored.sort(key=lambda x: (-x[0], x[1]))
        return [{**self.chunks[i], "score": s, "rank": r + 1} for r, (s, i) in enumerate(scored[:top_k]) if s > 0]


class Dense:
    name = "dense"

    def __init__(self, chunks, model="intfloat/multilingual-e5-small"):
        from sentence_transformers import SentenceTransformer
        import psycopg
        self.by_id = {c["id"]: c for c in chunks}
        self.model = SentenceTransformer(model, device="cpu")
        self.model_name, self.dim = model, int(self.model.get_sentence_embedding_dimension())
        self.conn = psycopg.connect(DB_URL, connect_timeout=5)  # raises if the Day-6 store is down; no fallback

    def embed(self, q):  # same convention as Day 6: "query: " prefix, L2-normalised
        v = self.model.encode([f"query: {q}"], normalize_embeddings=True, convert_to_numpy=True)[0]
        return "[" + ",".join(f"{x:.8f}" for x in v) + "]"

    def search(self, query, top_k=3, filters=None):
        where, params = ["strategy=%s"], [STRATEGY]
        for k, v in (filters or {}).items():
            if k != "chapter": raise ValueError(f"unsupported filter {k}")
            where.append("chapter=%s"); params.append(v)
        qv = self.embed(query)
        rows = self.conn.execute(
            f"SELECT chunk_id, 1-(embedding <=> %s::vector) FROM chunks WHERE {' AND '.join(where)} "
            "ORDER BY embedding <=> %s::vector LIMIT %s", [qv, *params, qv, top_k]).fetchall()
        return [{**self.by_id[cid], "score": float(s), "rank": r + 1} for r, (cid, s) in enumerate(rows)]


class Hybrid:
    name = "hybrid_rrf"

    def __init__(self, dense, bm25, k=60, pool=20):
        self.dense, self.bm25, self.k, self.pool = dense, bm25, k, pool

    def search(self, query, top_k=3, filters=None):
        fused, info = Counter(), {}
        for m in (self.dense, self.bm25):
            for h in m.search(query, self.pool, filters):
                fused[h["id"]] += 1 / (self.k + h["rank"])
                info.setdefault(h["id"], h)[f"rank_{m.name}"] = h["rank"]
        order = sorted(fused, key=lambda i: (-fused[i], i))[:top_k]
        return [{**{k: v for k, v in info[i].items()}, "score": fused[i], "rank": r + 1} for r, i in enumerate(order)]
