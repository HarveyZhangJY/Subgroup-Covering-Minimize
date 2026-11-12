# 三篇 B 级外部文献的原文核对报告

核对日期：2026-11-12。核对对象：`citation/` 下三份 PDF；对照目标：`output/solution.tex`（行号均指该文件 2026-11-12 12:26 版）。
方法：`pdftotext -layout -enc UTF-8` 全文提取并逐页比对期刊分页；三篇的卷期页与 DOI 另经 Crossref `works/{doi}` 复核。原文引文按印刷体转录，不补写未出现的字句。

---

## 0. 结论摘要

1. **三篇全部升为 A 级。** 三份 PDF 均可完整提取文字（非扫描件），页眉页码与期刊分页逐页吻合，定理编号、假设、页码可逐一核对。
2. 三篇的**书目信息全部正确**：作者、刊名、卷（期）、年份、页码、DOI 与 Crossref 记录逐字段一致，`solution.tex` 的 `\bibitem` 无需改动。
3. **不存在“把 B 级弱结论写成 A 级定理”的情况。** 相反，`solution.tex` 现在**低估**了两篇文献：Jungnickel (1999) 与 Jungnickel–Storme (2001) 仍标 B 并称“全文受访问防护阻断/出版页 403”，Foguel 等 (2025) 标 B 并称“正文未取得”，这些说法在拿到 PDF 后均已失效，且与 `research/pqalpha-literature.md` 第 14 行的 A 级记录互相矛盾。
4. **`solution.tex` 第 197 行所谓 sharp 构造“数量差异”不是差异**：Jungnickel (1999) 同时含 Proposition 4.2（p.418，$G=Z_{p^d}\times Z_{p^d}$ 给出 $e=p-1$，原文 p.419 明言此例使 Theorem 3.3 的界可取到）与 Proposition 4.3（p.419，$G=Z_{p^2}\times Z_p^{2d-2}$ 给出 $e=p$）。摘要与 zbMATH 评论各指其中一条，**两条都成立**。第 197 行应整段重写，不作为未决问题保留。
5. **`solution.tex` 第 324 行把一条已发表定理说成“本次显式构造”**：定理 \ref{thm:general-upper}（$\alpha(n)\le\prod(q_i+1)$，第 311–323 行）与 Jungnickel (1999) **Proposition 4.1（p.418）** 的构造与计数完全相同；同文 **Theorem 3.4（p.418）** 还给出幂零群的匹配下界 $|C|\ge\prod(q_i+1)$。这是本轮唯一的实质性归属错误（方向是“过度自谦”，不是夸大）。
6. **“Jungnickel 小覆盖定理 $\Rightarrow\alpha(n)\ge n+p_{\min}$”的转写严格成立**（见 §4.1），且现可用 Theorem 1.4（p.415）/ Theorem 3.3（p.417）精确署名。

---

## 1. 第一份：`citation/On Small Congruence Covers.pdf`

### 1.1 身份与书目

| 项 | 核对结果 |
|---|---|
| 作者 | Dieter Jungnickel（单作者，首页署名 "Dieter Jungnickel"，无单位行） |
| 标题 | *On Small Congruence Covers* |
| 期刊 | Bulletin of the Belgian Mathematical Society – Simon Stevin |
| 卷（期） | 6(3) |
| 年份 | 1999（Crossref `published-print` = 1999-01-01） |
| 页码 | 413–421（PDF 共 9 页，首页脚注 "Bull. Belg. Math. Soc. 6 (1999), 413–421"，末页页眉 421） |
| DOI | 10.36045/bbms/1103065860 ✔ Crossref 返回同名、同刊、6(3)、413-421、1999 |
| 收稿 | "Received by the editors January 1998. Communicated by J. Thas."（p.413 脚注） |

**判定：** 就是 `solution.tex` `\bibitem{Jungnickel1999}`（第 792–795 行）所指的那篇。书目无一处错误。

### 1.2 版本与可读性

PDF 元数据 `Creator: dvips 5.83 (OzTeX)`、`CreationDate: 2000-11-11`、`Title: Jungnickel.dvi`，即**作者自排的终稿/抽印本**（非出版方水印 PDF）。但：

- 页眉页脚为期刊体例（"On Small Congruence Covers 415"、"418 D. Jungnickel"），页码 413–421 与 Crossref 完全一致，9 页对 9 页；
- 正文、定理、公式、参考文献均可无歧义提取。

故**足以据以引用定理号与页码**。这一点需要在报告里如实注明，因为它决定了“A 级”是“读到终稿全文”，而不是“读到出版方 PDF”。

### 1.3 证据等级

**A（全文已读，逐页核对）。** 原先的 B 级及“Project Euclid 被 Incapsula 阻断”的限制说明作废。

### 1.4 精确引文（页码已按期刊分页核对）

**（a）术语与 excess 的定义，p.415：**

> "…of a congruence cover of excess $e$ of a group $G$ of square order $s^2$: This is a collection of subgroups $U_1,\dots,U_r$ of order $s$ the union of which is all of $G$, where $r=s+1+e$."

要点：**不要求成员两两不同、不要求无赘、不要求 $s$ 是素数幂、不要求 $G$ 幂零或阿贝尔**。

**（b）Theorem 1.4，p.415（主定理）：**

> "Any group of square order $s^2$ which admits a congruence cover of excess at most $p-2$, where $p$ is the smallest prime divisor of $s$, is necessarily elementary abelian."

紧随其后（同页）作者写道："The preceding theorem proves that small congruence covers are necessarily geometric."——即**定理陈述本身只断言"初等阿贝尔"**，"几何化"是紧接的推论句，摘要亦如此表述（p.413："…is necessarily elementary abelian; hence any such cover is in fact geometric"）。

**（c）Theorem 3.3，p.417（等价逆否形式）：**

> "Let $G$ be a group of square order $s^2$ which is not elementary abelian, and let $C$ be any congruence cover of $G$. Then $C$ has excess $e\ge p-1$, where $p$ is the smallest prime divisor of $s$."

**（d）Theorem 3.4，p.418（幂零群下界，本轮新发现、`solution.tex` 完全未用）：**

> "Let $C$ be a congruence cover of a group $G$ of square order $s^2$, where $s=q_1\cdots q_n$ with $n\ge2$ and where the $q_i$ are powers of pairwise distinct primes $p_i$. If $G$ is nilpotent, then $|C|\ge(q_1+1)\cdots(q_n+1)$."

**（e）Proposition 4.1，p.418（与本文定理 \ref{thm:general-upper} 同一构造）：**

> "Let $G:=\mathrm{EA}(q_1^2)\times\cdots\times\mathrm{EA}(q_n^2)$, where $n\ge2$ and where the $q_i$ are powers of pairwise distinct primes $p_i$. Then $\kappa(G)=(q_1+1)\cdots(q_n+1)$."

证明逐字为：每个因子 $\mathrm{EA}(q_i^2)$ 有 $q_i+1$ 个成员的 congruence cover $C_i$，取全部 $U=U_1\times\cdots\times U_n$（$U_i\in C_i$）。

**（f）Proposition 4.2，p.418（$e=p-1$ 的 sharp 例）：**

> "Let $G:=Z_{p^d}\times Z_{p^d}$, where $p$ is a prime. Then $\kappa(G)=p^d+p^{d-1}$."

取 $d=2$：$s=p^2$，$\kappa=p^2+p=s+p$，故 $e=\kappa-s-1=p-1$。p.419 开头原文："The case $d=2$ of Proposition 4.2 shows that the bound given in Theorem 3.3 can be sharp, even though it supplies only a single example for this phenomenon."

**（g）Proposition 4.3，p.419（$e=p$ 的构造）：**

> "Let $G:=Z_{p^2}\times Z_{p}^{2d-2}$, where $p$ is a prime. Then $\kappa(G)=p^d+p+1$."

故对 $s=p^d$ 有 $e=p$。p.419 原文："The next result proves that the bound in question is essentially best possible for all prime powers $s$: It can be off by at most 1." 命题本身未显式写 $d\ge2$；但摘要限定 "whenever $s$ is a **proper** power of a prime"，且证明用到 $p^{2d-1}$ 阶初等阿贝尔商群，$d\ge2$ 是隐含前提（$d=1$ 时 $G=Z_{p^2}$ 根本不可由 $p$ 阶子群覆盖）。引用时必须带 "proper prime power"。

**（h）Proposition 2.1，p.415（必要条件，`solution.tex` 第 103–105 行无引用处可用）：**

> "Let $G$ be a group of order $v$, and let $s$ be a divisor of $v$. If $G$ can be covered by subgroups of order $s$, then $\exp G$ divides $s$. Moreover, this necessary condition is also sufficient if $G$ is nilpotent."

**（i）记号，p.416：** $c(G,s)$ 表示"用 $s$ 阶子群覆盖 $G$ 的最小成员数"，$\kappa(G)$ 自第 4 节起同义。原文 p.416 有一句 "the smallest size of a congruence cover of a group G of square order is $c(G,|G|)$"，按上下文应为 $c(G,\sqrt{|G|})$，系原文/排版笔误，本文不依赖此句。

**（j）p.420 的公开问题：** Theorem 3.4 是否可推广到任意（或可解）群、$\kappa(G)$ 对阿贝尔群的确切值等。**这直接支持 `solution.tex`"未找到任意 $n$ 一般闭式"的限定表述**：原文自己把一般情形列为 open problem。

### 1.5 与 `output/solution.tex` 逐句对照

| 行 | 现文要点 | 判定 | 说明 |
|---|---|---|---|
| 186–187 | 标 B；"$|G|=s^2$，$e=r-s-1$，$p$ 为 $s$ 最小素因子，$e\le p-2$ 蕴含 $G$ 初等阿贝尔且覆盖几何化" | **内容正确，等级与说明过时** | 假设、量词、结论与 p.415 逐字相符；但"覆盖几何化"是定理后的推论句而非定理陈述的一部分，宜分开表述。等级应升 A 并补 Theorem 1.4/3.3 页码。 |
| 187 | "全文受访问防护阻断，故不标未核实的定理号" | **失效** | 全文已读，可标定理号。 |
| 197 | 称摘要 $e=p$ 与 zbMATH $e=p-1$ 存在"数量差异"，正文未取得前不作结论 | **失效且误导** | 二者是 Proposition 4.3 与 Proposition 4.2($d=2$) 两条**并存的正确命题**，原文 p.419 明确说明。应整段重写。 |
| 202 | "访问限制包括 Jungnickel (1999) 正文被防护拦截…" | **失效** | 三篇正文均已取得。 |
| 268 | "使用 Jungnickel 小覆盖定理的 $e=0$ 特例" | **正确** | $e=0\le p-2$（$p\ge2$）恒成立；可加 "(Theorem 1.4, p.415)"。 |
| 282 | "Jungnickel 的小同余覆盖定理（证据 B…）表明：若 $s^2$ 阶群能由 $r\le s+p-1$ 个 $s$ 阶子群覆盖…" | **内容正确，等级过时** | 与 Theorem 1.4 逐字等价（$e\le p-2\iff r\le s+p-1$）。改标 A 并给页码。 |
| 311–324 | 定理 \ref{thm:general-upper} 及"这是本次共享成果中的显式初等构造，不应冒充已核实的文献最优公式" | **归属错误（低估文献）** | 构造与计数 = Proposition 4.1（p.418）；且 Theorem 3.4（p.418）给出幂零群的匹配下界。 |
| 103–105 | $\exp(G)\mid n$，无引用 | **可补三处 A 级引用** | Jungnickel 1999 Prop 2.1（p.415）；Jungnickel–Storme 2001 Prop 2.1（p.194）；Foguel 等 Lemma 2.1（p.353）。 |

### 1.6 可直接替换的句子

**（1）替换第 186–187 行整行（`tab:literature` 的 Jungnickel 行）：**

```latex
Jungnickel (1999), \emph{On small congruence covers} \cite{Jungnickel1999} & A &
Theorem 1.4（p.415）：设 $|G|=s^2$，congruence cover 指 $r=s+1+e$ 个 $s$ 阶子群之并，$p$ 为 $s$ 的最小素因子；则 $e\le p-2$（等价于 $r\le s+p-1$）迫使 $G$ 初等阿贝尔，原文紧接一句指出此时覆盖几何化。逆否形式见 Theorem 3.3（p.417）：非初等阿贝尔群的一切此类覆盖满足 $e\ge p-1$。本文用它得到非素数幂下界与等号群分类；同文 Theorem 3.4 与 Proposition 4.1（p.418）另给出幂零群的精确值。\\
```

**（2）替换第 197 行整段：**

```latex
Jungnickel (1999) 的 sharp 构造不构成矛盾，而是两条并存的命题：Theorem 3.3（p.417）断言非初等阿贝尔群的 excess 满足 $e\ge p-1$；Proposition 4.2（p.418）在 $G=Z_{p^d}\times Z_{p^d}$ 上达到 $\kappa(G)=p^d+p^{d-1}$，取 $d=2$ 得 $e=p-1$，原文 p.419 明言此例说明 Theorem 3.3 的界“can be sharp”；Proposition 4.3（p.419）在 $G=Z_{p^2}\times Z_p^{2d-2}$（$d\ge2$）上给出 $\kappa(G)=p^d+p+1$，即 $e=p$，说明对素数幂 $s$ 该界至多差 $1$。摘要中的 $s+p+1$ 与 zbMATH 评论中的 $e=p-1$ 分别指这两条，二者互不冲突；本文实际使用的“小覆盖必初等阿贝尔”不依赖其中任何一条。
```

**（3）替换第 282 行的证据等级括注：**

```latex
Jungnickel 的小同余覆盖定理（证据 A：Theorem 1.4，p.415；逆否形式 Theorem 3.3，p.417）表明：若 $s^2$ 阶群能由 $r\le s+p-1$ 个 $s$ 阶子群覆盖，其中 $p$ 为 $s$ 的最小素因子，则该群必为初等阿贝尔群。
```

**（4）替换第 324 行整句：**

```latex
该构造与计数即 Jungnickel (1999) 的 Proposition 4.1（p.418）：对 $G=\mathrm{EA}(q_1^2)\times\cdots\times\mathrm{EA}(q_r^2)$ 有 $\kappa(G)=(q_1+1)\cdots(q_r+1)$；同文 Theorem 3.4（p.418）进一步证明，当 $n$ 含至少两个不同素因子时，任何幂零群 $G$（$|G|=n^2$）的 $n$-cover 都满足 $|\mathcal C|\ge\prod_i(q_i+1)$。因此定理 \ref{thm:general-upper} 的上界在幂零群类中恰为最小值，$\alpha(n)$ 若要更小只能由非幂零群实现——这与 $\alpha(12)=17<20=P(12)$ 的见证群 $A_4^2$ 非幂零完全一致。
```

**（5）替换第 202 行首句：**

```latex
本次已取得三篇文献的完整正文（Jungnickel (1999) 为作者自排终稿、页码与期刊 413--421 一致；Jungnickel--Storme (2001) 与 Foguel 等 (2025) 为出版排版 PDF），故三者均由 B 级升为 A 级；此前“正文被防护拦截”“出版页返回 403”“正文连接失败”的记录不再适用。
```

**（6）第 103–105 行后补一句引用：**

```latex
该必要条件亦见 Jungnickel \cite{Jungnickel1999} Proposition 2.1（p.415）、Jungnickel--Storme \cite{JungnickelStorme2001} Proposition 2.1（p.194）与 Foguel 等 \cite{Foguel2025} Lemma 2.1（p.353）。
```

### 1.7 本节的连带发现（可用作交叉验证，非错误）

Theorem 3.4 + Proposition 4.1（均在 p.418）给出：若 $n$ 含至少两个不同素因子，则
$$\min\{c_n(G):G\ \text{幂零},\ |G|=n^2\}=\prod_{p^a\parallel n}(p^a+1)=P(n).$$
`solution.tex` 的全部已认证值与此一致：$P(6)=12>\alpha(6)=10$、$P(12)=20>\alpha(12)=17$、$P(18)=30>\alpha(18)=27$ 三者必须由非幂零群达到（$C_2\times D$、$A_4^2$、$C_3^4{:}C_2^2$ 均非幂零），而 $P(15)=24=\alpha(15)$、$P(20)=30=\alpha(20)$、$P(28)=40=\alpha(28)$ 的达到者 $C_{15}^2$、$C_5^2\times C_2^4$、$C_7^2\times C_2^4$ 均幂零。**若 `solution.tex` 曾把某个达到 $P(n)$ 的群说成非幂零，或把 $\alpha(n)<P(n)$ 的见证群说成幂零，就会与已发表定理矛盾；现状无此问题，反而构成一次独立一致性检验。** 另外，$n=20,28$ 的达到群上的最优性（$c_n=P(n)$）现已可由 Theorem 3.4 直接给出，无需依赖 MILP 对偶界。

---

## 2. 第二份：`citation/Packing_and_Covering_Groups_with_Subgrou.pdf`

### 2.1 身份与书目

| 项 | 核对结果 |
|---|---|
| 作者 | D. Jungnickel（Univ. Augsburg）、L. Storme（Ghent University） |
| 标题 | Packing and Covering Groups with Subgroups |
| 期刊 | Journal of Algebra |
| 卷（期） | 239(1) |
| 年份 | 2001（Crossref `published-print` = 2001-05） |
| 页码 | 191–214（PDF 24 页，首页 "Journal of Algebra 239, 191–214 (2001)"，末页页眉 214） |
| DOI | 10.1006/jabr.2000.8640 ✔ Crossref 返回同名、同刊、239(1)、191-214、2001 |
| 其他 | "Communicated by Walter Feit"、"Received March 17, 2000" |

**判定：** 就是 `\bibitem{JungnickelStorme2001}`（第 797–801 行）所指的那篇。书目无一处错误。另可交叉确认：1999 年文的 p.416 承诺 "this will be the subject of a forthcoming paper [16]"，而本篇参考文献 [22] 正是 "D. Jungnickel, On small congruence covers, Bull. Belg. Math. Soc. 6 (1999), 413–421"（p.214），两文确为姊妹篇。

### 2.2 版本与可读性

PDF 由 Ghostscript 9.26 重制（`CreationDate 2023-03-13`），页面 359×617 pt（缩小版），保留 Elsevier 版权行 "© 2001 Academic Press" 与 "available online at http://www.idealibrary.com"。**文字层可提取，但旧式字体编码把括号、等号、属于号等映射成 `Ž`、`s`、`g` 等字符**（例如 "order s2" 实为 "order $s^2$"，"excess at most p y 2" 实为 "excess at most $p-2$"）。定理编号、假设结构与页码可靠；若要逐字引用公式，须按语义还原并对版面复核。

### 2.3 证据等级

**A（全文已读，逐页核对；公式符号按语义还原）。** 原先的 B 级及"ScienceDirect 403"限制说明作废。

### 2.4 精确引文

**（a）Result 1.3，p.192（重述 1999 年主定理，可作为独立旁证）：**

> "Any group of square order $s^2$ which admits a congruence cover of excess at most $p-2$, where $p$ is the smallest prime divisor of $s$, is necessarily elementary abelian."

同页紧接："It was also shown that the bound given there is essentially best possible; indeed, there exists a congruence cover of excess $p$ in a suitable non-elementary abelian group whenever $s$ is a proper prime power."

**（b）术语，p.193：** "$s$-cover of $G$"＝由 $s$ 阶子群组成、覆盖全部元素的族；"$s$-packing"＝两两不交的 $s$ 阶子群族。

**（c）Proposition 2.1，p.194：** "Let $G$ be a group of order $v$, and let $s$ be a divisor of $v$. If $G$ admits an $s$-cover, then $\exp G$ divides $s$. Moreover, this necessary condition is also sufficient when $G$ is nilpotent."

**（d）Proposition 2.5，p.195（任意 $p$ 群，不只阿贝尔）：** "Let $G$ be any group of order $p^d$, where $p$ is a prime. Then $\kappa(G,p^{d-1})=p+1$, and every $p^{d-1}$-cover of $G$ of size $p+1$ consists of the $p+1$ subgroups passing through some subgroup of size $p^{d-2}$ of $G$."

**（e）Theorem 3.2，p.197：** "Let $G$ be an abelian $p$-group of order $v=p^d$, and let $t<d$ be a positive integer. If $G$ is not elementary abelian, one has $\pi(G,p^t)\le p^{d-t-1}+\cdots+p^2+p+1$."（$\pi$ = packing 数）

**（f）Theorem 3.5，p.198（唯一的任意 $s$ 结果，但只针对 packing）：** "Let $G$ be a nilpotent group of order $v$ and $s$ a divisor of $v$. Write $v=q_1\cdots q_n$ and $s=s_1\cdots s_n$ … Then … $\pi(G,s)\le\min\{\pi(P_i,s_i)\}\le\min\{(q_i-1)/(s_i-1)\}$."

**（g）Theorem 4.1，p.200（cover 主结果）：** (a) $G$ 为阶 $p^d$ 的非初等阿贝尔阿贝尔群，$\mathcal C$ 为任意 $p^t$-cover，$d=at+b$，$1\le b\le t\ne1$，$a\ge2$，则
$e(\mathcal C)\ge(p-2)p^{(a-2)t+b}+(p-1)p^b(p^{(a-3)t}+\cdots+p^t+1)$。
(b) 同型 $G$ 按型 $(p^{d_1},\dots,p^{d_N})$ 的加强形式。

**（h）Corollary 4.2，p.201（初等阿贝尔刻画）：** 在上述参数且 $(a,p)\ne(2,2)$ 下，若 $e(\mathcal C)$ 严格小于 (7) 式右端，则 $G$ 初等阿贝尔。

**（i）Theorem 6.1，pp.203–204：** 任意（不必阿贝尔）$p$ 群、$\Phi(G)=p^f$、$f<t$、$d-f=\alpha(t-f)+\beta$ 时
$\kappa(G,p^t)\le p^\beta(p^{(\alpha-1)(t-f)}+\cdots+p^{2(t-f)}+p^{t-f}+1)+1$。

**（j）p.201 明文与 1999 年文的关系：** "The preceding approach does not give us anything for $a=1$, unless $t=b$; but then we are considering congruence covers, the case already dealt with in [22]."

**（k）p.213 结论与公开问题：** 结果限于"characterised the elementary abelian groups **among the abelian $p$-groups**"，且明说其界质量 "inferior to those obtained for the special case of congruence covers in [22]"；问题 (1) 明确问 Theorem 3.2/4.1 能否推广到非阿贝尔 $p$ 群乃至任意/幂零群——**说明本篇未解决一般群**。

### 2.5 与 `output/solution.tex` 逐句对照

| 行 | 现文要点 | 判定 | 说明 |
|---|---|---|---|
| 188–189 | 标 B；"已核实范围是固定阿贝尔 $p$ 群中 $p^t$-cover/packing 的上下界及初等阿贝尔刻画，不是任意 $n$ 的存在型一般公式。评论没有可安全转录的精确界，本文不作补写" | **结论正确，范围表述偏窄，等级过时** | ① "固定阿贝尔 $p$ 群"漏掉两处非阿贝尔内容：Proposition 2.5（**任意** $p$ 群）与 Theorem 6.1（**任意** $p$ 群）；② "任意 $s$"确有结果但只对 packing（Theorem 3.5），对 cover 只有 Prop 2.1 与转述的 Result 1.3；③ 现在可以转录精确界。 |
| 202 | "Jungnickel--Storme (2001) 出版页返回 403" | **失效** | 全文已取得。 |
| 189 | "不是任意 $n$ 的存在型一般公式" | **正确且可加强引用** | 其自身公开问题 (1) 即为 "what can be said about arbitrary (or at least nilpotent) groups?"，可直接引 p.213 作"未解决"的权威依据。 |

### 2.6 可直接替换的句子

**替换第 188–189 行整行：**

```latex
Jungnickel--Storme (2001), \emph{Packing and covering groups with subgroups} \cite{JungnickelStorme2001} & A &
全文 24 页已读。cover 方面的结果限于 $p$ 群：Proposition 2.5（p.195）对任意阶 $p^d$ 的群给出 $\kappa(G,p^{d-1})=p+1$；Theorem 4.1（p.200）与 Corollary 4.2（p.201）给出阿贝尔 $p$ 群 $p^t$-cover 的 excess 下界与初等阿贝尔刻画；Theorem 6.1（pp.203--204）给出一般 $p$ 群的构造上界。对任意 $s$ 只有 Proposition 2.1（p.194，packing 侧为 Theorem 3.5，p.198）与转述 1999 年结果的 Result 1.3（p.192）。原文 p.213 自己把“任意群或幂零群”列为公开问题，故其不构成任意 $n$ 的存在型一般公式。\\
```

---

## 3. 第三份：`citation/10.24330-ieja.1567377-4288611.pdf`

### 3.1 身份识别

**该文件是：** T. Foguel, A. R. Moghaddamfar, J. Schmidt, A. Velasquez-Berroteran, **"Concerning Equally Covered Groups"**, *International Electronic Journal of Algebra* **37** (2025), 352–365, DOI **10.24330/ieja.1567377**。首页明载 "Volume 37 (2025) 352-365 / DOI: 10.24330/ieja.1567377"；收稿 2024-08-21、修回 2024-08-29、接受 2024-09-08；PDF 由 pdfTeX 于 2025-01-13 生成，共 14 页，与 352–365 吻合；Crossref 记录 `published-print` = 2025-01-14。

**与论文引用的对应关系：它是被引用的**，对应 `output/solution.tex` 第 808–810 行 `\bibitem{Foguel2025}`，并在第 192 行 `tab:literature` 中以 B 级出现。**不存在"论文未引用它"的情况**——第三份 PDF 不是"未引用的多余文献"，而是三篇中唯一一篇已被论文正式列目的期刊论文。

需注意：`research/literature.md`（§4.5）与 `research/pqalpha-literature.md`（第 14 行、L5）对这篇的访问状态**互相矛盾**（前者称 Dergipark DNS 失败、只有摘要；后者称正文已 `pdftotext` 通读并升为 A）。本轮的 PDF 证明 `pqalpha-literature.md` 正确，`solution.tex` 沿用了过时的 B 判断。

### 3.2 书目核对

| 项 | 核对结果 |
|---|---|
| 作者（4 人，顺序） | T. Foguel, A. R. Moghaddamfar, J. Schmidt, A. Velasquez-Berroteran ✔ |
| 刊名 | International Electronic Journal of Algebra ✔ |
| 卷（期） | 37（Crossref 记为 37(37)） |
| 页码 | 352–365 ✔ |
| 年份 | 2025 ✔（Crossref 2025-01-14；OpenAlex 记 2024 系预发布，期刊卷期以 2025 为准） |
| DOI | 10.24330/ieja.1567377 ✔ |

`\bibitem{Foguel2025}` 作者、刊名、卷、页、年份、DOI **全部正确**；仅未写期号（37(37)），属可接受的省略。

### 3.3 证据等级

**A（全文已读，出版排版 PDF）。**

### 3.4 与 `solution.tex` 相关的精确引文

**（a）p.352，Isaacs 分类的转述（可作第 185 行 Isaacs 行的独立 A 级旁证）：**

> "Isaacs [15] established that the noncyclic $p$-groups of exponent $p$ are the only groups having an equal partition."

参考文献 [15] 为 "I. M. Isaacs, Equally partitioned groups, Pacific J. Math., 49 (1973), 109-116"（p.364），书目与 `\bibitem{Isaacs1973}` 一致。

**（b）Lemma 2.1，p.353（必要条件）：**

> "If $G$ has an equal covering $\Pi=\{H_1,\dots,H_n\}$, then $\exp(G)$ divides $|H_i|$ for all $H_i\in\Pi$. In particular, we have $\pi(H_i)=\pi(G)$ for all $H_i\in\Pi$."

**（c）p.352 式 (3)（覆盖成员数与指数的关系）：**

> "$1<|G:H_i|<n$, for $i=1,2,\dots,n$."

**（d）Lemma 2.10，p.356（唯一与本文数值相关的条目）：**

> "If $G$ is a group with $\exp(G)=|G|/p$ where $p$ is the smallest prime dividing $|G|$, then every equal covering of $G$ is a maximal equal covering of $G$ which contains proper normal subgroups of index $p$. Moreover, in this situation, $G$ has a maximal equal covering consists of $p+1$ proper normal subgroups of index $p$."

**（e）摘要，p.352：** 有限单群无等阶覆盖；任意有限群的某个有限笛卡尔幂有等阶覆盖；$\xi(G)$ 在第 3 节定义（p.357）。

**（f）全文范围：** 只研究等阶覆盖的**存在性与结构**（单群、笛卡尔幂、$\xi(G)$、超可解与幂零群），**没有**任何"最小成员数"的公式，也没有 $\alpha(n)$ 意义上的量。故它不能也不应被用来支持 $\alpha(n)$ 的数值。

### 3.5 与 `output/solution.tex` 逐句对照

| 行 | 现文要点 | 判定 | 说明 |
|---|---|---|---|
| 192–193 | 标 B；"已核实摘要涉及等阶覆盖的存在性与结构，未据此声称含有最小数公式；正文未取得" | **"正文未取得"失效，等级过时；"未含最小数公式"正确** | 升 A，并补 Lemma 2.1（p.353）与 Lemma 2.10（p.356）的具体条目。 |
| 202 | "Foguel 等论文正文连接失败" | **失效** | 全文已取得。 |
| 106 | $\exp(G)\mid n$ 无引用 | **可补 Lemma 2.1（p.353）** | 见 §1.6(6)。 |
| 246–252 | 定理 \ref{thm:primepower}（$\alpha(n)=n+1\iff n$ 为素数幂）的 $n=p$ 情形仅由计数与展形构造得出 | **可补文献旁证（非必需）** | 对 $|G|=p^2$ 有 $\exp(G)=p=|G|/p$（$C_{p^2}$ 除外，其 $\exp=p^2$ 不满足假设），故 Lemma 2.10 给出 $p+1$ 个指数 $p$（即 $p$ 阶）正规子群的等阶覆盖，与计数下界 $p+1$ 合并即 $c_p(G)=p+1$，从而 $\alpha(p)=p+1$。**注意：此旁证只对 $a=1$，不能推广到 $p^a$。** |

### 3.6 可直接替换的句子

**替换第 192–193 行整行：**

```latex
Foguel 等，\emph{Concerning equally covered groups} \cite{Foguel2025} & A &
全文 14 页已读。Lemma 2.1（p.353）给出等阶覆盖的必要条件 $\exp(G)\mid|H_i|$ 与 $\pi(H_i)=\pi(G)$；Lemma 2.10（p.356）证明 $\exp(G)=|G|/p$（$p$ 为 $|G|$ 的最小素因子）时存在由 $p+1$ 个指数 $p$ 的正规子群组成的极大等阶覆盖，为 $\alpha(p)=p+1$ 提供文献旁证。全文研究等阶覆盖的存在性与结构（单群、笛卡尔幂、$\xi(G)$），不含最小成员数公式，也不涉及 $\alpha(n)$。\\
```

---

## 4. 三个专项判定

### 4.1 "Jungnickel 小覆盖定理 $\Rightarrow\alpha(n)\ge n+p_{\min}(n)$" 是否严格成立

**严格成立。** 逐步核对：

1. 取 $s=n$。Jungnickel 的 Theorem 1.4 对**任意**有限群 $G$（阶为平方数 $s^2$）成立，对 $s$ 无素因子结构要求，因此 $s=n$ 合法。
2. excess 定义 $e=r-s-1$ 给出 $e\le p-2\iff r\le s+p-1$。故"$r\le n+p-1$ 个 $n$ 阶子群覆盖 $G$"正是定理假设。
3. 结论"$G$ 初等阿贝尔"要求 $|G|=q^{2a}$，即 $n=q^a$。若 $n$ 非素数幂，$n^2$ 也不是素数幂，故无群满足结论，于是**任何** $|G|=n^2$ 都不存在 $r\le n+p-1$ 的覆盖，即对一切此类 $G$ 有 $c_n(G)\ge n+p$。
4. 对 $G$ 取 $\min$ 得 $\alpha(n)\ge n+p$。若某 $G$ 完全不可覆盖（$c_n(G)=\infty$），不影响最小值方向。

**无隐藏假设**：定理不要求覆盖无赘、不要求成员两两不同、不要求 $G$ 可解或幂零、不要求 $p$ 与 $n$ 的关系。$e=0$ 特例（第 268 行所用）同样合法，因为 $p\ge2$ 保证 $0\le p-2$。

**唯一需注意的表述精度**：$\alpha(n)\ge n+p_{\min}$ 是**本项目的推论**，不是原文陈述（原文只说"小覆盖 $\Rightarrow$ 初等阿贝尔"，从不提 $\alpha$、也不讨论非素数幂的 $n$）。`solution.tex` 已把它写成自证的 Proposition \ref{prop:jungnickel-lower}（第 275–283 行），**归属正确，无需修改结论**，只需把"证据 B"改为 A 并加页码。

### 4.2 Jungnickel–Storme 2001 的 sharp cover 与 $e=p$ / $e=p-1$ 是否被正确表述

**未被正确表述，且原因不是"缺全文"，而是"两个数值本就不冲突"。**

- **$e=p-1$（zbMATH 评论）** = Proposition 4.2（p.418）取 $d=2$：$G=Z_{p^2}\times Z_{p^2}$，$\kappa(G)=p^2+p=s+p$，故 $e=p-1$。原文 p.419 亲口说这使 Theorem 3.3 的界 "can be sharp"。
- **$e=p$（出版方摘要）** = Proposition 4.3（p.419）：$G=Z_{p^2}\times Z_p^{2d-2}$（$d\ge2$），$\kappa(G)=p^d+p+1=s+p+1$，故 $e=p$。原文 p.419 亲口说这是"essentially best possible … off by at most 1"。
- 二者对**同一** $p$、同一 $s=p^d$ 都成立，只是不同群、不同命题。Jungnickel–Storme 2001 的 p.192 重述亦同时保留两句话（excess $\le p-2$ 定理 + "there exists a congruence cover of excess $p$ … whenever $s$ is a proper prime power"）。

**因此 `solution.tex` 第 197 行"二手转录存在一处数量差异…在正文未取得前不作结论"整段应删除重写**（替换文本见 §1.6(2)）。这也是本轮最需要纠正的一处：原先的"证据不足"叙述现在会显得研究者没有读原文。

### 4.3 是否存在把 B 级弱结论写成 A 级定理

**不存在。** 逐条排查 `solution.tex` 中依赖这三篇的断言：

| 断言 | 位置 | 判定 |
|---|---|---|
| $e\le p-2\Rightarrow G$ 初等阿贝尔 | 187、282、268 | 与原文定理逐字相符，**未夸大** |
| $\alpha(n)\ge n+p_{\min}$ | 275–283 | 明确写成本项目 Proposition，**归属正确** |
| 等号情形 $G\cong C_p^{2a}$ | 268–271 | 由 Isaacs + $e=0$ 组合，标注了"本题额外条件"，**正确** |
| Jungnickel–Storme 不含任意 $n$ 公式 | 188–189 | **正确**，且可由原文 p.213 公开问题直接支撑 |
| Foguel 不含最小数公式 | 192–193 | **正确** |

**反方向的问题存在**：两处把 A 级文献降格（第 186–189、192–193 行仍标 B，第 202 行仍称全文不可得），一处把已发表定理当成自研构造（第 324 行，见 §1.6(4)）。没有任何一处把弱结论冒充强定理。

### 4.4 B→A 升级的连带影响（需一并处理的正文表述）

1. 第 167–171 行的证据分级说明中，"B 级"在此文将**无实例可用**；应在表后声明"本次三篇外部文献均已取得全文，表中等级全为 A"。
2. 第 764 行附录索引 "`research/primary-sources.md` & 三篇原始文献的 A/B 级证据复核" 应改为 "A 级证据复核（三篇均已读全文）"。
3. `research/primary-sources.md` §2.2 与 §3 的"证据 B""sharp 构造不一致"结论已被本轮推翻，建议在协调文件中标注 superseded（本轮未改动该文件）。

---

## 5. 按行号的修改清单（按优先级）

| 优先级 | 行 | 动作 |
|---|---|---|
| 高 | 197 | 整段替换：$e=p$ 与 $e=p-1$ 不矛盾，分别对应 Prop 4.3 / Prop 4.2，删除"未决差异"表述 |
| 高 | 324 | 整句替换：定理 \ref{thm:general-upper} 即 Jungnickel 1999 Prop 4.1（p.418），并补 Theorem 3.4（p.418）的幂零群精确值 |
| 高 | 186–187 | 表中行替换：B→A，补 Theorem 1.4（p.415）/Theorem 3.3（p.417），删"受访问防护阻断" |
| 高 | 188–189 | 表中行替换：B→A，精确化范围（含 Prop 2.5/Thm 6.1 的任意 $p$ 群结果、Thm 3.5 的任意 $s$ packing 结果），补 p.213 公开问题 |
| 中 | 192–193 | 表中行替换：B→A，补 Lemma 2.1（p.353）/Lemma 2.10（p.356） |
| 中 | 202 | 删除"访问限制"三项，改为已取得全文的说明 |
| 中 | 282 | "（证据 B…）"→"（证据 A：Theorem 1.4，p.415；Theorem 3.3，p.417）" |
| 低 | 103–105 | 补三处 A 级引用（Jungnickel 1999 Prop 2.1 p.415；JS2001 Prop 2.1 p.194；Foguel Lemma 2.1 p.353） |
| 低 | 246–252 / 268 | 可选补 $\alpha(p)=p+1$ 的文献旁证（Foguel Lemma 2.10, p.356）与 $e=0$ 的定理号 |
| 低 | 764 | 索引描述由 "A/B 级" 改为 "A 级" |

**书目条目：无需任何修改**（第 788–810 行五个 `\bibitem` 的卷期页与 DOI 全部经 Crossref 与 PDF 首页双重核对）。可选的小改进：`Foguel2025` 补期号 `37(37)`。

---

## 6. 仍无法确认 / 不应声称的点

1. **1999 年 PDF 的版本性质**：系作者自排 `dvips` 输出（非出版方水印 PDF）。页眉页脚、页码 413–421、9 页页数与 Crossref 完全吻合，可判定为终稿分页版本；但严格说"读到的是作者终稿，不是出版方 PDF"。若审稿方要求"出版方 PDF"，此点需注明。
2. **2001 年 PDF 的公式符号**：文本层的括号/等号/属于号被旧字体编码破坏，定理编号、假设、页码可靠，**逐字公式引用需对版面复核**。本报告已按语义还原并标注。
3. **Proposition 4.3 的 $d\ge2$**：原文命题未显式写出，须由摘要 "proper power of a prime" 与证明结构补出。引用时**必须**写 "proper prime power"，否则 $d=1$ 时公式给出 $2p+1$ 而 $Z_{p^2}$ 根本不可覆盖。
4. **1999 年文 p.416 的 $c(G,|G|)$**：疑为 $c(G,\sqrt{|G|})$ 的排印/提取残缺。本文所用定理不经过该句，不影响结论；但不要引用这句。
5. **Isaacs 1973 本身不在 `citation/` 中**：其 A 级仍依赖上一轮 `primary-sources.md` 的核对。本轮新增一条独立 A 级旁证：Foguel 等 p.352 的 "the noncyclic $p$-groups of exponent $p$ are the only groups having an equal partition"。**但 Isaacs 的定理号（Theorem 6, p.111）与 Theorem 10 内容本轮未复核**，维持原记录。
6. **不可声称**："Jungnickel 证明了 $\alpha(n)\ge n+p$"（他只是证了小覆盖 $\Rightarrow$ 初等阿贝尔）；"Jungnickel–Storme 处理了两个素因子情形"（其 cover 结果全在 $p$ 群内，p.213 公开问题明示一般情形未解）；"$\alpha(n)\le\prod(q_i+1)$ 是本文新构造"（这是 1999 年文 Prop 4.1）。
