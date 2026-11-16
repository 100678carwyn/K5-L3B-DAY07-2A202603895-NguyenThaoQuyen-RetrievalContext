"""Interactive chat with the advanced agent. Type a question; empty line or 'exit' quits.
  .venv/bin/python adv/chat.py                      # DeepSeek (needs DEEPSEEK_API_KEY in .env)
  .venv/bin/python adv/chat.py --llm ollama         # local model, no key
Each question is independent (no memory). Nothing is written to adv/results unless you pass --log."""
import sys, json, argparse
sys.path.insert(0, "adv"); from common import *
from rag.llm import make_llm
ap = argparse.ArgumentParser(); ap.add_argument("--llm", default="deepseek", choices=["deepseek", "ollama"]); ap.add_argument("--model")
ap.add_argument("--method", default="hybrid_rrf", choices=["dense", "bm25", "hybrid_rrf"]); ap.add_argument("--top-k", type=int, default=5)
ap.add_argument("--max-searches", type=int, default=4); ap.add_argument("--verbose", action="store_true", help="show tool calls and retrieved ids"); ap.add_argument("--log")
a = ap.parse_args()
chunks = load_chunks(); R = build_retrievers(chunks); llm = make_llm(a.llm, a.model)
agent = AdvAgent(llm, R, chunks, AdvConfig("chat", a.method, a.top_k, 12000, a.max_searches))
by_id = {c["id"]: c for c in chunks}
print(f"Chat về 'Báo cáo Quốc gia về Khí hậu và Phát triển - Việt Nam' (LLM: {llm.name}/{llm.model}; {a.method}). Gõ câu hỏi; Enter trống để thoát.")
while True:
    try: q = input("\nBạn> ").strip()
    except (EOFError, KeyboardInterrupt): break
    if not q or q.lower() in ("exit", "quit"): break
    t = agent.run({"id": "chat", "question": q})
    if t["status"] == "error": print("LỖI:", t.get("error")); continue
    if a.verbose:
        for e in t["events"]:
            if e["event"] == "search": print(f"  [tool] {e['tool']} {e['args']} -> {[r['id'].split(':',1)[1] for r in e['results']]}")
    print("\nTrợ lý>", t["answer"], "\n")
    cited = [by_id[c] for c in t["citations"] if c in by_id]
    for c in cited: print(f"  nguồn: trang PDF {c['page']} (trang in {c['page']-10}) · {c['metadata']['chunk_type']} · {c['metadata'].get('figure_id') or c['id'].split(':',1)[1]}")
    if not cited and t["status"] == "answered": print("  (câu trả lời không có citation hợp lệ — hãy kiểm tra thủ công)")
    print(f"  [{t['status']} · {t.get('searches')} lượt tìm · {t['seconds']}s · {t['prompt_tokens']}+{t['completion_tokens']} token]")
    if a.log: open(a.log, "a", encoding="utf-8").write(json.dumps({"q": q, "answer": t["answer"], "citations": t["citations"], "status": t["status"]}, ensure_ascii=False) + "\n")
