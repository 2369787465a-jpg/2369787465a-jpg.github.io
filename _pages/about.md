---
permalink: /
title: ""
excerpt: ""
lang: en
lang_switch_label: "中文"
lang_switch_url: "/zh/"
author_profile: true
author_bio: "B.Sc. student in Foundations of Mathematical Science at Dalian University of Technology"
sidebar_intro: "I am an undergraduate student interested in optimization, reinforcement learning, and applied data analysis."
redirect_from:
  - /about/
  - /about.html
---

<span class='anchor' id='about'></span>

<div class="homepage-hero">
  <p class="section-kicker">Academic Resume</p>
  <h1>Lifeng Han</h1>
  <p>I am a B.Sc. student in Foundations of Mathematical Science at Dalian University of Technology. My undergraduate work has mainly involved optimization, reinforcement learning, mathematical modeling, and applied machine learning.</p>
  <p>I built this page as a short record of several projects and competition experiences that may be relevant for master's applications.</p>
  <div class="link-pills">
    <a class="link-pill" href="mailto:lh481@student.le.ac.uk">Email</a>
    <a class="link-pill" href="/files/resume/lifeng-han-resume.pdf">Resume PDF</a>
    <a class="link-pill" href="https://github.com/2369787465a-jpg">GitHub</a>
    <a class="link-pill" href="/publications/">Projects & Achievements</a>
    <a class="link-pill" href="/#competitions">Competition Highlights</a>
  </div>
</div>

<div class="highlight-grid">
  <div class="highlight-card">
    <h3>Education</h3>
    <p>Dalian University of Technology</p>
    <p>B.Sc. in Foundations of Mathematical Science, Sep. 2023 - Jun. 2027</p>
    <p>GPA 92.5/100, First-class Academic Scholarship (Top 5%)</p>
  </div>
  <div class="highlight-card">
    <h3>Interests</h3>
    <p>Optimization and reinforcement learning</p>
    <p>Mathematical modeling and data analysis</p>
    <p>Applied machine learning</p>
  </div>
  <div class="highlight-card">
    <h3>Selected Experience</h3>
    <p>Routing and optimization research projects</p>
    <p>Mathematical modeling competitions</p>
    <p>Short internships in banking and statistics</p>
  </div>
  <div class="highlight-card">
    <h3>Highlights</h3>
    <p>CIPAE 2025 accepted paper</p>
    <p>One manuscript under review</p>
    <p>Kaggle bronze medal and modeling awards</p>
  </div>
</div>

<span class='anchor' id='research'></span>

## Research Interests

<div class="chip-row">
  <span class="chip">Optimization</span>
  <span class="chip">Reinforcement Learning</span>
  <span class="chip">Mathematical Modeling</span>
  <span class="chip">Applied Machine Learning</span>
  <span class="chip">Data Analysis</span>
</div>

My main interest is applying mathematical and computational methods to structured decision problems. So far, most of my experience has come from course-related work, undergraduate research, and competitions.

<span class='anchor' id='projects'></span>

{% assign publications = site.data.publications.items %}
{% assign publication_limit = site.data.publications.home_limit | default: 4 %}

## Selected Projects

<p class="section-note">{{ site.data.publications.quartile_note.en }}</p>

{% if publications.size > publication_limit %}
  {% for publication in publications limit:publication_limit %}
    {% include publication-card.html publication=publication lang='en' variant='home' %}
  {% endfor %}
{% else %}
  {% for publication in publications %}
    {% include publication-card.html publication=publication lang='en' variant='home' %}
  {% endfor %}
{% endif %}

<div class="section-actions">
  <a class="link-pill" href="/publications/">View More</a>
</div>

<span class='anchor' id='competitions'></span>

## Competition Experience

<div class="timeline-card">
  <h3>March Machine Learning Mania 2026</h3>
  <p class="timeline-meta">Kaggle Bronze Medalist | Awarded on Apr. 8, 2026 | Rank 240/3462 teams</p>
  <p>Participated under the username <strong>hlf111</strong> and received a bronze medal. This was a useful hands-on machine learning competition experience for me.</p>
</div>

<div class="timeline-card">
  <h3>ICM 2025 Problem F: Cyber Strong?</h3>
  <p class="timeline-meta">Team Leader | Jan. 2025 - Feb. 2025 | Meritorious Winner Award (Top 6%)</p>
  <p>Worked on a team project about cybersecurity policy analysis, including data collection, modeling, and result interpretation.</p>
</div>

<div class="timeline-card">
  <h3>Contemporary Undergraduate Mathematical Contest in Modeling</h3>
  <p class="timeline-meta">Team Leader | Sep. 2025 | Provincial Third Prize (Top 25%)</p>
  <p>Completed a data modeling project based on maternal clinical records, using statistical analysis and machine learning methods.</p>
</div>

<div class="timeline-card">
  <h3>APMCM 2024 Problem C</h3>
  <p class="timeline-meta">Team Leader | Nov. 2024 | First Prize (Top 5%)</p>
  <p>Completed a mathematical modeling project on the pet industry, covering forecasting, simulation, and optimization-related methods.</p>
</div>

<span class='anchor' id='experience'></span>

## Research and Internship Experience

<div class="timeline-card">
  <h3>Provincial Undergraduate Innovation & Entrepreneurship Training Program</h3>
  <p class="timeline-meta">Project Leader | Sep. 2025 - Present</p>
  <p>An undergraduate project on reinforcement learning methods for the traveling salesman problem.</p>
</div>

<div class="timeline-card">
  <h3>Research on Cluster-Aware Vehicle Routing Problem Based on DRL</h3>
  <p class="timeline-meta">First Author | Sep. 2023 - Present</p>
  <p>A research project on routing optimization with simulation data and reinforcement learning. One related manuscript is under review.</p>
</div>

<div class="timeline-card">
  <h3>Physics-Consistent ML Framework for High-Resolution Ozone Downscaling</h3>
  <p class="timeline-meta">Co-first Author | Nov. 2025 - Dec. 2025</p>
  <p>A short project using environmental and meteorological data for ozone prediction.</p>
</div>

<div class="timeline-card">
  <h3>China Construction Bank, Zhangzhou Branch</h3>
  <p class="timeline-meta">Business Department Intern | Jul. 2024 - Aug. 2024</p>
  <p>Assisted with business department routines, data organization, and weekly reporting.</p>
</div>

<div class="timeline-card">
  <h3>Statistics Bureau, Xiangcheng District Government</h3>
  <p class="timeline-meta">Intern | Jan. 2024 - Feb. 2024</p>
  <p>Helped with data organization and verification work during the economic census.</p>
</div>

<span class='anchor' id='education'></span>

## Education

<div class="timeline-card">
  <h3>Dalian University of Technology</h3>
  <p class="timeline-meta">B.Sc. in Foundations of Mathematical Science | Sep. 2023 - Jun. 2027 | Dalian, China</p>
  <p>GPA: 92.5/100 | First-class Scholarship for Academic Excellence (Top 5%)</p>
  <p><strong>Selected coursework:</strong> Mathematical Analysis, Advanced Algebra, Probability Theory, Mathematical Statistics, Numerical Analysis, Data Structures, Python, and R.</p>
  <p><strong>English:</strong> IELTS 6.0.</p>
</div>

## Exchange Programs

<div class="timeline-card">
  <h3>NUS SCALE Youth Program, National University of Singapore</h3>
  <p class="timeline-meta">Artificial Intelligence and Machine Learning | Feb. 2025</p>
  <p>Participated in a short AI and machine learning exchange program.</p>
</div>

<div class="timeline-card">
  <h3>Top Innovative Talent Program, Massachusetts Institute of Technology</h3>
  <p class="timeline-meta">Scientific Data Analysis and Machine Learning Applications | Mar. 2024 - Jun. 2024</p>
  <p>Completed coursework and project work on scientific data analysis and machine learning applications.</p>
</div>

## Technical Skills

<div class="chip-row">
  <span class="chip">Python</span>
  <span class="chip">R</span>
  <span class="chip">MATLAB</span>
  <span class="chip">C</span>
  <span class="chip">C++</span>
  <span class="chip">Java</span>
  <span class="chip">PyTorch</span>
  <span class="chip">XGBoost</span>
  <span class="chip">LaTeX</span>
  <span class="chip">MS Excel</span>
  <span class="chip">SPSS</span>
  <span class="chip">Stata</span>
  <span class="chip">MS Office</span>
  <span class="chip">Deep Reinforcement Learning</span>
</div>

<span class='anchor' id='honors'></span>

## Honors and Awards

- **Apr. 8, 2026:** Kaggle Bronze Medalist, March Machine Learning Mania 2026, ranked 240th among 3,462 teams
- **2025:** First-class Scholarship for Academic Excellence, Dalian University of Technology (Top 5%)
- **2025:** Meritorious Winner Award, ICM Problem F (Top 6%)
- **2025:** Provincial Third Prize, Contemporary Undergraduate Mathematical Contest in Modeling
- **2024:** First Prize, APMCM 2024 (Top 5%)
- **2025:** CIPAE 2025 accepted paper
- **Ongoing:** One manuscript under review

## Featured Credential

<div class="paper-box">
  <div class='paper-box-image'>
    <div>
      <div class="badge">Kaggle | Bronze Medalist</div>
      <img src="/images/highlights/kaggle-bronze-2026.png" alt="Kaggle March Machine Learning Mania 2026 certificate" width="100%">
    </div>
  </div>
  <div class='paper-box-text'>
    <h3>Kaggle March Machine Learning Mania 2026</h3>
    <p class="publication-meta">Awarded on Apr. 8, 2026 | Username: hlf111</p>
    <ul>
      <li>Placed 240th among 3,462 teams and received a bronze medal.</li>
      <li>This page only keeps one public credential image and does not include my full transcript.</li>
    </ul>
    <div class="pub-links">
      <a href="/images/highlights/kaggle-bronze-2026.png">View Certificate</a>
      <a href="/files/resume/lifeng-han-resume.pdf">Download Resume</a>
    </div>
  </div>
</div>
