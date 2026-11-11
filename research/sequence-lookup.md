# 存在型最小覆盖数列与 Jungnickel 后续文献的定向反查

检索日期：2026-11-11。本文只记录针对既有结果的反查，不重新证明小例，也不把数据库未检出解释为公式或文献绝对不存在。

## 1. 检索对象与量词

记 `alpha(n)` 为：在所有满足 `|G|=n^2` 且能由阶 `n` 的子群覆盖的有限群 `G` 上，覆盖所需子群数的最小值。当前已认证的输入为

| `n` | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 12 | 15 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `alpha(n)` | 3 | 4 | 5 | 6 | 10 | 8 | 9 | 10 | 16 | 17 | 24 |

因此反查数列为

```text
3,4,5,6,10,8,9,10,16,17,24
```

此量词不同于固定 `G=C_n×C_n` 时的最小值

```text
psi(n)=prod_{p^a||n} p^(a-1)(p+1),
```

也不同于一般有限群的 proper-subgroup covering number、maximal-subgroup irredundant cover 或对称群覆盖问题。检索中这些相近问题均单独排除，未借用其开放性陈述。

## 2. OEIS：连续片段、显式 `seq:` 与有序子序列

### 2.1 查询语义

依据 [OEIS search hints](https://oeis.org/hints.html)：普通逗号数值查询匹配连续、有序片段；`subseq:` 匹配可跳过中间项但保持顺序的子序列。因此后者对短整数和重复值非常不敏感，不能把命中条目直接视为候选公式。

### 2.2 完整数列及连续前缀

以下 JSON 请求均实际访问，HTTP 状态为 200，返回 JSON `null`：

1. 完整普通查询：

   <https://oeis.org/search?q=3%2C4%2C5%2C6%2C10%2C8%2C9%2C10%2C16%2C17%2C24&fmt=json>

2. 前 8 项普通查询：

   <https://oeis.org/search?q=3%2C4%2C5%2C6%2C10%2C8%2C9%2C10&fmt=json>

3. 显式连续序列查询：

   ```text
   seq:3,4,5,6,10,8,9,10,16,17,24
   ```

   在同一 `https://oeis.org/search?...&fmt=json` 接口返回 `null`。

4. OEIS 精确短语 `"congruence cover"` 的 JSON 查询也返回 `null`。非精确关键词 `congruence cover`、`minimum congruence cover`、`Jungnickel` 有返回，但所见条目与本题无关。

### 2.3 较短连续片段的偶然命中

为排除“完整前缀尚未录入、但后缀已可识别”的情况，还查了若干短片段：

- `8,9,10,16,17,24` 命中 [A004825](https://oeis.org/A004825)（至多三个正立方数之和）和 [A214980](https://oeis.org/A214980)（A214979 的零点位置）；名称与后续数据均不指向群覆盖。
- `10,16,17,24` 还命中若干 coordination sequences 与三角阵列，未识别出 congruence cover 或群子群覆盖含义。
- `3,4,5,6,10` 命中 [A075163](https://oeis.org/A075163) 等；A075163 的局部为 `...,3,4,5,6,10,8,7,...`，下一项不是本题已认证的 `9`，故不是完整前缀匹配。

这些只是说明短数值片段高度非特异，并非额外的本题候选。

### 2.4 `subseq:` 查询及审查边界

实际查询：

```text
subseq:3,4,5,6,10,8,9,10,16,17,24
```

对应接口：

<https://oeis.org/search?q=subseq%3A3%2C4%2C5%2C6%2C10%2C8%2C9%2C10%2C16%2C17%2C24&fmt=json>

接口报告共 444 条命中。已查看的前 110 条结果名称未显示与本题相关的群覆盖条目；首页包括 [A056239](https://oeis.org/A056239)、[A066328](https://oeis.org/A066328)、[A053645](https://oeis.org/A053645)、[A060681](https://oeis.org/A060681)、[A304818](https://oeis.org/A304818)、[A252464](https://oeis.org/A252464)、[A155043](https://oeis.org/A155043)、[A338913](https://oeis.org/A338913)、[A270652](https://oeis.org/A270652)、[A022290](https://oeis.org/A022290)，均属于其他主题。**没有逐条人工审查全部 444 条，故不声称已穷尽排除所有非连续子序列命中。**

OEIS 小结：普通连续片段未检出完整数列或前 8 项匹配；有序非连续子序列命中很多且高度非特异，本轮未找到可识别的本题条目。

## 3. 精确关键词、递归与有限优化公式

### 3.1 实际使用的定向查询

以下引号均表示精确短语检索；未加引号的词用于限定群论语境：

```text
"congruence cover number" groups subgroups
"congruence cover number" Jungnickel Storme
"congruence cover number" mathematics
"minimum congruence cover" Jungnickel
"minimum congruence cover" finite group
"minimum congruence cover" mathematics
"minimal congruence cover" group
"smallest congruence cover" group
"congruence cover" "open problem" group
"congruence cover" "not known" group
"congruence cover" "unknown" subgroup
"congruence cover" "closed formula" groups
"congruence cover" "recursive" groups subgroups
"congruence cover" recursion prime factors group
"congruence cover" "prime divisors" group
"Packing and covering groups with subgroups" citations
"Packing and covering groups with subgroups" pdf
"Packing and covering groups" "open problem"
"On small congruence covers" cited
```

返回内容主要是 Jungnickel 1999、Jungnickel–Storme 2001 的元数据/摘要，或同余子群、双曲流形、一般 proper-subgroup covering、maximal-subgroup irredundant cover 等无关主题。未检出以 `n` 的素因子为输入、直接给出本题 `alpha(n)` 的递归式或有限优化公式。

普通群覆盖文献中可见“determining the size of a smallest covering is an open problem for many simple groups”一类句子，但其对象是特定群或特定群族，不是此处“对任意 `n`，允许选择阶 `n^2` 的可覆盖群”的存在型最小值，不能作为本问题的明确开放性声明。

### 3.2 本轮结论的严格边界

- 本轮未找到任意 `n` 的一般闭式、按素因子递归式、有限优化公式，亦未找到一篇可访问原文明确把**这一精确问题**称为 open problem。
- 已核实的原始来源范围仍见 `research/primary-sources.md`：Jungnickel 1999 的小覆盖结构定理、素数幂构造，以及 Jungnickel–Storme 2001 对固定阿贝尔 `p`-群的 packing/covering 上下界；这些不等同于任意 `n` 的存在型精确公式。
- 上述结论只表示本轮定向查询未检出，不证明相关公式不存在，也不证明学界已正式宣布该问题开放。

## 4. Jungnickel 1999 的前向引文

目标文献：D. Jungnickel, *On small congruence covers of finite groups*, 1999，[DOI](https://doi.org/10.36045/bbms/1103065860)，OpenAlex `W1603700654`。

### 4.1 OpenAlex

实际访问的过滤端点：

<https://api.openalex.org/works?filter=cites:W1603700654&per-page=100>

响应 `meta.count=1`，唯一记录为 Jungnickel–Storme 2001 的 *Packing and covering groups with subgroups*。采用过滤端点是因为直接 `/works/W1603700654/citations` 请求出现 504。

### 4.2 Semantic Scholar 与 Crossref 交叉核对

- Semantic Scholar Graph API 的文献记录给 `citationCount=1`；citations 查询同样只返回 Jungnickel–Storme 2001。
- [Crossref 元数据](https://api.crossref.org/works/10.36045/bbms/1103065860)显示的被引计数为 0。

三个数据库计数不同，说明任何单一数据库都不能视为完整引文宇宙；这里只把它们作为“所查索引内”的证据。

## 5. Jungnickel–Storme 2001 的前向引文

目标文献：D. Jungnickel and L. Storme, *Packing and covering groups with subgroups*, 2001，[DOI](https://doi.org/10.1006/jabr.2000.8640)，OpenAlex `W2083823125`。

### 5.1 OpenAlex 的六条记录

实际访问：

<https://api.openalex.org/works?filter=cites:W2083823125&per-page=100>

响应 `meta.count=6`，记录如下：

1. A. Maróti, *Covering the symmetric groups with proper subgroups* (2005)，[DOI](https://doi.org/10.1016/j.jcta.2004.10.003)。
2. A. Abdollahi et al., *Groups with a Maximal Irredundant 6-Cover* (2005)，[DOI](https://doi.org/10.1081/AGB-200066157)。
3. C. J. Maxson and K. C. Smith, *Maximal rings associated with covers of abelian groups* (2007)，[DOI](https://doi.org/10.1016/J.JALGEBRA.2007.02.047)。
4. A. Abdollahi, F. Ataei, and A. Mohammadi Hassanabadi, *Minimal Blocking Sets in PG(n, 2) and Covering Groups by Subgroups* (OpenAlex 2008；Semantic Scholar 记录为 2007)，[DOI](https://doi.org/10.1080/00927870701715639)，[arXiv:0708.2282](https://arxiv.org/abs/0708.2282)。
5. A. Maróti, *Orders, Conjugacy Classes, and Coverings of Permutation Groups* (2007)，OpenAlex 无 DOI，属于预印本/重复版本记录。
6. R. A. Tarmizi and J. Sulaiman, *Nilpotent groups having a maximal irredundant 11-covering with core-free intersection* (2019)，[DOI](https://doi.org/10.1063/1.5136368)。

从可访问题名和摘要看，这些工作研究对称群/排列群覆盖、极大无赘 6/11-cover、与覆盖相关的环、或 blocking sets，未显示对任意 `n` 求 `alpha(n)` 的一般闭式或按素因子递归。特别是 arXiv:0708.2282 的摘要明确针对 maximal subgroups 的 irredundant covers，量词与本题不同。

Semantic Scholar 返回 8 条引文记录，额外包含 Abdollahi blocking-set 预印本、Maróti 预印本等重复/版本记录；不能把数据库记录数直接当作不同论文数。

### 5.2 前向引文结论

在 OpenAlex 与 Semantic Scholar 所覆盖并实际返回的上述前向引文中，未见任意 `n` 的一般公式或按素因子递归。此结论限于可访问记录及题名/摘要层面的定向筛查，不声称穷尽所有后续引用或所有全文。

## 6. 全文访问与证据等级补充

- Jungnickel 1999 与 Jungnickel–Storme 2001 的正文仍未取得；本轮依赖出版方/DOI 元数据、摘要、zbMATH 评论和引文索引，未虚构定理号、页码或正文中的开放性语句。
- Jungnickel–Storme 的 ScienceDirect 页面/PDF 请求返回 403；Elsevier `view=FULL` 返回 401，另一次 plain-text API 请求返回 429；尝试的 Augsburg/Ghent 猜测 PDF 地址返回 404。可访问的 Elsevier 基础 XML 只有 coredata，虽标 `openaccess=1`，并不含正文，因此不据此声称已读全文。
- zbMATH 网页查询曾返回 403，沿用 `research/primary-sources.md` 已保存的 `api.zbmath.org` 评论证据，没有重复绕过访问限制。

## 7. 可供后续工作直接使用的结论

1. OEIS 普通连续查询没有识别出该存在型数列；`subseq:` 的 444 条宽泛命中不足以支持任何识别。
2. 所查 Jungnickel 前向引文未显示任意 `n` 的一般闭式、按素因子递归或有限优化公式。
3. 精确关键词检索未找到针对本精确量词的明确开放性原文；后续若需声称“开放”，应表述为“本项目尚未解决且本轮文献未检出一般公式”，而不是冒充已有权威声明。
4. 若继续文献工作，优先取得两篇 Jungnickel 正文并核对其自身引言/结尾是否提出一般问题；不要把其他群覆盖问题的开放性句子移植到本题。
