---
permalink: /
title: ""
excerpt: ""
lang: en
lang_switch_label: "中文"
lang_switch_url: "/zh/"
author_profile: true
author_bio: "B.Sc. student in Foundations of Mathematical Science at Dalian University of Technology"
sidebar_intro: "I work at the intersection of reinforcement learning, combinatorial optimization, data analysis, and applied machine learning for real-world decision problems."
redirect_from:
  - /about/
  - /about.html
---

<span class='anchor' id='about'></span>

<div class="homepage-hero">
  <p class="section-kicker">Academic Resume</p>
  <h1>Lifeng Han</h1>
  <p>I am a B.Sc. student in Foundations of Mathematical Science at Dalian University of Technology. My recent work centers on deep reinforcement learning for routing and combinatorial optimization, data-driven modeling, and physics-aware machine learning for environmental prediction.</p>
  <p>I enjoy turning messy decision problems into structured models, running end-to-end experiments, and presenting results clearly in papers and competitions. I am especially interested in research roles that combine optimization, machine learning, and practical impact.</p>
  <div class="link-pills">
    <a class="link-pill" href="mailto:lh481@student.le.ac.uk">Email</a>
    <a class="link-pill" href="/files/resume/lifeng-han-resume.pdf">Resume PDF</a>
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
    <h3>Research Focus</h3>
    <p>Deep reinforcement learning for TSP and vehicle routing</p>
    <p>Decision-oriented data analysis and predictive modeling</p>
    <p>Physics-consistent machine learning for ozone downscaling</p>
  </div>
  <div class="highlight-card">
    <h3>Recognition</h3>
    <p>Kaggle Bronze Medalist, March Machine Learning Mania 2026</p>
    <p>Meritorious Winner, ICM 2025 (Top 6%)</p>
    <p>First Prize, APMCM 2024 (Top 5%)</p>
  </div>
  <div class="highlight-card">
    <h3>Selected Output</h3>
    <p>Co-first and corresponding author paper accepted by CIPAE 2025</p>
    <p>First-author Q2 SCI manuscript under review</p>
    <p>Leader of a provincial undergraduate innovation project</p>
  </div>
</div>

<span class='anchor' id='research'></span>

## Research Interests

<div class="chip-row">
  <span class="chip">Reinforcement Learning</span>
  <span class="chip">Neural Combinatorial Optimization</span>
  <span class="chip">Vehicle Routing</span>
  <span class="chip">Traveling Salesman Problem</span>
  <span class="chip">Applied Machine Learning</span>
  <span class="chip">Environmental Data Science</span>
  <span class="chip">Optimization</span>
  <span class="chip">Statistical Modeling</span>
</div>

My work so far combines mathematical modeling, machine learning, and careful empirical analysis. I like problems with strong structure, such as routing and scheduling, but I am equally motivated by applied prediction tasks where model performance, interpretability, and physical consistency all matter.

<span class='anchor' id='projects'></span>

{% assign publications = site.data.publications.items %}
{% assign publication_limit = site.data.publications.home_limit | default: 4 %}

## Selected Projects and Outputs

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
  <a class="link-pill" href="/publications/">View All Projects and Achievements</a>
</div>

<span class='anchor' id='competitions'></span>

## Competition Experience

<div class="timeline-card">
  <h3>March Machine Learning Mania 2026</h3>
  <p class="timeline-meta">Kaggle Bronze Medalist | Awarded on Apr. 8, 2026 | Rank 240/3462 teams</p>
  <p>Competed under the username <strong>hlf111</strong> and finished in the top tier of a large-scale machine learning competition. This result reflects my ability to iterate quickly, validate ideas under leaderboard pressure, and translate modeling intuition into competitive performance.</p>
</div>

<div class="timeline-card">
  <h3>ICM 2025 Problem F: Cyber Strong?</h3>
  <p class="timeline-meta">Team Leader | Jan. 2025 - Feb. 2025 | Meritorious Winner Award (Top 6%)</p>
  <p>Built a coupled LSTM plus multi-period DID framework to study cybersecurity strategies across 113 countries. I handled data integration, risk clustering, policy-effect estimation, and robustness checks including sensitivity analysis.</p>
</div>

<div class="timeline-card">
  <h3>Contemporary Undergraduate Mathematical Contest in Modeling</h3>
  <p class="timeline-meta">Team Leader | Sep. 2025 | Provincial Third Prize (Top 25%)</p>
  <p>Analyzed 1,082 maternal clinical records, identified key factors through statistical testing, and developed a workflow combining a linear mixed model, a Weibull AFT model, and a two-stage XGBoost classifier.</p>
</div>

<div class="timeline-card">
  <h3>APMCM 2024 Problem C</h3>
  <p class="timeline-meta">Team Leader | Nov. 2024 | First Prize (Top 5%)</p>
  <p>Constructed correlation, forecasting, differential-equation, and Monte Carlo pipelines to analyze the global pet industry under tariff shocks, with implementation spanning ARIMA, grey models, PSO, and MATLAB ODE solvers.</p>
</div>

<span class='anchor' id='experience'></span>

## Research and Internship Experience

<div class="timeline-card">
  <h3>Provincial Undergraduate Innovation & Entrepreneurship Training Program</h3>
  <p class="timeline-meta">Project Leader | Sep. 2025 - Present</p>
  <p>I am leading a project on an improved deep reinforcement learning solver for the traveling salesman problem. The current pipeline combines a DACT-style encoder, synthetic attention, feasibility masking, and a mixed 2-opt/3-opt decoding strategy trained with PPO and curriculum learning.</p>
</div>

<div class="timeline-card">
  <h3>Research on Cluster-Aware Vehicle Routing Problem Based on DRL</h3>
  <p class="timeline-meta">First Author | Sep. 2023 - Present</p>
  <p>This work addresses clustered pickup-and-delivery style routing problems through a structured MDP design, simulation benchmarks, a dual-encoder transformer, and a dynamic dual-decoder. The manuscript is currently under review in a Q2-indexed SCI journal.</p>
</div>

<div class="timeline-card">
  <h3>Physics-Consistent ML Framework for High-Resolution Ozone Downscaling</h3>
  <p class="timeline-meta">Co-first Author | Nov. 2025 - Dec. 2025</p>
  <p>I integrated GEOS-Chem outputs, ERA5 meteorology, and ground observations, benchmarked Random Forest, MLP, and XGBoost models, and used SHAP analysis to verify that the learned patterns remained consistent with atmospheric photochemistry.</p>
</div>

<div class="timeline-card">
  <h3>China Construction Bank, Zhangzhou Branch</h3>
  <p class="timeline-meta">Business Department Intern | Jul. 2024 - Aug. 2024</p>
  <p>Supported corporate banking operations, client information checks, preliminary loan document review, and weekly business reporting. I also helped organize company and industry information for a local electronics industry research report.</p>
</div>

<div class="timeline-card">
  <h3>Statistics Bureau, Xiangcheng District Government</h3>
  <p class="timeline-meta">Intern | Jan. 2024 - Feb. 2024</p>
  <p>Contributed to the Fifth National Economic Census by assisting with enterprise information organization, field verification, data comparison, and outlier screening for SMEs within the district.</p>
</div>

<span class='anchor' id='education'></span>

## Education

<div class="timeline-card">
  <h3>Dalian University of Technology</h3>
  <p class="timeline-meta">B.Sc. in Foundations of Mathematical Science | Sep. 2023 - Jun. 2027 | Dalian, China</p>
  <p>GPA: 92.5/100 | First-class Scholarship for Academic Excellence (Top 5%)</p>
  <p><strong>Selected coursework:</strong> Mathematical Analysis, Advanced Algebra, Probability Theory, Mathematical Statistics, Numerical Analysis, Data Structures, C Programming, Java, Python, R, SPSS, and Stata.</p>
  <p><strong>English:</strong> IELTS 6.0 and National First Prize in the English Weekly National Translation Competition for College Students.</p>
</div>

## Exchange Programs

<div class="timeline-card">
  <h3>NUS SCALE Youth Program, National University of Singapore</h3>
  <p class="timeline-meta">Artificial Intelligence and Machine Learning | Feb. 2025</p>
  <p>Completed project practice and case-study based learning in AI and machine learning while collaborating with participants from diverse academic backgrounds.</p>
</div>

<div class="timeline-card">
  <h3>Top Innovative Talent Program, Massachusetts Institute of Technology</h3>
  <p class="timeline-meta">Scientific Data Analysis and Machine Learning Applications | Mar. 2024 - Jun. 2024</p>
  <p>Completed coursework and project assignments in scientific data analysis and machine learning applications, earning a score of 92/100.</p>
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
- **2025:** Co-first and corresponding author, CIPAE 2025 accepted paper
- **Ongoing:** First-author Q2 SCI manuscript under review on cluster-aware routing with deep reinforcement learning

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
      <li>Placed 240th among 3,462 teams and earned a bronze medal.</li>
      <li>Added a practical competition credential that complements my research and modeling background.</li>
      <li>The website intentionally leaves off the full transcript image because it contains sensitive personal details.</li>
    </ul>
    <div class="pub-links">
      <a href="/images/highlights/kaggle-bronze-2026.png">View Certificate</a>
      <a href="/files/resume/lifeng-han-resume.pdf">Download Resume</a>
    </div>
  </div>
</div>
