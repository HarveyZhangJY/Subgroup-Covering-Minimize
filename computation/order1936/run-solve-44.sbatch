#!/bin/bash
#SBATCH --job-name=pq44-solve
#SBATCH --partition=Students
#SBATCH --qos=qos_stu_default
#SBATCH --cpus-per-task=4
#SBATCH --mem=16G
#SBATCH --time=04:00:00
#SBATCH --output=logs/slurm-solve-44-%j.out
#SBATCH --error=logs/slurm-solve-44-%j.err
set -euo pipefail
cd "$HOME/subgroup-cover/computation/order1936"
mkdir -p parts logs
PY="$HOME/venv-pq/bin/python"
"$PY" -c "import scipy; print('scipy', scipy.__version__)"
rm -f parts/covers-solve-*.jsonl parts/covers-solve-*.jsonl.err parts/sol-*.jsonl parts/sol-*.jsonl.err parts/sol-*.log parts/sol-*.log.err
split -n l/4 -d --additional-suffix=.jsonl covers-44.jsonl parts/covers-solve-
pids=()
for f in parts/covers-solve-*.jsonl; do
  base="$(basename "$f" .jsonl)"
  json="parts/sol-${base}.jsonl"
  log="parts/sol-${base}.log"
  "$PY" solve-covers.py "$f" 44 120 "$json" > "$log" 2> "$log.err" &
  pids+=($!)
done
fail=0
for p in "${pids[@]}"; do wait "$p" || fail=1; done
if [ "$fail" -ne 0 ]; then echo "one or more solver shards failed"; exit 1; fi
cat parts/sol-*.jsonl > solutions-44-unsorted.jsonl
"$PY" - <<'PY'
import json
from pathlib import Path
rows = [json.loads(line) for line in Path('solutions-44-unsorted.jsonl').read_text().splitlines() if line.strip()]
rows.sort(key=lambda d: d['id'])
Path('solutions-44.jsonl').write_text(
    '\n'.join(json.dumps(r, ensure_ascii=False) for r in rows) + '\n',
    encoding='utf-8')
print('merged', len(rows), 'solution records')
PY
"$PY" audit.py | tee audit.log
