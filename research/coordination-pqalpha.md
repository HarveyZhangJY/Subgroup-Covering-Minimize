# \(n=pq^\alpha\) 协作分工（2026-11-11）

## 统一记号

- \(p,q\) 为不同素数，\(\alpha\ge1\)，\(b=q^\alpha\)，\(n=pb\)。
- \(\alpha(n)\)：允许选择阶 \(n^2\) 的群时，用 \(n\) 阶子群覆盖全群所需的最少子群数。
- \(P(n)=(p+1)(b+1)=n+p+b+1\)。
- 已知：\(p\mid b-1\) 时有半直积上界 \(\alpha(n)\le n+b+1\)；否则直积上界 \(P(n)\)。
- 已知：若 Sylow \(q\)-子群正规，则 \(m\ge n+b\)。
- 已知精确值：\(\alpha(12)=17\)（\(p=3,b=4\)，完整 197 群证书）。

## 已剔除的错误引理与有效替代

**警告：** 曾经猜测“Sylow \(p\)-子群正规时 \(m\ge P(n)\)”，此命题为假。反例是 \(n=12\) 的
\[
G=C_2^2\times S_3\times S_3=\texttt{SmallGroup}(144,192).
\]
其 Sylow \(3\)-子群 \(C_3^2\) 正规，但完整计算给出 19 个 12 阶子群的覆盖，而 \(P(12)=20\)。原因是商群在 \(P\) 上的共轭作用会移动直线，不能把每条直线单独计数。不得在证明中引用该假引理。

目前仍然有效的事实：

1. **正规 \(q\)-Sylow 下界（已有证明）：** 若阶 \(b^2\) 的 Sylow \(q\)-子群 \(Q\) 正规，则每个 \(n\) 阶子群与 \(Q\) 交于 \(b\) 阶，计数得 \(m\ge n+b\)。
2. **\(b=4\) 且 \(Q\) 正规时的结构限制：** 若 \(p\ge5\)，阶 16 群的 \(p\)-自同构只可能在 \(Q=C_2^4\) 且 \(p=5,7\) 出现；这两种情形下非平凡 \(p\)-自同构没有 2 维不变子空间，无法成为 \(H\cap Q\)（4 阶）的自同构。故所有出现的直线在 \(Q\) 上作用平凡，进而 \(G=P\times Q\)。此时对每条 \(P\)-直线，覆盖相应元素的 \(H\) 的 \(M=H\cap Q\) 必须覆盖 \(Q\)，至少需 5 个；\(P\) 需 \(p+1\) 条直线，故
\[
m\ge 5(p+1)=P(4p).
\]
所以“\(Q\) 正规”的 \(n=4p\) 覆盖不会优于 \(P(4p)\)。真正的未知只剩下 \(Q\) 非正规（包括 \(P\) 正规的 \(n=12\) 型作用）的情形。
3. **正常 \(q\)-Sylow 的半直积上界仍为 \(n+b+1\)**（\(p\mid b-1\)）；直积上界仍为 \(P(n)\)。

因此 C1/C2 的完整计算是本轮判断 \(\alpha(18),\alpha(20),\alpha(28)\) 的关键，不能靠上述假引理预设答案。

## 任务与文件归属

### C1：\(n=18\) 完整计算（324 阶，176 群）
- 目录：`computation/order324/`
- 参考：`computation/order144/` 的 `export-covers.g`、`solve-covers.py`、`audit.py`。
- 必须完整检查 176 个群；记录指数排除、不可覆盖、可覆盖最优值、MILP 对偶界与超时。
- 输出：`covers-18.jsonl`、`solutions-18.jsonl`、`export-18.log`、`solve-18.log`、`audit.py`、`audit.log`、`verification.md`、`SHA256SUMS.txt`。
- 核心问题：\(\alpha(18)=27\) 还是 \(28\)？若出现 27，给出所选子群证书并由审计展开验证。

### C2：\(n=20\) 与 \(n=28\) 完整计算（400 阶 221 群；784 阶 172 群）
- 目录：`computation/order400/`、`computation/order784/`。
- 同样流程与输出文件（`covers-20.jsonl` 等）。
- 核心问题：是否分别为 30 与 40；若更小，必须给出完整证书并指出群结构。

### T1：\(n=4p\) 的完整证明
- 文件：`proof/pq2-q2.md`
- 证明 \(\alpha(4p)=5(p+1)\)（\(p\ge5\) 素数），把 \(p=5,7\) 的 Sylow 非正规残余情形明确留给 C2 的完整计算；\(p=3\) 用 \(\alpha(12)=17\)，\(p=2\) 是素数幂。
- 严格核验上面的正规 \(p\)-Sylow 引理与 \(b=4\) 自同构论证；若发现缺口，明确写出。

### T2：一般 \(n=pq^\alpha\) 的结构与界
- 文件：`proof/pqalpha-general.md`
- 整理正规 \(p\)-Sylow 定理、\(p>q^{2\alpha}\) 推论、Sylow 计数何时强制正规、正常 \(q\)-Sylow 下的 \(n+b\) 下界、等号 \(n+b\) 与 \(n+b+1\) 的结构障碍。
- 不重复 C1/C2 的数值计算；不宣称未经证明的精确公式。

### L1：定向文献检索
- 文件：`research/pqalpha-literature.md`
- 检索 groups of order \(p^2q^{2\alpha}\)、covered by subgroups of order \(pq^\alpha\)、\(p^2q^2\) covering、subgroup covering number 等。
- 标注证据等级（原文/摘要/评论/仅检索到标题），不得把未读全文的结论写成已核实。

## 协作规则

- **C1 已完成（主 Agent 已独立复核）**：\(\alpha(18)=27\)，不是 28，也不是 26。达到者仅
  `SmallGroup(324,121)` 与 `SmallGroup(324,170)=(C3^4):(C2×C2)`；二者 Sylow 3-子群正规、Sylow 2-子群非正规，27 恰为正规 \(q\)-Sylow 下界 \(n+b=27\)。全部 176 群均交代（79 指数排除、32 不可覆盖、65 最优、0 超时）。主 Agent 已重跑 `audit.py` 与 `verify-certificates.g`，均 PASS。该结果说明半直积上界 \(n+b+1=28\) 在 \(n=18\) 不是最优，且 \(n+b\) 下界可以取等。
- **C2 已完成（主 Agent 已独立复核）**：\(\alpha(20)=30\)（400 阶 221 群；唯一达到者 `SmallGroup(400,221)=C5^2×C2^4`）；\(\alpha(28)=40\)（784 阶 172 群；唯一达到者 `SmallGroup(784,172)=C7^2×C2^4`）。两目录 `audit.py` 与 `sha256sum -c` 均 PASS；超时实例下界分别 \(\ge30,\ge40\)，不影响全局最小值。
- **平台 \(n=44\)**：USTC “一〇七”平台全 167 群导出、LP 与 32-CPU 对称破缺计算已完成。关键更正：T1 的 `scan11` 用共轭类代表而非全部子群（id166: 420/3780），故 \(\alpha(44)=60\) 未证。全子群 LP 下界 58；固定类型 B 子群后 SCIP 对偶界 58.333，整数下界升为 59；CP-SAT ≤59 可行性 4 小时 UNKNOWN，未找到 59。因此目前严格为 \(59\le\alpha(44)\le60\)。详见 `research/ustc-platform.md` 与 `proof/pq2-q2.md` §9.2。
- 只写自己归属的目录/文件；不要改 `output/solution.tex`、`output/solution.pdf`、其他 Agent 的目录。
- 完成时另写 `research/status-<角色>.md`（简短：结论、文件、未决点），供主 Agent 合并。
- 计算结论必须能由保存的 JSONL 与独立审计复现；理论结论必须区分已证、条件性、猜测。
- GAP 环境：
  `PATH="/c/gap-4.10.2/bin/i686-pc-cygwin-default32-kv3:$PATH" "C:/gap-4.10.2/gap.exe" -l /proc/cygdrive/C/gap-4.10.2 -q -A <script>`
- 单实例 MILP 可用 120 秒上限；超时须保留对偶下界，不能当作最优。
