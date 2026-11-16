import sys, json, collections, statistics
sys.path.insert(0, "adv"); from common import *
def summarize(path):
    T = json.load(open(path)); g = collections.defaultdict(lambda: [0, 0])
    for t in T:
        for k in ("all", t["group"]): g[k][1] += 1; g[k][0] += bool(t["auto_pass"])
    A = [t for t in T if t["answerable"]]; ok = [t for t in T if t["status"] != "error"]
    return {"file": path, "config": T[0]["config"]["name"], "llm": T[0]["llm"], "auto_pass": {k: f"{a}/{n}" for k, (a, n) in g.items()},
            "auto_pass_rate": round(g["all"][0] / g["all"][1], 4), "errors": len(T) - len(ok),
            "context_covers_gold": f"{sum(t.get('context_covers_gold', False) for t in A)}/{len(A)}",
            "tool_use": f"{sum(any(e['event']=='search' for e in t['events']) for t in ok)}/{len(ok)}", "searches_dist": dict(collections.Counter(t.get('searches', 0) for t in ok)),
            "abstain_on_absent": f"{sum(t['status']=='abstain' for t in T if not t['answerable'])}/{sum(not t['answerable'] for t in T)}",
            "false_abstain": f"{sum(t['status']=='abstain' for t in A)}/{len(A)}",
            "mean_seconds": round(statistics.mean(t["seconds"] for t in T), 1), "total_seconds": round(sum(t["seconds"] for t in T)),
            "prompt_tokens": sum(t["prompt_tokens"] for t in T), "completion_tokens": sum(t["completion_tokens"] for t in T), "cache_hit_tokens": sum(t.get("cache_hit_tokens", 0) for t in T), "llm_calls": sum(t["llm_calls"] for t in T)}
if __name__ == "__main__":
    for p in sys.argv[1:]: print(json.dumps(summarize(p), ensure_ascii=False, indent=1))
