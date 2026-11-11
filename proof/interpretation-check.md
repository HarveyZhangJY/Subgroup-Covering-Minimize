# 题意与结论核验

## 1. 必须先固定的量词

对固定的 \(n\ge2\)，令
\[
\mathcal U_n=\{G:|G|=n^2,\ G\text{ 能被若干个 }n\text{ 阶子群覆盖}\},
\]
并令 \(m_n(G)\) 为覆盖 \(G\) 所需的最少 \(n\) 阶子群数（不可覆盖时不定义）。三种读法分别是

- **(A) 选群后再最小化：** \(\alpha(n)=\min_{G\in\mathcal U_n}m_n(G)\)。
- **(B) 对任意可覆盖群作统一保证：** 若指“至多多少个必够”，应为 \(\beta(n)=\max_{G\in\mathcal U_n}m_n(G)\)；若只问“任何群至少需要多少”，那只是统一下界，其在整个类上的最佳值是 \(\alpha(n)\)。这两种“保证”不能混同。
- **(C) 默认 \(G=C_n^2\)：** 求的是 \(\mu(n)=m_n(C_n^2)\)，一般不等于 \(\alpha(n)\)。

群不总是可覆盖：例如 \(C_{n^2}\) 中有阶为 \(n^2>n\) 的元素，不可能属于任何 \(n\) 阶子群。另一方面，下文证明 \(C_n^2\in\mathcal U_n\)，故 (A)、(B) 的讨论范围非空。

## 2. 计数下界与等号

任何覆盖 \(H_1,\dots,H_m\) 都满足
\[
n^2-1=|G\setminus\{1\}|
\le \sum_i|H_i\setminus\{1\}|=m(n-1),
\]
所以 **\(m\ge n+1\)**。等号成立当且仅当各 \(H_i\setminus\{1\}\) 两两不交，即这些子群构成 \(G\) 的一个等阶划分（equal partition）。仅有计数不能断言等号能取到。

## 3. (A) 可在所有 \(G\) 中选择

**精确结论：**
\[
\boxed{\alpha(n)=n+1\iff n\text{ 是素数幂（包括素数）}.}
\]

必要性：若 \(m=n+1\)，上节说明得到等阶划分。等划分类定理指出，具有等阶划分的有限群必为非循环 \(p\)-群且指数为 \(p\)（Velasquez-Berroteran, *Equal Coverings of Finite Groups*, Theorem 10）。在本题阶数下遂有 \(n=p^a\)，且 \(G\cong C_p^{2a}\)。

充分性：设 \(n=p^a\)，取有限域 \(\mathbb F_n\) 的加法群
\[
G=(\mathbb F_n^2,+)\cong C_p^{2a},\qquad |G|=n^2.
\]
取
\[
H_t=\{(x,tx):x\in\mathbb F_n\}\ (t\in\mathbb F_n),\qquad
H_\infty=\{(0,x):x\in\mathbb F_n\}.
\]
这是 \(n+1\) 个 \(n\) 阶子群，两两交平凡且并集为 \(G\)。注意：当 \(a>1\) 时这个见证群不是 \(C_n^2\)。

对非素数幂 \(n\)，还可给出更强的严格下界。Jungnickel 的定理说：若 \(s^2\) 阶群能被至多 \(s+p-1\) 个 \(s\) 阶子群覆盖，其中 \(p\) 是 \(s\) 的最小素因子，则该群初等交换。非素数幂 \(n\) 不可能使 \(n^2\) 阶群初等交换，故
\[
\alpha(n)\ge n+p,\qquad \alpha(n)\le\mu(n)
\]
（上界来自第 5 节）。一般非素数幂的精确闭式不在此猜测。

**小例：** \(n=4\) 时 \(\alpha(4)=5\)，见证群为 \(C_2^4\)；但 \(\mu(4)=6\)。\(n=6\) 时上式给出 \(8\le\alpha(6)\le12\)。还可改进上界为 \(\alpha(6)\le10\)：在 \(S_3\times C_6\) 中，20 个 6 阶元素恰好生成 10 个循环 6 阶子群，按两个分量的元素阶直接核验，这 10 个子群已覆盖全群；而所有 6 阶元素又迫使它们全部出现，故其最小覆盖数恰为 10。

## 4. (B) 任意可覆盖 \(G\) 的统一值

若 \(B\) 指“选定 \(M\)，使每个可覆盖 \(G\) 都能用至多 \(M\) 个 \(n\) 阶子群覆盖”，则最小这样的 \(M\) 就是 \(\beta(n)\)。严格可知
\[
\boxed{\beta(n)\ge \mu(n)=\prod_{p^a\|n}p^{a-1}(p+1)},
\]
其中乘积取遍 \(n\) 的所有素幂因子 \(p^a\|n\)。当 \(n=p\) 为素数时，\(p^2\) 阶群只有 \(C_{p^2}\)（不可覆盖）和 \(C_p^2\)，故
\[
\boxed{\beta(p)=p+1.}
\]
但对每个合数 \(n\)，都有 \(\mu(n)>n+1\)，所以 **\(n+1\) 绝不是对所有可覆盖群的统一充分值**。例如 \(\beta(4)\ge6\)、\(\beta(6)\ge12\)。除上述素数情形和一般下界外，没有进一步分类或穷举时不应给 \(\beta(n)\) 猜测闭式。

若 \(B\) 只是问统一“至少需要多少”，则计数下界是 \(n+1\)；它在整个类上是否可达，仍按 (A) 区分 \(n\) 是否为素数幂。

## 5. (C) 固定 \(G=C_n^2\) 的精确答案

\[
\boxed{\mu(n)=\prod_{p^a\|n}p^{a-1}(p+1)
      =n\prod_{p\mid n}\left(1+\frac1p\right).}
\]

证明分两步：

1. **每个循环 \(n\) 阶子群都不可省略。** 若 \(x\) 是 \(n\) 阶元素，任何包含 \(x\) 的 \(n\) 阶子群都只能是 \(\langle x\rangle\)。因此所有循环 \(n\) 阶子群在任何覆盖中都必须出现。\(C_n^2\) 中 \(n\) 阶元素数为
   \[
   n^2\prod_{p\mid n}(1-p^{-2}),
   \]
   每个循环 \(n\) 阶子群有 \(\varphi(n)=n\prod_{p\mid n}(1-p^{-1})\) 个生成元，故这些子群数正是上述乘积。
2. **它们确实覆盖全群。** 任取 \(x\in C_n^2\)，设 \(d=|x|\)。在每个准素分量 \(C_{p^a}^2\) 中，若 \(|x_p|=p^b\)，则可写 \(x_p=p^{a-b}y_p\)，其中 \(|y_p|=p^a\)。用中国剩余定理合并各 \(y_p\)，得到 \(n\) 阶元素 \(y\) 使 \(x=(n/d)y\)，故 \(x\in\langle y\rangle\)。

特别地，
\[
\mu(p)=p+1,\quad \mu(4)=6,\quad \mu(6)=12,\quad
\mu(8)=12,\quad \mu(9)=12.
\]
所以把题目默认成 \(C_n^2\) 后仍回答 \(n+1\)，对一切合数 \(n\) 都是错误的；\(n=4\) 已是最小反例。

## 参考来源

- Andrew Velasquez-Berroteran, [*Equal Coverings of Finite Groups*](https://arxiv.org/abs/2206.14843), Theorem 10（等阶划分群的分类）。
- Dieter Jungnickel, *On Small Congruence Covers*, Bull. Belg. Math. Soc. Simon Stevin **6** (1999), 413–421；[作者出版物目录](https://www.uni-augsburg.de/de/fakultaet/mntf/math/prof/opt/team/ehemalige/jungnickel/publikationen/)及[定理摘要](https://m.zhangqiaokeyan.com/journal-foreign-detail/07040530865.html)。
