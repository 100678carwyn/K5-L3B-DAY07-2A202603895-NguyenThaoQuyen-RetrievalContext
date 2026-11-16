"""Run the advanced agent on a split. Resumable: already finished (non-error) questions in --out are kept. Needs a real LLM backend."""
import sys, json, argparse, os
sys.path.insert(0, "adv"); from common import *
from rag.llm import make_llm
CONFIGS = {"adv_dense": AdvConfig("adv_dense", "dense", 5, 12000, 4), "adv_hybrid": AdvConfig("adv_hybrid", "hybrid_rrf", 5, 12000, 4),
           "adv_hybrid_wide": AdvConfig("adv_hybrid_wide", "hybrid_rrf", 8, 16000, 6)}
ap = argparse.ArgumentParser(); ap.add_argument("--config", required=True, choices=CONFIGS); ap.add_argument("--split", required=True)
ap.add_argument("--llm", default="deepseek", choices=["deepseek", "ollama"]); ap.add_argument("--model", default=None)
ap.add_argument("--out", required=True); ap.add_argument("--limit", type=int); a = ap.parse_args()
cfg = CONFIGS[a.config]; chunks = load_chunks(); R = build_retrievers(chunks); llm = make_llm(a.llm, a.model)
agent = AdvAgent(llm, R, chunks, cfg)
Qs = load_questions(a.split)[:a.limit]
done = {}
if os.path.exists(a.out): done = {t["query_id"]: t for t in json.load(open(a.out)) if t["status"] != "error"}
out = []
for q in Qs:
    t = done.get(q["id"]) or agent.run(q)
    t["answerable"], t["split"], t["group"] = q["answerable"], q["split"], q["group"]
    if q["answerable"]: t["context_covers_gold"] = covers(q["gold"], [{"page": c["page"], "metadata": {"chunk_type": c["type"]}} for c in t.get("context", [])])
    t["auto_pass"] = auto_pass(q, t)
    out.append(t); json.dump(out + [done[k] for k in done if k not in {x["query_id"] for x in out} and k in {qq["id"] for qq in Qs}], open(a.out, "w"), ensure_ascii=False, indent=1)
    print(f"{q['id']:10s} {t['status']:8s} pass={t['auto_pass']} s={t.get('searches')} {t['seconds']}s {'ERR '+t.get('error','') if t['status']=='error' else ''}", flush=True)
