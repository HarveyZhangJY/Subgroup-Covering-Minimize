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
- 求解作业 **157153**：已取消。原因：调用 `solve-covers.py` 时缺少第 4 个参数（JSON 输出路径），四个分片会同时写同一个 `solutions-18.jsonl`，证书不可用。未采用其结果。
- 求解作业 **157173**：已用修正后的脚本重新提交，4 路并行，单实例 120 秒，输出到 `parts/sol-covers-solve-*.jsonl`，完成后自动合并、排序并运行 `audit.py`。
- 环境：`$HOME/venv-pq/bin/python`，SciPy 1.18.1 / NumPy 2.5.4。
- 平台限制：仅 `qos_stu_default` 可用；4 CPU、16G、4 小时、MaxJobsPU=4。
- 当前状态：运行中，已完成约 29/73 个群；部分实例出现 `status=1`（超时），需等待最终审计判断全局下界是否仍为 60。若全局下界不足，需增加线类有效不等式或硬超时后重跑。

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
