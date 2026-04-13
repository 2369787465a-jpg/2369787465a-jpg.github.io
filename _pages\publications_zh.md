---
permalink: /zh/publications/
title: "项目与成果"
excerpt: ""
lang: zh
lang_switch_label: "English"
lang_switch_url: "/publications/"
author_profile: true
author_name: "韩立峰"
author_bio: "大连理工大学数理基础科学专业本科生"
sidebar_intro: "这里汇总了我当前简历中的代表性项目、论文成果与竞赛证明。"
---

# 项目与成果

<p class="page-lead">本页汇总了我当前简历中的代表性科研项目、正式论文成果以及竞赛与认证记录。</p>

<div class="link-pills">
  <a class="link-pill" href="/zh/">返回主页</a>
  <a class="link-pill" href="/files/resume/lifeng-han-resume.pdf">PDF 简历</a>
  <a class="link-pill" href="mailto:lh481@student.le.ac.uk">邮箱</a>
</div>

<p class="section-note">{{ site.data.publications.quartile_note.zh }}</p>

{% assign publications = site.data.publications.items %}

## 科研项目

{% for publication in publications %}
  {% if publication.section == 'research' %}
    {% include publication-card.html publication=publication lang='zh' variant='full' %}
  {% endif %}
{% endfor %}

## 论文成果

{% for publication in publications %}
  {% if publication.section == 'paper' %}
    {% include publication-card.html publication=publication lang='zh' variant='full' %}
  {% endif %}
{% endfor %}

## 竞赛与证明

{% for publication in publications %}
  {% if publication.section == 'achievement' %}
    {% include publication-card.html publication=publication lang='zh' variant='full' %}
  {% endif %}
{% endfor %}
