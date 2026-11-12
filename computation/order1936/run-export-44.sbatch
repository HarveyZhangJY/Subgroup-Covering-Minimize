#!/bin/bash
#SBATCH --job-name=pq44-export
#SBATCH --partition=Students
#SBATCH --qos=qos_stu_default
#SBATCH --cpus-per-task=4
#SBATCH --mem=16G
#SBATCH --time=04:00:00
#SBATCH --output=logs/slurm-export-44-%j.out
#SBATCH --error=logs/slurm-export-44-%j.err
set -euo pipefail
cd "$HOME/subgroup-cover/computation/order1936"
mkdir -p parts logs
GAP="$HOME/.conda/envs/gap/bin/gap"
pids=()
for k in $(seq 0 3); do
  lo=$(( k * 42 + 1 ))
  hi=$(( (k + 1) * 42 ))
  if [ "$hi" -gt 167 ]; then hi=167; fi
  if [ "$lo" -gt 167 ]; then continue; fi
  LO=$lo HI=$hi OUT="parts/covers-44-$k.jsonl" \
    "$GAP" -q -A export-covers.g > "parts/export-44-$k.log" 2>&1 &
  pids+=($!)
done
fail=0
for p in "${pids[@]}"; do wait "$p" || fail=1; done
if [ "$fail" -ne 0 ]; then echo "one or more GAP exports failed"; exit 1; fi
cat parts/covers-44-*.jsonl > covers-44.jsonl
cat parts/export-44-*.log > export-44.log
echo "export done: $(wc -l < covers-44.jsonl) groups, $(wc -l < export-44.log) log lines"
