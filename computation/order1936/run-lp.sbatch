#!/bin/bash
#SBATCH --job-name=pq44-lp
#SBATCH --partition=Students
#SBATCH --qos=qos_stu_default
#SBATCH --cpus-per-task=4
#SBATCH --mem=16G
#SBATCH --time=02:00:00
#SBATCH --output=logs/slurm-lp-44-%j.out
#SBATCH --error=logs/slurm-lp-44-%j.err
set -euo pipefail
cd "$HOME/subgroup-cover/computation/order1936"
"$HOME/venv-pq/bin/python" lp_bounds.py covers-44.jsonl lp-bounds-44.jsonl
