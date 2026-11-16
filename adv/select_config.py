"""Apply the criteria declared in adv/SELECTION.md to the DEV runs only (never reads test)."""
import sys, json, glob
sys.path.insert(0, "adv"); from summarize import summarize
rows = [summarize(p) for p in sorted(glob.glob("adv/results/dev_*.json"))]
def key(r):
    c = lambda s: int(s.split("/")[0])
    return (-r["auto_pass_rate"], -c(r["context_covers_gold"]), r["mean_seconds"])
rows.sort(key=key)
for r in rows: print(r["config"], r["auto_pass"]["all"], "ctx", r["context_covers_gold"], r["mean_seconds"], "s")
json.dump({"selected": rows[0]["config"], "ranking": [{"config": r["config"], "auto_pass_all": r["auto_pass"]["all"], "context_covers_gold": r["context_covers_gold"], "mean_seconds": r["mean_seconds"]} for r in rows]}, open("adv/results/selected.json", "w"), indent=1)
print("SELECTED:", rows[0]["config"])
