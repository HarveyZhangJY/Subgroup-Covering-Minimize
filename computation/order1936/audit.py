import json
import re
import sys
from pathlib import Path

n = 44
N = 1936
total_groups = 167
root = Path(__file__).resolve().parent

done = {}
skipped = {}
log_path = root / "export-44.log"
for line in log_path.read_text(encoding="utf-8").splitlines():
    m = re.fullmatch(r"done 1936 (\d+) subs (\d+)", line.strip())
    if m:
        done[int(m.group(1))] = int(m.group(2))
        continue
    m = re.fullmatch(r"skip 1936 (\d+) exp (\d+)", line.strip())
    if m:
        skipped[int(m.group(1))] = int(m.group(2))

all_ids = set(range(1, total_groups + 1))
if set(done) & set(skipped):
    sys.exit("FAIL: id both done and skipped")
if set(done) | set(skipped) != all_ids:
    sys.exit(f"FAIL: ids missing: {sorted(all_ids - set(done) - set(skipped))[:10]}")
for i, e in skipped.items():
    if n % e == 0:
        sys.exit(f"FAIL: id {i} skipped but exponent {e} divides {n}")

covers = {}
for line in (root / "covers-44.jsonl").read_text(encoding="utf-8").splitlines():
    if not line.strip():
        continue
    d = json.loads(line)
    covers[d["id"]] = d
if set(covers) != set(done):
    sys.exit(f"FAIL: exported ids differ: covers={len(covers)} log={len(done)}")

for i, d in covers.items():
    if d["exp"] != skipped.get(i) and i in skipped:
        sys.exit(f"FAIL: id {i} has inconsistent exponent")
    orders = d["orders"]
    if len(orders) != N:
        sys.exit(f"FAIL: id {i} has {len(orders)} element orders")
    if len(d["subs"]) != done[i]:
        sys.exit(f"FAIL: id {i} subs {len(d['subs'])} log {done[i]}")
    seen = set()
    for s in d["subs"]:
        if len(s) != n or len(set(s)) != n:
            sys.exit(f"FAIL: id {i} bad subgroup size")
        if 0 not in s:
            sys.exit(f"FAIL: id {i} subgroup lacks identity")
        if not all(0 <= x < N for x in s):
            sys.exit(f"FAIL: id {i} index out of range")
        if not all(n % orders[x] == 0 for x in s):
            sys.exit(f"FAIL: id {i} subgroup contains element of order not dividing {n}")
        key = tuple(sorted(s))
        if key in seen:
            sys.exit(f"FAIL: id {i} duplicate subgroup")
        seen.add(key)

solutions = {}
for line in (root / "solutions-44.jsonl").read_text(encoding="utf-8").splitlines():
    if not line.strip():
        continue
    d = json.loads(line)
    solutions[d["id"]] = d
if set(solutions) != set(covers):
    missing = sorted(set(covers) - set(solutions))[:10]
    sys.exit(f"FAIL: no solution record for ids {missing}")

finite = {}
lower = {}
for i, d in solutions.items():
    if d.get("cover") is not None:
        if len(d["selected"]) != d["cover"]:
            sys.exit(f"FAIL: id {i} selected count")
        union = set()
        for j in d["selected"]:
            union.update(covers[i]["subs"][j])
        if union != set(range(N)):
            sys.exit(f"FAIL: id {i} selected union {len(union)}/{N}")
        finite[i] = d["cover"]
    if d.get("status") == 0:
        if d.get("cover") is None or abs(float(d["bound"]) - d["cover"]) > 1e-6:
            sys.exit(f"FAIL: id {i} optimal record bound mismatch")
        lower[i] = d["cover"]
    elif d.get("bound") is not None:
        lower[i] = float(d["bound"])

if not finite:
    sys.exit("FAIL: no finite cover")
best = min(finite.values())
best_ids = sorted(i for i, v in finite.items() if v == best)
certified_lb = min(lower.values()) if lower else None
if certified_lb is None or certified_lb < best:
    print(f"WARNING: global minimum {best} not certified by bounds (lb={certified_lb})")
else:
    print(f"GLOBAL MINIMUM (proved): {best}, attained by {len(best_ids)} group(s): {best_ids}")
    print(f"certified global lower bound={certified_lb}")

for i in best_ids:
    d = solutions[i]
    print(f"MIN SmallGroup(1936,{i}): status={d.get('status')}, cover={d.get('cover')}, "
          f"dual_bound={d.get('bound')}, union={N}/{N}, exp={covers[i]['exp']}")
    print(f"  structure={covers[i].get('structure')}  "
          f"Sylow(11) normal={covers[i].get('sylow_p_normal')}  "
          f"Sylow(2) normal={covers[i].get('sylow_q_normal')}")
    print(f"  selected={d.get('selected')}")

dist = {}
for v in finite.values():
    dist[v] = dist.get(v, 0) + 1
print("finite cover distribution:", dict(sorted(dist.items())))
print("status counts:", {s: sum(1 for d in solutions.values() if d.get("status") == s)
                         for s in sorted({d.get("status") for d in solutions.values()})})
print("AUDIT RESULT: PASS" if certified_lb is not None and certified_lb >= best else "AUDIT RESULT: INCOMPLETE")
