#!/usr/bin/env python3
"""Exact 0-1 set cover for every exported SmallGroup(225,i) instance."""
import json
import time
from collections import Counter
from pathlib import Path

import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp
from scipy.sparse import lil_matrix

ROOT = Path(__file__).resolve().parent
N = 15
ORDER = N * N
records = []
for line in (ROOT / "covers-15.jsonl").read_text(encoding="utf-8").splitlines():
    if not line.strip():
        continue
    data = json.loads(line)
    subs = data["subs"]
    counts = Counter(e for sub in subs for e in sub)
    forced = [j for j, sub in enumerate(subs) if any(counts[e] == 1 for e in sub)]
    covered = set(counts)
    out = {
        "id": data["id"],
        "exp": data["exp"],
        "variables": len(subs),
        "union_size": len(covered),
        "uncovered_count": ORDER - len(covered),
        "forced_subgroups": forced,
    }
    if covered != set(range(ORDER)):
        out.update(status="no_cover", cover=None, bound=None,
                   reason="uncovered elements")
        records.append(out)
        print(json.dumps(out), flush=True)
        continue

    A = lil_matrix((ORDER, len(subs)), dtype=float)
    for j, sub in enumerate(subs):
        for e in sub:
            A[e, j] = 1
    start = time.time()
    result = milp(
        np.ones(len(subs)),
        integrality=np.ones(len(subs)),
        bounds=Bounds(0, 1),
        constraints=LinearConstraint(A.tocsr(), 1, np.inf),
        options={"time_limit": 60, "mip_rel_gap": 0, "presolve": True},
    )
    out.update(
        solver_status=int(result.status),
        solver_message=result.message,
        seconds=round(time.time() - start, 6),
        cover=None if result.x is None else round(float(result.fun)),
        bound=getattr(result, "mip_dual_bound", None),
    )
    if result.x is not None:
        out["selected"] = [j for j, x in enumerate(result.x) if x > 0.5]
        out["status"] = "optimal" if result.status == 0 else "nonoptimal_incumbent"
    else:
        out["status"] = "no_incumbent"
    records.append(out)
    print(json.dumps(out), flush=True)

with (ROOT / "solutions-15.jsonl").open("w", encoding="utf-8", newline="\n") as f:
    for record in records:
        f.write(json.dumps(record, separators=(",", ":")) + "\n")
