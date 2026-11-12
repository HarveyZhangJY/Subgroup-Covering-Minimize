import json, sys, time
from pathlib import Path
from pyscipopt import Model, quicksum

path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(r"C:\Users\Felix\AppData\Local\Temp\covers-44.jsonl")
d = None
for line in path.read_text(encoding="utf-8").splitlines():
    if not line.strip():
        continue
    rec = json.loads(line)
    if rec["id"] == 166:
        d = rec
        break
assert d is not None
N = 1936
subs = d["subs"]
m = len(subs)
print("vars", m, "N", N, flush=True)
incidence = [[] for _ in range(N)]
for j, s in enumerate(subs):
    for e in s:
        incidence[e].append(j)

model = Model("cover166")
model.hideOutput(False)
model.setParam("limits/time", 600.0)
model.setParam("parallel/maxnthreads", 4)
model.setParam("display/verblevel", 4)
x = [model.addVar(vtype="B", lb=0, ub=1, name=f"x{j}") for j in range(m)]
for e in range(N):
    model.addCons(quicksum(x[j] for j in incidence[e]) >= 1)
model.addCons(quicksum(x) <= 60)
model.setObjective(quicksum(x), "minimize")
# warm start from the known 60-cover
import os as _os
_warm_path = r"C:\Users\Felix\AppData\Local\Temp\t1_166_60_full.json"
if _os.path.exists(_warm_path):
    _warm = json.loads(open(_warm_path, encoding="utf-8").read())["selected"]
    _sol = model.createSol()
    for _j in _warm:
        model.setSolVal(_sol, x[_j], 1.0)
    model.addSol(_sol)
    print("added warm start", len(_warm), flush=True)
t0 = time.time()
model.optimize()
print("status", model.getStatus(), "sec", round(time.time()-t0, 2), flush=True)
if model.getNSols() > 0:
    sol = model.getBestSol()
    sel = [j for j in range(m) if model.getSolVal(sol, x[j]) > 0.5]
    union = set()
    for j in sel:
        union.update(subs[j])
    print("best", model.getObjVal(), "selected", len(sel), "union", len(union), flush=True)
    if union == set(range(N)):
        Path(r"C:\Users\Felix\AppData\Local\Temp\scip166.json").write_text(
            json.dumps({"id": 166, "count": len(sel), "selected": sel, "union": len(union),
                        "status": model.getStatus(), "objective": model.getObjVal()}))
        print("SAVED", flush=True)
print("dualbound", model.getDualbound(), flush=True)
