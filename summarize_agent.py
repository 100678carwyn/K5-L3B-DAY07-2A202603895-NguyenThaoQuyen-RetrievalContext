"""Automatic (non-manual) metrics from agent traces: context evidence, tool use, abstention by status, time, tokens."""
import json, sys, statistics, collections
def summ(path):
    T = json.load(open(path)); A = [t for t in T if t["answerable"]]; U = [t for t in T if not t["answerable"]]
    ok = [t for t in T if t["status"] != "error"]
    cits = sum(len(t["citations"]) for t in ok); bad = sum(len(t.get("invalid_citations", [])) for t in ok)
    return {
      "file": path, "config": T[0]["config"]["name"], "N_answerable": len(A), "N_absent": len(U), "errors": len(T) - len(ok),
      "context_evidence_rate": f"{sum(t.get('context_evidence', False) for t in A)}/{len(A)}",
      "agent_first_query_hit1": f"{sum(t.get('first_search_hit1', False) for t in A)}/{len(A)}",
      "tool_use": f"{sum(any(e['event']=='search' for e in t['events']) for t in ok)}/{len(ok)}",
      "searches_dist": dict(collections.Counter(t.get('searches', 0) for t in ok)),
      "abstain_on_absent": f"{sum(t['status']=='abstain' for t in U)}/{len(U)}",
      "false_abstain_on_answerable": f"{sum(t['status']=='abstain' for t in A)}/{len(A)}",
      "citations_in_context": f"{cits-bad}/{cits} (ID-valid only, NOT support-verified)",
      "answers_with_citation": f"{sum(bool(t['citations']) for t in ok if t['status']=='answered')}/{sum(t['status']=='answered' for t in ok)}",
      "mean_seconds": round(statistics.mean(t["seconds"] for t in T), 1), "total_seconds": round(sum(t["seconds"] for t in T)),
      "tokens_prompt": sum(t["prompt_tokens"] for t in T), "tokens_completion": sum(t["completion_tokens"] for t in T),
      "llm_calls": sum(t["llm_calls"] for t in T), "cost_usd": 0.0}
if __name__ == "__main__":
    for p in sys.argv[1:]: print(json.dumps(summ(p), indent=1))
