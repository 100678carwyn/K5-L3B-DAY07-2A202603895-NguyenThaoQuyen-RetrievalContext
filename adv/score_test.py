"""Final TEST score from HUMAN labels (adv/results/labels_test.json). Pass rate = passed / ALL published test questions (errors and unlabeled count as fail)."""
import sys, json
sys.path.insert(0, "adv"); from common import *
L = json.load(open("adv/results/labels_test.json")); Qs = load_questions("test"); g = {}
missing = [q["id"] for q in Qs if q["id"] not in L]
for q in Qs:
    k = q["group"]; g.setdefault(k, [0, 0]); g.setdefault("all", [0, 0]); ok = bool(L.get(q["id"], {}).get("pass"))
    for key in (k, "all"): g[key][1] += 1; g[key][0] += ok
need = -(-9 * g["all"][1] // 10)  # ceil(0.9*N), no rounding up of the rate
print({k: f"{a}/{n}" for k, (a, n) in g.items()}, "| rate %.1f%%" % (100 * g["all"][0] / g["all"][1]), "| need >=", need, "| unlabeled:", missing)
print("BONUS CONDITION MET" if g["all"][0] >= need and not missing else "bonus condition NOT met")
