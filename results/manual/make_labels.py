"""Manual labels for TEST traces. Written after reading every answer/context against the source chunks
(reviewer: Claude, an AI assistant, working for the student; student must re-check - see report)."""
import json
RULE = "answer_grade: 2 = correct, fully supported by retrieved context, no unsupported extra claim; 1 = core answer correct but contains an unsupported/contradicted extra claim or wrong/missing source; 0 = wrong/no evidence."
# (config, qid) -> (answer_grade|None, [citation_support], abstention_correct|None, context_grade|None, reason)
L = {
 ("base_dense","test-n01"):(1,[],None,2,"Core ok (aspect of real-world data) but merges the definition of 'database' ('business process or problem setting') into miniworld; no citation."),
 ("base_dense","test-n02"):(1,[True,False],None,2,"Final answer DDL compiler correct, but it is cited to p382:B02 which does not contain the DDL sentence (it is in p379:B01); first sentence about security manager is irrelevant."),
 ("base_dense","test-n03"):(1,[],None,2,"'possible but not common' correct; adds unsupported claim that one primary language 'can still be sufficient for many projects'; no citation."),
 ("base_dense","test-n04"):(1,[],None,2,"Multiplicities + exactly one Car per AdaptiveCruiseControl correct; then wrongly says numbers can indicate on/off state; no citation."),
 ("base_dense","test-n05"):(1,[],None,2,"'ignores any physical aspects' correct; adds database-design/validation claims taken from another page (p387) and misattributes 'where information comes from' to logical design; no citation."),
 ("base_dense","test-n06"):(2,[True],None,2,"Google Maps, cited chunk p377:B02 contains the sentence."),
 ("base_dense","test-a1"):(None,[],True,None,"Abstains; context (p459 mentions Scrum/Kanban/sprints only) has no meeting duration. No invented claim."),
 ("base_dense","test-a2"):(None,[],True,None,"Abstains; Oracle appears only as a DBMS example (p380/382), no price."),
 ("imp_topk5","test-n01"):(1,[],None,2,"Core ok but mixes 'specific business process or problem setting' (definition of database) and adds an invented 'structure and operations for managing student grades'; no citation."),
 ("imp_topk5","test-n02"):(2,[True],None,2,"DDL compiler correct; cited p379:B01 contains the sentence; security-manager sentence is true but unnecessary."),
 ("imp_topk5","test-n03"):(1,[],None,2,"Core correct; adds loosely supported list ('mobile apps, websites, video games, data structures management'); no citation."),
 ("imp_topk5","test-n04"):(1,[],None,2,"Multiplicities correct; example claims a '1' between BlindSpotDetection and Car which the text does not state (it states one Car per AdaptiveCruiseControl); no citation."),
 ("imp_topk5","test-n05"):(1,[],None,2,"'ignores any physical aspects' + cruise-control example correct; 'how information is stored' not in source; no citation."),
 ("imp_topk5","test-n06"):(2,[True],None,2,"Google Maps, quotes the evidence sentence, cites p377:B02."),
 ("imp_topk5","test-a1"):(None,[],True,None,"Abstains; no meeting duration in corpus."),
 ("imp_topk5","test-a2"):(None,[],True,None,"Abstains; no license price in corpus."),
}
cases = [{"id": q["id"], "split": q["split"], "answerable": q["answerable"]} for q in json.load(open("benchmark/questions.json"))["questions"] if q["split"] == "test"]
json.dump(cases, open("results/manual/cases_test.json", "w"), indent=1)
for cfg in ("base_dense", "imp_topk5"):
    T = json.load(open(f"results/agent/test_{cfg}.json"))
    for t in T: assert len(L[(cfg, t["query_id"])][1]) == len(t["citations"]), (cfg, t["query_id"])
    traces = [{"query_id": t["query_id"], "status": t["status"], "events": t["events"], "citations": t["citations"]} for t in T]
    reviews = []
    for t in T:
        g, sup, ab, cg, why = L[(cfg, t["query_id"])]
        r = {"query_id": t["query_id"], "citation_support": sup, "reason": why}
        if g is not None: r["answer_grade"] = g; r["context_grade"] = cg
        if ab is not None: r["abstention_correct"] = ab
        reviews.append(r)
    json.dump(traces, open(f"results/manual/traces_test_{cfg}.json", "w"), indent=1)
    json.dump({"rule": RULE, "context_rule": "0 = no evidence in final context; 1 = evidence but missing condition/source; 2 = full evidence + source id/page", "reviews": reviews}, open(f"results/manual/reviews_test_{cfg}.json", "w"), ensure_ascii=False, indent=1)
    json.dump(reviews, open(f"results/manual/reviews_plain_{cfg}.json", "w"), ensure_ascii=False, indent=1)
