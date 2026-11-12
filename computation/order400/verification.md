# 400 阶群覆盖计算（n = 20）：归档、证书与离线审计

## 结论

**α(20) = 30**，且在全 221 个 400 阶群中**唯一**达到 30 的是

\[
\texttt{SmallGroup}(400,221)=C_{10}\times C_{10}\times C_2\times C_2
\cong C_5^2\times C_2^4 ,
\]

阿贝尔群，指数 10，共 210 个 20 阶子群；其中 30 个（下标见 `audit.log` 的 `MIN` 行）覆盖全部 400 个元素，HiGHS 以 `status=0`、对偶界 30.0 证明最优。

- 221 个群全部有交代：125 个被指数条件排除，96 个导出全部 20 阶子群。
- 96 个导出群中：1 个不可覆盖（`SmallGroup(400,213)`），95 个可覆盖；其中 92 个精确最优，3 个 120 s 超时（保留对偶下界，三者下界分别为 34、35、30）。
- 因此**全局下界 30 与构造上界 30 相符**，α(20)=30 为精确值，不依赖任何未证猜想。

参考组的核对（仅为 sanity check，不参与结论）：

| 群 | 结构 | 最优覆盖数 |
|---|---|---|
| `SmallGroup(400,205)` | \((C_5{:}C_4)\times(C_5{:}C_4)\) | **31**（与已知 31 覆盖一致，并被证明最优） |
| `SmallGroup(400,108)` | \(C_{20}\times C_{20}=C_4^2\times C_5^2\) | 36 |
| `SmallGroup(400,221)` | \(C_5^2\times C_2^4\) | **30**（全局最小） |

注意：\(P(20)=(5+1)(4+1)=30\) 的等号不是由 \(C_b^2=C_4^2\) 达成（那里是 36），而是由 \(C_5^2\times C_2^4\) 达成：\(C_2^4\) 可用 5 个 4 阶子群（一个 spread）覆盖，而 \(C_4^2\) 至少需要 6 个。

## 下界为何恰好是 30/40（用于超时实例的认证）

用于给超时实例补足下界的引理（也解释了最小值）：

> 设 \(n=pq^\alpha\)，\(|G|=n^2\)，Sylow \(q\)-子群 \(P\cong C_q^2\) 正规且 \(\exp(G)\mid 2q\)（于是 Sylow 2-子群 \(Q\) 为 16 阶初等阿贝尔群 \(C_2^4\)）。任一 \(n\) 阶子群满足 \(H\cap P=L\)（一条线）且 \(H=L\cdot M\)，\(M=H\cap Q\) 为 4 阶。\(P\) 中非零元 \(x\) 恰在唯一一条线 \(L(x)\) 上，“\(x\) 与整个 \(Q\)”这一层 \(L\times Q\) 只能由 \(H\cap P=L\) 的子群覆盖，故该线类的 \(M\) 必须覆盖 \(Q\)；4 个 4 阶子群无法覆盖 \(C_2^4\)（它们必须两两平凡相交，只能覆盖 15 个非零元中的 12 个），故每条线至少需 5 个子群。\(C_p^2\) 有 \(p+1\) 条线，于是 \(m\ge 5(p+1)\)。

对 \(p=5\) 得 \(m\ge30\)，对 \(p=7\) 得 \(m\ge40\)；由 \(C_p^2\times C_2^4\) 取“全部线 × \(C_2^4\) 的一个 spread”即达到等号，这与计算结果完全吻合。

`SmallGroup(400,220)=C_2^3\times((C_5\times C_5){:}C_2)\) 与 `SmallGroup(784,171)`（见另一目录）正是靠该引理作为**有效不等式**加入 MILP 后，HiGHS 才在 120 s 内把对偶下界抬到 30 / 40 的（`cuts=6`），从而即使它们本身超时，也不影响“全局最小 = 30”的严格性。

## 文件

| 文件 | 内容 |
|---|---|
| `export-covers.g` | GAP 4.10.2 导出脚本：对每个通过 `20 mod Exponent(G) = 0` 的群枚举 `ConjugacyClassesSubgroups` 展平后按大小 20 过滤，元素标签为 `AsList(G)` 下标减 1；同时保存结构描述、Sylow(2)/Sylow(5) 正规性与各元素阶 |
| `covers-20.jsonl` | 96 个群的 20 阶子群全集（含元数据），共 96 行 |
| `export-20.log` | 221 行：`done 400 i subs s` 或 `skip 400 i exp e`，覆盖 1..221 每个 ID 恰一次 |
| `solve-covers.py` | SciPy 1.13.1 / HiGHS 精确 0-1 集合覆盖；`mip_rel_gap=0`，单实例 120 s；逐实例子进程隔离 + 归约/presolve 阶梯回退 + 线类有效不等式 + LP 下界兜底 |
| `solutions-20.jsonl` | 96 条求解记录：状态、覆盖数、对偶界、所选下标 |
| `solve-20.log` | 分批原始 stdout + 最终逐 ID 结果表 |
| `audit.py` / `audit.log` | 纯离线审计及输出 |
| `SHA256SUMS.txt` | 归档文件哈希 |
| `parts/` | 分批运行的中间 covers/solutions/日志（合并后冗余，保留作批次证据） |

## 分批运行记录

- 批次 A：单进程跑全部 96 个导出群。中途 HiGHS 在某个实例的 presolve 中崩溃（access violation），进程重启后日志被截断，故 `solve-20.log` 中批次 A 只保留部分行；这些 ID 的结果保存在 `solutions-20.jsonl`。
- 批次 B1–B3：剩余 27 个 ID 按步长分成 3 组并行（`parts/solve-20-p*.log`）。
- 批次 Q1：`SmallGroup(400,220)` 用线类有效不等式重跑，使对偶下界从 28 提升到 30（`parts/solve-20-q1.log`）。
- 合并规则：同一 ID 以最后一次运行为准；最终 `solutions-20.jsonl` 共 96 条，与 `covers-20.jsonl` 的 ID 集合完全一致。

## 求解细节与稳定性

- 归约：元素若落在完全相同的子群集合中，其覆盖约束相同，只保留一行（等价模型）。行支配归约虽然更强，但在 HiGHS 1.x 上会触发段错误，故不采用；每个实例的父进程按 “merged/presolve=off → merged/presolve=on → full/presolve=off” 阶梯回退，全部为同一实例的精确模型。
- 本阶所有实例最终都返回了结果（无“硬超时无记录”的实例）。
- 超时实例构造覆盖均经审计重新展开验证；其 `bound` 为 HiGHS 对偶下界（或 LP 松弛下界，字段 `bound_source="lp_relaxation"`），均不当最优。

## 离线审计（`audit.py`，仅读已保存 JSONL）

审计内容：SHA-256 自校验；导出日志覆盖 1..221 且每 ID 恰一次；`skip` 行的指数确实不整除 20（故该群必不可覆盖）；导出集合 = 指数整除 20 的集合；每个子群恰 20 个互异元素标签、含 0、元素阶均整除 20、无重复子群；子群数与日志一致；每条记录的 `selected` 重新展开恰好覆盖 400/400 且数量等于 `cover`；`status=0` 的对偶界等于覆盖数；`status=1` 保留下界且不当作最优；全局最小 = 30 且所有超时下界 ≥ 30（`certified global lower bound=30`）。

审计结果：**PASS**（见 `audit.log`）。

## 复现命令

```bash
# 1) 导出（约 4 分钟）
PATH="/c/gap-4.10.2/bin/i686-pc-cygwin-default32-kv3:$PATH" \
  "C:/gap-4.10.2/gap.exe" -l /proc/cygdrive/C/gap-4.10.2 -q -A computation/order400/export-covers.g
# 2) 求解（单进程即可，约 15–40 分钟；子进程隔离使崩溃可恢复）
python computation/order400/solve-covers.py computation/order400/covers-20.jsonl 20 120 \
  computation/order400/solutions-20.jsonl > computation/order400/solve-20.log 2>&1
# 3) 离线审计
sha256sum -c computation/order400/SHA256SUMS.txt
python computation/order400/audit.py
```

## 局限与未决点

1. `SmallGroup(400,180)`、`(400,192)`、`(400,220)` 的**精确值**未定（区间 [34,35]、[35,37]、[30,36]）；这不影响 α(20)=30，因为三者下界均 ≥ 30。
2. 子群枚举依赖 GAP 4.10.2 `ConjugacyClassesSubgroups` 的完备性；本目录用逐 ID 日志保证 221 个群无遗漏，但未独立重算子群。
3. HiGHS 1.x 在个别模型上会忽略 `time_limit` 甚至段错误；已用子进程隔离、阶梯回退与线类不等式规避，超时实例均标注为超时。
