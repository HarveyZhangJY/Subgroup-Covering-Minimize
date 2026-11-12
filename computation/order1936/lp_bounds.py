#!/usr/bin/env python3
"""Valid LP lower bounds for the order-44 covering instances.

For each saved group, solve the LP relaxation of the 0-1 set cover:
min sum x_j,  A x >= 1,  0 <= x_j <= 1.
Its optimum is a certified lower bound for the integer covering number.
This is much faster than proving exact MILP optimality on hard instances.
"""

import json
import math
import sys
import time
from pathlib import Path

import numpy as np
from scipy.optimize import linprog
from scipy.sparse import coo_matrix

n = 44
N = n * n
covers_path = Path(sys.argv[1])
out_path = Path(sys.argv[2])
out = open(out_path, "w", encoding="utf-8")
records = []

for line in covers_path.read_text(encoding="utf-8").splitlines():
    if not line.strip():
        continue
    d = json.loads(line)
    subs = d["subs"]
    m = len(subs)
    covered = set().union(*(set(s) for s in subs)) if subs else set()
    rec = {"id": d["id"], "exp": d["exp"], "variables": m}
    if covered != set(range(N)):
        rec.update({"lp": None, "reason": "uncovered elements",
                    "uncovered": len(set(range(N)) - covered)})
        out.write(json.dumps(rec) + "\n")
        out.flush()
        print(f"id {d['id']:4d}: UNCOVERABLE ({rec['uncovered']} missing)", flush=True)
        continue
    rows, cols = [], []
    for j, s in enumerate(subs):
        for e in s:
            rows.append(e)
            cols.append(j)
    A = coo_matrix((np.ones(len(rows)), (rows, cols)), shape=(N, m)).tocsr()
    t0 = time.time()
    res = linprog(np.ones(m), A_ub=-A, b_ub=-np.ones(N),
                  bounds=(0, 1), method="highs")
    el = round(time.time() - t0, 3)
    if not res.success:
        rec.update({"lp": None, "reason": str(res.message), "seconds": el})
        out.write(json.dumps(rec) + "\n")
        out.flush()
        print(f"id {d['id']:4d}: LP FAILED {res.message}", flush=True)
        continue
    lp = float(res.fun)
    rec.update({"lp": lp, "ceil": math.ceil(lp - 1e-6), "seconds": el})
    out.write(json.dumps(rec) + "\n")
    out.flush()
    records.append(rec)
    print(f"id {d['id']:4d}: vars {m:5d} LP {lp:.6f} ceil {rec['ceil']} {el:.2f}s",
          flush=True)

out.close()
if records:
    best = min(r["ceil"] for r in records)
    print(f"MIN LP CEIL = {best}; groups with LP ceil < 60: "
          f"{[r['id'] for r in records if r['ceil'] < 60]}", flush=True)
print(f"wrote {len(records)} LP records to {out_path}", flush=True)
