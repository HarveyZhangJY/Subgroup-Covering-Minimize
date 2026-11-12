# 状态摘要：三篇外部文献原文核对（CIT）

1. **三篇均升 A 级**（文字可提取，非扫描件；页码与期刊分页逐页吻合；卷期页与 DOI 经 Crossref 复核）。
2. **书目无错**：三篇的作者、刊名、卷(期)、年份、页码、DOI 与 Crossref 逐字段一致；`solution.tex` 第 792–810 行的 `\bibitem` 无需改动。
3. `citation/On Small Congruence Covers.pdf` = Jungnickel, *On small congruence covers*, Bull. Belg. Math. Soc.–Simon Stevin **6**(3) (1999), 413–421, DOI 10.36045/bbms/1103065860。**A 级**。
4. `citation/Packing_and_Covering_Groups_with_Subgrou.pdf` = Jungnickel–Storme, *Packing and covering groups with subgroups*, J. Algebra **239**(1) (2001), 191–214, DOI 10.1006/jabr.2000.8640。**A 级**。
5. `citation/10.24330-ieja.1567377-4288611.pdf` = Foguel–Moghaddamfar–Schmidt–Velasquez-Berroteran, *Concerning equally covered groups*, IEJA **37** (2025), 352–365, DOI 10.24330/ieja.1567377。**论文已引用**（`\bibitem{Foguel2025}`，表第 192 行），**A 级**。
6. **修正一（最高优先）**：`solution.tex` 第 197 行所谓 sharp 构造“数量差异”不成立。$e=p-1$ 是 Prop 4.2（p.418，取 $d=2$），$e=p$ 是 Prop 4.3（p.419）；原文 p.419 明说前者使 Thm 3.3 的界 "can be sharp"、后者使其 "off by at most 1"。两者并存，须整段重写。
7. **修正二**：`solution.tex` 第 311–324 行定理 \ref{thm:general-upper} 的构造与计数即 Jungnickel 1999 **Prop 4.1（p.418）**；同文 **Thm 3.4（p.418）** 另给幂零群下界 $|C|\ge\prod(q_i+1)$。第 324 行“本次构造、不应冒充文献公式”应改为署名引用（方向是低估文献）。
8. **修正三**：第 186–193 行两处标 B 与第 202 行“访问限制”全部失效（1999 文防护拦截、2001 文 403、Foguel 正文连接失败）。三篇均已取得全文，须升 A 并补定理号：Thm 1.4/3.3（pp.415/417）、Thm 3.4+Prop 4.1（p.418）、Prop 2.1（p.415）；JS2001 Prop 2.1（p.194）、Prop 2.5（p.195）、Thm 3.2（p.197）、Thm 3.5（p.198）、Thm 4.1（p.200）、Cor 4.2（p.201）、Thm 6.1（pp.203–204）、p.213 公开问题；Foguel Lemma 2.1（p.353）、Lemma 2.10（p.356）。
9. **$e=p$ vs $e=p-1$ 已彻底澄清**，无需再作“未决”保留。
10. **$\alpha(n)\ge n+p_{\min}$ 转写严格成立**（$s=n$ 合法；$e\le p-2\iff r\le s+p-1$；非素数幂时初等阿贝尔不可能）。但它是本项目推论，原文不提 $\alpha$；`solution.tex` 已正确写成自证命题。
11. **未发现“B 级弱结论写成 A 级定理”**；反而发现两处降格（B 未升 A）与一处归属低估（Prop 4.1 被当自研）。
12. **JS2001 范围更正**：不只“阿贝尔 $p$ 群”——Prop 2.5 与 Thm 6.1 对任意 $p$ 群；任意 $s$ 只有 packing 侧 Thm 3.5 与 cover 侧 Prop 2.1（及转述的 Result 1.3）。其 p.213 公开问题可直接支撑“一般群未解”。
13. **交叉验证**：Jungnickel Thm 3.4+Prop 4.1 预言 $\min_{\text{幂零}}c_n(G)=P(n)$。与 `solution.tex` 的 $\alpha(6)=10<12$、$\alpha(12)=17<20$、$\alpha(18)=27<30$（见证群均非幂零）及 $\alpha(15)=24=P(15)$、$\alpha(20)=30=P(20)$、$\alpha(28)=40=P(28)$（见证群均幂零）完全一致，构成独立一致性检验。
14. **未确认点**：1999 文 PDF 为作者自排 dvips 终稿（非出版方水印 PDF）；2001 文文本层符号被旧字体编码破坏（需按版面复核公式）；Prop 4.3 隐含 $d\ge2$，引用须写 "proper prime power"；Isaacs 原文不在 `citation/`，其定理号维持上轮记录。
15. 产出：`research/citation-review.md`（逐篇报告、精确引文、行号对照、可替换句子、修改清单）。未改动 `output/solution.tex`、`output/solution.pdf` 及其他 Agent 文件。
