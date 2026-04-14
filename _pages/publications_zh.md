---
permalink: /zh/publications/
title: "简要背景"
excerpt: ""
lang: zh
lang_switch_label: "English"
lang_switch_url: "/publications/"
author_profile: true
author_name: "韩立峰"
author_bio: "大连理工大学数理基础科学专业本科生"
sidebar_intro: "这个公开页面只保留了非常简要的信息。"
---

# 简要背景

<p class="page-lead">这个页面刻意只保留有限的公开信息，不放置完整简历、证明材料或申请相关的详细内容。</p>

<div class="link-pills">
  <a class="link-pill" href="/zh/">返回主页</a>
  <a class="link-pill" href="mailto:lh481@student.le.ac.uk">邮箱</a>
  <a class="link-pill" href="https://github.com/2369787465a-jpg">GitHub</a>
</div>

<p class="section-note">{{ site.data.publications.quartile_note.zh }}</p>

{% assign publications = site.data.publications.items %}

{% for publication in publications %}
  {% include publication-card.html publication=publication lang='zh' variant='full' %}
{% endfor %}
