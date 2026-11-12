#!/usr/bin/env python3
"""Exact 0-1 set-cover solve for n=18 (SmallGroups of order 324).

Reads covers-18.jsonl (one group per line, all subgroups of order 18 as
0-based element index lists), checks the naive union first, and solves the
minimum cover exactly with scipy.optimize.milp (HiGHS) with mip_rel_gap=0.
Each group gets a 120 second time limit; a time limit hit is recorded with
status 1 and the solver dual bound, and is never treated as optimal.
"""

import json
import math
import sys
import time

import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp
from scipy.sparse import lil_matrix

covers_path = sys.argv[1] if len(sys.argv) > 1 else "covers-18.jsonl"
n = int(sys.argv[2]) if len(sys.argv) > 2 else 18
time_limit = float(sys.argv[3]) if len(sys.argv) > 3 else 120.0
out_path = sys.argv[4] if len(sys.argv) > 4 else "solutions-18.jsonl"

out = open(out_path, "w", encoding="utf-8")
records = 0
for line in open(covers_path, encoding="utf-8"):
    line = line.strip()
    if not line:
        continue
    d = json.loads(line)
    subs = d["subs"]
    universe = set(range(n * n))
    covered = set().union(*(set(s) for s in subs)) if subs else set()
    if covered != universe:
        rec = {
            "id": d["id"],
            "exp": d["exp"],
            "nsubgroups": len(subs),
            "variables": len(subs),
            "cover": None,
            "reason": "uncovered elements",
            "uncovered": len(universe - covered),
            "seconds": 0.0,
        }
        out.write(json.dumps(rec) + "\n")
        out.flush()
        print(
            f"id {d['id']:3d}: NOT COVERABLE by its {len(subs)} subgroups of order {n} "
            f"({len(universe - covered)} elements uncovered)",
            flush=True,
        )
        records += 1
        continue

    m = len(subs)
    A = lil_matrix((n * n, m), dtype=float)
    for j, s in enumerate(subs):
        for e in s:
            A[e, j] = 1.0
    A = A.tocsr()

    t0 = time.time()
    res = milp(
        np.ones(m),
        integrality=np.ones(m),
        bounds=Bounds(0, 1),
        constraints=LinearConstraint(A, 1, np.inf),
        options={"time_limit": time_limit, "mip_rel_gap": 0, "presolve": True},
    )
    elapsed = round(time.time() - t0, 3)
    rec = {
        "id": d["id"],
        "exp": d["exp"],
        "nsubgroups": m,
        "variables": m,
        "status": int(res.status),
        "message": str(res.message),
        "cover": None if res.fun is None else int(round(float(res.fun))),
        "bound": None
        if getattr(res, "mip_dual_bound", None) is None
        else float(res.mip_dual_bound),
        "gap": None if getattr(res, "mip_gap", None) is None else float(res.mip_gap),
        "seconds": elapsed,
    }
    if res.x is not None:
        selected = [int(j) for j, x in enumerate(res.x) if x > 0.5]
        rec["selected"] = selected
        union = set().union(*(set(subs[j]) for j in selected))
        rec["union_size"] = len(union)
        assert union == universe, d["id"]
        assert len(selected) == rec["cover"], d["id"]
    out.write(json.dumps(rec) + "\n")
    out.flush()
    records += 1
    if rec["cover"] is not None:
        status = "OPT" if rec["status"] == 0 else f"TIMEOUT(status={rec['status']})"
        print(
            f"id {d['id']:3d}: vars={m:3d} cover={rec['cover']} bound={rec['bound']:.6f} "
            f"{status} {elapsed:.2f}s",
            flush=True,
        )
    else:
        print(f"id {d['id']:3d}: no solution {rec['message']} {elapsed:.2f}s", flush=True)

out.close()
print(f"solved {records} exported groups -> {out_path}", flush=True)
