---
permalink: /
title: ""
excerpt: ""
lang: en
lang_switch_label: "中文"
lang_switch_url: "/zh/"
author_profile: true
author_bio: "B.Sc. student in Foundations of Mathematical Science at Dalian University of Technology"
sidebar_intro: "I am an undergraduate student interested in optimization, reinforcement learning, and applied machine learning."
redirect_from:
  - /about/
  - /about.html
---

<span class='anchor' id='about'></span>

<div class="homepage-hero">
  <p class="section-kicker">Public Profile</p>
  <h1>Lifeng Han</h1>
  <p>I am a B.Sc. student in Foundations of Mathematical Science at Dalian University of Technology. My interests mainly include optimization, reinforcement learning, mathematical modeling, and applied machine learning.</p>
  <p>This public page only keeps a brief overview. Detailed CV materials, supporting documents, and application-specific information are not posted online.</p>
  <div class="link-pills">
    <a class="link-pill" href="mailto:lh481@student.le.ac.uk">Email</a>
    <a class="link-pill" href="https://github.com/2369787465a-jpg">GitHub</a>
    <a class="link-pill" href="/publications/">Brief Background</a>
  </div>
</div>

<div class="highlight-grid">
  <div class="highlight-card">
    <h3>Education</h3>
    <p>Dalian University of Technology</p>
    <p>B.Sc. in Foundations of Mathematical Science</p>
    <p>Expected graduation: Jun. 2027</p>
  </div>
  <div class="highlight-card">
    <h3>Interests</h3>
    <p>Optimization and reinforcement learning</p>
    <p>Mathematical modeling</p>
    <p>Applied machine learning and data analysis</p>
  </div>
  <div class="highlight-card">
    <h3>Background</h3>
    <p>Coursework and project practice</p>
    <p>Team-based academic activities</p>
    <p>Short programs and exchanges</p>
  </div>
  <div class="highlight-card">
    <h3>Public Note</h3>
    <p>This page is intentionally concise.</p>
    <p>Detailed CV materials are shared privately when needed.</p>
  </div>
</div>

<span class='anchor' id='research'></span>

## Interests

<div class="chip-row">
  <span class="chip">Optimization</span>
  <span class="chip">Reinforcement Learning</span>
  <span class="chip">Mathematical Modeling</span>
  <span class="chip">Applied Machine Learning</span>
  <span class="chip">Data Analysis</span>
</div>

My undergraduate experience has mainly come from coursework, project-based practice, and team activities. I keep the public version of this page intentionally brief.

<span class='anchor' id='projects'></span>

{% assign publications = site.data.publications.items %}
{% assign publication_limit = site.data.publications.home_limit | default: 3 %}

## Public Overview

<p class="section-note">{{ site.data.publications.quartile_note.en }}</p>

{% for publication in publications limit:publication_limit %}
  {% include publication-card.html publication=publication lang='en' variant='home' %}
{% endfor %}

<div class="section-actions">
  <a class="link-pill" href="/publications/">View Brief Background</a>
</div>

<span class='anchor' id='experience'></span>

## Background

<div class="timeline-card">
  <h3>Coursework and Projects</h3>
  <p class="timeline-meta">Study-based and project-based practice</p>
  <p>I have worked on several quantitative and computational topics during undergraduate study, especially in optimization, modeling, and machine learning related areas.</p>
</div>

<div class="timeline-card">
  <h3>Team Activities</h3>
  <p class="timeline-meta">Collaborative analysis and problem solving</p>
  <p>My background also includes collaborative activities that involved quantitative analysis, modeling, and applied problem solving.</p>
</div>

<div class="timeline-card">
  <h3>Programs and Exchanges</h3>
  <p class="timeline-meta">Short-term academic and practical exposure</p>
  <p>I have also joined short academic or practical programs that helped broaden my perspective and interdisciplinary experience.</p>
</div>

<span class='anchor' id='education'></span>

## Education

<div class="timeline-card">
  <h3>Dalian University of Technology</h3>
  <p class="timeline-meta">B.Sc. in Foundations of Mathematical Science | Sep. 2023 - Jun. 2027 (expected)</p>
  <p>Public page note: detailed grades, supporting documents, and a full CV are not posted here.</p>
</div>

## Technical Skills

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

## Contact

If a fuller profile, CV, or supporting materials are needed for academic applications, please contact me by email.
