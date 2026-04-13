---
permalink: /zh/
title: ""
excerpt: ""
lang: zh
lang_switch_label: "English"
lang_switch_url: "/"
author_profile: true
author_name: "韩立峰"
author_bio: "大连理工大学数理基础科学专业本科生"
sidebar_intro: "我的兴趣集中在强化学习、组合优化、数据分析与面向真实决策问题的机器学习。"
---

<span class='anchor' id='about'></span>

<div class="homepage-hero">
  <p class="section-kicker">学术简历</p>
  <h1>韩立峰</h1>
  <p>我目前就读于大连理工大学数理基础科学专业，本科阶段的主要工作集中在旅行商与车辆路径问题上的深度强化学习、面向真实决策的数据分析建模，以及面向环境预测的物理一致性机器学习。</p>
  <p>我喜欢把复杂、零散的问题整理成可计算的模型，再通过实验、写作和竞赛把结论讲清楚。未来也希望继续在“优化 + 机器学习 + 实际应用”交叉方向深入发展。</p>
  <div class="link-pills">
    <a class="link-pill" href="mailto:lh481@student.le.ac.uk">邮箱</a>
    <a class="link-pill" href="/files/resume/lifeng-han-resume.pdf">PDF 简历</a>
    <a class="link-pill" href="/zh/publications/">项目与成果</a>
    <a class="link-pill" href="/zh/#competitions">竞赛亮点</a>
  </div>
</div>

<div class="highlight-grid">
  <div class="highlight-card">
    <h3>教育背景</h3>
    <p>大连理工大学</p>
    <p>数理基础科学专业本科，2023 年 9 月至 2027 年 6 月</p>
    <p>GPA 92.5/100，学业优秀一等奖学金（前 5%）</p>
  </div>
  <div class="highlight-card">
    <h3>研究方向</h3>
    <p>旅行商与车辆路径问题上的深度强化学习</p>
    <p>面向真实决策的数据分析与预测建模</p>
    <p>高分辨率臭氧降尺度的物理一致性机器学习</p>
  </div>
  <div class="highlight-card">
    <h3>竞赛成绩</h3>
    <p>Kaggle March Machine Learning Mania 2026 铜牌</p>
    <p>2025 美赛 Meritorious Winner（前 6%）</p>
    <p>2024 亚太赛一等奖（前 5%）</p>
  </div>
  <div class="highlight-card">
    <h3>代表成果</h3>
    <p>CIPAE 2025 录用论文共同一作兼通讯作者</p>
    <p>聚类感知路径优化方向 SCI Q2 一作在审稿件</p>
    <p>省级大学生创新创业训练计划项目负责人</p>
  </div>
</div>

<span class='anchor' id='research'></span>

## 研究方向

<div class="chip-row">
  <span class="chip">强化学习</span>
  <span class="chip">神经组合优化</span>
  <span class="chip">车辆路径规划</span>
  <span class="chip">旅行商问题</span>
  <span class="chip">应用机器学习</span>
  <span class="chip">环境数据科学</span>
  <span class="chip">优化建模</span>
  <span class="chip">统计建模</span>
</div>

我目前的工作把数学建模、机器学习与实证分析结合在一起。我尤其喜欢那些结构明确、但求解并不简单的问题，例如路径优化、调度、时空预测等，也同样关注模型性能、可解释性与实际价值之间的平衡。

<span class='anchor' id='projects'></span>

{% assign publications = site.data.publications.items %}
{% assign publication_limit = site.data.publications.home_limit | default: 4 %}

## 代表项目与成果

<p class="section-note">{{ site.data.publications.quartile_note.zh }}</p>

{% if publications.size > publication_limit %}
  {% for publication in publications limit:publication_limit %}
    {% include publication-card.html publication=publication lang='zh' variant='home' %}
  {% endfor %}
{% else %}
  {% for publication in publications %}
    {% include publication-card.html publication=publication lang='zh' variant='home' %}
  {% endfor %}
{% endif %}

<div class="section-actions">
  <a class="link-pill" href="/zh/publications/">查看全部项目与成果</a>
</div>

<span class='anchor' id='competitions'></span>

## 竞赛经历

<div class="timeline-card">
  <h3>March Machine Learning Mania 2026</h3>
  <p class="timeline-meta">Kaggle 铜牌 | 2026 年 4 月 8 日获奖 | 3462 支队伍中排名 240</p>
  <p>以 <strong>hlf111</strong> 的用户名参赛并获得铜牌，这项成绩说明我能够在真实竞赛环境中快速迭代方案、根据反馈修正模型，并把建模直觉落实成稳定成绩。</p>
</div>

<div class="timeline-card">
  <h3>ICM 2025 Problem F: Cyber Strong?</h3>
  <p class="timeline-meta">队长 | 2025 年 1 月至 2 月 | Meritorious Winner（前 6%）</p>
  <p>围绕 113 个国家的网络安全策略展开研究，构建 LSTM 与多期 DID 联合框架，完成多源数据整合、风险聚类、政策效果评估与敏感性分析。</p>
</div>

<div class="timeline-card">
  <h3>全国大学生数学建模竞赛</h3>
  <p class="timeline-meta">队长 | 2025 年 9 月 | 省三等奖（前 25%）</p>
  <p>处理 1082 条孕产妇临床记录，通过统计检验识别关键因素，并构建线性混合模型、Weibull AFT 模型与两阶段 XGBoost 分类器。</p>
</div>

<div class="timeline-card">
  <h3>APMCM 2024 Problem C</h3>
  <p class="timeline-meta">队长 | 2024 年 11 月 | 一等奖（前 5%）</p>
  <p>围绕全球宠物产业构建相关性分析、时间序列预测、微分方程建模与蒙特卡洛仿真流程，综合使用 ARIMA、灰色预测、粒子群优化与 MATLAB ODE 求解器。</p>
</div>

<span class='anchor' id='experience'></span>

## 科研与实习经历

<div class="timeline-card">
  <h3>省级大学生创新创业训练计划</h3>
  <p class="timeline-meta">项目负责人 | 2025 年 9 月至今</p>
  <p>围绕旅行商问题改进深度强化学习求解器，当前方案融合 DACT 风格编码器、合成注意力、可行性掩码以及 2-opt/3-opt 混合动作解码，并通过 PPO 与课程学习提升训练效率与泛化表现。</p>
</div>

<div class="timeline-card">
  <h3>基于深度强化学习的聚类感知车辆路径优化研究</h3>
  <p class="timeline-meta">第一作者 | 2023 年 9 月至今</p>
  <p>该项目聚焦带聚类结构的路径优化问题，从 MDP 建模、仿真数据构造、双编码器 Transformer、动态双解码器到端到端 PyTorch 训练均由我主导完成，相关稿件目前处于 SCI Q2 在审状态。</p>
</div>

<div class="timeline-card">
  <h3>大湾区高分辨率臭氧降尺度的物理一致性机器学习框架</h3>
  <p class="timeline-meta">共同第一作者 | 2025 年 11 月至 12 月</p>
  <p>整合 GEOS-Chem 输出、ERA5 气象数据与地面观测数据，比较 Random Forest、MLP、XGBoost 等模型，并通过 SHAP 分析验证结果与大气光化学机理的一致性。</p>
</div>

<div class="timeline-card">
  <h3>中国建设银行漳州分行</h3>
  <p class="timeline-meta">业务部实习生 | 2024 年 7 月至 8 月</p>
  <p>协助对公业务办理、客户信息核验、初步贷款资料审查和周报制作，并参与整理企业信息与行业数据，支持完成地方电子产业研究报告。</p>
</div>

<div class="timeline-card">
  <h3>芗城区政府统计局</h3>
  <p class="timeline-meta">实习生 | 2024 年 1 月至 2 月</p>
  <p>参与第五次全国经济普查相关工作，负责辖区企业与中小微企业信息整理、外出核查、数据比对和异常筛查等任务。</p>
</div>

<span class='anchor' id='education'></span>

## 教育背景

<div class="timeline-card">
  <h3>大连理工大学</h3>
  <p class="timeline-meta">数理基础科学专业本科 | 2023 年 9 月至 2027 年 6 月 | 大连</p>
  <p>GPA：92.5/100 | 学业优秀一等奖学金（前 5%）</p>
  <p><strong>主要课程：</strong>数学分析、高等代数、概率论、数理统计、数值分析、数据结构、C 语言程序设计、Java、Python、R、SPSS、Stata。</p>
  <p><strong>英语能力：</strong>IELTS 6.0；全国大学生英语周报翻译大赛国家一等奖。</p>
</div>

## 交流项目

<div class="timeline-card">
  <h3>新加坡国立大学 NUS SCALE Youth Program</h3>
  <p class="timeline-meta">Artificial Intelligence and Machine Learning | 2025 年 2 月</p>
  <p>完成与人工智能和机器学习相关的课程项目与案例实践，并与不同背景的学员合作完成讨论与展示。</p>
</div>

<div class="timeline-card">
  <h3>麻省理工学院 Top Innovative Talent Program</h3>
  <p class="timeline-meta">Scientific Data Analysis and Machine Learning Applications | 2024 年 3 月至 6 月</p>
  <p>完成科学数据分析与机器学习应用课程及项目实践，课程成绩 92/100。</p>
</div>

## 技术技能

<div class="chip-row">
  <span class="chip">Python</span>
  <span class="chip">R</span>
  <span class="chip">MATLAB</span>
  <span class="chip">C</span>
  <span class="chip">C++</span>
  <span class="chip">Java</span>
  <span class="chip">LaTeX</span>
  <span class="chip">PyTorch</span>
  <span class="chip">XGBoost</span>
  <span class="chip">MS Excel</span>
  <span class="chip">SPSS</span>
  <span class="chip">Stata</span>
  <span class="chip">MS Office</span>
  <span class="chip">深度强化学习</span>
</div>

<span class='anchor' id='honors'></span>

## 荣誉奖项

- **2026 年 4 月 8 日：** Kaggle March Machine Learning Mania 2026 铜牌，3462 支队伍中排名 240
- **2025 年：** 大连理工大学学业优秀一等奖学金（前 5%）
- **2025 年：** ICM Problem F Meritorious Winner（前 6%）
- **2025 年：** 全国大学生数学建模竞赛省三等奖
- **2024 年：** APMCM 2024 一等奖（前 5%）
- **2025 年：** CIPAE 2025 录用论文共同第一作者兼通讯作者
- **进行中：** 聚类感知路径优化方向 SCI Q2 一作稿件在审

## 代表性证明

<div class="paper-box">
  <div class='paper-box-image'>
    <div>
      <div class="badge">Kaggle | 铜牌</div>
      <img src="/images/highlights/kaggle-bronze-2026.png" alt="Kaggle March Machine Learning Mania 2026 证书" width="100%">
    </div>
  </div>
  <div class='paper-box-text'>
    <h3>Kaggle March Machine Learning Mania 2026</h3>
    <p class="publication-meta">获奖日期：2026 年 4 月 8 日 | 用户名：hlf111</p>
    <ul>
      <li>在 3462 支参赛队伍中排名第 240，获得铜牌。</li>
      <li>这项成绩为我的科研与建模背景补充了公开、可验证的实战证明。</li>
      <li>网站默认不公开完整成绩单图片，因为其中包含学号等敏感个人信息。</li>
    </ul>
    <div class="pub-links">
      <a href="/images/highlights/kaggle-bronze-2026.png">查看证书</a>
      <a href="/files/resume/lifeng-han-resume.pdf">下载简历</a>
    </div>
  </div>
</div>
