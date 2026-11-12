# 三篇原始文献复核

## 证据级别与结论边界

- **A 级：全文已读。** Isaacs (1973)、Jungnickel (1999)、Jungnickel–Storme (2001) 与 Foguel 等 (2025) 的全文均已取得并逐页核对；逐条引文、定理号与页码见 `research/citation-review.md`。
- 本节以下保留早期证据分级的历史记录；其中“B 级/正文未取得”的说法已被 2026-11-12 的全文核对取代，不再有效。

## 1. Isaacs (1973)：等阶划分分类

**文献。** I. M. Isaacs, *Equally partitioned groups*, Pacific J. Math. 49 (1973), 109–116。  
[出版方页面](https://msp.org/pjm/1973/49-1/p11.xhtml)；[公开 PDF](https://msp.org/pjm/1973/49-1/pjm-v49-n1-p11-s.pdf)；[DOI](https://doi.org/10.2140/pjm.1973.49.109)。**证据 A。**

### 1.1 准确假设与结论

- **p.109 的定义：**划分由真子群组成，且每个非单位元恰属于一个成员。该页还给出逆方向：若 \(G\) 是指数为 \(p\) 的 \(p\)-群且 \(|G|>p\)，所有循环子群构成等阶划分。
- **Theorem 6，p.111（证明续至 p.112）：**
  > “Let \(G\) be equally partitioned. Then \(G\) is a \(p\)-group of exponent \(p\).”

  结合 p.109 的逆方向，准确分类是：**有限群能由等阶真子群划分，当且仅当它是非循环、指数为某个素数 \(p\) 的 \(p\)-群。**这里不能加入“阿贝尔”。
- **Theorem 10，pp.115–116：**若 \(n\le p\)、\(q=p^e\)，则 \(GL(n,q)\) 的 Sylow \(p\)-子群可由阶 \(q\) 的阿贝尔子群划分；本节开头明确说明 \(p>2\) 时给出非阿贝尔例。故一般等阶划分群确实不限于初等阿贝尔群。
- **Theorem 8，pp.114–115：**若一个有限群的划分成员两两可置换（\(HK=KH\)），则 \(G\) 初等阿贝尔；原文还明确说不假定成员等阶。但本题等阶划分并不自动满足 \(HK=KH\)，所以不能单独借用此定理完成本题等号分类。

### 1.2 本题等号情形需要再加 Jungnickel

若 \(|G|=n^2\)，且 \(n+1\) 个阶 \(n\) 子群覆盖 \(G\)，计数表明它们构成等阶划分。Isaacs 只给出 \(n=p^a\)、\(\exp(G)=p\)，并不单独给出 \(G\) 初等阿贝尔。Jungnickel (1999) 的小覆盖定理中取 excess \(e=0\)，才有 \(G\) 初等阿贝尔，从而

\[
n=p^a,\qquad G\cong(C_p)^{2a}.
\]

所以 `literature.md` 原第 92 行把“一般等阶划分群的分类”直接用于“本题固定群阶 \(n^2\) 且成员数为 \(n+1\) 的等号分类”，范围混淆；现已修正。

## 2. Jungnickel (1999)：small congruence cover

**文献。** D. Jungnickel, *On small congruence covers*, Bull. Belg. Math. Soc. Simon Stevin 6(3) (1999), 413–421。  
[DOI / Project Euclid](https://doi.org/10.36045/bbms/1103065860)；[zbMATH 评论 API](https://api.zbmath.org/v1/document/1374975)。**证据 A（全文已读，作者自排终稿，页码与期刊 413–421 一致）。**

已核实的定理号与页码：Theorem 1.4（p.415，小覆盖迫使初等阿贝尔）、Theorem 3.3（p.417，逆否形式）、Theorem 3.4（p.418，幂零群下界）、Proposition 4.1（p.418，直积构造）、Proposition 4.2（p.418，\(e=p-1\) 的 sharp 例）、Proposition 4.3（p.419，\(e=p\) 的构造）。

### 2.1 两种独立转录一致的主定理

出版方摘要转录与 Norbert Knarr 的 zbMATH 评论一致给出以下假设和结论：

- \(|G|=s^2\)；congruence cover 是 \(r\) 个阶 \(s\) 子群，其并为 \(G\)；
- excess 定义为 \(e=r-s-1\)；
- \(p\) 是 \(s\) 的最小素因子；
- 若 \(e\le p-2\)，等价于 \(r\le s+p-1\)，则 **\(G\) 初等阿贝尔**，且覆盖是几何覆盖，即可视为适当射影空间的子空间覆盖。

本题若 \(r\le n+p-1\)，其中 \(p\) 为 \(n\) 的最小素因子，则 \(G\) 初等阿贝尔；非素数幂 \(n\) 因而不可能，故得到下界 \(M(n)\ge n+p\)。特别地 \(e=0\) 给出上节所需的等号群分类。由于全文未取得，上述结论可引用到文章摘要和 zbMATH 评论，但暂不标具体定理号或定理所在页。

### 2.2 sharp 构造：两条并存的命题（已由原文解决）

- **\(e=p-1\)：** Proposition 4.2（p.418）在 \(G=Z_{p^d}\times Z_{p^d}\) 上给出 \(\kappa(G)=p^d+p^{d-1}\)；取 \(d=2\) 得 \(e=p-1\)。原文 p.419 明言此例说明 Theorem 3.3 的界“can be sharp”。
- **\(e=p\)：** Proposition 4.3（p.419）在 \(G=Z_{p^2}\times Z_p^{2d-2}\)（\(d\ge2\)，proper prime power）上给出 \(\kappa(G)=p^d+p+1\)，即 \(e=p\)；原文 p.419 称该界“essentially best possible … off by at most 1”。

摘要中的 \(s+p+1\) 与 zbMATH 评论中的 \(e=p-1\) 分别指这两条，二者互不冲突。本文实际使用的“小覆盖必初等阿贝尔”不依赖其中任何一条。

## 3. Jungnickel–Storme (2001)：固定 \(p\)-群的界

**文献。** D. Jungnickel, L. Storme, *Packing and covering groups with subgroups*, J. Algebra 239(1) (2001), 191–214。  
[DOI](https://doi.org/10.1006/jabr.2000.8640)（正确 PII 为 `S002186930098640X`）；[zbMATH 评论 API](https://api.zbmath.org/v1/document/1643653)。**证据 A（全文 24 页已读）。**

已核实范围：cover 结果主要在 \(p\) 群内——Proposition 2.5（p.195）对任意阶 \(p^d\) 的群给出 \(\kappa(G,p^{d-1})=p+1\)；Theorem 4.1（p.200）与 Corollary 4.2（p.201）给出阿贝尔 \(p\) 群 \(p^t\)-cover 的 excess 下界与初等阿贝尔刻画；Theorem 6.1（pp.203–204）给出一般 \(p\) 群的构造上界。对任意 \(s\) 只有 Proposition 2.1（p.194，packing 侧 Theorem 3.5，p.198）与转述 1999 年结果的 Result 1.3（p.192）。原文 p.213 明确把“任意群或幂零群”列为公开问题，因此该文不构成任意 \(n\) 的存在型一般公式。

## 4. 对三个复核问题的最终回答

1. **等阶划分分类：**Isaacs Theorem 6 加 p.109 逆方向，恰为非循环、指数 \(p\) 的 \(p\)-群；一般有非阿贝尔例。本题 \(n+1\) 等号覆盖还需 Jungnickel 的 \(e=0\) 结论，才能得到 \(G\cong(C_p)^{2a}\)。
2. **小覆盖：**全文确认 \(e\le p-2\Rightarrow G\) 初等阿贝尔（Theorem 1.4, p.415）。sharp 构造的两条命题并存：Proposition 4.2（p.418）给 \(e=p-1\)，Proposition 4.3（p.419）给 \(e=p\)；二者分别对应 zbMATH 评论与摘要，不构成矛盾。
3. **一般公式：**这三篇文献没有给出任意 \(n\) 的存在型一般精确公式：Isaacs 是等阶划分分类；Jungnickel 给一般小覆盖结构定理、直积构造（Prop 4.1）与幂零群精确值（Thm 3.4）；Jungnickel–Storme 的 cover 结果主要在 \(p\) 群内，并在 p.213 把任意群/幂零群列为公开问题。准确说法是“本次三篇原始文献复核未见一般闭式”，而不是断言所有后续文献绝对不存在。
