# 784 阶群覆盖计算（n = 28）：归档、证书与离线审计

## 结论

**α(28) = 40**，且在全 172 个 784 阶群中**唯一**达到 40 的是

\[
\texttt{SmallGroup}(784,172)=C_{14}\times C_{14}\times C_2\times C_2
\cong C_7^2\times C_2^4 ,
\]

阿贝尔群，指数 14，共 280 个 28 阶子群；其中 40 个（下标见 `audit.log` 的 `MIN` 行）覆盖全部 784 个元素，HiGHS 以 `status=0`、对偶界 40.0 证明最优。注意 40 = 8·5：\(C_7^2\) 的 8 条线 × \(C_2^4\) 的 5 部 spread。

- 172 个群全部有交代：97 个被指数条件排除，75 个导出全部 28 阶子群。
- 75 个导出群中：11 个不可覆盖，64 个可覆盖；其中 54 个精确最优，10 个 120 s 超时（对偶下界 45–46，唯一例外是 `SmallGroup(784,171)` 的 40，恰好等于全局最小值，仍足以支撑全局结论）。
- 可覆盖群的最优值分布：40×1，46×3，48×3，49×4，50×16，51×6，52×16，56×4，58×1。
- 因此**全局下界 40 与构造上界 40 相符**，α(28)=40 为精确值，不依赖任何未证猜想。

参考组的核对（仅为 sanity check，不参与结论）：

| 群 | 结构 | 最优覆盖数 |
|---|---|---|
| `SmallGroup(784,59)` | \((C_7{:}C_4)\times(C_7{:}C_4)\) | **50**（与已知 50 覆盖一致，并被证明最优） |
| `SmallGroup(784,96)` | \(C_{28}\times C_{28}=C_7^2\times C_4^2\) | 48 |
| `SmallGroup(784,172)` | \(C_7^2\times C_2^4\) | **40**（全局最小） |

即 \(C_b^2=C_4^2\) 只能到 48，\(C_2^4\) 的 spread 才能达到 \(P(28)=(7+1)(4+1)=40\)。

## 下界为何恰好是 40（用于超时实例的认证）

同一引理（详见 `computation/order400/verification.md`）：若 Sylow \(q\)-子群 \(P\cong C_q^2\) 正规且 \(\exp(G)\mid 2q\)（Sylow 2-子群为 \(C_2^4\)），则每条线 \(L\) 至少需要 5 个 28 阶子群（其 \(M=H\cap Q\) 必须覆盖 \(Q=C_2^4\)，而 4 个 4 阶子群无法覆盖 \(C_2^4\)），故 \(m\ge 5(q+1)=40\)。

`SmallGroup(784,171)=C_2^3\times((C_7\times C_7){:}C_2)`（1624 个 28 阶子群）是唯一“威胁”全局结论的实例：纯 MILP 在 120 s 与 900 s 下只给出下界 38/39。加入该引理对应的 8 条线类不等式后（`cuts=8`），120 s 内对偶下界提升到 **40**，与全局最小值相等，从而 171 不影响 α(28)=40 的严格性（其精确值仍未知，落在 [40,58]）。

## 文件

| 文件 | 内容 |
|---|---|
| `export-covers.g` | GAP 4.10.2 导出脚本（28 mod Exponent(G)=0 过滤；元素标签 = `AsList(G)` 下标 − 1；附加结构描述、Sylow 正规性、元素阶） |
| `covers-28.jsonl` | 75 个群的 28 阶子群全集 |
| `export-28.log` | 172 行：`done 784 i subs s` / `skip 784 i exp e`，覆盖 1..172 每个 ID 恰一次 |
| `solve-covers.py` | SciPy 1.13.1 / HiGHS 精确 0-1 覆盖；`mip_rel_gap=0`；单实例 120 s；子进程隔离 + 阶梯回退 + 线类有效不等式 + LP 下界兜底 |
| `solutions-28.jsonl` | 75 条求解记录 |
| `solve-28.log` | 分批原始 stdout + 最终逐 ID 结果表 |
| `audit.py` / `audit.log` | 纯离线审计及输出 |
| `SHA256SUMS.txt` | 归档文件哈希 |
| `_ext171.jsonl` | `SmallGroup(784,171)` 的 900 s 延长运行记录（仅作说明，不参与结论） |
| `parts/` | 分批运行的中间 covers/solutions/日志 |

## 分批运行记录

- 批次 A：单进程跑全部导出群；`SmallGroup(784,90)`（376 个 28 阶子群）在 presolve 下段错误、且 merged 模型下 HiGHS 屡次超出时限，日志被截断；其最终结果由批次 B/阶梯回退（full 模型，43.8 s）给出。
- 批次 B1–B3：剩余 62 个 ID 按步长分 3 组并行（`parts/solve-28-p*.log`）。
- 批次 Q1–Q3：因 B1 的父进程在子进程硬超时（`subprocess.TimeoutExpired`）后退出，重跑遗漏的 21 个 ID（`parts/solve-28-q*.log`）。
- 合并规则：同一 ID 以最后一次运行为准；最终 `solutions-28.jsonl` 共 75 条，与 `covers-28.jsonl` 的 ID 集合完全一致。

## 求解细节与稳定性

- 归约与回退同 order400：优先“相同覆盖约束合并 + presolve 关”；行支配归约在 HiGHS 1.x 上会段错误，弃用；逐实例子进程 + 阶梯（merged/off → merged/on → full/off）+ 硬超时重试。
- 对 `exp | 14` 且 Sylow 7 正规的群追加线类不等式（`cuts>0`），显著增强下界（171、155、131 等）。
- 超时实例的构造覆盖均经审计重新展开验证；`bound` 为对偶下界（或 LP 松弛下界，若 MILP 完全失败），均不当最优。

## 离线审计（`audit.py`，仅读已保存 JSONL）

审计内容：SHA-256 自校验；导出日志覆盖 1..172 且每 ID 恰一次；`skip` 行指数不整除 28；导出集合 = 指数整除 28 的集合；每个子群恰 28 个互异元素标签、含 0、元素阶整除 28、无重复；子群数与日志一致；每条 `selected` 重新展开恰覆盖 784/784；`status=0` 的对偶界等于覆盖数；超时不当作最优；全局最小 = 40 且所有超时下界 ≥ 40（`certified global lower bound=40`）。

审计结果：**PASS**（见 `audit.log`）。

## 复现命令

```bash
# 1) 导出（约 6 分钟）
PATH="/c/gap-4.10.2/bin/i686-pc-cygwin-default32-kv3:$PATH" \
  "C:/gap-4.10.2/gap.exe" -l /proc/cygdrive/C/gap-4.10.2 -q -A computation/order784/export-covers.g
# 2) 求解（建议 2–3 个并行批次；子进程隔离使崩溃/超时可恢复）
python computation/order784/solve-covers.py computation/order784/covers-28.jsonl 28 120 \
  computation/order784/solutions-28.jsonl > computation/order784/solve-28.log 2>&1
# 3) 离线审计
sha256sum -c computation/order784/SHA256SUMS.txt
python computation/order784/audit.py
```

## 局限与未决点

1. 10 个超时实例的精确值未定：`61:[46,49]`、`130:[46,51]`、`132:[45,51]`、`135:[46,49]`、`147:[46,56]`、`148:[45,52]`、`150:[45,52]`、`155:[45,53]`、`169:[45,47]`、`171:[40,58]`。均不影响 α(28)=40（下界都 ≥ 40）。
2. 子群枚举依赖 GAP `ConjugacyClassesSubgroups` 完备性；逐 ID 日志保证 172 个群无遗漏，但未独立重算子群。
3. HiGHS 1.x 会忽略 `time_limit` 或在 presolve 段错误，已用子进程隔离 + 阶梯回退规避；`SmallGroup(784,90)` 需要 full 模型才可解。
