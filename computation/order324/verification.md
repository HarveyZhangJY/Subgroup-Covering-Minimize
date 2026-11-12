# \(n=18\) 完整计算：324 阶全部 176 个群

## 结论

\[
\boxed{\alpha(18)=27}
\]

- 27 个 18 阶子群的覆盖存在，达到者恰为两个群：
  - \(\texttt{SmallGroup}(324,121)\cong (C_3\times((C_3\times C_3){:}C_3)){:}(C_2\times C_2)\)，指数 6；
  - \(\texttt{SmallGroup}(324,170)\cong (C_3^4){:}(C_2\times C_2)\)，指数 6。
- 不存在 26 个 18 阶子群的覆盖：两个群的 MILP 对偶下界均为 27（`status=0`，`mip_rel_gap=0`），其余 63 个可覆盖群的最优值都 \(\ge 27\)（其中 28 有 5 个群），没有超时实例。
- 27 恰好等于已知下界 \(n+b=18+9=27\)（Sylow 3-子群正规时 \(m\ge n+b\)），所以该下界在 \(n=18\) 是**紧的**，不能改进到 27 以上；半直积上界 \(n+b+1=28\)（因 \(2\mid 8\)）也被 5 个群取到，但不是最优。
- 达到最小值的两个群 Sylow 3-子群（阶 81）正规、Sylow 2-子群 \(C_2^2\) **非**正规。**没有**发现 \(n=12\) 那样的“正规 \(p\)-Sylow 但覆盖低于朴素 \(P(n)\)”现象（详见第 6 节）。

## 1. 流程与文件

| 文件 | 作用 |
| --- | --- |
| `export-covers.g` | GAP：对 `SmallGroup(324,i)`，`i=1..176`，指数筛除后用 `ConjugacyClassesSubgroups` 展平并筛 `Size=18`，输出元素下标（`AsList(G)` 下标减 1） |
| `covers-18.jsonl` | 97 个群的全体 18 阶子群（共 14182 个，单群 12–2470 个） |
| `export-18.log` | 176 行 `skip`/`done`，含指数与计时 |
| `solve-covers.py` | SciPy `milp`（HiGHS）精确 0-1 集合覆盖，`mip_rel_gap=0`，单实例 120 s |
| `solutions-18.jsonl` | 97 条解记录（最优值、对偶界、所选下标） |
| `solve-18.log` | 逐群求解日志 |
| `audit.py` / `audit.log` | 只读 JSONL 的离线审计 |
| `verify-certificates.g` | GAP 独立验证两个 27-覆盖证书（不经过 MILP） |

复现命令（Git Bash，工作区根目录）：

```
PATH="/c/gap-4.10.2/bin/i686-pc-cygwin-default32-kv3:$PATH" \
  "C:/gap-4.10.2/gap.exe" -l /proc/cygdrive/C/gap-4.10.2 -q -A \
  computation/order324/export-covers.g                 # -> export-18.log, covers-18.jsonl
python computation/order324/solve-covers.py computation/order324/covers-18.jsonl 18 120 \
  computation/order324/solutions-18.jsonl               # -> solve-18.log, solutions-18.jsonl
python computation/order324/audit.py                    # -> audit.log
PATH=... gap.exe -l ... -q -A computation/order324/verify-certificates.g
```

导出一次连续跑完 176 个群（约 6 分钟，`EXIT=0`），**未使用分批，也没有跳过任何 ID**；逐个群的 `ms` 计时在 `export-18.log` 中（最慢 `id 175` 约 11.6 s）。

## 2. 176 个群的完全交代

`audit.py` 断言 `export-18.log` 恰好覆盖 `id=1..176` 各一次：

- **79 个群被指数条件排除**：`18 mod Exponent(G) != 0`。理由：阶 18 子群的指数整除 18，故其元素阶整除 18；若 `Exponent(G) ∤ 18` 则任何元素都不能落在阶 18 子群中，覆盖不可能。审计逐个核对 `18 % exp != 0`。
- **97 个群导出**（`18 % exp == 0`），其中
  - **32 个不可覆盖**：即便有阶 18 子群，全部阶 18 子群的并集也不等于 \(G\)（27 个群缺 216 个元素，5 个群缺 24 个元素）。审计重新展开并集确认不等于 324。
  - **65 个可覆盖且全部证得最优**（`status=0`，对偶界 = 覆盖数）。
  - **超时 0 个**。

\[
176 = 79\ (\text{指数排除}) + 32\ (\text{不可覆盖}) + 65\ (\text{最优})
\]

索引能覆盖全群的不可覆盖群举例：`id 46..60, 126..135, 160, 171` 等（Sylow 2 正规、Sylow 3 非正规的 `(C_2^2){:}Q` 型），以及 `id 114, 115, 118, 123, 125`（Sylow 3 正规）。这说明“正规 Sylow 3” 并不保证可覆盖，\(m\ge n+b\) 只是覆盖存在时的下界。

## 3. 可覆盖群的最优值分布（全部为 MILP 证明最优）

| 覆盖数 | 群数 | SmallGroup(324, ·) |
| --- | --- | --- |
| **27** | 2 | 121, 170 |
| 28 | 5 | 119, 169, 173, 174, 175 |
| 30 | 16 | 36, 61, 64, 74, 116, 117, 120, 122, 124, 138, 144, 145, 150, 166, 168, 176 |
| 31 | 21 | 62, 63, 68, 69, 70, 71, 72, 73, 75, 77, 78, 79, 80, 136, 140, 142, 143, 146, 147, 148, 149 |
| 32 | 1 | 167 |
| 33 | 5 | 37, 39, 40, 41, 165 |
| 34 | 1 | 172 |
| 36 | 4 | 81, 83, 139, 152 |
| 37 | 2 | 137, 141 |
| 39 | 8 | 82, 86, 87, 88, 89, 151, 153, 154 |

合计 65；全局最小值 27，次小 28，第三 30（\(=P(18)=3\cdot 10\)）。

求解开销：总计 100.3 s，最慢 `id 175`（2470 个变量）27.15 s，远低于 120 s 上限，故**没有任何实例以超时或对偶界代替最优值**。

## 4. 27-覆盖证书

`audit.py` 从保存的 `covers-18.jsonl` 重新展开所选子群，并集均为 324/324，且所选个数 = 27：

- `SmallGroup(324,121)`: `status=0`，`cover=27`，`dual_bound=26.999999999999996`，所选下标
  `[0, 13, 24, 28, 36, 37, 38, 39, 40, 41, 42, 43, 44, 60, 62, 65, 108, 109, 110, 111, 112, 113, 128, 134, 191, 219, 234]`
- `SmallGroup(324,170)`: `status=0`，`cover=27`，`dual_bound=26.999999999999982`，所选下标
  `[28, 36, 86, 94, 122, 133, 158, 163, 216, 224, 232, 250, 273, 278, 319, 320, 321, 322, 323, 324, 325, 326, 327, 335, 351, 355, 363]`

`verify-certificates.g` 直接从 `covers-18.jsonl` / `solutions-18.jsonl` 读取这两个证书，在 GAP 里重新构造群并检查：保存的每个 18 元集合生成（`Subgroup(G, ...)`）的阶正好 18（即为真子群）、该集合出现在 `ConjugacyClassesSubgroups` 枚举结果中、27 个集合的并集 = 324。输出：

```
CERT 121 subgroups=27 all_saved_sets_are_order18_subgroups=true pairs=486 union=324 covers_all=true
CERT 121 structure=(C3 x ((C3 x C3) : C3)) : (C2 x C2) exponent=6 sylow2_normal=false sylow3_normal=true
CERT 121 union_generates_order=324
CERT 170 subgroups=27 all_saved_sets_are_order18_subgroups=true pairs=486 union=324 covers_all=true
CERT 170 structure=(C3 x C3 x C3 x C3) : (C2 x C2) exponent=6 sylow2_normal=false sylow3_normal=true
CERT 170 union_generates_order=324
```

注意 \(27\cdot18=486>324\)：恰好是“27 个 18 元子群覆盖 324 个元素、平均重数 1.5”的配置。

稳健性：对 121、170 各再用 `presolve=False` 与显式 `node_limit` 两种设置重解一次，均返回 `status=0`、`fun=27`、`mip_dual_bound=27`，与主运行一致。

## 5. 达到最小值的群的结构

| 群 | 结构 | exp | Sylow 2 (阶 4) | Sylow 3 (阶 81) | \(\lvert Z\rvert\) | \(\lvert G'\rvert\) | 覆盖 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 121 | \((C_3\times((C_3\times C_3){:}C_3)){:}(C_2\times C_2)\) | 6 | \(C_2^2\)，81 个共轭，非正规 | \(C_3\times((C_3\times C_3){:}C_3)\)，正规 | 1 | 81 | 27 |
| 170 | \((C_3^4){:}(C_2\times C_2)\) | 6 | \(C_2^2\)，81 个共轭，非正规 | \(C_3^4\)，正规 | 1 | 81 | 27 |
| 119 | \(((C_3\times C_3){:}C_2)\times D_{18}\) | 18 | \(C_2^2\)，81 个共轭，非正规 | \(C_9\times C_3\times C_3\)，正规 | 1 | 81 | 28 |
| 169 | \(((C_3\times C_3){:}C_2)^2\) | 6 | \(C_2^2\)，81 个共轭，非正规 | \(C_3^4\)，正规 | 1 | 81 | 28 |
| 173 | \(C_3\times C_6\times((C_3\times C_3){:}C_2)\) | 6 | \(C_2^2\)，9 个共轭，非正规 | \(C_3^4\)，正规 | 18 | 9 | 28 |
| 174 | \(C_6\times((C_3^3){:}C_2)\) | 6 | \(C_2^2\)，27 个共轭，非正规 | \(C_3^4\)，正规 | 6 | 27 | 28 |
| 175 | \(C_2\times((C_3^4){:}C_2)\) | 6 | \(C_2^2\)，81 个共轭，非正规 | \(C_3^4\)，正规 | 2 | 81 | 28 |
| 176 | \(C_6\times C_6\times C_3\times C_3\)（交换） | 6 | \(C_2^2\)，正规 | \(C_3^4\)，正规 | 324 | 1 | 30 |

要点：

1. 全部 7 个覆盖数 \(\le 28\) 的群都有**正规的阶 81 Sylow 3-子群**（核分别为 \(C_3\times((C_3\times C_3){:}C_3)\)、\(C_3^4\)、\(C_9\times C_3^2\) 等，见表）；Sylow 2-子群都是 \(C_2^2\) 且非正规，所以截面 \(H\cap Q\)（阶 \(b=9\)）随 \(H\) 变化，正是 \(n+b\) 下界可以被“打满”的机制。
2. 因此 \(27=n+b\) 是**取等号**，不是违反下界；这说明 \(n=18\) 的 \(\alpha\) 由正规 \(q\)-Sylow 下界决定，而不能靠 \(P(18)=30\) 或半直积界 \(28\) 得到。
3. 有正规 Sylow 3 的 70 个可覆盖群中，覆盖数为 \(27,28,30,31,32,33,34,36,37,39\) 都有出现，说明仅凭“Sylow 3 正规”不能区分具体值，必须做精确计算。

## 6. 与 \(n=12\) 的 \(19<20\) 现象的对照

\(n=12\) 的异常是：Sylow **p**（\(p=3\)，阶 9）正规，但覆盖 19 低于朴素界 \(P(12)=20\)，原因是 \(P\) 在商上的共轭作用会移动直线。本计算的对应问题是 \(p=2\)：Sylow 2-子群（阶 4）正规时能否低于 \(P(18)=30\)。

结果：指数可除的群中 Sylow 2 正规的共 38 个，其最优值分布为

- 不可覆盖 26 个；
- 覆盖 39 的 8 个，覆盖 36 的 3 个，覆盖 **30** 的 1 个（`id 176`，交换群 \(C_6^2\times C_3^2\)）。

即 \(\min = 30 = P(18)\)，**没有任何正规 Sylow 2 的群低于 \(P(18)\)**，因此 \(n=18\) 没有 \(n=12\) 型反例。本轮的“异常”在另一侧：正规 Sylow **3** 时下界 \(n+b=27\) 被取到，比 \(n+b+1=28\) 与 \(P(18)=30\) 都小，这是本轮唯一需要写进论文的新数值事实。

（附带事实：32 个不可覆盖群里，27 个 Sylow 3 非正规、5 个 Sylow 3 正规，见 `id 114, 115, 118, 123, 125`。）

## 7. 审计结论

`audit.py` 只读取 `covers-18.jsonl`、`solutions-18.jsonl`、`export-18.log`，不重跑 GAP/HiGHS，检查项与结果：

- 176 个 ID 全部交代且无重复：79 skip + 97 done；
- 全部 14182 个保存子群大小 = 18、下标合法、互不相同、含单位元；子群个数与导出口志一致；
- 65 个解记录的所选下标个数 = 记录覆盖数，重新展开并集 = 324/324；
- 最优记录的对偶界与覆盖数一致（误差 < 1e-6）；超时集合为空；
- 全局最小值 27，达到者 121、170；无任何记录的最优值或下界小于 27。

```
AUDIT RESULT: PASS; 176/176 groups accounted for
(79 exponent-excluded, 32 non-coverable, 65 proved optimal, 0 time-limited with dual bounds);
every saved selected cover was re-expanded and checked to cover 324/324.
```

文件哈希见 `SHA256SUMS.txt`。
