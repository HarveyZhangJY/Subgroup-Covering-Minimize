#!/usr/bin/env python3
"""Feasibility test: is there a cover of one166 with at most 59 subgroups?"""
import json, time
import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp
from scipy.sparse import coo_matrix, vstack

d = json.loads(open("one166.jsonl", encoding="utf-8").readline())
subs = d["subs"]
N = 1936
m = len(subs)
ri, ci = [], []
for j, s in enumerate(subs):
    for e in s:
        ri.append(e); ci.append(j)
A = coo_matrix((np.ones(len(ri)), (ri, ci)), shape=(N, m)).tocsr()
card = coo_matrix((np.ones(m), (np.zeros(m, dtype=int), np.arange(m))), shape=(1, m))
A2 = vstack([A, card]).tocsr()
lb = np.r_[np.ones(N), -np.inf]
ub = np.r_[np.full(N, np.inf), 59.0]
t0 = time.time()
res = milp(np.zeros(m), integrality=np.ones(m), bounds=Bounds(0, 1),
           constraints=LinearConstraint(A2, lb, ub),
           options={"time_limit": 300, "disp": True})
print("status", res.status, "message", res.message, "seconds", time.time()-t0, flush=True)
if res.x is not None:
    sel = [j for j, x in enumerate(res.x) if x > 0.5]
    union = set()
    for j in sel:
        union.update(subs[j])
    print("selected", len(sel), "union", len(union), flush=True)
    open("find59-selected.json", "w", encoding="utf-8").write(
        json.dumps({"id": d["id"], "selected": sel, "count": len(sel), "union": len(union)}))
else:
    print("no feasible solution returned", flush=True)
