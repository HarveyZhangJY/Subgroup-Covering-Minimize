# \(n=18\) 与 \(n=2q^2\) 的计算认证

本目录归档新定理
\[
\alpha(2q^2)=3q^2\qquad(q\text{ 为奇素数幂})
\]
的计算验证，特别是
\[
\boxed{\alpha(18)=27.}
\]

理论证明见 `proof/2q2-exact.md`。

## 1. 文件

- `explicit_2q2_cover.py`：对 \(q=3,5,7,11,13\) 显式构造 \(3q^2\) 个 \(n=2q^2\) 阶子群，并逐元素验证闭包、互异性和全覆盖。
- `explicit_2q2_cover_q9.py`：在 \(\mathbb F_9\) 上验证 \(q=9\)（非素数基的素数幂）。
- `n18_min27.py`：枚举 \(\mathbb F_3^4\rtimes C_2^2\) 的六个忠实 \(C_2^2\)-作用下的全部 18 阶子群，用 SciPy/HiGHS 解精确 0–1 覆盖；作用 `1123` 的最优值为 27，对偶界为 27。运行后会生成完整的 `n18_results.json`（体积较大，不随仓库归档）。
- `verify_n18_cover.py`：独立重读 `n18_cover_1123.json` 中作用 `1123` 的 27 个所选子群，重新检查子群闭包、逆元、互异性和并集 324/324。
- `n18_nonnormal_uncoverable.py`：构造非正规 Sylow 3 的群 \(V\rtimes C_3^4\)（\(V=C_2^2\)），枚举全部 39 个 18 阶子群并验证它们只覆盖 108/324 个元素，故不可覆盖。
- `n18_cover_1123.json`：作用 `1123` 的 27 个所选子群的紧凑证书（元素集、像和核），供 `verify_n18_cover.py` 离线复核。
- `n18_nonnormal_results.json`：非正规 Sylow 3 群的子群数、并集大小及不可覆盖结论。

## 2. 关键结果

### \(n=18\)

见证群：
\[
G=\mathbb F_3^4\rtimes C_2^2,
\]
其中
\[
a=\operatorname{diag}(-1,-1,1,-1),\qquad
b=\operatorname{diag}(1,1,-1,-1).
\]
该作用无核且忠实。`n18_min27.py` 对该作用的全部 370 个 18 阶子群求解精确覆盖，得到
\[
\text{status}=0\ (\text{Optimal}),\qquad
\text{cover}=27,\qquad
\text{dual bound}=27.
\]
因此该群的最小覆盖数恰为 27，故 \(\alpha(18)\le 27\)。下界由 `proof/2q2-exact.md` 第 2 节给出：正规 Sylow 3 时 \(m\ge 18+9=27\)，非正规 Sylow 3 时群不可覆盖。

### 显式族

| \(q\) | \(n=2q^2\) | 子群数 \(3q^2\) | 群阶 | 覆盖 |
|---:|---:|---:|---:|---|
| 3 | 18 | 27 | 324 | 324/324 |
| 5 | 50 | 75 | 2500 | 2500/2500 |
| 7 | 98 | 147 | 9604 | 9604/9604 |
| 9 | 162 | 243 | 26244 | 26244/26244 |
| 11 | 242 | 363 | 58564 | 58564/58564 |
| 13 | 338 | 507 | 114244 | 114244/114244 |

### 非正规 Sylow 3 的数值旁证

`n18_nonnormal_uncoverable.py` 的群满足 \(n_3=4\)。全部 39 个 18 阶子群的并集只有 108 个元素，缺 216 个；MILP 不可行。这与理论证明一致：非正规 Sylow 3 的 324 阶群不可由 18 阶子群覆盖。

## 3. 复现

从本目录运行：
```bash
sha256sum -c SHA256SUMS.txt
python verify_n18_cover.py
python explicit_2q2_cover.py 3 5 7 11 13
python explicit_2q2_cover_q9.py
# 可选：完整重跑求解器；会重写 n18_results.json
python n18_min27.py
python n18_nonnormal_uncoverable.py
```

依赖：Python 3.12、NumPy、SciPy/HiGHS（见仓库根目录 `requirements.txt`）。`n18_min27.py` 会重写完整的 `n18_results.json`（不随仓库归档）；不同 HiGHS 版本可能返回等价但下标不同的最优解，但最优值 27 和对偶界 27 不应改变。`verify_n18_cover.py` 读取归档的紧凑证书 `n18_cover_1123.json`，不依赖重跑结果或下标顺序。`sha256sum -c` 应在其之前、针对归档数据运行；重跑求解器后完整 JSON 的哈希可能改变。

## 4. 与远端当前结论的关系

- 远端已有 \(\alpha(18)=27\) 的完整 176 群枚举证书；本目录的 27 覆盖与 MILP 是对该值的独立验证，并把它嵌入无限族 \(\alpha(2q^2)=3q^2\)。
- 远端 `proof/prime-times-primepower.md` 现在补充：严格下界 \(pb+b+1\) 在 \(p=2,\ b=q^2\) 族一般不成立，精确值为 \(pb+b=3q^2\)。
- 远端 `proof/general-n.md` 与 `README.md` 增加本族条目；远端的 \(n=18,20,28\) 结果保持不变。
