import json, unittest, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from rag.retrievers import BM25, tok, Hybrid
from rag.metrics import is_hit, norm

CH = [
    {"id": "x:p1:B00", "text": "A data steward runs data quality checks.", "source_id": "x", "source": "x", "page": 1, "metadata": {"chapter": 8}},
    {"id": "x:p2:B00", "text": "Agile models are iterative and incremental.", "source_id": "x", "source": "x", "page": 2, "metadata": {"chapter": 9}},
]

class Fake:
    name = "dense"
    def search(self, q, k=3, f=None): return [{**c, "score": 1.0, "rank": i + 1} for i, c in enumerate(CH)][:k]

class T(unittest.TestCase):
    def test_bm25_rank_and_filter(self):
        b = BM25(CH)
        self.assertEqual(b.search("data steward quality")[0]["id"], "x:p1:B00")
        self.assertEqual(b.search("data quality", filters={"chapter": 9}), [])
    def test_hit_requires_page_and_full_evidence(self):
        g = [{"source_id": "x", "page": 1, "evidence": "data   quality checks"}]
        self.assertTrue(is_hit(CH[0], g)); self.assertFalse(is_hit(CH[1], g))
        self.assertFalse(is_hit({**CH[0], "page": 3}, g))
    def test_hybrid_fuses_both(self):
        h = Hybrid(Fake(), BM25(CH)).search("agile iterative", 2)
        self.assertEqual(h[0]["id"], "x:p2:B00"); self.assertIn("rank_bm25", h[0])
    def test_benchmark_shape(self):
        q = json.load(open(pathlib.Path(__file__).resolve().parents[1] / "benchmark/questions.json"))["questions"]
        for sp, ans, n in (("dev", True, 15), ("dev", False, 2), ("test", True, 5), ("test", False, 2)):
            self.assertGreaterEqual(sum(x["split"] == sp and x["answerable"] == ans for x in q), n)
        self.assertGreaterEqual(sum(1 for x in q if x["split"] == "test" and x.get("filter")), 1)

if __name__ == "__main__": unittest.main()
