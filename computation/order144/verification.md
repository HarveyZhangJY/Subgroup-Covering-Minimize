# 144 阶群覆盖计算：归档与离线审计

## 归档范围

下列文件由计算阶段的临时工作目录按原字节归档到本目录：

- `export-covers.g`：GAP 4.10.2 导出脚本；
- `solve-covers.py`：SciPy 1.13.1 / HiGHS 精确 0-1 集合覆盖求解脚本；
- `covers-12.jsonl`：89 个指数候选群的全部 12 阶子群；
- `solutions-12.jsonl`：89 个候选群的求解状态、对偶界及所选子群；
- `export-12.log`：覆盖全部 `SmallGroup(144,1..197)` 的原始 GAP 导出日志。

另保存 `audit.py`、本次输出 `audit.log` 和归档文件哈希清单 `SHA256SUMS.txt`。临时的部分求解文件不属于最终证书，未归档。本次没有重新运行 GAP 枚举或 HiGHS 求解。

## SHA-256 核对

| 文件 | SHA-256 | 与 `proof/partition-approach.md` 第 5.2 节比较 |
|---|---|---|
| `covers-12.jsonl` | `5af630fdc06e680b7ef107ade80fc5c501160fd4d7a8aae30568b105d2b5d22f` | 一致 |
| `solutions-12.jsonl` | `695d9b5cb41520a86f7ac1b43af755426c64d8a8daf816ee254e721293980125` | 一致 |

其余归档文件的 SHA-256 见 `SHA256SUMS.txt`。

## 离线审计结果

`audit.py` 仅读取已保存数据，检查 JSON 唯一性与交叉引用、子群长度和元素范围、日志中的 197 个群是否完整，并把每个已保存的所选子群集合重新展开为元素集；没有调用群枚举或优化求解器。审计通过，输出见 `audit.log`。

- 197 群状态汇总：108 群因指数不整除 12 而排除，89 群导出；其中 15 群不可由全部 12 阶子群覆盖，剩余 74 群可覆盖。
- 74 个可覆盖实例中，73 个返回 `status=0`（最优），唯一超时为 `SmallGroup(144,196)`；其已保存对偶下界为 `18.000000000000178`，构造上界为 20。
- 73 个精确实例中，只有 `SmallGroup(144,184)`、`SmallGroup(144,193)`、`SmallGroup(144,194)` 的最优值为 17，其余 70 个均至少为 18。
- 三份 17 子群证书均为 `status=0`，对偶界分别为 `17.0`、`17.0`、`17.000000000000007`（浮点表示误差），所选子群数均为 17，重新展开的并集均为 **144/144**。对应 `selected` 下标已列于 `audit.log`，可由 `covers-12.jsonl` 唯一还原。
- 所有其他已保存的有限覆盖也都通过全群并集检查；`SmallGroup(144,101)` 的最优值 24 亦与第 5.2 节一致。

因此，归档数据、197 群状态汇总及全局最优值 17 的证书与第 5.2 节记录一致。本审计不改动任何理论结论。

## 复现命令

从仓库根目录执行哈希和离线审计：

```bash
cd computation/order144
sha256sum -c SHA256SUMS.txt
python audit.py
```

如需保存审计输出：

```bash
python audit.py 2>&1 | tee audit.log
```

如需在 Linux/macOS 上重跑完整计算，先安装 GAP（含 SmallGrp）和 Python 依赖，然后在该目录执行：

```bash
gap -q -A export-covers.g
python solve-covers.py covers-12.jsonl 12 60 > solutions-12-rerun.jsonl
```

Windows 下可把 `gap` 换成对应 `gap.exe` 的路径。`export-covers.g` 的当前版本会把数据写到运行目录下的 `covers-12.jsonl`。

完整复现后应另行比较新生成文件与归档文件的哈希；不同求解器版本可能改变等价最优解的所选下标或运行时间，但不应改变已审计的最优值和对偶下界结论。
