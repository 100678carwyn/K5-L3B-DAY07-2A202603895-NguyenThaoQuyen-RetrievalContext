"""Build a Markdown review sheet for TEST traces so a human can check every question against the ORIGINAL PDF page and write adv/results/labels_test.json:
 {"<qid>": {"pass": true/false, "reason": "...", "citations_support": [true,...]}}"""
import sys, json
sys.path.insert(0, "adv"); from common import *
T = {t["query_id"]: t for t in json.load(open(sys.argv[1]))}; Qs = load_questions("test"); ctxs = {}
out = ["# Phiếu chấm test (đối chiếu với bản gốc PDF, không chỉ dựa vào ghi chú chuyển ghi)\n"]
for q in Qs:
    t = T.get(q["id"]); out.append(f"## {q['id']} · {q['group']}\n**Câu hỏi:** {q['question']}\n")
    if q["answerable"]: out.append(f"**Đáp án chuẩn:** {q['expected_answer']}  \n**Evidence (trang PDF):** " + "; ".join(f"tr.{g['page']} [{g['evidence_type']}] {g['evidence']}" for g in q["gold"]) + "\n")
    else: out.append(f"**Mong đợi:** từ chối. {q['absence_reason']}\n")
    if not t: out.append("_Chưa có trace._\n"); continue
    out.append(f"**Trạng thái:** {t['status']} · lượt tìm: {t.get('searches')} · {t['seconds']}s · auto_pass (proxy): {t['auto_pass']}\n")
    out.append("**Công cụ:** " + "; ".join(f"{e.get('tool')}({e.get('args')}) → {[r['id'].split(':',1)[1] for r in e.get('results', [])]}" for e in t["events"] if e["event"] == "search") + "\n")
    out.append(f"**Câu trả lời:** {t['answer'] or t.get('error')}\n\n**Citation:** {t['citations']} (không hợp lệ: {t.get('invalid_citations')})\n")
    out.append("**Nhãn (điền vào labels_test.json):** pass = ?, lý do = ?\n")
open(sys.argv[2], "w", encoding="utf-8").write("\n".join(out)); print("wrote", sys.argv[2])
