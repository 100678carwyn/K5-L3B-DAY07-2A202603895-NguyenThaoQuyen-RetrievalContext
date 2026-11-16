import json, sys, argparse
from rag.retrievers import *
from rag.agent import Agent, Config
from rag.metrics import is_hit
CONFIGS = {
 "base_dense":  Config("base_dense", "dense"),
 "base_bm25":   Config("base_bm25", "bm25"),
 "base_hybrid": Config("base_hybrid", "hybrid_rrf"),
}
ap = argparse.ArgumentParser(); ap.add_argument("--config", required=True); ap.add_argument("--split", required=True)
ap.add_argument("--out", required=True); ap.add_argument("--set", nargs="*", default=[], help="key=value overrides")
ap.add_argument("--base", default=None); ap.add_argument("--limit", type=int)
a = ap.parse_args()
chunks = load_chunks(); dense = Dense(chunks); bm = BM25(chunks); R = {"dense": dense, "bm25": bm, "hybrid_rrf": Hybrid(dense, bm)}
cfg = Config(a.config, "dense") if a.base is None else CONFIGS[a.base]
cfg.name = a.config
for kv in a.set:
    k, v = kv.split("="); setattr(cfg, k, {"true": True, "false": False}.get(v, int(v) if v.isdigit() else v))
if a.base is None and a.config in CONFIGS: cfg = CONFIGS[a.config]
qs = [q for q in json.load(open("benchmark/questions.json"))["questions"] if q["split"] == a.split][:a.limit]
agent, out = Agent(R, chunks, cfg), []
for q in qs:
    t = agent.run(q); t["answerable"] = q["answerable"]; t["split"] = q["split"]
    if q["answerable"]:
        t["context_evidence"] = any(is_hit(c, q["gold"]) for c in t.get("context", []))
        first = next((e for e in t["events"] if e["event"] == "search"), None)
        t["first_search_hit1"] = bool(first and first["results"] and first["results"][0]["id"] and is_hit(next(c for c in chunks if c["id"] == first["results"][0]["id"]), q["gold"]))
    out.append(t)
    print(f"{q['id']:10s} {t['status']:8s} s={t.get('searches')} ctxEv={t.get('context_evidence')} {t['seconds']}s :: {(t['answer'] or t.get('error') or '')[:90]!r}", flush=True)
json.dump(out, open(a.out, "w"), ensure_ascii=False, indent=1)
