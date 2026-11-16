#!/bin/bash
cd "$(dirname "$0")"; PY=.venv/bin/python
$PY run_agent.py --config base_dense --split test --out results/agent/test_base_dense.json > results/agent/test_base_dense.log 2>&1
$PY run_agent.py --config imp_topk5 --base base_hybrid --set top_k=5 budget=4000 --split test --out results/agent/test_imp_topk5.json > results/agent/test_imp_topk5.log 2>&1
echo DONE > results/agent/test_done.flag
