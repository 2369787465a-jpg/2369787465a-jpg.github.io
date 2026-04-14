---
permalink: /publications/
title: "Projects & Achievements"
excerpt: ""
lang: en
lang_switch_label: "中文"
lang_switch_url: "/zh/publications/"
author_profile: true
author_bio: "B.Sc. student in Foundations of Mathematical Science at Dalian University of Technology"
sidebar_intro: "A short selection of projects and competition experiences from my undergraduate work."
---

# Selected Projects

<p class="page-lead">This page keeps a concise record of several projects, papers, and competition experiences from my undergraduate stage.</p>

<div class="link-pills">
  <a class="link-pill" href="/">Back to Homepage</a>
  <a class="link-pill" href="/files/resume/lifeng-han-resume.pdf">Resume PDF</a>
  <a class="link-pill" href="mailto:lh481@student.le.ac.uk">Email</a>
</div>

<p class="section-note">{{ site.data.publications.quartile_note.en }}</p>

{% assign publications = site.data.publications.items %}

## Research Projects

{% for publication in publications %}
  {% if publication.section == 'research' %}
    {% include publication-card.html publication=publication lang='en' variant='full' %}
  {% endif %}
{% endfor %}

## Papers

{% for publication in publications %}
  {% if publication.section == 'paper' %}
    {% include publication-card.html publication=publication lang='en' variant='full' %}
  {% endif %}
{% endfor %}

## Competitions

{% for publication in publications %}
  {% if publication.section == 'achievement' %}
    {% include publication-card.html publication=publication lang='en' variant='full' %}
  {% endif %}
{% endfor %}
