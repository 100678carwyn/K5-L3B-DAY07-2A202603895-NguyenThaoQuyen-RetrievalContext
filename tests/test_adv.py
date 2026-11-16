import json, os, pathlib, sys, unittest
ROOT = pathlib.Path(__file__).resolve().parents[1]; sys.path.insert(0, str(ROOT)); sys.path.insert(0, str(ROOT / "adv"))
os.environ.setdefault("DATABASE_URL", "postgresql://u:p@127.0.0.1:1/x")  # unit tests never connect
from rag.adv import norm, key_facts_ok, covers, BM25vi, AdvAgent, AdvConfig
from rag.llm import DeepSeek, LLMError

CH = [{"id": "ccdr-vn-2022:p19:tb4", "text": "Bảng 1 Việt Nam 3,8 Thái Lan 6,2", "page": 19, "source_id": "x", "metadata": {"chunk_type": "table", "chapter": 1}},
      {"id": "ccdr-vn-2022:p17:t0", "text": "thiệt hại 10 tỷ USD tương đương 3,2% GDP", "page": 17, "source_id": "x", "metadata": {"chunk_type": "text", "chapter": 1}}]

class Script:  # scripted LLM: first a tool call, then an answer
    name, model = "script", "script"
    def __init__(self, answers): self.answers, self.i = answers, 0
    def chat(self, messages, tools=None, **kw):
        a = self.answers[self.i]; self.i += 1; return a

def call(name, args): return {"id": "c1", "type": "function", "function": {"name": name, "arguments": json.dumps(args)}}
U = {"prompt": 10, "completion": 5, "cache_hit": 0}

class Dummy:
    def search(self, q, k=5, f=None): return [{**c, "score": 1.0, "rank": i + 1} for i, c in enumerate(CH)][:k]

class T(unittest.TestCase):
    def test_norm_numbers(self):
        self.assertEqual(norm("4.219"), norm("4219")); self.assertEqual(norm("3,8"), "3.8")
    def test_key_facts(self):
        self.assertTrue(key_facts_ok("Việt Nam 3,8 và chênh 2,4", [["3,8"], ["2,4"]])); self.assertFalse(key_facts_ok("3,8", [["3,8"], ["2,4"]]))
    def test_covers_visual_needs_table_or_figure(self):
        g = [{"page": 19, "evidence_type": "table"}, {"page": 17, "evidence_type": "text"}]
        self.assertTrue(covers(g, CH)); self.assertFalse(covers([{"page": 17, "evidence_type": "table"}], CH))
    def test_bm25vi_vietnamese(self):
        self.assertEqual(BM25vi(CH).search("Thái Lan phát thải")[0]["page"], 19)
    def test_agent_tool_then_answer_and_citation(self):
        llm = Script([{"content": "", "tool_calls": [call("search_documents", {"query": "x", "kind": "table"})], "usage": U},
                      {"content": "3,8 [ccdr-vn-2022:p19:tb4]", "tool_calls": [], "usage": U}])
        t = AdvAgent(llm, {"hybrid_rrf": Dummy()}, CH, AdvConfig("t")).run({"id": "q", "question": "câu hỏi thử"})
        self.assertEqual((t["status"], t["searches"], t["citations"], t["invalid_citations"]), ("answered", 1, ["ccdr-vn-2022:p19:tb4"], []))
    def test_agent_abstain_and_nudge(self):
        llm = Script([{"content": "đoán bừa", "tool_calls": [], "usage": U}, {"content": "", "tool_calls": [call("get_page", {"page": 17})], "usage": U},
                      {"content": "KHÔNG_ĐỦ_BẰNG_CHỨNG: không có", "tool_calls": [], "usage": U}])
        t = AdvAgent(llm, {"hybrid_rrf": Dummy()}, CH, AdvConfig("t")).run({"id": "q", "question": "câu hỏi thử"})
        self.assertEqual(t["status"], "abstain"); self.assertTrue(any(e["event"] == "nudge" for e in t["events"]))
    def test_missing_key_is_error_not_mock(self):
        old = os.environ.pop("DEEPSEEK_API_KEY", None)
        cwd = os.getcwd(); os.chdir("/tmp")  # no .env here
        try:
            with self.assertRaises(LLMError) as cm: DeepSeek()
            self.assertNotIn("sk-", str(cm.exception))
        finally:
            os.chdir(cwd)
            if old: os.environ["DEEPSEEK_API_KEY"] = old
    def test_deepseek_request_shape_and_no_key_leak(self):
        import httpx
        fake_key = "TESTKEY-not-a-real-secret-123456"
        seen = {}
        class R:
            def __init__(self, code, body): self.status_code, self._b, self.text = code, body, "unauthorized"
            def json(self): return self._b
        def ok(url, headers=None, json=None, timeout=None):
            seen.update(url=url, auth=headers["Authorization"], body=json)
            return R(200, {"choices": [{"message": {"content": "xin chào", "tool_calls": None}}], "usage": {"prompt_tokens": 7, "completion_tokens": 2, "prompt_cache_hit_tokens": 3}})
        def bad(url, headers=None, json=None, timeout=None): return R(401, {})
        old = httpx.post; os.environ["DEEPSEEK_API_KEY"] = fake_key
        try:
            httpx.post = ok; d = DeepSeek(); r = d.chat([{"role": "user", "content": "hi"}], tools=[{"type": "function"}])
            self.assertEqual(r["content"], "xin chào"); self.assertEqual(r["usage"], {"prompt": 7, "completion": 2, "cache_hit": 3})
            self.assertTrue(seen["url"].endswith("/chat/completions")); self.assertEqual(seen["body"]["model"], "deepseek-chat"); self.assertEqual(seen["body"]["temperature"], 0.0)
            httpx.post = bad
            with self.assertRaises(LLMError) as cm: d.chat([{"role": "user", "content": "hi"}])
            self.assertNotIn(fake_key, str(cm.exception))
        finally:
            httpx.post = old; os.environ.pop("DEEPSEEK_API_KEY", None)

    def test_advanced_benchmark_shape(self):
        q = json.load(open(ROOT / "adv/benchmark/questions.json"))["questions"]
        t = [x for x in q if x["split"] == "test"]; d = [x for x in q if x["split"] == "dev"]
        self.assertGreaterEqual(len(t), 30); self.assertGreaterEqual(sum(x["answerable"] for x in t), 24); self.assertGreaterEqual(sum(not x["answerable"] for x in t), 6)
        for g, n in (("bang", 6), ("anh", 5), ("bieu_do", 5), ("multi_hop", 4), ("text", 4)): self.assertGreaterEqual(sum(x["group"] == g for x in t), n, g)
        self.assertGreaterEqual(sum(x["answerable"] for x in d), 15); self.assertGreaterEqual(sum(not x["answerable"] for x in d), 3)
        self.assertFalse({x["question"] for x in t} & {x["question"] for x in d})

if __name__ == "__main__": unittest.main()
