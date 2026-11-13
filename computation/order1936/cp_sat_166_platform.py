import json, os, time
from pathlib import Path
from ortools.sat.python import cp_model

d = json.loads(Path("one166.jsonl").read_text(encoding="utf-8").splitlines()[0])
subs = d["subs"]
N = 1936
m = len(subs)
mode = os.environ.get("CP_MODE", "feas")
print("vars", m, "N", N, "mode", mode, flush=True)
incidence = [[] for _ in range(N)]
for j, s in enumerate(subs):
    for e in s:
        incidence[e].append(j)
model = cp_model.CpModel()
x = [model.NewBoolVar(f"x{j}") for j in range(m)]
fix = os.environ.get("FIX_INDEX")
if fix:
    model.Add(x[int(fix)] == 1)
    print("fixed subgroup", fix, flush=True)
for e in range(N):
    model.Add(sum(x[j] for j in incidence[e]) >= 1)
if mode == "min":
    model.Add(sum(x) <= 60)
    model.Minimize(sum(x))
else:
    model.Add(sum(x) <= 59)
solver = cp_model.CpSolver()
solver.parameters.max_time_in_seconds = float(os.environ.get("CP_TIME", "7200"))
solver.parameters.num_search_workers = int(os.environ.get("CP_WORKERS", "8"))
solver.parameters.log_search_progress = False
t0 = time.time()
status = solver.Solve(model)
print("status", solver.StatusName(status), "sec", round(time.time() - t0, 2), flush=True)
if status in (cp_model.OPTIMAL, cp_model.FEASIBLE):
    sel = [j for j in range(m) if solver.Value(x[j])]
    union = set()
    for j in sel:
        union.update(subs[j])
    print("selected", len(sel), "union", len(union), flush=True)
    if union == set(range(N)):
        Path("cp166_best.json").write_text(json.dumps(
            {"id": 166, "count": len(sel), "selected": sel, "union": len(union),
             "status": solver.StatusName(status)}))
        print("SAVED", flush=True)
elif status == cp_model.INFEASIBLE:
    print("PROVED NO COVER WITH <=59 SUBGROUPS", flush=True)
