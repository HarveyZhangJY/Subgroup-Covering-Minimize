# Computation archive

This directory contains the reproducible part of the subgroup-covering experiments. It deliberately excludes the local GAP source tree, package archives, downloaded HTML cache, and font files.

## Quick offline checks

From the repository root:

```bash
python -m pip install -r requirements.txt
python computation/verify_all.py
python computation/order144/audit.py
python computation/order225/audit.py
```

These commands read the saved subgroups and witness masks. They do not enumerate groups or rerun integer programming.

## Small and medium order scripts

- `prime_power_spreads.py`: constructs the \(n+1\) one-dimensional-subspace cover for \(n=2,3,4,5,7,8,9\).
- `order36_exhaustive.py`: reconstructs all 14 groups of order 36 from public GroupNames permutation generators, enumerates all order-6 subgroups, and solves the exact set-cover MILP.
- `composite_constructions.py`: order-100 classification and order-144 product constructions used in the early stage.
- `order144_products.py`: additional order-144 product constructions.
- `verify_all.py`: rechecks every saved witness mask for subgroup size, stated \(m\), and full-group union.

The order-36 script may download public GroupNames pages into `groupnames_cache/` on its first run.

Outputs include:

- `prime_power_results.json`
- `order36_results.json`
- `composite_results.json`
- `order144_product_results.json`
- corresponding `*_run.log` files and `verification.log`

## Complete certificates

### Order 144 (\(n=12\))

`order144/` contains the GAP export of all order-12 subgroups for the 89 candidate groups, the exact MILP records for all 89, and a standalone offline audit. The audit verifies all 197 group IDs are accounted for, the 15 non-coverable candidates, the 73 exact optima, and the one timeout with certified lower bound 18. The three optimal-17 certificates are re-expanded to \(144/144\) elements.

```bash
cd computation/order144
sha256sum -c SHA256SUMS.txt
python audit.py
```

See `order144/verification.md` for methodology and full rerun instructions.

### Order 225 (\(n=15\))

`order225/` contains all 6 groups of order 225, all order-15 subgroups, exact MILP output, and a private-element certificate. The unique coverable group is `SmallGroup(225,6) = C15 x C15`, with all 24 order-15 subgroups forced, proving \(\alpha(15)=24\).

```bash
cd computation/order225
sha256sum -c SHA256SUMS.txt
python audit.py
```

See `order225/results.md` for the complete classification and GAP rerun commands.

## Rerunning raw GAP exports

GAP is not bundled. Install GAP 4.10.2 or later with the SmallGrp package. Run each GAP script from its own directory so relative output paths write beside the script:

```bash
cd computation/order144
gap -q -A export-covers.g

cd ../order225
gap -q -A export-covers.g
```

On Windows, replace `gap` with the path to `gap.exe`. Rerunning can change log timings and equivalent selected indices; it should not change the classification, optimal values, or coverage certificates.

## Source data

The order-36 permutation data and group labels come from the public GroupNames database. The order-144 and order-225 subgroup data were generated with GAP's SmallGrp library. External sources and evidence limits are recorded in `../research/primary-sources.md` and `../research/sequence-lookup.md`.
