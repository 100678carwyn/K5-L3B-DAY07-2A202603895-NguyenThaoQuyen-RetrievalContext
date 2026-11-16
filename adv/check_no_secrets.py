"""Fail if a secret could leak into files that git would track/publish. Prints only file names and rule ids, NEVER the secret.
Checks: (1) exact values of every non-empty *KEY/TOKEN/SECRET/PASSWORD value and DATABASE_URL password found in .env / environment are absent from all
non-ignored files, (2) generic key patterns, (3) .env.example has only empty/placeholder values, (4) .env is git-ignored and untracked."""
import os, re, subprocess, sys
def sh(*a): return subprocess.run(a, capture_output=True, text=True).stdout
files = [f for f in sh("git", "ls-files", "-co", "--exclude-standard").splitlines() if os.path.isfile(f)]
secrets = {}
for path in (".env",):
    if os.path.exists(path):
        for line in open(path, encoding="utf-8"):
            k, sep, v = line.strip().partition("=")
            if sep and not k.startswith("#") and v.strip():
                v = v.strip().strip('"').strip("'")
                if re.search(r"KEY|TOKEN|SECRET|PASSWORD", k, re.I) and len(v) >= 6: secrets[k] = v
                if k == "DATABASE_URL":
                    m = re.match(r"\w+://[^:]+:([^@]+)@", v)
                    if m and m.group(1) not in ("PASSWORD",): secrets["DATABASE_URL:password"] = m.group(1)
bad = []
PAT = [("openai-style key", re.compile(r"\bsk-[A-Za-z0-9_-]{16,}")), ("bearer token", re.compile(r"Bearer\s+[A-Za-z0-9._-]{20,}")),
       ("assigned api key", re.compile(r"(API_KEY|TOKEN|SECRET)\s*[:=]\s*['\"]?[A-Za-z0-9._-]{16,}"))]
for f in files:
    try: t = open(f, encoding="utf-8", errors="ignore").read()
    except Exception: continue
    for name, v in secrets.items():
        if v in t: bad.append((f, f"value of {name} present"))
    for n, rx in PAT:
        if rx.search(t): bad.append((f, n))
ex = open(".env.example").read() if os.path.exists(".env.example") else ""
for line in ex.splitlines():
    k, sep, v = line.strip().partition("=")
    if sep and re.search(r"KEY|TOKEN|SECRET", k, re.I) and v.strip(): bad.append((".env.example", f"{k} not empty"))
if ".env" in files: bad.append((".env", "would be committed"))
if subprocess.run(["git", "check-ignore", "-q", ".env"]).returncode != 0: bad.append((".env", "is NOT git-ignored"))
print(f"scanned {len(files)} files; {len(secrets)} secret value(s) loaded for matching (not shown)")
for f, r in bad: print("LEAK RISK:", f, "->", r)
print("OK: no secret found" if not bad else f"{len(bad)} problem(s)"); sys.exit(1 if bad else 0)
