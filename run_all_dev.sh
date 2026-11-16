#!/bin/bash
cd "$(dirname "$0")"
PY=.venv/bin/python
$PY run_agent.py --config base_dense  --split dev --out results/agent/dev_base_dense.json  > results/agent/dev_base_dense.log 2>&1
$PY run_agent.py --config base_bm25   --split dev --out results/agent/dev_base_bm25.json   > results/agent/dev_base_bm25.log 2>&1
$PY run_agent.py --config base_hybrid --split dev --out results/agent/dev_base_hybrid.json > results/agent/dev_base_hybrid.log 2>&1
$PY run_agent.py --config imp_topk5 --base base_hybrid --set top_k=5 budget=4000 --split dev --out results/agent/dev_imp_topk5.json > results/agent/dev_imp_topk5.log 2>&1
$PY run_agent.py --config imp_neighbors --base base_hybrid --set budget=4000 neighbors=true max_searches=3 --split dev --out results/agent/dev_imp_neighbors.json > results/agent/dev_imp_neighbors.log 2>&1
echo DONE > results/agent/dev_done.flag
