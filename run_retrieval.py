"""Retrieval-only comparison (no LLM): original query, top-3, same chunks/index/questions."""
import json, sys, time, argparse
from rag.retrievers import *
from rag.metrics import is_hit, page_hit
ap = argparse.ArgumentParser()
ap.add_argument("--split", required=True); ap.add_argument("--out", required=True)
ap.add_argument("--methods", default="dense,bm25,hybrid_rrf"); ap.add_argument("--topk", type=int, default=3)
a = ap.parse_args()
qs = [q for q in json.load(open("benchmark/questions.json"))["questions"] if q["split"] == a.split and q["answerable"]]
chunks = load_chunks(); dense = Dense(chunks); bm = BM25(chunks); hy = Hybrid(dense, bm)
M = {"dense": dense, "bm25": bm, "hybrid_rrf": hy}
res, traces = {}, []
for m in a.methods.split(","):
    for use_filter in (False, True):
        h1 = h3 = ph3 = n = nf = fh3 = 0; t0 = time.time()
        for q in qs:
            flt = q.get("filter") if use_filter else None
            top = M[m].search(q["question"], a.topk, flt)
            hits = [is_hit(c, q["gold"]) for c in top[:3]]
            h1 += bool(hits[:1] and hits[0]); h3 += any(hits); ph3 += any(page_hit(c, q["gold"]) for c in top[:3]); n += 1
            if q.get("filter"): nf += 1; fh3 += any(hits)
            traces.append({"method": m, "filter_applied": bool(flt), "query_id": q["id"], "question": q["question"], "filter": flt,
                           "top": [{"id": c["id"], "page": c["page"], "chapter": c["metadata"].get("chapter"), "score": round(c["score"], 4), "hit": h, "text": c["text"]} for c, h in zip(top[:3], hits)]})
        res[f"{m}|filter={use_filter}"] = {"N": n, "hit1": h1, "hit3": h3, "page_hit3": ph3, "filter_questions": nf, "filter_hit3": fh3, "seconds": round(time.time() - t0, 2)}
json.dump(res, open(a.out + "_summary.json", "w"), indent=1)
json.dump(traces, open(a.out + "_traces.json", "w"), ensure_ascii=False, indent=1)
for k, v in res.items(): print(k, v)
