#!/bin/bash
# Full advanced run with a REAL LLM. Usage: LLM=deepseek ./adv/run_all.sh   (needs DEEPSEEK_API_KEY in .env; never printed)
set -e; cd "$(dirname "$0")/.."; PY=.venv/bin/python; LLM=${LLM:-deepseek}
$PY adv/check_no_secrets.py
$PY adv/build_adv_benchmark.py >/dev/null && echo "benchmark rebuilt/verified"
for C in adv_dense adv_hybrid adv_hybrid_wide; do
  $PY adv/run_agent.py --config $C --split dev --llm $LLM --out adv/results/dev_$C.json | tee adv/results/dev_$C.log
done
$PY adv/select_config.py
SEL=$($PY -c "import json;print(json.load(open('adv/results/selected.json'))['selected'])")
if [ -f adv/results/test_final.json ] && [ -z "$FORCE_TEST" ]; then echo "test_final.json exists: test is run ONCE; set FORCE_TEST=1 only if you accept it is no longer an independent test"; exit 1; fi
$PY adv/run_agent.py --config $SEL --split test --llm $LLM --out adv/results/test_final.json | tee adv/results/test_final.log
$PY adv/summarize.py adv/results/test_final.json
$PY adv/make_review_sheet.py adv/results/test_final.json adv/results/review_test.md
$PY adv/check_no_secrets.py
echo "Next: read adv/results/review_test.md against the PDF, write adv/results/labels_test.json, then: $PY adv/score_test.py"
