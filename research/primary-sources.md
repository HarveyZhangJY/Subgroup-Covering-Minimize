# 三篇原始文献复核

## 证据级别与结论边界

- **A 级：全文已读。** Isaacs (1973) 的出版方扫描 PDF 已下载并逐页核对。
- **B 级：未读到全文。** Jungnickel (1999) 目前只能核对出版方摘要转录与 zbMATH 专家评论；Project Euclid 的正文/PDF请求均被 Incapsula 阻断。Jungnickel–Storme (2001) 目前只能核对出版方书目信息、机构库记录与 zbMATH 专家评论；ScienceDirect 返回 403，Ghent 记录没有全文附件，Augsburg 记录在当前环境不可连接。
- 因此，下文只有 Isaacs 的页码、定理号和引文属于“原文逐字核对”。对后两篇不虚构定理号、构造所在页或未读到的精确公式。

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
[DOI / Project Euclid](https://doi.org/10.36045/bbms/1103065860)；[公开 PDF 地址（本轮被拦截）](https://projecteuclid.org/download/pdf_1/euclid.bbms/1103065860)；[zbMATH 评论 API](https://api.zbmath.org/v1/document/1374975)。**证据 B，不是全文核对。**

### 2.1 两种独立转录一致的主定理

出版方摘要转录与 Norbert Knarr 的 zbMATH 评论一致给出以下假设和结论：

- \(|G|=s^2\)；congruence cover 是 \(r\) 个阶 \(s\) 子群，其并为 \(G\)；
- excess 定义为 \(e=r-s-1\)；
- \(p\) 是 \(s\) 的最小素因子；
- 若 \(e\le p-2\)，等价于 \(r\le s+p-1\)，则 **\(G\) 初等阿贝尔**，且覆盖是几何覆盖，即可视为适当射影空间的子空间覆盖。

本题若 \(r\le n+p-1\)，其中 \(p\) 为 \(n\) 的最小素因子，则 \(G\) 初等阿贝尔；非素数幂 \(n\) 因而不可能，故得到下界 \(M(n)\ge n+p\)。特别地 \(e=0\) 给出上节所需的等号群分类。由于全文未取得，上述结论可引用到文章摘要和 zbMATH 评论，但暂不标具体定理号或定理所在页。

### 2.2 sharp 构造：目前不能消解的摘要不一致

- **出版方摘要转录：**每当 \(s\) 是素数的真幂，存在适当的非初等阿贝尔群，具有 \(s+p+1\) 个成员的 congruence cover，即 \(e=p\)。摘要只称该界“essentially best possible”。
- **zbMATH 评论：**“For \(p\)-groups this bound is sharp”，并称存在非初等阿贝尔 \(p\)-群具有 excess \(p-1\)，即 \(r=s+p\)。这比摘要构造少一个成员。

二者对主定理没有冲突，但对 sharp 构造的数量不一致。未读正文前，不能把 \(e=p-1\) 的构造细节、适用参数或定理号写成已由原文核实；也不能用摘要的 \(e=p\) 去否认专家评论。最稳妥的引用是：主定理采用上述两种来源一致的部分；sharp 性保留“zbMATH 评论称 \(e=p-1\)，摘要仅明确给出 \(e=p\)，正文待核”的证据限定。

## 3. Jungnickel–Storme (2001)：固定 \(p\)-群的界

**文献。** D. Jungnickel, L. Storme, *Packing and covering groups with subgroups*, J. Algebra 239(1) (2001), 191–214。  
[DOI](https://doi.org/10.1006/jabr.2000.8640)（正确 PII 为 `S002186930098640X`）；[Ghent 书目记录](https://biblio.ugent.be/publication/168724)；[Augsburg 书目记录](https://opus.bibliothek.uni-augsburg.de/opus4/frontdoor/index/index/docId/39233)；[zbMATH 评论 API](https://api.zbmath.org/v1/document/1643653)。**证据 B（专家评论），全文未取得。**

Patric Östergård 的 zbMATH 评论明确说明：论文研究用指定阶 \(s\) 的子群覆盖或 packing 有限群；改进的是**阿贝尔 \(p\)-群中 \(p^t\)-packing 与 \(p^t\)-cover 大小的上、下界**，包括非初等阿贝尔群，并由大 packing、小 cover 的存在刻画初等阿贝尔群。评论没有给出可安全转录的精确公式，故本报告不编造定理号、页码或界。

这篇论文的范围不是“对任意 \(n\)，在所有阶 \(n^2\) 的群上取最小值”的一般闭式，而是固定群类中的 covering/packing 数界。它能支持“已有固定阿贝尔 \(p\)-群上下界与结构刻画”，不能支持“已有任意 \(n\) 的一般精确公式”。

## 4. 对三个复核问题的最终回答

1. **等阶划分分类：**Isaacs Theorem 6 加 p.109 逆方向，恰为非循环、指数 \(p\) 的 \(p\)-群；一般有非阿贝尔例。本题 \(n+1\) 等号覆盖还需 Jungnickel 的 \(e=0\) 结论，才能得到 \(G\cong(C_p)^{2a}\)。
2. **小覆盖：**两种独立转录一致确认 \(e\le p-2\Rightarrow G\) 初等阿贝尔。sharp 构造存在摘要 \(e=p\) 与 zbMATH 评论 \(e=p-1\) 的差异；正文未得，不宣称已逐字解决。
3. **一般公式：**这三篇文献没有给出任意 \(n\) 的存在型一般精确公式：Isaacs 是等阶划分分类，Jungnickel 给一般小覆盖结构定理及素数幂构造，Jungnickel–Storme 的已核实范围是固定阿贝尔 \(p\)-群的上下界。准确说法是“本次三篇原始文献复核未见一般闭式”，而不是断言所有后续文献绝对不存在。
