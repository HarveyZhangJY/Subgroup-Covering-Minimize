#!/bin/bash
set -u
cd "$(dirname "$0")"
mkdir -p logs
PY="$HOME/venv-pq/bin/python"
FIX=55
SCIP_TIME=14400 SCIP_THREADS=8 FIX_INDEX=$FIX "$PY" scip_166_platform.py > logs/scip_fix.log 2>&1 &
p1=$!
SCIP_TIME=14400 SCIP_THREADS=8 SCIP_RADIUS=10 FIX_INDEX=$FIX "$PY" scip_166_platform.py > logs/scip_fix_r10.log 2>&1 &
p2=$!
CP_TIME=14400 CP_WORKERS=8 CP_MODE=feas FIX_INDEX=$FIX "$PY" cp_sat_166_platform.py > logs/cp_fix_feas.log 2>&1 &
p3=$!
CP_TIME=14400 CP_WORKERS=8 CP_MODE=min FIX_INDEX=$FIX "$PY" cp_sat_166_platform.py > logs/cp_fix_min.log 2>&1 &
p4=$!
wait "$p1" "$p2" "$p3" "$p4"
echo FIXED_CAMPAIGN_DONE
