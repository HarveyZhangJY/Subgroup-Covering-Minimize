# USTC “一〇七”本科生算力平台使用记录

## 访问与登录

- 入口：https://107.ustc.edu.cn/
- 登录方式：统一身份认证（学工号/GID + 密码），账号由用户本人持有；不要把凭据写入仓库或脚本。
- 平台：SCOW 门户 + Slurm；登录节点 Web Shell，路由 `/loginCluster`；文件管理 `/files/training/~`。
- 文档：https://107.ustc.edu.cn/docs/ （公开；资源、作业、环境、Slurm 速查均在此）。
- 平台规范：仅限学习、教学与科研；账号不得转借；计算任务须经 Slurm，不在登录节点跑重计算。

## 已配置环境（2026-11-12）

- 主目录：`/home/scc/pb26000042`，与 `/public` 共用 983T 存储（约 786T 可用）。
- 仓库克隆：`$HOME/subgroup-cover`（GitHub 公开仓库）。
- GAP：conda 环境 `/home/scc/pb26000042/.conda/envs/gap`，GAP 4.15.1，含 `smallgrp` 包；已验证 `NumberSmallGroups(324)=176`。
- 启动 GAP：
  `$HOME/.conda/envs/gap/bin/gap -q -A script.g`
- Python 3.12.3（系统）；conda base：`/public/app/miniconda3/py312_24.4.0-0`。
- module：`source /etc/profile.d/modules.sh; module load miniconda/py312`。

## Students 分区与 QOS 摘要

- Students：20 节点，每节点 128 CPU、512GB/1TB 内存、8×A100 或 8×RTX5090；分区 `MaxNodes=2`，`MaxTime=UNLIMITED`。
- 常用 QOS（每用户上限）：
  - `qos_stu_default`：4h，cpu=4，gpu=1，mem=16G，MaxJobsPU=4，MaxSubmitPU=10。
  - `qos_stu_small`：8h，cpu=8，gpu=1，mem=32G。
  - `qos_stu_medium`：24h，cpu=16，gpu=1，mem=64G。
  - `qos_stu_medium_2gpu`：24h，cpu=24，gpu=2，mem=128G。
  - `qos_stu_long`：3d，cpu=16，gpu=1，mem=64G。
  - `qos_stu_cpu_long`：3d，cpu=32，gpu=0，mem=128G。
  - `qos_stu_large`：12h，cpu=48，gpu=4，mem=240G。
  - `qos_stu_large_8gpu` / `_long`：12h/3d，cpu=96/128，gpu=8，mem=480G。

## \(n=44\) 平台复算进度（2026-11-12）

- 导出作业 **157146**：已完成。`covers-44.jsonl` 共 73 个候选群，`export-44.log` 共 167 行（全部 ID 交代）。
- LP 下界作业 **157269**：已完成。73 条记录（64 个可覆盖 + 9 个不可覆盖）；全局 LP 下界的最小值为 **58**，唯一低于 60 的群是 `SmallGroup(1936,166)`；其余可覆盖群的 LP 上整下界均 \(\ge60\)。
- `SmallGroup(1936,167)=C_{22}\times C_{22}\times C_2\times C_2\cong C_{11}^2\times C_2^4`：MILP 已精确求得 **60** 覆盖（`cover=60, bound=60, status=0`），证书在 `one167-sol.jsonl`。因此 \(\alpha(44)\le60\)。
- `SmallGroup(1936,166)=C_2^3\times((C_{11}^2):C_2)`：结构正是 T1 的 60 覆盖见证群；但其**全部** 44 阶子群有 3780 个，而 T1 的 `scan11.jsonl` 中该群只有 420 个（疑为仅保留“分裂型” \(H\cap Q\) 的受限模型）。全模型 LP 下界仅 58。
- 对全模型做的“是否存在 ≤59 覆盖”可行性 MILP（`find59.py`，目标 0 + 基数约束 \(\sum x\le59\)）在 HiGHS 1.2.0 下运行超过 6 分钟仍未返回可行解或不可行证明，已取消。
- 上述 LP/早期 MILP 只给出 \(\alpha(44)\in[58,60]\)；后续 32-CPU 高 QOS 与对称破缺将严格下界提升到 59，见下一节。
- 计算环境：`$HOME/venv-pq/bin/python`，后统一为 SciPy 1.13.1 / NumPy 2.2.6（并安装 PySCIPOpt 6.3.0、OR-Tools 9.15）。

## \(n=44\) 高 QOS 复算（2026-11-13）

- 用户已开通 `qos_stu_cpu_long`：32 CPU、128 GB，纯 CPU。GUI/CLI 提交高配额作业已成功。
- 四路并行 Campaign（Job 159548）：
  - SCIP 局部分支半径 10：**9.8 秒证明该邻域最优为 60**（`dualbound=60`）；
  - 后续半径 20、30、40 均被 SCIP 证明局部最优为 60（半径 40 用时 641 秒）；
  - 因此任何 59 覆盖与标准 60 覆盖的 Hamming 距离至少大于 40。
- `SmallGroup(1936,166)` 的分解与对称破缺：GAP 确认 \(\mathrm{Aut}(G)\) 在 44 阶子群上只有两个轨道——84 个类型 A（\(\pi(H)\cong C_{11}\)）与 3696 个类型 B（\(\pi(H)\cong D_{22}\)）。类型 A 无法覆盖 \(sP\)，故任何覆盖必含类型 B；Aut 在类型 B 上传递，因此可固定 60 覆盖中的 `index=55`（类型 B）而不失一般性。
- 对称固定后的最终作业 **159773**（32 CPU，4 小时）：
  - SCIP：primal 60，dual **58.333333**，时间上限到达；原问题整数下界 \(\lceil58.333333\rceil=59\)；
  - CP-SAT \(\le59\) 可行性：4 小时返回 **UNKNOWN**，未找到 59 覆盖，也未证明不可行；
  - CP-SAT 最小化：返回可行 **60**，未证最优。
- 因此严格结论为
  \[
  \boxed{59\le\alpha(44)\le60.}
  \]
  若后续证明 59 不可行，则 \(\alpha(44)=60\)；若找到 59 覆盖，则 \(\alpha(44)\le59\)。

## 待办（下次继续）

1. 上传 `computation/order1936/`（n=44=11·2²，1936 阶 167 群）的脚本并提交 Slurm 作业，完整计算 α(44)，验证 T1 的 α(44)=60。
2. 若平台独立复算成功，下载/归档证书，补 `verification.md` 与 SHA-256。
3. 可用平台独立复算 α(18), α(20), α(28)（本地已有完整证书；平台作为第二实现/第二 GAP 版本）。
4. 整合新结果到 `output/solution.tex` 与论文 PDF，更新 GitHub 仓库。

## 本地已确认的新结果（2026-11-12）

- α(12)=17（既有）。
- α(18)=27（324 阶 176 群完整枚举；达到者 SmallGroup(324,121)、(324,170)）。
- α(20)=30（400 阶 221 群；唯一达到者 SmallGroup(400,221)=C5²×C2⁴）。
- α(28)=40（784 阶 172 群；唯一达到者 SmallGroup(784,172)=C7²×C2⁴）。
- 一般定理：若 p>b²=q^{2α} 且 q∤p²−1，则 α(pq^α)=(p+1)(q^α+1)。
- 已撤回错误命题“正规 p-Sylow ⇒ m≥P(n)”；反例为 n=12 的 SmallGroup(144,192)，19<20。
