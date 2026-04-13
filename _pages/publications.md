---
permalink: /publications/
title: "Projects & Achievements"
excerpt: ""
lang: en
lang_switch_label: "中文"
lang_switch_url: "/zh/publications/"
author_profile: true
author_bio: "B.Sc. student in Foundations of Mathematical Science at Dalian University of Technology"
sidebar_intro: "Selected research projects, accepted papers, and competition credentials from my current resume."
---

# Projects and Achievements

<p class="page-lead">This page collects selected research projects, accepted paper outputs, and competition credentials from my current resume.</p>

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

## Paper Output

{% for publication in publications %}
  {% if publication.section == 'paper' %}
    {% include publication-card.html publication=publication lang='en' variant='full' %}
  {% endif %}
{% endfor %}

## Competition and Credential Highlights

{% for publication in publications %}
  {% if publication.section == 'achievement' %}
    {% include publication-card.html publication=publication lang='en' variant='full' %}
  {% endif %}
{% endfor %}
