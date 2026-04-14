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
sidebar_intro: "我是一名本科生，主要兴趣包括优化、强化学习和应用数据分析。"
---

<span class='anchor' id='about'></span>

<div class="homepage-hero">
  <p class="section-kicker">学术简历</p>
  <h1>韩立峰</h1>
  <p>我目前就读于大连理工大学数理基础科学专业。本科阶段的学习和实践主要围绕优化、强化学习、数学建模和应用机器学习展开。</p>
  <p>这个页面主要保留了几段和硕士申请相关的项目、竞赛和课程实践经历。</p>
  <div class="link-pills">
    <a class="link-pill" href="mailto:lh481@student.le.ac.uk">邮箱</a>
    <a class="link-pill" href="/files/resume/lifeng-han-resume.pdf">PDF 简历</a>
    <a class="link-pill" href="https://github.com/2369787465a-jpg">GitHub</a>
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
    <h3>兴趣方向</h3>
    <p>优化与强化学习</p>
    <p>数学建模与数据分析</p>
    <p>应用机器学习</p>
  </div>
  <div class="highlight-card">
    <h3>主要经历</h3>
    <p>路径优化相关科研项目</p>
    <p>数学建模竞赛经历</p>
    <p>银行与统计相关实习</p>
  </div>
  <div class="highlight-card">
    <h3>保留亮点</h3>
    <p>CIPAE 2025 录用论文</p>
    <p>一篇在审稿件</p>
    <p>Kaggle 铜牌与建模竞赛奖项</p>
  </div>
</div>

<span class='anchor' id='research'></span>

## 研究方向

<div class="chip-row">
  <span class="chip">优化</span>
  <span class="chip">强化学习</span>
  <span class="chip">数学建模</span>
  <span class="chip">应用机器学习</span>
  <span class="chip">数据分析</span>
</div>

我目前比较感兴趣的是把数学和计算方法用于结构化决策问题。本科阶段的大部分经验也主要来自课程、科研训练和竞赛实践。

<span class='anchor' id='projects'></span>

{% assign publications = site.data.publications.items %}
{% assign publication_limit = site.data.publications.home_limit | default: 4 %}

## 部分项目

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
  <a class="link-pill" href="/zh/publications/">查看更多</a>
</div>

<span class='anchor' id='competitions'></span>

## 竞赛经历

<div class="timeline-card">
  <h3>March Machine Learning Mania 2026</h3>
  <p class="timeline-meta">Kaggle 铜牌 | 2026 年 4 月 8 日获奖 | 3462 支队伍中排名 240</p>
  <p>以 <strong>hlf111</strong> 的用户名参赛并获得铜牌，这是一次比较直接的机器学习竞赛实践经历。</p>
</div>

<div class="timeline-card">
  <h3>ICM 2025 Problem F: Cyber Strong?</h3>
  <p class="timeline-meta">队长 | 2025 年 1 月至 2 月 | Meritorious Winner（前 6%）</p>
  <p>围绕网络安全政策分析完成了一次团队建模项目，包含数据整理、建模和结果分析。</p>
</div>

<div class="timeline-card">
  <h3>全国大学生数学建模竞赛</h3>
  <p class="timeline-meta">队长 | 2025 年 9 月 | 省三等奖（前 25%）</p>
  <p>围绕临床数据完成了一次结合统计分析和机器学习方法的建模项目。</p>
</div>

<div class="timeline-card">
  <h3>APMCM 2024 Problem C</h3>
  <p class="timeline-meta">队长 | 2024 年 11 月 | 一等奖（前 5%）</p>
  <p>完成了一次以预测、仿真和优化为主的数学建模项目。</p>
</div>

<span class='anchor' id='experience'></span>

## 科研与实习经历

<div class="timeline-card">
  <h3>省级大学生创新创业训练计划</h3>
  <p class="timeline-meta">项目负责人 | 2025 年 9 月至今</p>
  <p>一个围绕旅行商问题强化学习方法展开的本科项目。</p>
</div>

<div class="timeline-card">
  <h3>基于深度强化学习的聚类感知车辆路径优化研究</h3>
  <p class="timeline-meta">第一作者 | 2023 年 9 月至今</p>
  <p>一个结合仿真数据和强化学习的路径优化研究项目，目前有一篇相关稿件在审。</p>
</div>

<div class="timeline-card">
  <h3>大湾区高分辨率臭氧降尺度的物理一致性机器学习框架</h3>
  <p class="timeline-meta">共同第一作者 | 2025 年 11 月至 12 月</p>
  <p>一个使用环境与气象数据进行臭氧预测的短期项目。</p>
</div>

<div class="timeline-card">
  <h3>中国建设银行漳州分行</h3>
  <p class="timeline-meta">业务部实习生 | 2024 年 7 月至 8 月</p>
  <p>参与业务部的日常辅助工作、数据整理和周报制作。</p>
</div>

<div class="timeline-card">
  <h3>芗城区政府统计局</h3>
  <p class="timeline-meta">实习生 | 2024 年 1 月至 2 月</p>
  <p>参与经济普查期间的数据整理与核查工作。</p>
</div>

<span class='anchor' id='education'></span>

## 教育背景

<div class="timeline-card">
  <h3>大连理工大学</h3>
  <p class="timeline-meta">数理基础科学专业本科 | 2023 年 9 月至 2027 年 6 月 | 大连</p>
  <p>GPA：92.5/100 | 学业优秀一等奖学金（前 5%）</p>
  <p><strong>主要课程：</strong>数学分析、高等代数、概率论、数理统计、数值分析、数据结构、Python、R。</p>
  <p><strong>英语能力：</strong>IELTS 6.0。</p>
</div>

## 交流项目

<div class="timeline-card">
  <h3>新加坡国立大学 NUS SCALE Youth Program</h3>
  <p class="timeline-meta">Artificial Intelligence and Machine Learning | 2025 年 2 月</p>
  <p>参加过一次与人工智能和机器学习相关的短期交流项目。</p>
</div>

<div class="timeline-card">
  <h3>麻省理工学院 Top Innovative Talent Program</h3>
  <p class="timeline-meta">Scientific Data Analysis and Machine Learning Applications | 2024 年 3 月至 6 月</p>
  <p>完成科学数据分析与机器学习应用相关课程和项目实践。</p>
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
- **2025 年：** CIPAE 2025 录用论文
- **进行中：** 一篇在审稿件

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
      <li>页面只保留了一张公开证书，没有放完整成绩单图片。</li>
    </ul>
    <div class="pub-links">
      <a href="/images/highlights/kaggle-bronze-2026.png">查看证书</a>
      <a href="/files/resume/lifeng-han-resume.pdf">下载简历</a>
    </div>
  </div>
</div>
