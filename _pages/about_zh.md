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
sidebar_intro: "我是一名本科生，主要兴趣包括优化、强化学习和应用机器学习。"
---

<span class='anchor' id='about'></span>

<div class="homepage-hero">
  <p class="section-kicker">公开主页</p>
  <h1>韩立峰</h1>
  <p>我目前就读于大连理工大学数理基础科学专业，主要兴趣包括优化、强化学习、数学建模以及应用机器学习。</p>
  <p>这个公开页面只保留非常简要的背景信息，不放置完整简历、证明材料或申请相关的详细内容。</p>
  <div class="link-pills">
    <a class="link-pill" href="mailto:lh481@student.le.ac.uk">邮箱</a>
    <a class="link-pill" href="https://github.com/2369787465a-jpg">GitHub</a>
    <a class="link-pill" href="/zh/publications/">简要背景</a>
  </div>
</div>

<div class="highlight-grid">
  <div class="highlight-card">
    <h3>教育背景</h3>
    <p>大连理工大学</p>
    <p>数理基础科学专业本科</p>
    <p>预计毕业时间：2027 年 6 月</p>
  </div>
  <div class="highlight-card">
    <h3>兴趣方向</h3>
    <p>优化与强化学习</p>
    <p>数学建模</p>
    <p>应用机器学习与数据分析</p>
  </div>
  <div class="highlight-card">
    <h3>背景概况</h3>
    <p>课程与项目实践</p>
    <p>团队型学习活动</p>
    <p>短期项目与交流</p>
  </div>
  <div class="highlight-card">
    <h3>公开说明</h3>
    <p>这个页面刻意保持简短。</p>
    <p>更详细的材料仅在需要时私下提供。</p>
  </div>
</div>

<span class='anchor' id='research'></span>

## 兴趣方向

<div class="chip-row">
  <span class="chip">优化</span>
  <span class="chip">强化学习</span>
  <span class="chip">数学建模</span>
  <span class="chip">应用机器学习</span>
  <span class="chip">数据分析</span>
</div>

我本科阶段的主要经验来自课程学习、项目实践和团队活动，因此公开页面只保留了比较概括的信息。

<span class='anchor' id='projects'></span>

{% assign publications = site.data.publications.items %}
{% assign publication_limit = site.data.publications.home_limit | default: 3 %}

## 公开概览

<p class="section-note">{{ site.data.publications.quartile_note.zh }}</p>

{% for publication in publications limit:publication_limit %}
  {% include publication-card.html publication=publication lang='zh' variant='home' %}
{% endfor %}

<div class="section-actions">
  <a class="link-pill" href="/zh/publications/">查看简要背景</a>
</div>

<span class='anchor' id='experience'></span>

## 背景概况

<div class="timeline-card">
  <h3>课程与项目</h3>
  <p class="timeline-meta">以学习和项目为主的实践经历</p>
  <p>本科阶段接触过一些与优化、建模和机器学习相关的定量与计算问题，公开页面不展开更细内容。</p>
</div>

<div class="timeline-card">
  <h3>团队活动</h3>
  <p class="timeline-meta">围绕分析与问题求解的协作经历</p>
  <p>也参与过一些以团队协作、定量分析和应用问题求解为主的活动。</p>
</div>

<div class="timeline-card">
  <h3>短期项目与交流</h3>
  <p class="timeline-meta">短期学术或实践接触</p>
  <p>此外也有一些短期项目与交流经历，用来补充实践视角和跨方向体验。</p>
</div>

<span class='anchor' id='education'></span>

## 教育背景

<div class="timeline-card">
  <h3>大连理工大学</h3>
  <p class="timeline-meta">数理基础科学专业本科 | 2023 年 9 月至 2027 年 6 月（预计）</p>
  <p>公开页面说明：这里不展示详细成绩、证明材料或完整简历。</p>
</div>

## 技术技能

<div class="chip-row">
  <span class="chip">Python</span>
  <span class="chip">R</span>
  <span class="chip">MATLAB</span>
  <span class="chip">C/C++</span>
  <span class="chip">Java</span>
  <span class="chip">PyTorch</span>
  <span class="chip">XGBoost</span>
  <span class="chip">LaTeX</span>
</div>

<span class='anchor' id='honors'></span>

## 联系方式

如果申请或正式审核需要更完整的背景材料，可以通过邮件联系我。
