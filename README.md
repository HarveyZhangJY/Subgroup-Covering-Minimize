# Subgroup Covering Minimize

Research archive for the following problem:

> Let \(n\ge 2\). There exists a group \(G\) of order \(n^2\) that can be covered by \(m\) subgroups of order \(n\). Determine the minimum possible \(m\).

Define
\[
\alpha(n)=\min_{|G|=n^2}\min\left\{m:\ G=\bigcup_{i=1}^m H_i,\quad |H_i|=n\right\}.
\]
The minimization allows the group \(G\) itself to be chosen. This is different from fixing \(G=C_n\times C_n\).

## Status

**No exact closed form for \(\alpha(n)\) for all \(n\) is obtained in this project, and no such general formula was found in the literature reviewed.** This is a bounded research report, not a claim that such a formula does not exist.

The results that are proved or certified here are:

\[
\boxed{\alpha(n)=n+1\quad\Longleftrightarrow\quad n\text{ is a prime power}.}
\]

For primes \(p<q\),

\[
\boxed{
\alpha(pq)=
\begin{cases}
pq+q+1, & p\mid q-1,\\[2pt]
(p+1)(q+1), & p\nmid q-1.
\end{cases}}
\]

For a fixed group \(G=C_n\times C_n\), there is a closed formula for every \(n\):

\[
\boxed{
c_n(C_n\times C_n)
=n\prod_{p\mid n}\left(1+\frac1p\right)
=\prod_{p^a\parallel n}p^{a-1}(p+1).
}
\]

For general \(n\),

\[
\boxed{L(n)\le \alpha(n)\le U(n)\le P(n)},
\qquad
P(n)=\prod_{p^a\parallel n}(p^a+1),
\]
where
\[
L(n)=
\begin{cases}
n+1,& n\text{ is a prime power},\\
n+p_{\min}(n),& \text{otherwise},
\end{cases}
\]
and \(U(n)\) is a finite combination of the proved product and semidirect-product constructions. \(U(n)\) is only an upper bound, not a proved exact formula.

Further proved upper bound: if \(p\) is prime, \(b\) is a prime power, and \(p\mid b-1\), then
\[
\alpha(pb)\le pb+b+1.
\]

Further exact family: if \(p,q\) are distinct primes, \(b=q^\alpha\), \(p>b^2\), and \(q\nmid p^2-1\), then
\[
\boxed{\alpha(pq^\alpha)=(p+1)(b+1)=P(pq^\alpha).}
\]

Computed/certified values include
\[
\alpha(6)=10,\qquad \alpha(12)=17,\qquad \alpha(15)=24,\qquad
\alpha(18)=27,\qquad \alpha(20)=30,\qquad \alpha(28)=40.
\]

## Paper

- [Complete 20-page Chinese paper (PDF)](paper/solution.pdf)
- [LaTeX source](paper/solution.tex)

The paper contains the literature review, complete proofs for prime powers and \(pq\), the fixed-\(C_n^2\) formula, general upper/lower bounds, computation certificates, counterexamples to natural closed-form guesses, and the precise boundary of what remains unresolved.

## Repository layout

```text
paper/                 Full report: PDF and LaTeX source
research/              Literature review and shared research log
proof/                 Individual proofs and peer-review reports
computation/           Reproducible scripts, results, and coverage certificates
  order144/            Complete n=12 certification over all 197 groups of order 144
  order225/            Complete n=15 certification over all 6 groups of order 225
  order324/            Complete n=18 certification over all 176 groups of order 324
  order400/            Complete n=20 certification over all 221 groups of order 400
  order784/            Complete n=28 certification over all 172 groups of order 784
  order1936/           Scripts for the platform-assisted n=44 computation (not a certified result here)
```

Key documents:

- `research/primary-sources.md`: A/B evidence grading for Isaacs (1973), Jungnickel (1999), and Jungnickel–Storme (2001).
- `proof/candidate-proof.md`: general bounds, Sylow lower bounds, and complete \(pq\) proof.
- `proof/partition-approach.md`: equal-partition structure and the \(n=12\) computation.
- `proof/general-n.md`: final synthesis for arbitrary \(n\), including unresolved gaps.
- `proof/pqalpha-general.md`: general \(n=pq^\alpha\) structure, Sylow bounds, and the exact values for \(n=18,20,28\).
- `proof/pq2-q2.md`: the \(n=4p\) analysis, Burnside reduction, and the \(p\ge5\) lower-bound gap.
- `research/pqalpha-literature.md`: targeted literature search for \(n=pq^\alpha\).
- `proof/semidirect-upper.md`: the \(pb+b+1\) construction.
- `research/coordination.md`: shared coordination log showing how parallel research and computation were deduplicated.

## Reproduce the checks

Requirements:

- Python 3.12
- NumPy 1.26
- SciPy 1.13.1 / HiGHS
- GAP 4.10.2 with the SmallGrp package (only for rerunning the raw subgroup export)
- XeLaTeX with `ctex` (the paper uses the Fandol fonts bundled with TeX Live)

Install Python dependencies from the repository root:
```bash
python -m pip install -r requirements.txt
```

Offline audit of the saved certificates (no group enumeration or MILP rerun):
```bash
python computation/verify_all.py
python computation/order144/audit.py
python computation/order225/audit.py
python computation/order324/audit.py
python computation/order400/audit.py
python computation/order784/audit.py
```

Lightweight constructions and small-order computations:
```bash
python computation/prime_power_spreads.py
python computation/order36_exhaustive.py
python computation/composite_constructions.py
python computation/order144_products.py
```

The order-36 script downloads public GroupNames pages on its first run. Exact rerun commands for the full order-144 and order-225 GAP calculations are in `computation/order144/verification.md` and `computation/order225/results.md`.

Build the paper:
```bash
cd paper
xelatex solution.tex
xelatex solution.tex
```

## Evidence and scope limits

- The literature statement is limited to the sources reviewed in `research/primary-sources.md` and `research/sequence-lookup.md`.
- “No formula found” does not mean “proved impossible.”
- The values \(\alpha(18)=27\), \(\alpha(20)=30\), \(\alpha(28)=40\) are exact, certified by complete enumerations of the 176, 221, and 172 groups of the respective orders. The remaining small-n range is
  \[
  32\le\alpha(30)\le60.
  \]
- The \(n=12\) certificate uses a complete enumeration of the 197 groups of order 144 with exact integer programming. One instance timed out, but its certified dual lower bound is 18, so it cannot affect the global minimum 17.
- The \(n=15\) certificate is complete: all 6 groups of order 225 were enumerated, with no timeout.
- The \(n=44\) platform-assisted run is recorded in `research/ustc-platform.md`; it is not used as a certified value in the paper.

## Citation

If this archive is useful, cite the GitHub repository and the paper in `paper/solution.pdf`.
