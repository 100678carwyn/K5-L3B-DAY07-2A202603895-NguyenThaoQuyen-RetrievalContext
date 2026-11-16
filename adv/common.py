import json, re, sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from rag.adv import *

def load_questions(split):
    return [q for q in json.load(open("adv/benchmark/questions.json"))["questions"] if q["split"] == split]

def cited_pages(trace):
    ctx = {c["id"]: c for c in trace.get("context", [])}
    return {ctx[i]["page"] for i in trace.get("citations", []) if i in ctx}

def auto_pass(q, t):
    """Automatic PROXY of the pass criterion (final labels are manual): answerable -> answered + all key facts + >=1 valid citation on a gold page;
    absent -> abstained. Errors count as fail."""
    if t["status"] == "error": return False
    if not q["answerable"]: return t["status"] == "abstain"
    gold_pages = {g["page"] for g in q["gold"]}
    return t["status"] == "answered" and key_facts_ok(t["answer"], q["key_facts"]) and bool(cited_pages(t) & gold_pages)
