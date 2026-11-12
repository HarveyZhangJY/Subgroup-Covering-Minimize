import json, sys, time
from pathlib import Path
from ortools.sat.python import cp_model

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

model = cp_model.CpModel()
x = [model.NewBoolVar(f"x{j}") for j in range(m)]
for e in range(N):
    model.Add(sum(x[j] for j in incidence[e]) >= 1)
model.Add(sum(x) <= 59)
solver = cp_model.CpSolver()
solver.parameters.max_time_in_seconds = 600
solver.parameters.num_search_workers = 8
solver.parameters.log_search_progress = False
t0 = time.time()
status = solver.Solve(model)
print("status", solver.StatusName(status), "sec", round(time.time()-t0, 2), flush=True)
if status in (cp_model.OPTIMAL, cp_model.FEASIBLE):
    sel = [j for j in range(m) if solver.Value(x[j])]
    union = set()
    for j in sel:
        union.update(subs[j])
    print("selected", len(sel), "union", len(union), flush=True)
    if union == set(range(N)) and len(sel) <= 59:
        Path(r"C:\Users\Felix\AppData\Local\Temp\cp59-166.json").write_text(
            json.dumps({"id": 166, "count": len(sel), "selected": sel, "union": len(union)}))
        print("SAVED", flush=True)
elif status == cp_model.INFEASIBLE:
    print("PROVED NO COVER WITH <=59 SUBGROUPS", flush=True)
