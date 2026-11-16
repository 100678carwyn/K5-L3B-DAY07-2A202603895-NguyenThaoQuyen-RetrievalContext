import re, unicodedata
def norm(s): return re.sub(r"\s+", " ", unicodedata.normalize("NFKC", s)).strip().lower()

def is_hit(chunk, gold_list):
    """Hit = chunk is on a gold (source,page) AND contains the whole gold evidence (normalised)."""
    t = norm(chunk["text"])
    return any(chunk["source_id"] == g["source_id"] and chunk["page"] == g["page"] and norm(g["evidence"]) in t for g in gold_list)

def page_hit(chunk, gold_list):
    return any(chunk["source_id"] == g["source_id"] and chunk["page"] == g["page"] for g in gold_list)
