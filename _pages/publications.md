---
permalink: /publications/
title: "Brief Profile"
excerpt: ""
lang: en
lang_switch_label: "中文"
lang_switch_url: "/zh/publications/"
author_profile: true
author_bio: "B.Sc. student in Foundations of Mathematical Science at Dalian University of Technology"
sidebar_intro: "This public page keeps only a brief overview."
---

# Brief Profile

<p class="page-lead">This page intentionally keeps only limited public information. Detailed CV materials, supporting documents, and application-specific content are not posted online.</p>

<div class="link-pills">
  <a class="link-pill" href="/">Back to Homepage</a>
  <a class="link-pill" href="mailto:lh481@student.le.ac.uk">Email</a>
  <a class="link-pill" href="https://github.com/2369787465a-jpg">GitHub</a>
</div>

<p class="section-note">{{ site.data.publications.quartile_note.en }}</p>

{% assign publications = site.data.publications.items %}

{% for publication in publications %}
  {% include publication-card.html publication=publication lang='en' variant='full' %}
{% endfor %}
