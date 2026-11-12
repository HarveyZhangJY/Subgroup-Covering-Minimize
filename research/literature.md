# 阶为 \(n^2\) 的群由阶为 \(n\) 的子群覆盖：文献研究报告

> **2026-11-12 更新：** Jungnickel (1999)、Jungnickel–Storme (2001)、Foguel 等 (2025) 的全文均已取得并升为 A 级；逐页引文、定理号与页码见 `research/citation-review.md`。本文中旧的“B 级/正文未取得/访问受限”记录不再有效。

## 1. 问题、记号与结论摘要

设 \(n\ge 2\)。对有限群 \(G\)，定义

\[
c_n(G)=\min\{|\mathcal C|:\mathcal C\text{ 是 }G\text{ 的覆盖，且每个 }H\in\mathcal C\text{ 都满足 }|H|=n\},
\]

若不存在这样的覆盖，则记 \(c_n(G)=\infty\)。本题“存在一个阶为 \(n^2\) 的群 \(G\)，对可做到这一点的 \(G\) 求最小 \(m\)”最自然的含义是

\[
M(n)=\min_{|G|=n^2}c_n(G).
\]

这与“固定某个 \(G\) 求 \(c_n(G)\)”以及“对任意阶为 \(n^2\) 的 \(G\) 求统一答案”是不同问题。

### 核心结论

1. **总有计数下界 \(m\ge n+1\)**。等号成立当且仅当覆盖成员在非单位元上互不重叠，即形成等阶子群划分（equal partition）。
2. **若 \(n=p^a\) 是素数幂（包括 \(n=p\)），则**
   \[
   \boxed{M(n)=n+1}.
   \]
   取 \(G=(C_p)^{2a}\)，把它看作二维 \(\mathbb F_{p^a}\)-向量空间；其 \(p^a+1\) 个一维子空间都是阶 \(p^a\) 的子群并构成划分。
3. **若 \(n\) 不是素数幂，则 \(M(n)>n+1\)**。这是 Isaacs 1973 年等阶划分分类的直接推论。更强的文献推论是：若 \(p\) 为 \(n\) 的最小素因子，则
   \[
   \boxed{M(n)\ge n+p}.
   \]
   依据是 Jungnickel 1999 年关于 small congruence covers 的定理。
4. 对任意 \(n=\prod_i p_i^{a_i}\)，本次给出一个初等构造（**不是已核实的文献公式**）：
   \[
   \boxed{M(n)\le \prod_i(p_i^{a_i}+1)}.
   \]
   因而 \(M(n)\) 对所有 \(n\) 都有限。非素数幂情形目前可写为
   \[
   n+p\le M(n)\le \prod_i(p_i^{a_i}+1).
   \]
   例如 \(8\le M(6)\le 12\)。**本次检索未找到一般非素数幂 \(n\) 的存在型精确闭式，不能声称该区间两端通常相等。**
5. 对固定群 \(C_n\times C_n\)，本次独立推出并核对：
   \[
   \boxed{c_n(C_n\times C_n)=\psi(n):=n\prod_{p\mid n}(1+1/p)}.
   \]
   这不是存在型答案。例如 \(c_4(C_4\times C_4)=6\)，而 \(M(4)=5\)，最优群可取 \((C_2)^4\)。
6. “对任意 \(G\)”没有统一有限答案。例如 \(C_{n^2}\) 根本不能被阶为 \(n\) 的子群覆盖。更一般地，固定的 \(G\) 若存在这样的覆盖，则必须有 \(\exp(G)\mid n\)。

下表概括两种读法：

| 问题 | 已知结果 |
|---|---|
| 存在某个 \(|G|=n^2\)，\(n=p^a\) | \(M(n)=n+1\) |
| 存在某个 \(|G|=n^2\)，\(n\) 非素数幂，\(p\) 为最小素因子 | \(n+p\le M(n)\le\prod_i(p_i^{a_i}+1)\) |
| 固定 \(G=C_n\times C_n\) | \(c_n(G)=n\prod_{p\mid n}(1+1/p)\) |
| 固定 \(G=C_{n^2}\) | 不存在所需覆盖 |
| 任意固定 \(G\) | 依赖 \(G\)；必要条件为 \(\exp(G)\mid n\) |

---

## 2. 基础推导及其与文献的衔接

### 2.1 计数下界与等号情形

所有覆盖子群都含单位元。若 \(\mathcal C\) 由 \(m\) 个阶 \(n\) 子群组成，则

\[
n^2=|G|\le 1+m(n-1),
\]

所以 \(m\ge n+1\)。

若 \(m=n+1\)，上述并集计数必须处处为等号，因此任意两个不同成员的非单位元集合不相交，即任意两个成员交为平凡子群；它们构成 equal partition。反之，等阶划分显然给出 \(n+1\) 个成员。因此，“能否达到 \(n+1\)”完全转化为等阶划分问题。

### 2.2 素数与素数幂

当 \(n=p\) 时，阶 \(p^2\) 的群只有 \(C_{p^2}\) 和 \(C_p\times C_p\) 两种同构类型。前者不能由阶 \(p\) 子群覆盖其生成元；后者的 \(p+1\) 条一维 \(\mathbb F_p\)-子空间给出最优覆盖。因此 \(M(p)=p+1\)。

当 \(n=p^a\) 时，取

\[
G=(C_p)^{2a}\cong (\mathbb F_{p^a})^2
\]

的加法群。二维向量空间有

\[
\frac{p^{2a}-1}{p^a-1}=p^a+1
\]

个一维 \(\mathbb F_{p^a}\)-子空间，每个作为加法群的阶为 \(p^a\)，它们两两平凡相交且覆盖全群。因此达到通用下界。

Isaacs 的一般分类是：有限群有等阶真子群划分，当且仅当它是非循环、指数为某个素数 \(p\) 的 \(p\)-群；其中确有非阿贝尔例，因此不能由该定理单独推出本题等号群初等交换。但在本题 \(|G|=n^2\)、由 \(n+1\) 个阶 \(n\) 子群覆盖的等号情形，Jungnickel 的小覆盖定理（\(e=0\le p-2\)）进一步迫使 \(G\) 初等阿贝尔；结合 Isaacs 得 \(n=p^a\) 且 \(G\cong(C_p)^{2a}\)。一般等阶划分分类与本题等号分类不可混同。

### 2.3 非素数幂：文献给出的下界

若 \(n\) 至少有两个不同素因子，则阶 \(n^2\) 的群不可能是初等阿贝尔群。Jungnickel 1999 的结果说：若阶 \(s^2\) 的群能由至多 \(s+p-1\) 个阶 \(s\) 子群覆盖，其中 \(p\) 是 \(s\) 的最小素因子，则该群必为初等阿贝尔群。于是本题中非素数幂 \(n\) 不可能有 \(m\le n+p-1\)，故 \(m\ge n+p\)。

特别地，这也排除了 \(m=n+1\)；不过仅排除等号时，Isaacs 1973 的定理已经足够，而且更基础。

### 2.4 一般 \(n\) 的显式上界（本次自行构造）

写 \(n=\prod_{i=1}^r q_i\)，其中 \(q_i=p_i^{a_i}\)。取

\[
G=\prod_{i=1}^r(C_{p_i})^{2a_i}.
\]

第 \(i\) 个分量是 \(2a_i\) 维 \(\mathbb F_{p_i}\)-向量空间。将其看作二维 \(\mathbb F_{q_i}\)-空间，可得到 \(q_i+1\) 个 \(a_i\) 维 \(\mathbb F_{p_i}\)-子空间组成的 spread：它们两两只交于零且覆盖该分量。

对每个多元组 \((U_1,\ldots,U_r)\)，其中 \(U_i\) 取自第 \(i\) 个 spread，构造

\[
H_{U_1,\ldots,U_r}=U_1\times\cdots\times U_r.
\]

其阶为 \(\prod_i q_i=n\)，总数为 \(\prod_i(q_i+1)\)。任给 \(x=(x_1,\ldots,x_r)\in G\)，逐分量选取含 \(x_i\) 的 \(U_i\)，即有一个上述 \(H\) 含 \(x\)。故这些子群覆盖 \(G\)，得到所声称的上界。

该证明只使用有限域一维子空间计数。它是本次为补全一般 \(n\) 的有限上界而给出的初等构造，**不应引作 Jungnickel、Isaacs 或其他论文已证明的最优公式**。

---

## 3. 固定 \(C_n\times C_n\) 的精确公式（本次独立推导）

令 \(A=C_n\times C_n\)。

### 3.1 为什么所有阶 \(n\) 循环子群都必须出现

若 \(x\in A\) 的阶为 \(n\)，任何覆盖成员 \(H\le A\) 若含 \(x\) 且 \(|H|=n\)，则

\[
\langle x\rangle\subseteq H,\qquad |\langle x\rangle|=|H|=n,
\]

故 \(H=\langle x\rangle\)。因此，任何合法覆盖必须包含每一个阶 \(n\) 循环子群，不能只挑选其中一部分。

### 3.2 为什么这些循环子群足以覆盖

在 \(C_{p^a}\times C_{p^a}\) 中，任给元素 \(x\)，可写成 \(x=p^t y\)，其中 \(y=(y_1,y_2)\) 的两个坐标至少一个不被 \(p\) 整除。于是 \(y\) 的阶为 \(p^a\)，而 \(x\in\langle y\rangle\)。对每个 \(p^a\parallel n\) 的准素分量分别这样做，再取各循环子群的直积，可知 \(A\) 的每个元素都落在某个阶 \(n\) 循环子群中。

所以全部阶 \(n\) 循环子群既是必要成员，又构成覆盖，最小数恰为它们的个数。

### 3.3 计数

\(A\) 中阶 \(n\) 元素数可按素因子分解计算：

\[
N_n=\prod_{p^a\parallel n}\left(p^{2a}-p^{2a-2}\right)
=n^2\prod_{p\mid n}(1-p^{-2}).
\]

每个阶 \(n\) 循环子群恰有 \(\varphi(n)\) 个生成元，不同循环子群的生成元集合互不重叠。因此循环子群数为

\[
\frac{N_n}{\varphi(n)}
=\frac{n^2\prod_{p\mid n}(1-p^{-2})}{\varphi(n)}
=n\prod_{p\mid n}(1+1/p).
\]

这正好是 Dedekind psi 函数，OEIS A001615 也明确把该序列解释为 \(C_n\times C_n\) 中同构于 \(C_n\) 的子群数。

例子：

- \(n=p\)：\(c_p(C_p\times C_p)=p+1\)；
- \(n=4\)：\(c_4(C_4\times C_4)=4(1+1/2)=6\)；
- \(n=6\)：\(c_6(C_6\times C_6)=6(1+1/2)(1+1/3)=12\)。

OEIS A000203 的约数和 \(\sigma(n)\) 则计数 \(C_n\times C_n\) 的**所有**阶 \(n\) 子群，而非最小覆盖数。例如 \(n=4\) 时总数为 \(\sigma(4)=7\)，但合法最小覆盖只用其中 6 个循环子群。这两个数列不能混用。

---

## 4. 最直接相关文献

### 4.1 I. Martin Isaacs, *Equally partitioned groups* (1973)

- 期刊：*Pacific Journal of Mathematics* 49(1), 109–116。
- DOI：[10.2140/pjm.1973.49.109](https://doi.org/10.2140/pjm.1973.49.109)
- 出版方页面：[msp.org/pjm/1973/49-1/p11.xhtml](https://msp.org/pjm/1973/49-1/p11.xhtml)
- 相关定理：能由等阶真子群划分的有限群，恰为非循环、指数为某个素数 \(p\) 的 \(p\)-群。
- 与本题关系：完全刻画 \(m=n+1\) 的等号情形；直接推出非素数幂 \(n\) 不可能达到通用计数下界。它也说明固定群与存在型问题必须区分。

### 4.2 Dieter Jungnickel, *On small congruence covers* (1999)

- 期刊：*Bulletin of the Belgian Mathematical Society – Simon Stevin* 6(3), 413–421。
- DOI：[10.36045/bbms/1103065860](https://doi.org/10.36045/bbms/1103065860)
- zbMATH 记录及评论：[zbmath.org/1374975](https://zbmath.org/1374975)，标识 Zbl 0947.51006。
- 术语：阶 \(s^2\) 的群中，由阶 \(s\) 子群构成的覆盖称为 congruence cover；若有 \(r\) 个成员，定义 excess 为 \(e=r-s-1\)。
- zbMATH 评论所载定理：若 \(p\) 是 \(s\) 的最小素因子且 \(e\le p-2\)，则 \(G\) 为初等阿贝尔群，覆盖可解释为射影空间中的几何覆盖。
- 与本题关系：\(e\le p-2\) 等价于 \(r\le s+p-1\)，因此给出非素数幂情形的 \(M(n)\ge n+p\)。这是本次找到的对原题最直接的小覆盖结构定理。

**二手资料的数值冲突：**出版方摘要的检索转录称，在适当的非初等阿贝尔群中存在 \(s+p+1\) 个成员的 congruence cover；zbMATH 评论则称，对 \(p\)-群该界是 sharp，非初等阿贝尔例子有 excess \(p-1\)，即 \(s+p\) 个成员。本次未能读取原文来消解这一处差异，因此不据此声称任何非初等阿贝尔群的精确最小值。两种资料对本报告实际使用的“小覆盖必初等阿贝尔”部分没有冲突。

### 4.3 Dieter Jungnickel, Leo Storme, *Packing and Covering Groups with Subgroups* (2001)

- 期刊：*Journal of Algebra* 239(1), 191–214。
- DOI：[10.1006/jabr.2000.8640](https://doi.org/10.1006/jabr.2000.8640)
- Ghent University 书目记录：[biblio.ugent.be/publication/168724](https://biblio.ugent.be/publication/168724)
- zbMATH 记录及评论：[zbmath.org/1643653](https://zbmath.org/1643653)，标识 Zbl 0992.20017。
- 术语：\(s\)-cover 是阶 \(s\) 子群组成的覆盖；\(s\)-packing 是忽略单位元后两两不交的阶 \(s\) 子群族。
- zbMATH 评论所载内容：论文改进了阿贝尔 \(p\)-群中 \(p^t\)-packing 与 \(p^t\)-cover 大小的上下界，包括非初等阿贝尔群，并用大 packing、小 cover 的存在刻画初等阿贝尔群。
- 与本题关系：这是固定阶子群覆盖的直接后续文献，尤其与固定 \(p\)-群的最小覆盖数有关；评论本身并未给出本题对一般合数 \(n\)、并在所有阶 \(n^2\) 群上取最小值的闭式。由于未读到全文，本报告不转录评论之外的精确界。

### 4.4 Andrew Velasquez-Berroteran, *Equal Coverings of Finite Groups* (2022)

- 文献类型：学位论文，同时作为 arXiv 预印本公开；不应写成同行评审期刊论文。
- 日期：论文首页为 2022-04-27；arXiv v1 提交于 2022-06-28。
- arXiv：[2206.14843](https://arxiv.org/abs/2206.14843)；[PDF](https://arxiv.org/pdf/2206.14843)。
- 定义：equal covering 是由真子群组成、且各成员阶相同的覆盖；共同阶并未预先固定为本题的 \(n\)。
- 已读全文中与本题有关的定理：
  - **Theorem 13**：若 \(G\) 有 equal covering，则 \(\exp(G)\) 整除每个覆盖成员的共同阶。用于本题即必要条件 \(\exp(G)\mid n\)。
  - **Theorem 15**：每个非循环有限 \(p\)-群都有 equal covering，可取所有极大子群。
  - **Theorem 16**：若 \(G\) 或 \(H\) 有 equal covering，则 \(G\times H\) 有；证明使用 \(G_i\times H\)。
  - **Theorem 17**：每个非循环有限幂零群都有 equal covering。
  - **Theorem 18**：阶为至少两个不同素数的平方自由乘积的群没有 equal covering。
  - **Theorem 19**：若正规商 \(G/H\) 有 equal covering，则可提升为 \(G\) 的 equal covering。
- “Possible Future Work”第 2 项明确提出研究 equal covering number，即等阶覆盖的最小成员数。这说明该学位论文主要研究存在性，而没有解决一般最小数问题。
- 与本题关系：提供术语、必要条件及结构性背景，但没有给出 \(M(n)\) 或 \(c_n(C_n\times C_n)\) 的公式。

### 4.5 T. Foguel, A. R. Moghaddamfar, J. Schmidt, A. Velasquez-Berroteran, *Concerning equally covered groups*

- 期刊：*International Electronic Journal of Algebra* 37(37), 352–365。
- DOI：[10.24330/ieja.1567377](https://doi.org/10.24330/ieja.1567377)
- 开放 PDF 地址（本次未能连接）：[Dergipark article-file/4288611](https://dergipark.org.tr/en/download/article-file/4288611)
- 年份说明：Crossref 记录正式发布日期为 **2025-01-14**；OpenAlex 记录为 2024-10-14、publication year 2024。这里按正式卷期及 Crossref 写 2025，并保留数据库差异。
- 已核实摘要：有限单群没有 equal covering；对任意有限群 \(G\)，其某个有限笛卡尔幂 \(G^n\) 有 equal covering。
- 与本题关系：这是 2022 学位论文之后检出的直接相关正式期刊论文，主要摘要结论仍是存在性/结构性结果。摘要没有给出本题的最小覆盖数公式；但因出版站 DNS 解析失败，本次未读正文，不能仅据摘要断言全文完全不含相关数值结果。

---

## 5. 其他检索线索及为何不能直接套用

### 5.1 一般 covering number \(\sigma(G)\)

通常的 covering number 允许覆盖成员为不同阶的真子群：

\[
\sigma(G)=\min\{k:G=H_1\cup\cdots\cup H_k,\ H_i<G\}.
\]

它与本题的固定阶 \(c_n(G)\) 不同。相关背景文献包括：

- J. H. E. Cohn, *On \(n\)-Sum Groups*, *Mathematica Scandinavica* 75 (1994), 44 ff.，[DOI: 10.7146/math.scand.a-12501](https://doi.org/10.7146/math.scand.a-12501)。
- M. J. Tomkinson, *Groups as the union of proper subgroups*, *Mathematica Scandinavica* 81 (1997), 191–198，[DOI: 10.7146/math.scand.a-12873](https://doi.org/10.7146/math.scand.a-12873)。
- R. A. Bryce, L. Serena, *A note on minimal coverings of groups by subgroups*, *Journal of the Australian Mathematical Society* 71(2) (2001), 159–168，[DOI: 10.1017/S1446788700002809](https://doi.org/10.1017/S1446788700002809)。

这些文献对理解 minimal/irredundant cover 的术语很有用，但其公式或分类不能直接改写为等阶、固定阶覆盖的答案。同样，群划分、半划分（semi-partition）、同构阿贝尔子群覆盖也都施加了不同条件。

### 5.2 循环子群覆盖与阿贝尔子群覆盖

晏林，《有限群的最小子群覆盖》，*江西师范大学学报（自然科学版）* 31(6) (2007)，[DOI: 10.3969/j.issn.1000-5862.2007.06.012](https://doi.org/10.3969/j.issn.1000-5862.2007.06.012)，讨论一般、循环及阿贝尔子群最小覆盖。其中 \(n_a(C_{p^r}\times C_{p^s})=p+1\) 是**最小阿贝尔子群覆盖**，成员不必同阶，更不是本题“全部为阶 \(n\)”的覆盖，不能据此回答 \(c_n(G)\)。

### 5.3 Math StackExchange / MathOverflow

检出一篇相关社区讨论：

- [A group of order \(n^2\) with \(n+1\) subgroups of order \(n\) with trivial intersection is abelian](https://math.stackexchange.com/questions/2422793/)。

它可用于寻找关键词和初等思路，但本报告的核心结论不依赖其回答。站点定向搜索及 Stack Exchange API 检索中，未检出直接给出本题存在型一般闭式的 MathOverflow 帖子。社区帖子不能替代 Isaacs、Jungnickel 等正式文献。

### 5.4 OEIS

- [A001615](https://oeis.org/A001615)：Dedekind psi，\(\psi(n)=n\prod_{p\mid n}(1+1/p)\)，页面明确给出其为 \(C_n\times C_n\) 中同构于 \(C_n\) 的子群数。
- [A000203](https://oeis.org/A000203)：约数和 \(\sigma(n)\)，页面包含其计数 \(C_n\times C_n\) 的所有阶 \(n\) 子群的解释。

OEIS 在这里用于核对计数序列，不是覆盖最小性的来源；最小性证明见第 3 节。

---

## 6. 检索范围、访问限制与结论边界

### 检索词与路径

本次组合检索了以下中英文关键词及其变体：

- subgroup cover, subgroup covering, covering number, minimal cover, minimal covering；
- equal covering, equally covered groups, equal-order subgroups, same-order subgroups, fixed-order subgroups；
- congruence cover, small congruence covers, packing and covering groups with subgroups；
- group partition, equal partition, equally partitioned groups, semi-partition；
- groups covered by subgroups of order \(s\), groups of square order, \(C_n\times C_n\), cyclic subgroups, abelian \(p\)-groups；
- 有限群、同阶子群覆盖、固定阶子群、最小子群覆盖、循环子群覆盖、阿贝尔子群覆盖。

使用了出版方页面、Crossref、OpenAlex、zbMATH API、arXiv、大学机构库、OEIS、WebSearch/WebFetch 和 Stack Exchange API，并对直接相关论文做了引用追踪。

### 全文访问限制

1. Jungnickel 1999 的 Project Euclid 页面/PDF请求受到 Incapsula 阻断；本报告使用 DOI 元数据、出版方摘要转录和 zbMATH 评论，未声称读过全文。
2. Jungnickel–Storme 2001 的 ScienceDirect 页面/PDF返回 403，Elsevier FULL API 需要密钥；其他镜像尝试亦未成功。本报告只转录已核实的书目信息与 zbMATH 评论。
3. *Concerning equally covered groups* 的 Dergipark 域名在当前环境发生 DNS 解析失败，WebFetch 也未成功；本报告只使用 Crossref/OpenAlex 元数据和摘要。
4. zbMATH 普通网页曾返回 403，但其公开 API 成功返回评论全文；报告中的两条评论来自 API。
5. 搜索引擎对 MathOverflow/MathStackExchange 的站点定向结果噪声较大，故改用 Stack Exchange API；未检出不等于绝对不存在。
6. 2022 学位论文全文已下载并读取，是“equal covering number 仍作为后续问题”的直接依据。

因此，关于一般非素数幂 \(n\) 的准确表述应是：**在本次检索到的文献中，未找到对 \(M(n)\) 的一般精确闭式；已有直接结果足以给出素数幂精确答案、非素数幂下界以及若干固定 \(p\)-群的上下界。**这不是对“文献中绝对不存在”的证明。后续最值得优先核对的是 Jungnickel 1999、Jungnickel–Storme 2001 的完整正文，以及 Foguel 等正式论文的全文和后续被引文献。

---

## 7. 最终回答建议

若只需回答原题的存在型读法，可简洁写为：

\[
\boxed{n=p^a\Longrightarrow M(n)=n+1}.
\]

若 \(n\) 非素数幂且 \(p\) 是其最小素因子，则

\[
\boxed{n+p\le M(n)\le\prod_i(p_i^{a_i}+1)},
\]

其中上界来自本次显式直积构造，下界来自 Jungnickel 1999。一般精确闭式本次未找到。若题目实际固定 \(G=C_n\times C_n\)，答案则改为

\[
\boxed{m=n\prod_{p\mid n}(1+1/p)}.
\]
