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
sidebar_intro: "这里保留了一部分和申请相关的本科项目、论文与竞赛经历。"
---

# 项目简述

<p class="page-lead">这里简单记录了几段本科阶段和申请相关的项目、论文与竞赛经历。</p>

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

## 论文

{% for publication in publications %}
  {% if publication.section == 'paper' %}
    {% include publication-card.html publication=publication lang='zh' variant='full' %}
  {% endif %}
{% endfor %}

## 竞赛

{% for publication in publications %}
  {% if publication.section == 'achievement' %}
    {% include publication-card.html publication=publication lang='zh' variant='full' %}
  {% endif %}
{% endfor %}
