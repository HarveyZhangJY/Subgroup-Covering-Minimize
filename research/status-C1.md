# 状态：C1（\(n=18\) 完整计算，324 阶 176 群）

## 结论

1. **\(\alpha(18)=27\)**。两个群达到且仅两个：`SmallGroup(324,121) = (C3 × ((C3×C3):C3)) : (C2×C2)`（exp 6）与 `SmallGroup(324,170) = (C3^4):(C2×C2)`（exp 6）。二者 Sylow 3-子群（阶 81）正规、Sylow 2-子群 \(C_2^2\) 非正规、中心平凡。
2. **不存在 26 覆盖**：两个群的 MILP（HiGHS，`mip_rel_gap=0`）对偶下界均为 27（`status=0`），换 `presolve=False` 重解结果一致；其余 63 个可覆盖群最优均 \(\ge 27\)。**零超时**。
3. 27 恰等于已知下界 \(n+b=27\)（正规 Sylow 3 ⇒ \(m\ge n+b\)），故该下界在 \(n=18\) **是紧的**；半直积界 \(n+b+1=28\) 被 5 个群（119,169,173,174,175）取到，\(P(18)=30\) 被 16 个群取到。
4. 176 个群全部交代：79 个被指数条件排除（\(18\nmid \mathrm{Exp}(G)\)），32 个虽有 18 阶子群但并集不覆盖全群，65 个可覆盖且全证最优。分布：27×2, 28×5, 30×16, 31×21, 32×1, 33×5, 34×1, 36×4, 37×2, 39×8。
5. **未发现 \(n=12\) 型现象**：Sylow 2 正规的 38 个指数可除群中最小覆盖为 30 \(=P(18)\)（交换群 176），没有低于 \(P(18)\) 者（其中 26 个不可覆盖）。新的数值事实是另一侧：正规 Sylow **3** 时下界 \(n+b=27\) 被取到。
6. 附带事实：正规 Sylow 3 并不保证可覆盖（`id 114,115,118,123,125` 不可覆盖），因此论文引用 \(m\ge n+b\) 时必须说明“覆盖存在时”。

## 文件（均在 `computation/order324/`）

`export-covers.g`、`covers-18.jsonl`（97 群 14182 个 18 阶子群）、`export-18.log`、
`solve-covers.py`、`solutions-18.jsonl`、`solve-18.log`、`audit.py`、`audit.log`（PASS）、
`verify-certificates.g`（GAP 独立验证两个 27-证书）、`verification.md`、`SHA256SUMS.txt`。

审计（只读 JSONL）：`AUDIT RESULT: PASS; 176/176 groups accounted for (79 exponent-excluded, 32 non-coverable, 65 proved optimal, 0 time-limited); every saved selected cover re-expanded to 324/324.`

## 未决点

1. 论文写法：\(\alpha(18)=27\) 需与 \(n+b\) 下界、\(P(n)\) 上界一起表述；27 的证书可引 `solutions-18.jsonl` 的 121 与 170 两组下标。
2. T1/T2 若要用“\(b=9\) 正规 Sylow 3 ⇒ \(m=27\) 可达”作为一般结论，需注意本例 Sylow 2 非正规、结构为 \(C_3^4{:}C_2^2\)，不能外推到所有 \(n=pq^\alpha\)。
3. C2（\(n=20,28\)）是否也出现“下界取等”现象，需其自身计算确认；本轮不预设。
