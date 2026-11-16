"""Build Day 7 benchmark: Day-6 questions (re-used as DEV) + new TEST questions + abstention questions.
Every answerable evidence is verified to occur (normalised) on the gold page; absence questions are
verified by keyword grep on all 40 pages. Written BEFORE any Day-7 retrieval/agent run."""
import json, re, unicodedata, sys
D6 = "/Users/carwyn/K5-L3B-DAY06-2A202603895-DataIngestion/benchmark/questions.json"
def norm(s): return re.sub(r"\s+", " ", unicodedata.normalize("NFKC", s)).strip().lower()
pages = {}
for l in open("data/real/pages.jsonl"):
    r = json.loads(l); pages[r["page"]] = norm(r["text"])
SRC = "openstax-intro-cs"
out = []
for q in json.load(open(D6))["questions"]:
    gold = [{"source_id": q["gold_source_id"], "page": q["gold_page"], "evidence": q["evidence_quote"]}]
    for a in q.get("alt_gold") or []:
        gold.append({"source_id": SRC, "page": a["page"], "evidence": a["quote"]})
    # Day-6 test questions were already looked at in Day 6 -> they are re-labelled DEV in Day 7
    out.append({"id": "dev-" + q["id"], "split": "dev", "origin": "day6-" + q["split"] + ":" + q["id"], "type": q["type"],
                "question": q["question"], "expected_answer": q["expected_answer"], "answerable": True,
                "gold": gold, **({"filter": q["filter"]} if q.get("filter") else {})})
new_test = [
 ("n01", "What does the term miniworld (universe of discourse) refer to in a database context?", "A miniworld represents some aspect of the real-world data that are stored in a database.", 377, "A miniworld, or universe of discourse (UoD), represents some aspect of the real-world data that are stored in a database", None, "truc_tiep"),
 ("n02", "Which DBMS component translates statements written in a high-level language into low-level instructions for the query evaluation engine?", "The data description language (DDL) compiler.", 379, "The data description language (DDL) compiler translates statements in a high-level language into low-level instructions that the query evaluation engine understands", None, "dien_dat_lai"),
 ("n03", "Is it possible to be employed as a software engineer while knowing only a single programming language?", "Yes, it is possible but not common.", 450, "It is possible, though not common, to be employed as a software engineer knowing only a single programming language", None, "dieu_kien"),
 ("n04", "In a UML class diagram of a domain model, what do the numbers at the associations express?", "They are multiplicities, e.g., exactly one Car per AdaptiveCruiseControl.", 455, "The numbers at associations are multiplicities, and they say that there is exactly one Car associated with each AdaptiveCruiseControl", {"chapter": 9}, "metadata_filter"),
 ("n05", "What does logical design ignore when a solution is designed?", "Logical design ignores any physical aspects.", 457, "Logical design ignores any physical aspects", None, "dieu_kien"),
 ("n06", "Which example is given for a Geographic Information Systems (GIS) database application?", "Google Maps.", 377, "Geographic Information Systems (GIS) applications (e.g., Google Maps)", {"chapter": 8}, "metadata_filter"),
]
for i, qs, ans, pg, ev, flt, typ in new_test:
    out.append({"id": "test-" + i, "split": "test", "origin": "day7-new", "type": typ, "question": qs, "expected_answer": ans,
                "answerable": True, "gold": [{"source_id": SRC, "page": pg, "evidence": ev}], **({"filter": flt} if flt else {})})
absent = [
 ("dev", "a1", "How many rows can a single PostgreSQL table hold at most?", ["postgres"]),
 ("dev", "a2", "What is the average yearly salary of a database administrator?", ["salary"]),
 ("dev", "a3", "Which continuous integration tool, such as Jenkins, does the chapter recommend for automating builds?", ["jenkins", "continuous integration"]),
 ("test", "a1", "How many minutes should a daily stand-up meeting last in Scrum?", ["stand-up", "standup", "minutes"]),
 ("test", "a2", "How much does an Oracle DBMS enterprise license cost?", ["per month", "license fee", "licensing cost"]),
]
for sp, i, qs, kws in absent:
    hits = {k: [p for p, t in pages.items() if k in t] for k in kws}
    assert not any(hits.values()), (qs, hits)
    out.append({"id": f"{sp}-{i}", "split": sp, "origin": "day7-new", "type": "thieu_bang_chung", "question": qs, "answerable": False,
                "expected_behavior": "search_and_abstain",
                "absence_reason": f"Keyword grep over all 40 corpus pages (370-389, 440-459) finds none of {kws}; topic is adjacent to the corpus but not stated."})
# verify evidence
bad = 0
for q in out:
    if not q["answerable"]: continue
    for g in q["gold"]:
        ok = norm(g["evidence"]) in pages[g["page"]]
        if not ok: bad += 1; print("EVIDENCE NOT ON PAGE:", q["id"], g["page"])
json.dump({"_readme": "Day 7 benchmark. dev = 24 answerable (Day-6 dev 18 + Day-6 test 6, re-labelled dev because Day-6 test was already viewed) + 3 absent; test = 6 NEW answerable (written from the corpus before any Day-7 run) + 2 absent. Filters are user-context (chapter being read), never derived from gold.",
           "questions": out}, open("benchmark/questions.json", "w"), ensure_ascii=False, indent=1)
from collections import Counter
print(Counter((q["split"], q["answerable"]) for q in out), "bad evidence:", bad)
