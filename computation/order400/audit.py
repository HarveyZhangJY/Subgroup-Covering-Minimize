# Offline audit of the n = 20 computation.
#
# Reads only the saved files in this directory (export-20.log, covers-20.jsonl,
# solutions-20.jsonl) plus SHA256SUMS.txt; it does not run GAP or HiGHS.
#
# Checks:
#   * every SmallGroup(400, i), i = 1..221, is accounted for exactly once in
#     the export log, as "skip ... exp e" (e does not divide 20, so the group
#     cannot be covered by subgroups of order 20) or "done ... subs s";
#   * the exported set equals the set of groups whose exponent divides 20;
#   * each saved subgroup has exactly 20 distinct element labels in [0,400),
#     contains the identity label 0, and all its element orders divide 20;
#   * the recorded subgroup counts agree with the log;
#   * every saved selected set re-expands to a cover of all 400 elements, and
#     its size equals the recorded cover value;
#   * status 0 (proved optimal) has dual bound equal to the cover value;
#     time-outs keep a dual lower bound and are not counted as optimal.
#
# It then reports the global minimum over proved-optimal instances together
# with the structure / Sylow normality of the minimising groups.

import hashlib
import json
import math
import re
from pathlib import Path

root = Path(__file__).resolve().parent
ORDER = 400
n = 20
N = n * n
M = 221
COVERS = "covers-20.jsonl"
SOLUTIONS = "solutions-20.jsonl"
EXPORT_LOG = "export-20.log"
CANDIDATE = 205  # (C5:C4) x (C5:C4), the known 31-subgroup construction

# ---------------------------------------------------------------- hashes
sums = {}
for line in (root / "SHA256SUMS.txt").read_text(encoding="utf-8").splitlines():
    if not line.strip():
        continue
    digest, name = line.split()
    sums[name.lstrip("*")] = digest
for name in (COVERS, SOLUTIONS):
    if name in sums:
        actual = hashlib.sha256((root / name).read_bytes()).hexdigest()
        assert actual == sums[name], (name, actual, sums[name])
        print(f"SHA256 {name}: {actual} (matches SHA256SUMS.txt)")

# ---------------------------------------------------------------- export log
log_records = {}
for line in (root / EXPORT_LOG).read_text(encoding="utf-8", errors="replace").splitlines():
    match = re.fullmatch(r"(skip|done) %d (\d+)(?: exp (\d+)| subs (\d+))" % ORDER, line.strip())
    if match:
        action, group_id, exponent, subgroups = match.groups()
        group_id = int(group_id)
        assert group_id not in log_records, f"duplicate log line for {group_id}"
        log_records[group_id] = (
            action,
            int(exponent) if exponent else None,
            int(subgroups) if subgroups else None,
        )
assert set(log_records) == set(range(1, M + 1)), "export log does not cover 1..%d" % M
skipped = {i for i, rec in log_records.items() if rec[0] == "skip"}
done = {i for i, rec in log_records.items() if rec[0] == "done"}
assert len(skipped) + len(done) == M
for i in skipped:
    assert n % log_records[i][1] != 0, f"group {i} skipped although exponent divides n"
for i in done:
    # "done" log lines carry the subgroup count; the exponent is checked below
    # against the exported record.  Together with the skip test this proves that
    # the exported set is exactly {i : Exponent(G_i) divides n}.
    assert log_records[i][2] is not None

# ---------------------------------------------------------------- covers
covers_list = [
    json.loads(line) for line in (root / COVERS).read_text().splitlines() if line.strip()
]
covers = {r["id"]: r for r in covers_list}
assert len(covers_list) == len(covers) == len(done)
assert set(covers) == done
for i, rec in covers.items():
    assert n % rec["exp"] == 0
    assert len(rec["subs"]) == log_records[i][2]
    assert len(rec["orders"]) == N
    assert all(o > 0 and n % o == 0 for o in rec["orders"]), i
    normalized = []
    for subgroup in rec["subs"]:
        assert len(subgroup) == n == len(set(subgroup)), i
        assert all(type(e) is int and 0 <= e < N for e in subgroup), i
        assert 0 in subgroup, i
        assert all(n % rec["orders"][e] == 0 for e in subgroup), i
        normalized.append(tuple(sorted(subgroup)))
    assert len(set(normalized)) == len(normalized), f"duplicate subgroup in group {i}"

# ---------------------------------------------------------------- solutions
solutions_list = [
    json.loads(line) for line in (root / SOLUTIONS).read_text().splitlines() if line.strip()
]
solutions = {r["id"]: r for r in solutions_list}
assert len(solutions_list) == len(solutions) == len(covers)
assert set(solutions) == set(covers)

uncoverable, optimal, timeouts = set(), set(), set()
certificates = {}
for i, sol in solutions.items():
    rec = covers[i]
    assert sol["variables"] == len(rec["subs"]) and sol["exp"] == rec["exp"]
    if sol.get("reason") == "uncovered elements":
        assert sol["cover"] is None and "selected" not in sol
        union = set().union(*(set(s) for s in rec["subs"])) if rec["subs"] else set()
        assert union != set(range(N))
        assert sol["uncovered_count"] == N - len(union)
        uncoverable.add(i)
        continue
    selected = sol["selected"]
    assert len(selected) == len(set(selected)) == sol["cover"]
    assert all(type(j) is int and 0 <= j < sol["variables"] for j in selected)
    union = set().union(*(set(rec["subs"][j]) for j in selected))
    assert union == set(range(N)), f"selected cover of group {i} is not a cover"
    certificates[i] = selected
    if sol["status"] == 0:
        assert math.isclose(sol["bound"], sol["cover"], rel_tol=0, abs_tol=1e-8), i
        optimal.add(i)
    else:
        assert sol["status"] == 1
        assert sol["bound"] is not None and sol["bound"] <= sol["cover"] + 1e-6, i
        timeouts.add(i)
assert len(uncoverable) + len(optimal) + len(timeouts) == len(solutions)

# ---------------------------------------------------------------- report
print(
    f"{ORDER}-group summary: exponent-excluded={len(skipped)}, exported={len(done)}, "
    f"noncoverable={len(uncoverable)}, coverable={len(optimal) + len(timeouts)}"
)
print(f"Solver summary: optimal={len(optimal)}, timeout={len(timeouts)}")

distribution = {}
for i in optimal:
    distribution.setdefault(solutions[i]["cover"], []).append(i)
print("Distribution of proved-optimal cover values (value: count, ids):")
for value in sorted(distribution):
    ids = sorted(distribution[value])
    shown = ids if len(ids) <= 12 else ids[:12] + ["..."]
    print(f"  {value:3d}: {len(ids):3d}  {shown}")

upper = {i: solutions[i]["cover"] for i in timeouts}
print(
    "Time-out intervals (cover is a constructed upper bound, lower_bound is certified): "
    + ", ".join(f"{i}:[{lower_bound}, {upper[i]}]" for i, lower_bound in
                sorted((i, solutions[i]["lower_bound"]) for i in timeouts))
)

for i in sorted(timeouts):
    sol = solutions[i]
    print(
        f"TIMEOUT SmallGroup({ORDER},{i}): status={sol['status']}, dual lower bound="
        f"{sol['bound']:.6f} (ceil {sol['lower_bound']}), constructed cover={sol['cover']}"
    )

if uncoverable:
    print(f"Noncoverable groups ({len(uncoverable)}):")
    for i in sorted(uncoverable):
        sol = solutions[i]
        print(
            f"  SmallGroup({ORDER},{i}) exp={sol['exp']} vars={sol['variables']} "
            f"missing={sol['uncovered_count']} element orders={sol['uncovered_orders']} "
            f"| {covers[i]['structure']}"
        )

global_min = min(solutions[i]["cover"] for i in optimal)
min_ids = sorted(i for i in optimal if solutions[i]["cover"] == global_min)
assert all(solutions[i]["lower_bound"] >= global_min for i in timeouts
           if solutions[i]["lower_bound"] is not None), "a time-out could be below the minimum"
certified_lower = min(
    [solutions[i]["cover"] for i in optimal]
    + [solutions[i]["lower_bound"] for i in timeouts if solutions[i]["lower_bound"] is not None]
)
print(
    f"GLOBAL MINIMUM (proved): {global_min}, attained by {len(min_ids)} group(s): {min_ids}; "
    f"certified global lower bound={certified_lower}"
)
assert certified_lower == global_min
for i in min_ids:
    rec, sol = covers[i], solutions[i]
    print(
        f"MIN SmallGroup({ORDER},{i}): status={sol['status']}, cover={sol['cover']}, "
        f"dual_bound={sol['bound']}, union={N}/{N}, exp={rec['exp']}"
    )
    print(
        f"  structure={rec['structure']}  Sylow({rec['p']}) normal={rec['sylow_p_normal']}  "
        f"Sylow({rec['q']}) normal={rec['sylow_q_normal']}  variables={sol['variables']}"
    )
    print(f"  selected={certificates[i]}")

for label, subset in (
    ("Sylow q normal", {i for i in optimal if covers[i]["sylow_q_normal"]}),
    ("Sylow q not normal", {i for i in optimal if not covers[i]["sylow_q_normal"]}),
):
    if subset:
        print(
            f"{label}: {len(subset)} proved-optimal groups, min="
            f"{min(solutions[i]['cover'] for i in subset)}"
        )

rec, sol = covers[CANDIDATE], solutions[CANDIDATE]
print(
    f"Candidate SmallGroup({ORDER},{CANDIDATE}) = {rec['structure']}: "
    f"status={sol['status']}, cover={sol['cover']}, dual_bound={sol['bound']}, "
    f"vars={sol['variables']}, union={N}/{N}"
)

# Regression guard on the numbers recorded in verification.md.  It does not
# replace the checks above; it only pins the reported figures so that a later
# edit of the saved data cannot silently change the conclusion.
EXPECTED = {"global_min": 30, "min_ids": [221], "skipped": 125, "exported": 96, "uncoverable": 1, "timeouts": 3}
assert global_min == EXPECTED["global_min"], (global_min, EXPECTED["global_min"])
assert min_ids == EXPECTED["min_ids"], (min_ids, EXPECTED["min_ids"])
assert len(skipped) == EXPECTED["skipped"]
assert len(done) == EXPECTED["exported"]
assert len(uncoverable) == EXPECTED["uncoverable"]
assert len(timeouts) == EXPECTED["timeouts"]
print("Regression guard: matches the figures recorded in verification.md")

print(
    "AUDIT RESULT: PASS; all %d groups are accounted for and every saved selected "
    "cover was re-expanded and checked without rerunning GAP or HiGHS." % M
)
