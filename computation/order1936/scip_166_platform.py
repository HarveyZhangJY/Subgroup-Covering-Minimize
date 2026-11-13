import json, os, time
from pathlib import Path
from pyscipopt import Model, quicksum

d = json.loads(Path("one166.jsonl").read_text(encoding="utf-8").splitlines()[0])
subs = d["subs"]
N = 1936
m = len(subs)
print("vars", m, "N", N, flush=True)
incidence = [[] for _ in range(N)]
for j, s in enumerate(subs):
    for e in s:
        incidence[e].append(j)

model = Model("cover166")
model.hideOutput(False)
model.setParam("limits/time", float(os.environ.get("SCIP_TIME", "7200")))
model.setParam("parallel/maxnthreads", int(os.environ.get("SCIP_THREADS", "8")))
model.setParam("display/verblevel", 4)
x = [model.addVar(vtype="B", lb=0, ub=1, name=f"x{j}") for j in range(m)]
fix = os.environ.get("FIX_INDEX")
if fix:
    model.addCons(x[int(fix)] == 1)
    print("fixed subgroup", fix, flush=True)
for e in range(N):
    model.addCons(quicksum(x[j] for j in incidence[e]) >= 1)
model.addCons(quicksum(x) <= 60)
warm = []
wp = Path("warm166.json")
if wp.exists():
    warm = json.loads(wp.read_text(encoding="utf-8"))["selected"]
    sol = model.createSol()
    for j in warm:
        model.setSolVal(sol, x[j], 1.0)
    model.addSol(sol)
    print("warm", len(warm), flush=True)
radius = os.environ.get("SCIP_RADIUS")
if radius and warm:
    ws = set(warm)
    expr = quicksum(1 - x[j] for j in warm) + quicksum(x[j] for j in range(m) if j not in ws)
    model.addCons(expr <= int(radius))
    print("local branching radius", radius, flush=True)
model.setObjective(quicksum(x), "minimize")
t0 = time.time()
model.optimize()
print("status", model.getStatus(), "sec", round(time.time() - t0, 2), flush=True)
if model.getNSols() > 0:
    sol = model.getBestSol()
    sel = [j for j in range(m) if model.getSolVal(sol, x[j]) > 0.5]
    union = set()
    for j in sel:
        union.update(subs[j])
    print("best", model.getObjVal(), "selected", len(sel), "union", len(union), flush=True)
    Path("scip166_best" + os.environ.get("SCIP_TAG","") + ".json").write_text(json.dumps(
        {"id": 166, "count": len(sel), "selected": sel, "union": len(union),
         "status": model.getStatus(), "objective": model.getObjVal()}))
print("dualbound", model.getDualbound(), flush=True)
