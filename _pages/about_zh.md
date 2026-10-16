---
layout: "default"
permalink: "/zh/"
title: "韩立峰 | 数学与机器学习"
excerpt: "韩立峰，莱斯特大学与大连理工大学合作办学项目本科生。研究兴趣包括强化学习、优化与多视图机器学习。"
lang: "zh"
lang_switch_label: "English"
lang_switch_url: "/"
author_profile: true
author_name: "韩立峰"
author_avatar: "/assets/portrait/lifeng-han.jpg"
author_avatar_width: 1279
author_avatar_height: 1791
author_bio: "数学与数理基础科学专业本科生"
sidebar_intro: "莱斯特大学 · 大连理工大学. 预计毕业 · 2027 年 6 月"
---


<span class="anchor" id="about"></span>
<header class="homepage-hero">
  <p class="section-kicker">合作办学项目本科生 · 数学 · 机器学习</p>
  <h1>韩立峰</h1>
  <p>我就读于莱斯特大学与大连理工大学合作办学项目，学习数学与数理基础科学，预计于 2027 年 6 月毕业。</p>
  <p>研究兴趣包括强化学习、优化、深度学习、自然语言处理与大语言模型，以及数理统计。</p>
  <div class="link-pills"><a class="link-pill" href="mailto:lh481@student.le.ac.uk">邮箱</a><a class="link-pill" href="https://github.com/2369787465a-jpg">GitHub</a><a class="link-pill" href="/zh/publications/">学术论文</a></div>
</header>

<div class="highlight-grid">
  <section class="highlight-card"><h3>研究方向</h3><p>强化学习与优化</p><p>多视图机器学习</p><p>数理统计</p></section>
  <section class="highlight-card"><h3>学术论文</h3><p>Applied Intelligence · 修回中</p><p>ICONIP 2026 · 已录用</p><p>CIPAE 2025 · 已发表</p></section>
  <section class="highlight-card"><h3>研究代码</h3><p>CAADRL / CluPDTSP</p><p>MC-TRCM</p><p>臭氧降尺度 · Ozone-Downscaling</p></section>
</div>

<section aria-labelledby="research-heading">
  <span class="anchor" id="research"></span>
  <h2 id="research-heading">研究兴趣</h2>
  <div class="chip-row"><span class="chip">强化学习</span><span class="chip">优化</span><span class="chip">深度学习</span><span class="chip">自然语言处理与大语言模型</span><span class="chip">数理统计</span></div>
</section>

<section aria-labelledby="projects-heading">
  <span class="anchor" id="projects"></span>
  <h2 id="projects-heading">精选研究与代码</h2>
  <p class="section-note">探索复杂数据中的结构化决策与有效表示。</p>
  <article class="paper-box">
    <div class="paper-box-image"><div><span class="badge">修回中</span><a href="/assets/research/clupdtsp-architecture.png" aria-label="查看完整研究配图 — Cluster-Aware Attention-Based Deep Reinforcement Learning for Pickup and Delivery Problems"><img src="/assets/research/clupdtsp-architecture.png" alt="论文中的 CAADRL 模型架构，展示注意力编码器与路径解码器。" width="1601" height="996" loading="lazy" decoding="async"></a><p class="figure-note">模型架构 · 论文原图 2</p></div></div>
    <div class="paper-box-text"><h3>Cluster-Aware Attention-Based Deep Reinforcement Learning for Pickup and Delivery Problems</h3><p class="publication-meta">共同第一作者 · 导师：大连理工大学 Guangyu Zou 教授<br>2025.09 – 2026.07</p><p>本项目面向具有空间聚类结构的取送货问题，在配对与先后顺序约束下构建 CAADRL 模型。通过全局自注意力和簇内注意力提取多尺度空间特征，再以分层解码器处理簇内路径选择与簇间转移。</p><p class="project-contribution"><strong>个人分工:</strong> 我负责 NCS 基线复现、消融实验设计与分析及实验图表制作，并参与不同问题规模与数据分布下的评估。</p><div class="pub-links">
<a href="https://github.com/2369787465a-jpg/CluPDTSP/blob/main/Clupdtsp_main.pdf">论文 PDF</a><a href="https://github.com/2369787465a-jpg/CluPDTSP">代码</a><a href="https://arxiv.org/abs/2603.10053">arXiv 预印本</a></div></div>
  </article>
  <article class="paper-box paper-box--centered-split" data-project="mctrcm">
    <figure class="paper-box-figure"><a href="/assets/research/mctrcm-architecture.png" aria-label="查看完整研究配图 — MC-TRCM: Observation-Aware Recursive Fusion for Incomplete Mobile and Wearable Mental-Health Feature Views"><img src="/assets/research/mctrcm-architecture.png" alt="论文中的 MC-TRCM 架构，展示观测感知 token、特征融合与递归细化。" width="1443" height="505" loading="lazy" decoding="async"></a><figcaption class="figure-note">模型架构 · 论文原图 2</figcaption></figure>
    <div class="paper-box-text"><span class="badge">已录用</span><h3>MC-TRCM: Observation-Aware Recursive Fusion for Incomplete Mobile and Wearable Mental-Health Feature Views</h3><p class="publication-meta">共同第一作者 · 导师：大连理工大学 Guangyu Zou 教授<br>2026.04 – 2026.07</p><p>本项目提出 MC-TRCM，在大量缺失观测下融合异构移动设备与可穿戴特征。以特征源 token 和缺失感知门控结合条件化 Transformer，再通过递归解码细化预测；在 DepreST-CAT 与 PSYCHE-D 的六个回归和分类任务上开展评估。</p><p class="project-contribution"><strong>个人分工:</strong> 我参与多源数据处理、模型设计与实验验证，包括基线对比、消融实验，以及缺失模式建模和递归预测机制的分析。</p><div class="pub-links">
<a href="https://github.com/2369787465a-jpg/MC-TRCM/blob/main/main.pdf">论文 PDF</a><a href="https://github.com/2369787465a-jpg/MC-TRCM">代码</a></div></div>
  </article>
  <details class="publication-collapse more-research"><summary>更多研究项目</summary>
    <article class="timeline-card project-card project-card--publication project-card--illustrated" data-project="did">
<div class="project-card-media"><span class="badge">已发表</span><figure class="project-figure"><a href="/assets/research/cybercrime-cluster-clouds.png" aria-label="查看完整图片: 网络犯罪指标与政策效果评估"><img src="/assets/research/cybercrime-cluster-clouds.png" alt="原始建模报告中的三个国家名称词云，以绿色、蓝色和红色展示网络犯罪率 K-means 聚类结果。" width="1980" height="740" loading="lazy" decoding="async"></a><figcaption>K-means 国家聚类词云 · 原始建模报告图 10</figcaption></figure></div>      <div class="project-card-copy"><h3>网络犯罪指标与政策效果评估</h3><p class="timeline-meta">项目负责人 · 2025.01 – 2025.05</p><p>分析 110 个国家的犯罪、报案与起诉指标，结合 K-means、LSTM 反事实预测和多期双重差分，评估中国、德国与美国的政策效果。成果发表于 CIPAE 2025。</p><p class="project-contribution"><strong>个人分工:</strong> 我完成 K-means 聚类、相关分析与可视化，构建 LSTM–多期 DiD 实验流程，并开展数据清洗与敏感性分析。</p><div class="pub-links">
<a href="https://doi.org/10.1109/CIPAE66821.2025.00018">DOI</a></div></div>
    </article>
    <article class="timeline-card project-card project-card--illustrated" data-project="ozone">
<div class="project-card-media"><figure class="project-figure"><a href="/assets/research/ozone-regridding.png" aria-label="查看完整图片: 高分辨率臭氧降尺度预测"><img src="/assets/research/ozone-regridding.png" alt="原始报告图，比较 2020 年 1 月 1 日 GEOS-Chem 粗网格臭氧场与空间重网格后的臭氧场。" width="2155" height="955" loading="lazy" decoding="async"></a><figcaption>项目报告中的 GEOS-Chem 臭氧场与空间重网格示例（图 1）。</figcaption></figure></div>      <div class="project-card-copy"><h3>高分辨率臭氧降尺度预测</h3><p class="timeline-meta">项目负责人 · 导师：大连理工大学 Libin Jiao 教授 · 2025.10 – 2025.12</p><p>融合 GEOS-Chem、ERA5 与地面监测数据，统一到 0.01° × 0.01° 网格。比较树模型与神经网络，以交叉验证、模型置信集检验与 SHAP 分析评估性能及大气化学一致性。</p><p class="project-contribution"><strong>个人分工:</strong> 我负责多源数据预处理与空间插值、模型训练和调参、性能评估，以及 MCS 检验与 SHAP 分析的可视化。</p><div class="pub-links">
<a href="https://github.com/2369787465a-jpg/Ozone-Downscaling/blob/main/report.pdf">项目报告 PDF</a><a href="https://github.com/2369787465a-jpg/Ozone-Downscaling">代码</a></div></div>
    </article>
    <article class="timeline-card project-card" data-project="asset-pricing">
      <div class="project-card-copy"><h3>实证资产定价与股票 Beta 预测</h3><p class="timeline-meta">项目负责人 · 导师：大连理工大学 Shuai Qiao 教授 · 2025.07 – 2026.01</p><p>基于 CSMAR 数据，运用投资组合排序、Fama–MacBeth 回归、多因子风险调整与 Newey–West 推断研究中国 A 股 MAX 异象，并探索机器学习动态 Beta 预测。</p><p class="project-contribution"><strong>个人分工:</strong> 我复现投资组合排序与 Fama–MacBeth 回归，完成金融数据清洗，并整理机器学习 Beta 预测的滚动训练与评估流程。</p></div>
    </article>
  </details>
  <h3 class="subsection-heading">Kaggle 竞赛</h3>
  <div class="competition-grid">
<article class="timeline-card competition-card"><figure class="project-figure"><a href="/assets/competitions/birdclef-2026-official-header.jpg" aria-label="查看完整图片: BirdCLEF+ 2026 · 自然声景识别"><img src="/assets/competitions/birdclef-2026-official-header.jpg" alt="Kaggle 官方赛事配图：birdclef-2026" width="560" height="280" loading="lazy" decoding="async"></a><figcaption><a href="https://www.kaggle.com/competitions/birdclef-2026">官方赛事配图 · Kaggle</a></figcaption></figure><h3>BirdCLEF+ 2026 · 自然声景识别</h3><p class="timeline-meta">团队负责人 · 2026.04 – 2026.06</p><p>结合 EoS8、BirdNET 与 PCEN 的多标签音频集成，研究排序校正、分类学平滑与时序一致性。获 Kaggle 铜牌，前 8%（公榜 0.94221，私榜 0.95044）。最终排名：287 / 4,084。</p><div class="pub-links"><a href="https://www.kaggle.com/competitions/birdclef-2026">官方比赛页面</a></div><a class="evidence-link" href="/assets/evidence/birdclef-2026-bronze.jpg" aria-label="查看证明材料: BirdCLEF+ 2026 · 自然声景识别"><span>获奖证明</span></a></article><article class="timeline-card competition-card"><figure class="project-figure"><a href="/assets/competitions/march-machine-learning-mania-2026-official-header.jpg" aria-label="查看完整图片: March Machine Learning Mania 2026"><img src="/assets/competitions/march-machine-learning-mania-2026-official-header.jpg" alt="Kaggle 官方赛事配图：march-machine-learning-mania-2026" width="560" height="280" loading="lazy" decoding="async"></a><figcaption><a href="https://www.kaggle.com/competitions/march-machine-learning-mania-2026">官方赛事配图 · Kaggle</a></figcaption></figure><h3>March Machine Learning Mania 2026</h3><p class="timeline-meta">团队负责人 · 2026 年</p><p>参加 Kaggle 2026 年 NCAA 篮球锦标赛结果预测竞赛，获铜牌、前 7%；最终排名：240 / 3,462。</p><div class="pub-links"><a href="https://www.kaggle.com/competitions/march-machine-learning-mania-2026">官方比赛页面</a></div><a class="evidence-link" href="/assets/evidence/march-ml-mania-2026-bronze.jpg" aria-label="查看证明材料: March Machine Learning Mania 2026"><span>获奖证明</span></a></article>  </div>
</section>

<section aria-labelledby="publications-heading">
  <span class="anchor" id="publications"></span>
  <h2 id="publications-heading">学术论文</h2><p class="section-note">完整作者信息与当前稿件状态。</p>
<article class="timeline-card publication-card" id="paper-caadrl">
  <span class="badge">修回中</span>
  <h3>Cluster-Aware Attention-Based Deep Reinforcement Learning for Pickup and Delivery Problems</h3>
  <p class="publication-authors">Wentao Wang<sup>†</sup>, <strong>Lifeng Han</strong><sup>†</sup>, Guangyu Zou</p>
  <p class="publication-meta">Applied Intelligence<br>期刊稿件修回中；另有 arXiv 预印本。</p>
  <div class="pub-links">
<a href="https://github.com/2369787465a-jpg/CluPDTSP/blob/main/Clupdtsp_main.pdf">论文 PDF</a><a href="https://github.com/2369787465a-jpg/CluPDTSP">代码</a><a href="https://arxiv.org/abs/2603.10053">arXiv 预印本</a></div>
</article><article class="timeline-card publication-card" id="paper-mctrcm">
  <span class="badge">已录用</span>
  <h3>MC-TRCM: Observation-Aware Recursive Fusion for Incomplete Mobile and Wearable Mental-Health Feature Views</h3>
  <p class="publication-authors">Wentao Wang<sup>†</sup>, <strong>Lifeng Han</strong><sup>†</sup>, Zining Ren, Hengyu Zhong, Guangyu Zou</p>
  <p class="publication-meta">The 33rd International Conference on Neural Information Processing (ICONIP 2026)<br>已获 ICONIP 2026 录用。</p>
  <div class="pub-links">
<a href="https://github.com/2369787465a-jpg/MC-TRCM/blob/main/main.pdf">论文 PDF</a><a href="https://github.com/2369787465a-jpg/MC-TRCM">代码</a></div>
</article><article class="timeline-card publication-card" id="paper-did">
  <span class="badge">已发表</span>
  <h3>Multidimensional Metrics Analysis Based on K-Means Clustering and LSTM-Multi-Period DiD</h3>
  <p class="publication-authors"><strong>Lifeng Han</strong><sup>†</sup>, Zhihan Zhang<sup>†</sup>, Guanqi Wang<sup>†</sup></p>
  <p class="publication-meta">The 6th International Conference on Computers, Information Processing and Advanced Education (CIPAE 2025)<br>IEEE CPS · 2025 年 8 月 · 第 74–79 页</p>
  <div class="pub-links">
<a href="https://doi.org/10.1109/CIPAE66821.2025.00018">DOI</a></div>
</article>  <p class="section-note"><sup>†</sup> 标注作者为同等贡献。</p>
  <div class="section-actions"><a class="link-pill" href="/zh/publications/">全部论文</a></div>
</section>

<section aria-labelledby="education-heading">
  <span class="anchor" id="education"></span>
  <h2 id="education-heading">本科教育</h2>
<article class="timeline-card institution-card education-card"><header class="institution-card-heading"><div class="institution-card-text"><h3>莱斯特大学</h3><p class="timeline-meta">数学理学学士 · 2023.09 – 2027.06（预计）</p><p class="education-metrics">第一学年：90.62/100
第二学年：90.48/100
排名：4/99</p><p class="section-note">预计获得一等荣誉学位</p></div><div class="institution-logo"><img src="/assets/institutions/university-of-leicester.png" alt="莱斯特大学" width="522" height="158" loading="lazy" decoding="async"></div></header></article><article class="timeline-card institution-card education-card"><header class="institution-card-heading"><div class="institution-card-text"><h3>大连理工大学</h3><p class="timeline-meta">数理基础科学理学学士 · 2023.09 – 2027.06（预计）</p><p class="education-metrics">平均成绩：93.50/100
GPA：4.35/5.0</p><p class="section-note">与莱斯特大学合作办学项目</p></div><div class="institution-logo"><img src="/assets/institutions/dalian-university-of-technology.png" alt="大连理工大学" width="287" height="287" loading="lazy" decoding="async"></div></header></article></section>

<section aria-labelledby="experience-heading">
  <span class="anchor" id="experience"></span>
  <h2 id="experience-heading">补充学习经历</h2>
<article class="timeline-card institution-card"><header class="institution-card-heading"><div class="institution-card-text"><h3>新加坡国立大学 SCALE Youth Program</h3><p class="timeline-meta">短期交流项目 · 新加坡 · 2025.02.17–02.21</p></div><div class="institution-logo"><img src="/assets/institutions/national-university-of-singapore.png" alt="National University of Singapore" width="273" height="139" loading="lazy" decoding="async"></div></header><p>参加人工智能与机器学习交流课程，完成实践项目、案例学习、小组讨论与汇报。</p><a class="evidence-link" href="/assets/evidence/nus-ai-ml-completion-2025.jpg" aria-label="查看证明材料: 新加坡国立大学 SCALE Youth Program"><span>课程结业证明</span></a></article><article class="timeline-card institution-card"><header class="institution-card-heading"><div class="institution-card-text"><h3>数据分析课程 · MIT 教授授课</h3><p class="timeline-meta">ITSTP／Neoscholar · 在线课程 · 2024.03.08 – 05.26</p></div><div class="institution-logo"><img src="/assets/institutions/neoscholar.png" alt="Neoscholar Education" width="440" height="126" loading="lazy" decoding="async"></div></header><p>授课教师为麻省理工学院物理系 Gunther Roland 教授。完成 48 学时课程，学习 Python、数据可视化、多元分析与机器学习。考核成绩：92/100（A+）。</p><a class="evidence-link" href="/assets/evidence/itstp-data-analysis-92.png" aria-label="查看证明材料: 数据分析课程 · MIT 教授授课"><span>课程考核证明</span></a></article>  <details class="publication-collapse"><summary>学生工作</summary><p>莱斯特国际学院学生会：权益部副部长（2024.09 – 2025.06）；理论学习部成员（2023.09 – 2024.06）。</p></details>
</section>

<section aria-labelledby="honors-heading">
  <span class="anchor" id="honors"></span>
  <h2 id="honors-heading">荣誉与奖励</h2>
  <ul class="news-list awards-list"><li><span class="award-date">2026.09</span><div class="award-description">大连理工大学学习优秀一等奖学金 <span class="award-percent">(前 5%)</span></div><div class="award-evidence"><a class="evidence-link" href="/assets/evidence/academic-excellence-2026.jpg" aria-label="查看证明材料: 大连理工大学学习优秀一等奖学金"><span>审核记录</span></a></div></li><li><span class="award-date">2025.09</span><div class="award-description">大连理工大学学习优秀一等奖学金 <span class="award-percent">(前 5%)</span></div><div class="award-evidence"><a class="evidence-link" href="/assets/evidence/academic-excellence-2025.jpg" aria-label="查看证明材料: 大连理工大学学习优秀一等奖学金"><span>审核记录</span></a></div></li><li><span class="award-date">2025.01</span><div class="award-description">美国大学生数学建模竞赛（ICM）M 奖 <span class="award-percent">(前 6%)</span> <span class="award-role">负责人</span></div><div class="award-evidence"><a class="evidence-link" href="/assets/evidence/icm-meritorious-2025.jpg" aria-label="查看证明材料: 美国大学生数学建模竞赛（ICM）M 奖"><span>获奖证明</span></a></div></li><li><span class="award-date">2026.06</span><div class="award-description">Kaggle 铜牌 · BirdCLEF+ 2026 <span class="award-percent">(前 8%)</span> <span class="award-role">负责人</span></div><div class="award-evidence"><a class="evidence-link" href="/assets/evidence/birdclef-2026-bronze.jpg" aria-label="查看证明材料: Kaggle 铜牌 · BirdCLEF+ 2026"><span>获奖证明</span></a></div></li><li><span class="award-date">2026.04</span><div class="award-description">Kaggle 铜牌 · March Machine Learning Mania 2026 <span class="award-percent">(前 7%)</span> <span class="award-role">负责人</span></div><div class="award-evidence"><a class="evidence-link" href="/assets/evidence/march-ml-mania-2026-bronze.jpg" aria-label="查看证明材料: Kaggle 铜牌 · March Machine Learning Mania 2026"><span>获奖证明</span></a></div></li><li><span class="award-date">2025.01</span><div class="award-description">2024 年亚太地区大学生数学建模竞赛一等奖 <span class="award-percent">(前 5%)</span> <span class="award-role">负责人</span></div><div class="award-evidence"><a class="evidence-link" href="/assets/evidence/apmcm-first-prize-2024.jpg" aria-label="查看证明材料: 2024 年亚太地区大学生数学建模竞赛一等奖"><span>获奖证明</span></a></div></li></ul>
  <details class="publication-collapse awards-collapse"><summary>更多荣誉与奖励</summary><ul class="news-list awards-list"><li><span class="award-date">2025.09</span><div class="award-description">全国大学生数学建模竞赛三等奖 <span class="award-percent">(前 15%)</span> <span class="award-role">负责人</span></div><div class="award-evidence"><a class="evidence-link" href="/assets/evidence/cumcm-liaoning-third-prize-2025.jpg" aria-label="查看证明材料: 全国大学生数学建模竞赛三等奖"><span>获奖名单</span></a></div></li><li><span class="award-date">2026.09</span><div class="award-description">大连理工大学精神文明奖学金 <span class="award-percent">(前 10%)</span></div><div class="award-evidence"><a class="evidence-link" href="/assets/evidence/cultural-ethical-scholarship-2026.jpg" aria-label="查看证明材料: 大连理工大学精神文明奖学金"><span>审核记录</span></a></div></li><li><span class="award-date">2024.08</span><div class="award-description">全国大学生英语翻译能力竞赛一等奖 <span class="award-percent">(前 5%)</span></div><div class="award-evidence"><a class="evidence-link" href="/assets/evidence/english-translation-first-prize-2024.jpg" aria-label="查看证明材料: 全国大学生英语翻译能力竞赛一等奖"><span>获奖证明</span></a></div></li></ul></details>
</section>

<section aria-labelledby="skills-heading">
  <span class="anchor" id="skills"></span><h2 id="skills-heading">方法与工具</h2>
  <div class="chip-row"><span class="chip">C</span><span class="chip">C++</span><span class="chip">Java</span><span class="chip">Python</span><span class="chip">MATLAB</span><span class="chip">R</span><span class="chip">LaTeX</span></div>
  <p><strong>研究方法:</strong> 注意力与 Transformer · 深度强化学习 · 多视图学习 · 统计推断 · 计量经济学 · 时间序列 · 模型解释</p><p><strong>语言:</strong> 中文（母语） · 英语（熟练）</p>
</section>
<section class="early-programming" aria-labelledby="early-programming-heading">
  <h2 id="early-programming-heading">早期独立编程实践</h2>
  <p class="timeline-meta">Lua 脚本 · mini科技 · 始于 2020 年</p>
  <p>高一时，我开始通过mini科技中的 Lua 脚本深入接触编程，编辑地图并实现多种自定义游戏模式。这让我较早地将编程用于可以让他人实际体验的作品。</p>
  <dl class="early-programming-metrics"><div><dt>次下载</dt><dd>2,226,777</dd></div><div><dt>次游玩</dt><dd>2,595,700</dd></div></dl>
  <p class="section-note">截图所示创作者页面全部作品累计数据。</p>
  <a class="evidence-link" href="/assets/evidence/mini-world-creator-stats.png" aria-label="查看证明材料: 早期独立编程实践"><span>查看创作者页面截图</span></a>
</section>

<section class="contact-section" aria-labelledby="contact-heading">
  <span class="anchor" id="contact"></span><h2 id="contact-heading">联系</h2>
  <p>如需讨论研究、合作或学术相关事宜，欢迎通过邮件联系我。</p><p><a href="mailto:lh481@student.le.ac.uk">lh481@student.le.ac.uk</a> · <a href="https://github.com/2369787465a-jpg">GitHub</a></p><p class="section-note">完整简历与相关材料可按需私下提供。</p>
</section>

<footer class="homepage-footer">© 2026 韩立峰 · Lifeng Han · <a href="/" lang="en">English</a></footer>