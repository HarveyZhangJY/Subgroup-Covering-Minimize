# \(n=pq^\alpha\) 定向文献检索：\(p^2q^{2\alpha}\) 由 \(pq^\alpha\) 阶子群覆盖

检索日期：2026-11-11。本文只做定向检索与证据分级，不重新证明小例，不重复 `literature.md`、`primary-sources.md`、`sequence-lookup.md` 已有的广泛检索。所有“未检出”均指**在本文列出的检索通道与检索词下未检出**，不等于绝对不存在。

---

## 0. 结论摘要

1. **没有任何文献给出 \(\alpha(18)\)、\(\alpha(20)\)、\(\alpha(28)\) 或同类小参数的精确值。** 等级 D（检索不到）。这三个量词下的值只能来自 C1/C2 的完整计算。
2. **没有任何文献研究“阶 \(p^2q^{2\alpha}\) 的群由阶 \(pq^\alpha\) 的子群覆盖”这一具体族。** 等级 D。存在的只有两种相邻文献：(i) Jungnickel 的 **任意平方阶** \(s^2\) 的小覆盖结构定理（对 \(s=pq^\alpha\) 可用，但只给弱下界 \(s+p_{\min}\)）；(ii) 几何方向的 \(s\)-cover（\(s\) 为素数幂），与本族无关。
3. **可以安全引用的文献下界只有 \(\alpha(n)\ge n+p_{\min}(n)\)**（Jungnickel 1999，等级 B）。对本项目关心的三个 \(n\)，它给出的 20/22/30 分别**严格弱于**项目内部已有的 \(n+b\) 下界（27/24/32）。因此 T2 的 \(n+b\) 下界在文献中无对应结果，必须作为本项目结果呈现。
4. **可以安全引用的文献结构约束**：等阶覆盖的公共阶被 \(\exp(G)\) 整除（等级 A，两处独立原文）；\(n=pq^\alpha\) 非素数幂时不可能存在等阶**划分**（等级 A，Isaacs 1973），故 \(\alpha(n)\ge n+2\)。
5. 术语 “equal covering number” 确由 2022 年学位论文在 “Possible Future Work” 中提出（等级 A），此后 Foguel 等（2025，等级 A）与 Lucchini（2025，等级 B）都只研究存在性与 \(\xi(G)\)，**无人给出该数的一般公式或算法**。
6. 本轮把 Foguel 等的**正文**取到并通读（前一份报告标记为“未能连接”），因此该文的定理号与陈述升级为 A 级证据。

---

## 1. 量词区分（避免混引）

| 记号 | 定义 | 本文是否涉及 |
|---|---|---|
| \(\alpha(n)\) | \(\min\{c_n(G): |G|=n^2\}\)，\(c_n(G)\) 为用阶 \(n\) 子群覆盖 \(G\) 的最少个数；不可覆盖记 \(\infty\) | 是（本项目主量） |
| \(c_n(G)\) | 固定 \(G\)、固定阶 \(n\) 的最小覆盖数 | 是（C1/C2 的中间量） |
| \(\sigma(G)\) | 用**任意**真子群覆盖 \(G\) 的最小数（Cohn/Tomkinson 传统） | 否，只作背景 |
| \(\xi(G)\) | 使 \(G^n\)（笛卡尔幂）有等阶覆盖的最小 \(n\)（Foguel 等） | 否，只作背景 |
| “equal covering number” | 固定 \(G\) 的等阶覆盖最小成员数（论文提出的**开放**量） | 否（与 \(\alpha\) 相差外层 \(\min_G\) 与“公共阶是否等于 \(\sqrt{|G|}\)”） |

关键差别：\(\alpha(n)\) 要求公共阶**恰为** \(n=\sqrt{|G|}\)，而等阶覆盖文献允许公共阶为任意真子群的阶。因此 Foguel 等与 Velasquez-Berroteran 的定理**不能**直接给出 \(\alpha(n)\)。

---

## 2. 检索执行

### 2.1 通道

- WebSearch（中英文精确短语与作者/引文链）；
- WebFetch（出版方页面、Dergipark PDF、arXiv PDF）；
- zbMATH Open API（`api.zbmath.org/v1/document/_search`，含 `ti:`、`any:`、`cc:` 结构化检索与评论全文）；
- OpenAlex API（`search=`、`filter=cites:`）；
- arXiv API 与 `export.arxiv.org` PDF；
- Crossref（书目与被引计数）；
- OEIS JSON 接口（沿用 `sequence-lookup.md` 的记录，本轮不重复）；
- Stack Exchange API（mathoverflow / math.stackexchange）。

### 2.2 主要检索词（实际提交）

```text
"groups of order p^2q^2" covered by subgroups of order pq
"subgroup covering number" finite group fixed order
"number of subgroups" "groups of order p^2q^2" classification
"covering number" group "order p^2 q" sigma(G)
"equal covering number" group subgroups same order minimum
minimal coverings of groups of small order computed covering number sigma table GAP
"Hall subgroups" "union" cover finite group "covers by Hall subgroups"
"p^2q^2" 群 子群个数 "pq阶子群" 覆盖
"p^2q^2阶群" 覆盖 子群 极小 覆盖数
```

zbMATH 结构化检索：

```text
cc:20D30 & any:cover
ti:cover* & cc:20D              (328 条，逐条看标题)
any:"equal covering"            (8 条，其中仅 3 条相关)
any:"congruence cover"          (5 条，仅 Jungnickel 1999 相关)
any:"covering number" & cc:20D  (77 条)
any:"s-cover" / any:"homogeneous cover" / any:"coverings by subgroups" & cc:20D
```

OpenAlex 全文检索：`"covered by subgroups of order"`、`"subgroups of order pq"`、`"subgroups of the same order"`、`"equally covered groups"`、`"groups of order p^2q^2"`、`"congruence cover group subgroups order"`。

### 2.3 本轮访问状态

- **成功**：Dergipark 上 Foguel 等正文 PDF（`https://dergipark.org.tr/en/download/article-file/4288611`，315 235 字节，已 `pdftotext` 通读）；arXiv `2206.14843` PDF（经 `export.arxiv.org` 下载并通读）；zbMATH API 评论；OpenAlex；Crossref。
- **未成功/未再尝试**：Project Euclid 的 Jungnickel 1999 正文（前轮被 Incapsula 阻断，本轮未重试）；ScienceDirect 的 Jungnickel–Storme 2001 正文（前轮 403）；zbMATH 网页版（沿用 API 评论）。
- 因此 Jungnickel 两篇仍为 B 级。

---

## 3. 命中一览

| 编号 | 文献 | 等级 | 与本题关系 |
|---|---|---|---|
| L1 | Isaacs, *Equally partitioned groups*, 1973 | **A** | 排除 \(n=pq^\alpha\) 的 \(n+1\) 实现 |
| L2 | Jungnickel, *On small congruence covers*, 1999 | **B** | 任意平方阶：\(m\le s+p-1\Rightarrow\) 初等阿贝尔 ⇒ \(\alpha(n)\ge n+p_{\min}\) |
| L3 | Jungnickel–Storme, *Packing and covering groups with subgroups*, 2001 | **B** | 固定阿贝尔 \(p\)-群的 \(s\)-cover/\(s\)-packing 界；无两素数情形 |
| L4 | Velasquez-Berroteran, *Equal Coverings of Finite Groups*, 2022 | **A** | \(\exp(G)\mid\) 公共阶；把 equal covering number 列为未来工作 |
| L5 | Foguel–Moghaddamfar–Schmidt–Velasquez-Berroteran, *Concerning equally covered groups*, 2025 | **A** | 等阶覆盖的结构引理（含 \(n=p\) 时恰 \(p+1\) 的结论） |
| L6 | Lucchini, *Answering a question on equally covered groups*, 2025 | **B** | \(\xi(G)\) 无界；与 \(\alpha\) 无关 |
| L7 | Sun, *Finite covers of groups by cosets or subgroups*, 2006 | **B** | 正规 Hall 子群覆盖的普适不等式；数值上弱 |
| L8 | 陈松良 2009；陈松良–张传军 2012 | **C** | \(p^2q^2\) 阶群完全分类（4/11/15/6/7 型）；无覆盖数 |
| L9 | 苗雷星–曹洪平 2021 | **C** | \(\sigma(G)=k(G)\) 的群只有 \(C_p\times C_p\) 与非交换 \(pq\) 群 |
| L10 | 钱国华 2011 | **C** | 能表为 \(p+1\)/\(p+2\) 个真子群并的群的结构 |
| L11 | Bryce–Fedri–Serena 1999 | **B** | \(\sigma(\mathrm{GL}_2(q))\) 等精确值；方法学参照 |
| L12 | Zappa, *Partitions and other coverings of finite groups*, 2003 | **B** | 群划分史综述，确认无“固定阶覆盖数”公式 |
| L13 | Szegedy, *Coverings of abelian groups and vector spaces*, 2007 | **C** | 阿贝尔群/向量空间的子群覆盖；非固定阶 |
| L14 | 社区与数据库 | C/D | MO/MSE 无本题；OEIS 无本数列 |

---

## 4. 逐条证据

### L1 Isaacs 1973（A）

- I. M. Isaacs, *Equally partitioned groups*, Pacific J. Math. **49**(1) (1973), 109–116. DOI [10.2140/pjm.1973.49.109](https://doi.org/10.2140/pjm.1973.49.109)。前轮已下载出版方扫描 PDF 并逐页核对（见 `primary-sources.md`）。
- 已核实：Theorem 6（p.111，证明至 p.112）——“Let \(G\) be equally partitioned. Then \(G\) is a \(p\)-group of exponent \(p\)”；结合 p.109 的逆方向得“非循环、指数为素数 \(p\) 的 \(p\)-群”。
- **对 \(n=pq^\alpha\) 的直接推论（本项目推导，非 Isaacs 原文陈述）**：\(\alpha(n)=n+1\) 会迫使 \(|G|=n^2\) 的群有等阶划分，从而 \(G\) 是 \(p\)-群，与 \(n\) 有两个素因子矛盾。故 \(\alpha(n)\ge n+2\)。这条比 L2 弱，但等级最高。

### L2 Jungnickel 1999（B）

- D. Jungnickel, *On small congruence covers*, Bull. Belg. Math. Soc. Simon Stevin **6**(3) (1999), 413–421. DOI [10.36045/bbms/1103065860](https://doi.org/10.36045/bbms/1103065860)；Zbl 0947.51006（[zbMATH 1374975](https://zbmath.org/1374975)）。
- zbMATH 评论（Norbert Knarr）原文：“Let \(G\) be a group of square order \(s^2\). A congruence cover of \(G\) is a collection of \(r\) subgroups of \(G\) of order \(s\) the union of which is all of \(G\). The number \(e=r-s-1\) is called the excess of the cover. Let \(p\) be the smallest prime divisor of \(s\) and assume that \(G\) admits a congruence cover of excess at most \(p-2\). Then \(G\) is elementary abelian…For \(p\)-groups this bound is sharp; there are examples of non-elementary abelian \(p\)-groups admitting a congruence cover of excess \(p-1\).”
- 出版方摘要（二手转录，与评论在**主定理**上一致）：“any group of square order \(s^2\) which admits a cover by at most \(s+p-1\) subgroups of order \(s\) … is necessarily elementary abelian”；并称 sharp 构造为 \(s+p+1\) 个成员。
- **对本问题的可用形式**：\(s\) 任意（不限于素数幂），故 \(s=n=pq^\alpha\) 时，\(m\le n+p_{\min}-1\Rightarrow\) 初等阿贝尔 ⇒ 矛盾；即
  \[
  \alpha(n)\ \ge\ n+p_{\min}(n).
  \]
- **重要限定**：这是本项目从“小覆盖 ⇒ 初等阿贝尔”转写出的推论，原文并未讨论 \(n=pq^\alpha\)，也未给出 \(\alpha(n)\) 的记号和数值。e 的 sharp 值在摘要（\(e=p\)）与评论（\(e=p-1\)）间不一致，正文未读，不得据此声称任何非初等阿贝尔群的精确最小值。

### L3 Jungnickel–Storme 2001（B）

- D. Jungnickel, L. Storme, *Packing and covering groups with subgroups*, J. Algebra **239**(1) (2001), 191–214. DOI [10.1006/jabr.2000.8640](https://doi.org/10.1006/jabr.2000.8640)；Zbl 0992.20017。
- zbMATH 评论（Patric Östergård）：研究用指定阶 \(s\) 子群覆盖或 packing 有限群；改进的是**阿贝尔 \(p\)-群**中 \(p^t\)-packing 与 \(p^t\)-cover 的上下界，并刻画初等阿贝尔群。
- **与本问题的关系**：两素数阶 \(p^2q^{2\alpha}\) **不在**其已核实范围内（评论只提到阿贝尔 \(p\)-群）。不得把其界移植到 \(n=pq^\alpha\)。

### L4 Velasquez-Berroteran 2022（A）

- 学位论文 / arXiv:[2206.14843](https://arxiv.org/abs/2206.14843)（本轮重新下载 PDF 并通读关键段）。
- **Theorem 13**（已逐字核对）：“If \(G\) has an equal covering \(\mathcal H=\{H_i\}\), then \(\exp(G)\) divides \(|H_i|\) for all \(H_i\in\mathcal H\).”
- **Theorem 18**（已逐字核对）：阶为两个或更多**互异**素数的一次乘积（平方自由）的群没有等阶覆盖。
- **第 4 节 “Possible Future Work” 第 2 条**（已逐字核对）：定义 \(\gamma(G)=\min\{|\mathcal H|:\mathcal H \text{ is an equal covering of } G\}\)，即 equal covering number，作为**未解决问题**提出。
- 论文 Table 1/2 对阶 ≤ 60 的群（**含阶 18、20、28**）逐群判定“是否**存在**等阶覆盖”，并用 GAP 给出 Yes/No 与依据。这是最接近 \(\alpha(18)/\alpha(20)/\alpha(28)\) 的既有计算，但：
  - 它判定的是**该阶群自身**是否有等阶覆盖，而不是“阶 \(n^2\) 的群用阶 \(n\) 子群覆盖”；
  - 只有布尔值，没有最小成员数；
  - 覆盖允许的阶可以是 6、12、18 等任意真子群阶。
  因此**不能**从中读出 \(\alpha\) 的任何值。

### L5 Foguel, Moghaddamfar, Schmidt, Velasquez-Berroteran 2025（A，正文已读）

- Int. Electron. J. Algebra **37** (2025), 352–365. DOI [10.24330/ieja.1567377](https://doi.org/10.24330/ieja.1567377)；Zbl 1560.20048。正文 PDF 本轮获取成功并通读。
- 与本问题结构相关、已逐字核对的条目：
  - **Lemma 2.1**：“If \(G\) has an equal covering \(\mathcal H=\{H_1,\dots,H_n\}\), then \(\exp(G)\) divides \(|H_i|\) for all \(H_i\)”，即 \(\pi(H_i)=\pi(G)\)。
  - **Lemma 2.2**：有等阶覆盖的群至少有两个非共轭极大子群 \(M_1,M_2\) 且 \(\pi(M_1)=\pi(M_2)=\pi(G)\)。
  - **Lemma 2.10**：“If \(G\) is a group with \(\exp(G)=|G|/p\) where \(p\) is the smallest prime dividing \(|G|\), then every equal covering of \(G\) is a maximal equal covering…by proper normal subgroups of index \(p\). Moreover…\(G\) has a maximal equal covering consists of \(p+1\) proper normal subgroups of index \(p\).”
  - **Corollary 2.7**：超可解群、\(p\) 为最小素因子且 Sylow \(p\)-子群非循环 ⇒ 有等阶覆盖。
  - 引言式 (3)：\(n\) 个真子群的不可去覆盖满足 \(1<|G:H_i|<n\)。
- **对 \(n=p\) 的校验**：此时 \(|G|=p^2\)、成员阶 \(p\)、指数 \(p\)、\(\exp(G)=p\)，Lemma 2.10 直接给出 \(p+1\) 个正规子群，与本项目 \(\alpha(p)=p+1\) 一致（文献级旁证）。
- **对 \(n=pq^\alpha\)**：Lemma 2.1 给出必要条件 \(\exp(G)\mid n\)；但文献不涉及“公共阶固定为 \(\sqrt{|G|}\)”，也不给最小数，故**无 \(\alpha\) 值**。

### L6 Lucchini 2025（B）

- A. Lucchini, *Answering a question on equally covered groups*, Int. Electron. J. Algebra **38** (2025), 70–73. DOI [10.24330/ieja.1582755](https://doi.org/10.24330/ieja.1582755)；Zbl 1575.20017。
- zbMATH 评论（Egle Bettio）：Foguel 等定义 \(\xi(G)\) 为最小的 \(n\) 使 \(G^n\) 有等阶覆盖，观察到 \(\xi(G)\le |G|+1\)，并问是否存在与 \(G\) 无关的上界；Lucchini 否定回答：“For every positive integer \(t\), there exists a finite simple group \(G\) with \(\xi(G)>t\)”。打开 DOI 页面只见摘要句 “We prove that the answer is negative.”，全文未读。
- **与本问题关系**：\(\xi\) 与 \(\alpha\) 是不同的量；此文既不给覆盖数，也不涉及 \(p^2q^{2\alpha}\)。

### L7 Sun Zhi-Wei 2006（B）

- Z.-W. Sun, *Finite covers of groups by cosets or subgroups*, Int. J. Math. **17**(9) (2006), 1047–1064. DOI [10.1142/S0129167X06003813](https://doi.org/10.1142/S0129167X06003813)；Zbl 1113.20037。
- zbMATH 评论所载主要结果：(a) 若 \(G_1,\dots,G_k\) 是正规 Hall 子群，则 \(|\bigcup a_iG_i|\ge|\bigcup G_i|\)；(b) 若 \(\{a_iG_i\}\) 是极小 \(m\)-覆盖且 \(G\) 循环或 \(G_i\) 为正规 Hall 子群，则
  \[
  k\ \ge\ m+f\!\left(\left[G:\bigcap_i G_i\right]\right),\qquad f(n)=\sum_t \alpha_t(p_t-1)\ \ (n=\textstyle\prod_t p_t^{\alpha_t}).
  \]
- **对本题的适用性**：当覆盖成员恰为正规 Hall 子群（在 \(G\) 有正规 Sylow 子群的可解情形可能发生）时，取 \(m=1\) 得 \(k\ge 1+f([G:\bigcap H_i])\)。由于 \([G:\bigcap H_i]\le n^2\)，最优情形下也只给 \(k\ge 1+2\sum\alpha_t(p_t-1)\)（\(n=18\) 时约 11），**远弱于** \(n+b\)，数值上无帮助。仅可作为“正规 Hall 覆盖的普适不等式”引用。

### L8 \(p^2q^2\) 阶群的分类（C）

- 陈松良，《\(p^2q^2\) 阶群的完全分类》，《华中师范大学学报（自然科学版）》2009 年第 4 期，531–533（[CNKI 记录](https://read.cnki.net/web/Journal/Article/HZSZ200904002.html)）。摘要（经 CNKI 镜像页转录）：设 \(p,q\) 为奇素数、\(p>q\)，分类结果依 \(q\mid p^2-1\) 的情形分别为 4/11/15/6/7 个同构型。
- 陈松良、张传军，《关于“\(p^2q^2\) 阶群的完全分类”一文的注记》，同刊 2012 年第 2 期，137–139（[CNKI 记录](https://wap.cnki.net/touch/web/Journal/Article/HZSZ201202004.html)）：非交换超可解且 Sylow \(p\)-子群初等交换时，\(q\mid p-1\) 但 \(q^2\nmid p-1\) 有 \(q+4\) 型，\(q^2\mid p-1\) 有 \((q^2+3q+10)/2\) 型。
- **等级说明**：只读到索引页摘要，未读正文，故 C。**用途**：为 \(n=pq\)（\(b=q\)）枚举提供结构清单与型数校验，但两文都不涉及覆盖，不含任何覆盖数。

### L9 苗雷星–曹洪平 2021（C）

- 《真子群个数与极小真子群覆盖数相等的群》，《西南师范大学学报（自然科学版）》2021 年第 8 期，7–9。DOI [10.13718/j.cnki.xsxb.2021.08.002](https://doi.org/10.13718/j.cnki.xsxb.2021.08.002)。
- 摘要与部分正文（出版方页面）：\(\sigma(G)=k(G)\)（极小真子群覆盖数等于真子群总数）当且仅当 \(G=C_p\times C_p\) 或 \(G\) 为非交换 \(pq\) 阶群；文中另证非交换 \(pq\) 群有 \(q+1\) 个真子群且 \(\sigma(G)=q+1\)。
- **关系**：这是中文文献中唯一把“两素数阶群”与“覆盖数”联系起来的条目，但对象是 \(\sigma\)（成员可不同阶）且只讨论 \(\sigma=k\) 的极端情形，与 \(\alpha\) 无关。

### L10 钱国华 2011（C）

- 《能表示成四个真子群并的有限群》，《数学杂志》31(5) (2011), 891–892。摘要（经索引页与部分正文）：设 \(p\) 为 \(|G|\) 的最小素因子，则 \(G\) 不能表为 \(p\) 个真子群之并；能表为 \(p+1\) 个真子群之并且不能更少 \(\iff\) \(G\) 有商群 \(\cong C_p\times C_p\)；\(p+2\) 个的情形 \(\iff p=2\) 且有商群 \(\cong C_3\times C_3\) 或 \(S_3\)。
- **关系**：小覆盖（成员阶不限）的结构定理，其“\(p+1\) 个成员 \(\iff\) 有 \(C_p\times C_p\) 商”与本项目小 \(n\) 的结构论证可互相参证；但不含固定阶覆盖数。

### L11 Bryce–Fedri–Serena 1999（B）

- *Subgroup coverings of some linear groups*, Bull. Austral. Math. Soc. **60**(2) (1999), 227–238；Zbl 0939.20053。
- zbMATH 评论载 Theorem 3.5：\(q\ge4\) 且 \(G\in\{\mathrm{GL}_2(q),\mathrm{PGL}_2(q),\mathrm{SL}_2(q),\mathrm{PSL}_2(q)\}\) 时 \(\sigma(G)=\tfrac12q(q+1)\)（\(q\) 偶）或 \(\tfrac12q(q+1)+1\)（\(q\) 奇），\(q\ne5,7,9\) 例外另行处理。
- **关系**：说明“精确覆盖数”文献的典型形态是**固定群族**的 \(\sigma\)，而非固定成员阶、更非在阶 \(n^2\) 的群上取 \(\min\)。可作为“为何 \(\alpha(n)\) 无文献值”的旁证。

### L12 Zappa 2003（B）

- G. Zappa, *Partitions and other coverings of finite groups*, Illinois J. Math. **47**(1–2) (2003), 571–580；Zbl 1033.20018。
- zbMATH 评论：对有限群**划分**理论从 1900 年代初起做详细历史综述，33 条参考文献；关键词含 group partitions、group coverings。
- **关系**：综述性确认“划分/覆盖”传统关注存在性与结构，不含固定阶最小覆盖数公式。可作为“未见一般公式”的弱旁证（B 级评论，未读正文）。

### L13 Szegedy 2007（C）

- B. Szegedy, *Coverings of Abelian groups and vector spaces*, J. Combin. Theory Ser. A **114**(1) (2007), 20–34；Zbl 1105.20045。zbMATH 评论不可用（“contents unavailable due to conflicting licenses”），仅得题名与关键词（finite Abelian groups, coverings by subgroups, cosets, coverings systems, flows, colorings）。
- **关系**：阿贝尔群/向量空间被子群或陪集覆盖的组合问题，非固定阶、非覆盖数最小化。C 级，仅备查。

### L14 社区与数据库（C/D）

- MathOverflow / Math.SE：用 Stack Exchange API 检索 `union of subgroups of order n`、`cover by subgroups of same order`、`subgroups of order pq cover`、`covered by subgroups of order`，未检出与 \(\alpha(n)\) 或 \(p^2q^{2\alpha}\) 相关的提问（仅命中极大子群、七覆盖反例等无关帖）。**D（本次检索下）**。
- OEIS：本数列 \(3,4,5,6,10,8,9,10,16,17,24\) 的连续查询与 `seq:` 查询均返回 `null`（详见 `sequence-lookup.md`）。**D**。

---

## 5. 四个重点问题的直接回答

**Q1：是否存在“\(p^2q^2\)（或 \(p^2q^{2\alpha}\)）由 \(pq\)（或 \(pq^\alpha\)）阶子群覆盖”的覆盖数结果？**
没有。等级 D。存在的只有：
- Jungnickel 1999 的**任意平方阶**小覆盖结构定理（B），它不区分阶的素因子结构，也不给最小数，只在 \(m\le s+p-1\) 时断言群初等阿贝尔；
- Jungnickel–Storme 2001 的**阿贝尔 \(p\)-群** \(s\)-cover 界（B）；
- 几何方向的 congruence cover / line cover（\(s\) 为素数幂时的射影空间子空间覆盖），与本族无关。

**Q2：是否有文献给出 \(\alpha(18)\)、\(\alpha(20)\)、\(\alpha(28)\) 或类似小参数的精确覆盖数？**
没有。等级 D。最接近的既有计算是 Velasquez-Berroteran 论文 Table 2 对**阶 18、20、28 的群**逐群判定“是否存在等阶覆盖”（A 级，但只是布尔值，量词也不同）。因此本项目 \(\alpha(18)\in\{27,28\}\)、\(\alpha(20)\le30\)、\(\alpha(28)\le40\) 的判定完全依赖 C1/C2 的完整计算，不能在文献中找到印证或反驳。

**Q3：是否有 “subgroup covering number” / “covering number by subgroups of fixed order” / “equal-order subgroup cover” 的一般公式或算法？**
没有一般公式。等级 D。分项：
- “equal-order subgroup cover” 是既有术语（equal covering），但其文献（A/B）只做存在性与结构，且 2022 论文明确把 equal covering number 列为**未来工作**；
- \(\sigma(G)\)（成员阶不限）有大量精确结果，但都是**固定群族**（\(\mathrm{GL}_2(q)\)、\(S_n\)、散在群、\(p\)-群），没有以 \(n\) 的素因子分解为输入、在阶 \(n^2\) 的群上取最小的公式；
- 唯一与“固定阶”相关的普适工具是 Jungnickel 的 excess 定理（B）与 Sun 的正规 Hall 覆盖不等式（B），二者都只给弱界。

**Q4：Isaacs 等阶划分、Jungnickel 小覆盖定理之后，是否有针对两个素因子的后续工作？**
没有专门后续。等级 D（就可达索引而言）。引文链证据：OpenAlex `filter=cites:W1603700654` 仅 1 条（即 Jungnickel–Storme 2001）；Jungnickel–Storme 的前向引文 6 条（Maróti 对称群、Abdollahi 等 irredundant 6-cover、Maxson–Smith 环、Abdollahi–Ataei–Mohammadi Hassanabadi blocking sets、Maróti 预印本、Tarmizi–Sulaiman 11-covering）均不针对两素数阶。等阶覆盖这条线上最新的两篇（Foguel 等 2025、Lucchini 2025）也不涉及 \(p^2q^{2\alpha}\)。

---

## 6. 文献可支持的界与本项目界的对比

下表把**文献界**与**项目内部界**分开，避免把项目结果误标为文献结果。

| \(n\) | \(p,b=q^\alpha\) | 文献下界 \(n+p_{\min}\)（L2, B） | 项目下界 \(n+b\)（正规 \(q\)-Sylow，项目自证） | 项目上界 |
|---|---:|---:|---:|---:|
| 18 | \(p=2,\ b=9\) | 20 | 27 | 28（半直积，\(2\mid 8\)） |
| 20 | \(p=5,\ b=4\) | 22 | 24 | 30（直积 \(P(20)\)） |
| 28 | \(p=7,\ b=4\) | 30 | 32 | 40（直积 \(P(28)\)） |

结论：**在每个关心的 \(n\) 上，文献下界都严格弱于项目下界**；文献没有 \(n+b\) 型结论，也没有 \(P(n)\) 型上界的成文引用（直积/展形构造应作为初等构造陈述，不署文献）。

另需注意：\(n=p\) 时 \(\alpha(p)=p+1\) 有文献旁证（L5 Lemma 2.10，A）；\(n=p^a\) 时 \(\alpha(n)=n+1\) 的构造是几何/展形的经典事实（L2 的“e=0 即几何覆盖”，B），可引作背景但不必署为某定理。

---

## 7. 明确空白（gap statement）

1. **空白一（核心）**：不存在以“阶 \(n^2\) 的群、成员阶恰为 \(n\)、在所有此类群上取最小”为对象的一般公式、递归或算法结果。文献中连该量的标准记号都没有（\(\alpha\) 为本项目记号）。
2. **空白二**：不存在 \(n=pq^\alpha\)（\(\alpha\ge1\)，两素数）的专门覆盖数文献。\(p^2q^2\) 阶群的文献是**分类**（L8, C），不是覆盖。
3. **空白三**：不存在 \(\alpha(18),\alpha(20),\alpha(28)\) 的任何文献值；连“\(\alpha(12)\)”这类小参数也没有。项目已认证的 \(\alpha(12)=17\) 亦无文献对照。
4. **空白四**：Jungnickel 1999 的正文未取得（B 级），其 sharp 构造（\(e=p\) vs \(e=p-1\)）仍不一致；Jungnickel–Storme 2001 正文未取得（B 级），无法确认是否含非 \(p\)-群章节。
5. **不得声称的内容**：
   - 不得写“Jungnickel 证明了 \(\alpha(n)\ge n+p\)”——他只证了小覆盖必初等阿贝尔，转写是本项目的推论；
   - 不得把 Foguel 等/Lucchini 的 \(\xi(G)\) 结果当作 \(\alpha\) 的结果；
   - 不得把论文 Table 2 的“18/20/28 阶群是否有等阶覆盖”当作 \(\alpha(18)/\alpha(20)/\alpha(28)\) 的信息；
   - 不得声称该问题在文献中被明确称为 open problem（本项目只能说“本项目未解决且本轮未检出一般公式”）。

---

## 8. 后续优先核对（若还要继续文献工作）

1. Jungnickel 1999 正文（Project Euclid / 作者主页）：确认定理对任意 \(s\) 的精确假设、\(e=0\) 的推论、以及 sharp 构造的成员数。作者出版物页 `https://www.uni-augsburg.de/de/fakultaet/mntf/math/prof/opt/team/ehemalige/jungnickel/publikationen/` 已确认该文条目存在（6, 413–421 (1999)）。
2. Jungnickel–Storme 2001 正文：确认是否含非 \(p\)-群（如 \(s=p^aq^b\)）章节；若含，可能直接给两素数情形。
3. Foguel 等后续：OpenAlex 记录 `cited_by_count=1`；zbMATH 评论明确 Lucchini 2025 就是回答其提问者。可据此把它当作唯一已索引的后续，并检查是否有 2026 年新文开始计算 equal covering number。
4. 中文文献：查《数学进展》《代数集刊》是否有“固定阶子群覆盖”条目；CNKI 全文不可得时不要据摘要断言。
