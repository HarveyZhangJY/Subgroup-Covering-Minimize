import hashlib
import json
import math
import re
from pathlib import Path

root = Path(__file__).resolve().parent
expected_hashes = {
    "covers-12.jsonl": "5af630fdc06e680b7ef107ade80fc5c501160fd4d7a8aae30568b105d2b5d22f",
    "solutions-12.jsonl": "695d9b5cb41520a86f7ac1b43af755426c64d8a8daf816ee254e721293980125",
}
for name, expected in expected_hashes.items():
    actual = hashlib.sha256((root / name).read_bytes()).hexdigest()
    assert actual == expected, (name, actual, expected)
    print(f"SHA256 {name}: {actual} (matches partition-approach.md)")

log_records = {}
for line in (root / "export-12.log").read_text(encoding="utf-8", errors="replace").splitlines():
    match = re.fullmatch(r"(skip|done) 144 (\d+)(?: exp (\d+)| subs (\d+))", line.strip())
    if match:
        action, group_id, exponent, subgroups = match.groups()
        group_id = int(group_id)
        assert group_id not in log_records
        log_records[group_id] = (
            action,
            int(exponent) if exponent else None,
            int(subgroups) if subgroups else None,
        )
assert set(log_records) == set(range(1, 198))
skipped = {i for i, record in log_records.items() if record[0] == "skip"}
done = {i for i, record in log_records.items() if record[0] == "done"}
assert len(skipped) == 108 and len(done) == 89
for i in skipped:
    assert 12 % log_records[i][1] != 0

covers_list = [
    json.loads(line)
    for line in (root / "covers-12.jsonl").read_text().splitlines()
    if line.strip()
]
covers = {record["id"]: record for record in covers_list}
assert len(covers_list) == len(covers) == 89
assert set(covers) == done
for i, record in covers.items():
    assert 12 % record["exp"] == 0
    assert len(record["subs"]) == log_records[i][2]
    normalized = []
    for subgroup in record["subs"]:
        assert len(subgroup) == len(set(subgroup)) == 12
        assert 0 in subgroup
        assert all(type(element) is int and 0 <= element < 144 for element in subgroup)
        normalized.append(tuple(sorted(subgroup)))
    assert len(set(normalized)) == len(normalized)

solutions_list = [
    json.loads(line)
    for line in (root / "solutions-12.jsonl").read_text().splitlines()
    if line.strip()
]
solutions = {record["id"]: record for record in solutions_list}
assert len(solutions_list) == len(solutions) == 89
assert set(solutions) == set(covers)
uncoverable = set()
optimal = set()
timeouts = set()
certificates = {}
for i, solution in solutions.items():
    cover_record = covers[i]
    assert solution["variables"] == len(cover_record["subs"])
    assert solution["exp"] == cover_record["exp"]
    if solution.get("reason") == "uncovered elements":
        assert solution["cover"] is None and "selected" not in solution
        union = (
            set().union(*(set(s) for s in cover_record["subs"]))
            if cover_record["subs"]
            else set()
        )
        assert union != set(range(144))
        uncoverable.add(i)
        continue
    selected = solution["selected"]
    assert len(selected) == len(set(selected)) == solution["cover"]
    assert all(type(j) is int and 0 <= j < solution["variables"] for j in selected)
    union = set().union(*(set(cover_record["subs"][j]) for j in selected))
    assert union == set(range(144)), i
    certificates[i] = selected
    if solution["status"] == 0:
        assert math.isclose(solution["bound"], solution["cover"], rel_tol=0, abs_tol=1e-8)
        optimal.add(i)
    else:
        timeouts.add(i)

assert len(uncoverable) == 15
assert len(optimal) == 73 and timeouts == {196}
optimal_17 = {i for i in optimal if solutions[i]["cover"] == 17}
assert optimal_17 == {184, 193, 194}
assert all(solutions[i]["cover"] >= 18 for i in optimal - optimal_17)
assert solutions[196]["status"] == 1
assert solutions[196]["cover"] == 20 and solutions[196]["bound"] >= 18
assert solutions[101]["cover"] == 24 and solutions[101]["status"] == 0
assert min(solutions[i]["cover"] for i in optimal) == 17
assert all(solutions[i]["bound"] > 17 for i in timeouts)

print(
    f"197-group summary: exponent-excluded={len(skipped)}, exported={len(done)}, "
    f"noncoverable={len(uncoverable)}, coverable={len(optimal | timeouts)}"
)
print(
    f"Solver summary: optimal={len(optimal)}, timeout={len(timeouts)}, "
    f"optimal value 17={sorted(optimal_17)}, optimal values >=18={len(optimal - optimal_17)}"
)
print(
    f"Timeout: SmallGroup(144,196), status={solutions[196]['status']}, "
    f"dual lower bound={solutions[196]['bound']}, constructed cover={solutions[196]['cover']}"
)
print(f"Fixed-group check: SmallGroup(144,101), optimal={solutions[101]['cover']}")
for i in sorted(optimal_17):
    solution = solutions[i]
    print(
        f"CERT17 SmallGroup(144,{i}): status={solution['status']}, "
        f"cover={solution['cover']}, dual_bound={solution['bound']}, union=144/144"
    )
    print(f"  selected={certificates[i]}")
print(
    "AUDIT RESULT: PASS; all 197 groups are accounted for and every saved selected "
    "cover was re-expanded and checked without rerunning GAP or HiGHS."
)
