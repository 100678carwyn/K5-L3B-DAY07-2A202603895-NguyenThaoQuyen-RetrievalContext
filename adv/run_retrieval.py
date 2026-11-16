"""Retrieval-only comparison on the advanced benchmark (original question as query, no LLM, no filter)."""
import sys, json, time, argparse
sys.path.insert(0, "adv"); from common import *
ap = argparse.ArgumentParser(); ap.add_argument("--split", required=True); ap.add_argument("--out", required=True); a = ap.parse_args()
chunks = load_chunks(); R = build_retrievers(chunks)
Qs = [q for q in load_questions(a.split) if q["answerable"]]
res, traces = {}, []
for m, r in R.items():
    row = {"all": {"N": 0, "hit1": 0, "hit3": 0, "hit5": 0}}; t0 = time.time()
    for q in Qs:
        top = r.search(q["question"], 5)
        h1, h3, h5 = covers(q["gold"], top[:1]), covers(q["gold"], top[:3]), covers(q["gold"], top[:5])
        for k in ("all", q["group"]):
            row.setdefault(k, {"N": 0, "hit1": 0, "hit3": 0, "hit5": 0}); row[k]["N"] += 1; row[k]["hit1"] += h1; row[k]["hit3"] += h3; row[k]["hit5"] += h5
        traces.append({"method": m, "query_id": q["id"], "top": [{"id": c["id"], "page": c["page"], "type": c["metadata"]["chunk_type"], "score": round(c["score"], 4)} for c in top], "hit1": h1, "hit3": h3, "hit5": h5})
    row["seconds"] = round(time.time() - t0, 2); res[m] = row
json.dump(res, open(a.out + "_summary.json", "w"), indent=1, ensure_ascii=False); json.dump(traces, open(a.out + "_traces.json", "w"), indent=1, ensure_ascii=False)
for m, row in res.items(): print(m, {k: (f"{v['hit1']}/{v['N']} | {v['hit3']}/{v['N']} | {v['hit5']}/{v['N']}" if isinstance(v, dict) else v) for k, v in row.items()})
