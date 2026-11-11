# 阶 \(n^2\) 群的 \(n\) 阶子群覆盖：划分、下界与小阶精确值

## 0. 量词、记号与主要结论

以下恒设 \(n\ge2\)。对阶为 \(n^2\) 的有限群 \(G\)，令
\[
c_n(G)=\min\{m:\text{存在 }m\text{ 个 }n\text{ 阶子群 }H_1,\dots,H_m
\text{ 使 }G=\bigcup_{i=1}^mH_i\}.
\]
若不存在这样的覆盖，记 \(c_n(G)=\infty\)。本文研究的是**允许在所有 \(n^2\) 阶群中选群后再取最小**的量
\[
M(n)=\min_{|G|=n^2}c_n(G).
\]
它既不是固定群 \(C_n^2\) 的覆盖数，也不是所有可覆盖群上的最大值。循环群 \(C_{n^2}\) 的生成元不属于任何真子群，故根本没有这种覆盖；不能把循环群或 \(C_n^2\) 单例的结论推给所有群。

主要结论为：
\[
\boxed{M(n)=n+1\iff n\text{ 是素数幂}.}
\]
若 \(n\) 不是素数幂，而 \(p\) 是其最小素因子，则
\[
\boxed{M(n)\ge n+p.}
\]
这只是下界，不是普遍等式。逐例精确结果为
\[
\boxed{M(4)=5,\quad M(6)=10,\quad M(8)=9,\quad M(9)=10,\quad M(12)=17.}
\]
其中 \(n=12\) 是完整的计算机辅助穷举与精确整数规划结果，不是抽样猜测。

## 1. 计数下界及等号的结构

每个 \(H_i\) 都含单位元，因此
\[
n^2=\left|\bigcup_{i=1}^mH_i\right|
\le 1+\sum_{i=1}^m(|H_i|-1)=1+m(n-1),
\]
从而
\[
\boxed{m\ge\left\lceil\frac{n^2-1}{n-1}\right\rceil=n+1.}\tag{1}
\]
等号成立当且仅当上述并集估计没有重复计数，即每个非单位元素恰属于一个 \(H_i\)。等价地，
\[
H_i\cap H_j=\{1\}\quad(i\ne j),
\]
且这些子群覆盖 \(G\)。这正是有限群的**等阶子群划分**（equal partition）。

等号情形还有乘积结构。若两个不同分量的阶均为 \(n\)，则
\[
|HK|=\frac{|H||K|}{|H\cap K|}=n^2=|G|,
\]
故
\[
\boxed{G=HK.}\tag{2}
\]
所以等号不只是数值现象，而是很强的组合与群论限制。

## 2. 等阶划分的分类与 \(n+1\) 的精确判定

### 2.1 Isaacs 分类定理

I. M. Isaacs 的等阶划分定理（原文 Theorem 6 及收尾；亦见 Velasquez-Berroteran 的综述 Theorem 10）为：

> 有限群具有所有分量同阶的真子群划分，当且仅当它是非循环、指数为某个素数 \(p\) 的 \(p\)-群。

任意分量阶不必相同的 partitionable groups 还有 Baer–Kegel–Suzuki 的分类；本题使用上述更强的“等阶”分类即可。

若本题达到 \(m=n+1\)，由第 1 节得到等阶划分，再由 Isaacs 定理，\(G\) 是 \(p\)-群。于是 \(|G|=n^2\) 和 \(|H_i|=n\) 都是 \(p\) 的幂，故 \(n\) 必为素数幂。特别地，若 \(n\) 至少有两个不同素因子，就绝不能达到 \(n+1\)。

注意量词：不能由该定理推出“每一个指数为 \(p\) 的非循环 \(p\)-群，只要阶为 \(n^2\)，就必有分量阶恰为 \(n\) 的划分”。下面只需构造一个见证群来证明全局充分性。

### 2.2 素数幂构造

设 \(n=q=p^a\)，取二维 \(\mathbb F_q\)-向量空间的加法群
\[
G=(\mathbb F_q^2,+)\cong C_p^{2a}.
\]
其 \(\mathbb F_q\)-一维子空间共有 \(q+1\) 个，每个有 \(q=n\) 个元素，任意两个交为零子群，并且并集为整个 \(G\)。也可显式写成
\[
H_t=\{(x,tx):x\in\mathbb F_q\}\quad(t\in\mathbb F_q),\qquad
H_\infty=\{(0,x):x\in\mathbb F_q\}.
\]
因此 \(c_n(G)=n+1\)。结合必要性即得
\[
\boxed{M(n)=n+1\iff n\text{ 为素数幂}.}
\]
所以“非素数 \(n\) 不可能达到 \(n+1\)”是错误的；正确分界是**素数幂与非素数幂**，而不是素数与合数。

## 3. 非素数幂时的更强下界及一般公式问题

Jungnickel 关于小同余覆盖的定理给出：若 \(s^2\) 阶群能由至多 \(s+p-1\) 个 \(s\) 阶子群覆盖，其中 \(p\) 是 \(s\) 的最小素因子，则该群必为初等交换群。

若 \(n\) 不是素数幂，则 \(n^2\) 不是素数幂，故 \(n^2\) 阶群不可能是初等交换群。于是不可能有至多 \(n+p-1\) 个子群的覆盖，即
\[
\boxed{n\text{ 非素数幂}\implies M(n)\ge n+p.}\tag{3}
\]
但小例已经否定常见闭式猜测：
\[
M(6)=10>n+ p=8,\qquad M(12)=17>n+p=14;
\]
并且
\[
M(12)=17>n+2p=16.
\]
因此 \(n+p\) 和 \(n+2p\) 都不是一般公式。现有论证只给出下界和若干精确小例，不能据此编造任意非素数幂的统一闭式。

另一个必要条件是：若 \(G\) 能被同阶子群覆盖，则每个元素的阶都整除该公共阶；在本题中特别得到
\[
\boxed{\exp(G)\mid n.}\tag{4}
\]
这一条件用于排除不可覆盖群，但不是充分条件。

## 4. 固定 \(C_n^2\) 与全局 \(M(n)\) 的区别

固定 \(G=C_n^2\) 时，最小覆盖数有精确公式
\[
\boxed{\mu(n):=c_n(C_n^2)
=\prod_{p^a\parallel n}p^{a-1}(p+1)
=n\prod_{p\mid n}\left(1+\frac1p\right).}\tag{5}
\]
证明如下：

1. 每个 \(n\) 阶元素 \(x\) 若属于某个 \(n\) 阶子群 \(H\)，则 \(\langle x\rangle=H\)。故所有循环 \(n\) 阶子群在任何覆盖中都不可省略。\(C_n^2\) 中 \(n\) 阶元素数为
   \[
   n^2\prod_{p\mid n}(1-p^{-2}),
   \]
   每个循环 \(n\) 阶子群有 \(\varphi(n)\) 个生成元，相除即得 (5)。
2. 这些循环子群确实覆盖全群。任取阶为 \(d\) 的元素 \(x\)，在各准素分量中把 \(x_p\) 写成 \(p^{a-b}y_p\)，其中 \(y_p\) 具有该分量的最大阶；再用中国剩余定理合并，可得 \(n\) 阶元素 \(y\) 使 \(x=(n/d)y\)。

例如
\[
\mu(4)=6,\quad \mu(6)=12,\quad \mu(8)=12,\quad
\mu(9)=12,\quad \mu(12)=24.
\]
与下面的全局值比较可见，固定群公式不能替代 \(M(n)\)。

## 5. 指定小例

| \(n\) | 是否素数幂 | 下界 \(n+1\) | 全局精确值 \(M(n)\) | 见证或说明 |
|---|---:|---:|---:|---|
| 4 | 是 | 5 | **5** | \(\mathbb F_4^2\cong C_2^4\) 的 5 条直线 |
| 6 | 否 | 7 | **10** | \(C_2\times(C_3^2\rtimes C_2)\) 等；见第 5.1 节 |
| 8 | 是 | 9 | **9** | \(\mathbb F_8^2\cong C_2^6\) 的 9 条直线 |
| 9 | 是 | 10 | **10** | \(\mathbb F_9^2\cong C_3^4\) 的 10 条直线 |
| 12 | 否 | 13 | **17** | \(A_4^2\) 等；完整穷举见第 5.2 节 |

其中 \(4,8,9\) 直接证明“合数也可能达到 \(n+1\)”。而固定群 \(C_4^2,C_8^2,C_9^2\) 的覆盖数分别为 \(6,12,12\)，再次说明选群量词不可省略。

### 5.1 关于 \(n=6\) 的纯理论下界

下面给出完整手证，排除所有 36 阶群的 8 个或 9 个六阶子群覆盖。

#### （a）只需检查五种指数 6 的群

由 (4)，可覆盖群的指数必为 6。其三阶、二阶 Sylow 子群分别为
\[
P\cong C_3^2,\qquad V\cong C_2^2.
\]
Sylow 定理给出 \(n_3\in\{1,4\}\)。

若 \(n_3=4\)，对四个三阶 Sylow 子群的共轭作用之核 \(K\) 有阶 3：核若平凡，则 36 阶群会嵌入 \(S_4\)，矛盾。商群 \(G/K\) 是含四个三阶 Sylow 子群的 12 阶群，故为 \(A_4\)。取 \(W/K\) 为其中的正规四阶子群，由 Schur–Zassenhaus 可得 \(V\triangleleft W\)；而 \(V\) 是 \(W\) 的特征子群，故 \(V\triangleleft G\)。再写 \(G=V\rtimes P\)，作用像为 \(C_3\)，其核给出中心直因子，遂得 \(G\cong C_3\times A_4\)。

若 \(n_3=1\)，则 \(G=P\rtimes V\)。交换二群 \(V\) 中元素的最小多项式均整除在 \(\mathbb F_3\) 上无重根的 \(X^2-1\)，故可同时对角化。两个特征的不同选择恰给出
\[
C_6^2,\qquad C_6\times S_3,\qquad C_2\times D,\qquad S_3^2,
\]
其中 \(D=C_3^2\rtimes C_2\)，作用为全反演。故指数条件只留下这五种候选；它们是候选，并不都真的可覆盖。

事实上 \(C_3\times A_4\) 不可覆盖。若一个六阶子群 \(H\) 含有 \(A_4\) 分量非平凡的三阶元素，则 \(H\) 在 \(A_4\) 中的投影只能是相应的 \(C_3\)（\(A_4\) 没有六阶子群）。于是该投影的核在 \(H\) 中有阶 2；但整个直积投影的核是中心直因子 \(C_3\)，其中没有二阶元素，矛盾。因此这样的三阶元素根本不属于任何六阶子群。

其余四群的三阶元素都在正规的 \(P\cong C_3^2\) 中，恰有四条三阶直线。

#### （b）统一重复覆盖计数

六阶群只有 \(C_6\) 和 \(S_3\)，两者都恰含两个三阶元素；前者有 1 个 involution、2 个六阶元素，后者有 3 个 involutions、没有六阶元素。若用 \(k\) 个子群覆盖，则 35 个非单位元的总重复量为 \(5k-35\)，仅三阶元素就贡献
\[
2k-8=2(k-4).
\]
当 \(k=8\) 时，总重复量为 5，却至少为 8，矛盾。

当 \(k=9\) 时，两者都等于 10。因此其余元素不得有任何重复，得到
\[
\boxed{\text{每个 involution 和每个六阶元素都恰好被覆盖一次}.}\tag{T}
\]
若循环六阶子群有 \(c\) 个，六阶元素共有 \(t\) 个，则 \(t=2c\)。逐群排除：

- **\(C_6^2\)：**由 (5) 需要 12 个循环子群，故不可能用 9 个。
- **\(C_6\times S_3\)：**有 18 个六阶元素，故 (T) 迫使 \(c=9\)。但全群只有 7 个 involutions，9 个循环六阶子群各含一个，必重复，矛盾。
- **\(C_2\times D\)：**有 8 个六阶元素，故 \(c=4\)。循环六阶子群恰为 \(\langle z\rangle\times L\)，其中 \(z\) 是中心 involution，\(L\) 遍历四条三阶直线；四群都含 \(z\)，与 (T) 矛盾。
- **\(S_3^2\)：**固定两因子的三循环 \(a,b\)，令 \(T\) 为一个因子中三个 transpositions 的集合。12 个六阶元素迫使选出全部六个循环子群
  \[
  \langle a\rangle\times\langle\tau\rangle,\qquad
  \langle\sigma\rangle\times\langle b\rangle\qquad(\sigma,\tau\in T).
  \]
  其余三个子群均为 \(S_3\)，还须覆盖两条混合直线 \(R=\langle(a,b)\rangle\)、\(S=\langle(a,b^{-1})\rangle\)。含 \(R\) 的子群的三个混合 involutions 可写为
  \[
  (\sigma a^\ell,\tau b^\ell),\qquad \ell=0,1,2;
  \]
  含 \(S\) 者相应为
  \[
  (\sigma' a^m,\tau' b^{-m}),\qquad m=0,1,2.
  \]
  写 \(\sigma'=\sigma a^r,\tau'=\tau b^s\)，坐标相等化为 \(\ell=r+m=s-m\)，模 3 总有解 \(2\ell=r+s\)。所以这两类子群必重复覆盖一个 involution，再与 (T) 矛盾。

故任何 36 阶群都不能用 8 或 9 个六阶子群覆盖，即 \(M(6)\ge10\)。

#### （c）显式 10 子群覆盖

令
\[
G=\langle z\rangle\times(N\rtimes\langle t\rangle),\qquad
N=C_3^2,
\]
其中 \(|z|=2\) 且 \(z\) 居中，\(t\) 在 \(N\) 上作全反演。取 \(N\) 的四条直线 \(L\)，先选四个子群
\[
\langle z\rangle\times L\cong C_6.
\]
它们已覆盖 \(N\cup zN\)。固定一条直线 \(L\)，对 \(\varepsilon\in\{0,1\}\) 及 \(N/L\) 的三个陪集代表 \(u\)，再选六个子群
\[
H_{\varepsilon,u}=\langle L,z^\varepsilon ut\rangle\cong S_3.
\]
每个 \(Nt\) 中元素均可写成 \(l(ut)\)，每个 \(zNt\) 中元素均可写成 \(l(zut)\)，其中 \(l\in L\)，故后六群覆盖所有剩余元素。总计 10 个子群，所以
\[
\boxed{M(6)=10.}
\]
独立的 GAP 穷举与整数规划核验还显示：可覆盖的四个 36 阶群中，\(S_3^2,C_6\times S_3,C_2\times D\) 的精确值均为 10，\(C_6^2\) 为 12；其余十个群不可覆盖。

### 5.2 \(n=12\)：完整穷举与精确集合覆盖证书

144 阶群共有 197 个（GAP Small Groups Library）。对每个群，计算全部 12 阶子群，并解精确 0-1 集合覆盖模型。令 \(\mathcal H_{12}(G)=\{H_1,\dots,H_r\}\)，则
\[
\begin{aligned}
\min\quad &\sum_{j=1}^r x_j\\
\text{s.t.}\quad &\sum_{j:g\in H_j}x_j\ge1
 &&(g\in G),\\
&x_j\in\{0,1\}&&(j=1,\dots,r).
\end{aligned}\tag{6}
\]
最优值就是 \(c_{12}(G)\)。这里没有随机搜索或启发式近似。

实际使用 GAP 4.10.2 枚举子群，SciPy 1.13.1 的 `milp`/HiGHS 求解，单实例时限 60 秒、相对 MIP gap 为 0。审计结果如下：

1. 197 个群中，108 个因 \(\exp(G)\nmid12\) 由 (4) 排除；其余 89 个全部导出。
2. 89 个候选中，15 个即使取全部 12 阶子群，其并集也不是全群，故不可覆盖。
3. 其余 74 个中，73 个由 HiGHS 返回精确最优值；只有 `SmallGroup(144,196)` 到时，但其对偶下界已为 **18**，并找到 20 子群覆盖。
4. 73 个精确实例中，恰有以下三个最优值为 **17**，其余精确最优值均至少 18：
   - `SmallGroup(144,184)`：\(A_4\times A_4\)；
   - `SmallGroup(144,193)`：\(C_2\times C_6\times A_4\)；
   - `SmallGroup(144,194)`：\(C_3\times(C_2^4\rtimes C_3)\)。
5. `SmallGroup(144,101)` 即 \(C_{12}^2\)，最优值 24，与 (5) 一致。

因此所有 144 阶群都已排除、得到精确值，或得到大于 17 的认证下界；唯一超时实例不影响全局结论，故
\[
\boxed{M(12)=17.}
\]

复现文件（仓库相对路径）：

- GAP 导出脚本：`computation/order144/export-covers.g`；
- 精确求解脚本：`computation/order144/solve-covers.py`；
- 全部候选及子群数据：`computation/order144/covers-12.jsonl`；
- 全部求解状态、对偶界和所选子群：`computation/order144/solutions-12.jsonl`。

数据完整性校验（SHA-256）：
\[
\begin{aligned}
\texttt{covers-12.jsonl:}&\quad
\texttt{5af630fdc06e680b7ef107ade80fc5c501160fd4d7a8aae30568b105d2b5d22f},\\
\texttt{solutions-12.jsonl:}&\quad
\texttt{695d9b5cb41520a86f7ac1b43af755426c64d8a8daf816ee254e721293980125}.
\end{aligned}
\]

## 6. 最终判断与可信程度

1. 计数下界 \(1+m(n-1)\ge n^2\)、等号与等阶划分的等价，以及乘积条件 \(G=HK\)，均为直接严格证明。
2. \(M(n)=n+1\) 的充要条件是 \(n\) 为素数幂；故 \(4,8,9\) 虽为合数仍可达到 \(n+1\)。
3. 非素数幂时有 \(M(n)\ge n+p\)，但 \(n+p\) 不是一般精确公式；\(n+2p\) 也被 \(n=12\) 排除。一般非素数幂的闭式仍是未解决问题，不能把下界写成答案。
4. \(n=4,6,8,9\) 的精确值有纯理论证明；\(n=12\) 的 17 有完整群库枚举和精确整数规划证书，可信度高，但应与手证结论区分。
5. 固定 \(C_n^2\) 的公式 \(\mu(n)\) 与全局 \(M(n)\) 不同，例如 \(\mu(6)=12\) 而 \(M(6)=10\)，\(\mu(12)=24\) 而 \(M(12)=17\)。

## 参考文献

- I. M. Isaacs, *Equally partitioned groups*, Pacific Journal of Mathematics **49**(1) (1973), 109–116，[原文 PDF](https://msp.org/pjm/1973/49-1/pjm-v49-n1-p11-s.pdf)。
- Dieter Jungnickel, *On Small Congruence Covers*, Bulletin of the Belgian Mathematical Society—Simon Stevin **6** (1999), 413–421，[DOI](https://doi.org/10.36045/bbms/1103065860)，[定理摘要](https://www.zhangqiaokeyan.com/journal-foreign-detail/07040530865.html)，[作者出版物目录](https://www.uni-augsburg.de/de/fakultaet/mntf/math/prof/opt/team/ehemalige/jungnickel/publikationen/)。
- Andrew Velasquez-Berroteran, *Equal Coverings of Finite Groups*，特别是 Theorem 10（等阶划分分类）和 Theorem 13（指数必要条件），[arXiv:2206.14843](https://arxiv.org/abs/2206.14843)。
