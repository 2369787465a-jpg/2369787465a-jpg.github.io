# Lifeng Han · Academic homepage

A bilingual academic homepage at [2369787465a-jpg.github.io](https://2369787465a-jpg.github.io/), hosted by GitHub Pages from the `main` branch, repository root.

The site uses its original **Jekyll / Minimal Mistakes** framework: white background, horizontal top navigation, author sidebar, pale blue hero, three research overview cards, and research cards. The shared Sass theme and Font Awesome assets remain active.

## Pages and content

| Jekyll source | Public route |
| --- | --- |
| `_pages/about.md` | `/` |
| `_pages/about_zh.md` | `/zh/` |
| `_pages/publications.md` | `/publications/` |
| `_pages/publications_zh.md` | `/zh/publications/` |

`/about/` and `/about.html` redirect to the English homepage through `jekyll-redirect-from`. Existing section anchors are retained. Each page's language switch leads to its counterpart.

The four page sources are generated from `tools/content.json` and `tools/templates/page.html`; they include Jekyll frontmatter. Update facts, links, and both languages in the shared JSON, then regenerate:

```sh
python -m pip install -r tools/requirements.txt
python tools/build.py
python tools/build.py --check
python tools/check.py
```

Use Python 3.10 or later. If `python` is a Windows Store alias, use an installed interpreter's absolute path. Commit the generated `_pages` files together with the source edits; GitHub Pages does **not** run the Python generator. `tools/` is excluded from the published site.

## Native build and preview

Install Ruby and Bundler, then use the retained `Gemfile` and `Gemfile.lock`:

```sh
bundle install
bundle exec jekyll build
python tools/check.py --site _site
bundle exec jekyll serve --host 127.0.0.1
```

Open `http://127.0.0.1:4000/`. A plain file server cannot compile this Jekyll source; preview the native `_site` output or use `jekyll serve`.

- `_layouts/default.html`: original page/author-sidebar shell.
- `_includes/masthead.html` and `_data/navigation*.yml`: bilingual top navigation.
- `_includes/author-profile.html`: original author profile and contact links.
- `assets/css/main.scss` and `_sass/`: original white/blue theme with small responsive and accessibility additions.
- `assets/js/site.js`: optional accessible mobile menu. Content, links, navigation, and disclosure sections work without JavaScript.
- `assets/research/`: original manuscript architecture figures, the original modeling report's country-cluster word clouds and supplementary CIPAE scatterplots, and the ozone report's spatial regridding figure.
- `assets/competitions/`: original official Kaggle competition images, with source links in the page captions.
- `assets/evidence/`: reviewed award-record and certificate crops; text links open the full image on demand.

## Portrait and later evidence

The owner's supplied portrait is `assets/portrait/lifeng-han.jpg`, used on all four pages. Its original image pixels are retained, with responsive display sizing. The blue LH illustration remains at `images/lifeng-han-avatar.svg` as a fallback. To update the portrait, change `site.portrait` and its dimensions in `tools/content.json`, then regenerate. `images/wentao-wang.jpg` belongs to another person and is excluded from publication.

The two project code links and manuscript PDFs point to their actual public GitHub repositories. The arXiv link is a preprint, labeled separately from the Applied Intelligence manuscript's **under revision** status. ICONIP 2026 is **accepted**; CIPAE 2025 is **published**. Update statuses only after an author-confirmed change or a verified publication record. Preserve complete author lists and co-first-author markers.

The first six honors are visible: the two academic excellence scholarships, ICM, the two Kaggle medals, and APMCM. The remaining three (CUMCM, cultural scholarship, and translation competition) share one collapsed section. All nine entries use text links to reviewed supporting crops, matching the Kaggle cards; supporting images open only when clicked. The five team-competition award entries carry the owner's confirmed Leader role, and both Kaggle project cards show Team leader. The English translation competition is an individual event and has no leadership label. Scholarship screenshots are labeled approval records; the CUMCM proof is a Liaoning Division award-list excerpt. The compact display title is “Third Prize · CUMCM.” The NUS short-course entry links to its completion certificate. Competition year and award date are kept distinct for APMCM.

The overview emphasizes research and public code. A compact undergraduate section immediately before Additional training lists Leicester first (Year 1: 90.62/100; Year 2: 90.48/100; rank 4/99), then DUT (93.50/100, GPA 4.35/5.0), with each university logo vertically centered on the right of its card. It retains degree names, expected graduation, and Leicester's expected First Class Honours, while omitting individual course tables. The two internship entries remain omitted. Two short training entries follow: NUS SCALE and the ITSTP course taught by MIT faculty, including its verified 92/100 assessment.

The two featured research cards are CAADRL and MC-TRCM, both labeled Co-first author with their specific personal contributions retained. MC-TRCM uses a dedicated two-column card: its original architecture image is vertically centered on the left, with the title, metadata, description, contribution, and links on the right. The status badge stays at the top-left of the card, matching the preceding project. This left/right arrangement also remains on narrow screens; the image opens at full size on click. The “More research projects” disclosure follows, ordered as CIPAE, NIPT timing and aneuploidy risk modeling, the provincial TSP innovation project, ozone downscaling, then empirical asset pricing. The innovation entry identifies Han as a team member and describes the proposed research plan; the full proposal materials remain private. The CIPAE and ozone cards keep their original figure on the left and the project description on the right on desktop, tablet, and mobile screens, with smaller spacing and type on narrow screens. Full-size images open on click. The CIPAE project displays the original modeling report's three-cluster country word clouds (Fig. 10); its caption distinguishes that report from the published CIPAE paper. Research summaries distinguish the project method from Han's personal contribution. Equal-contribution markers follow each original paper, including all three authors of the CIPAE paper. Figure sources are recorded in [assets/README.md](assets/README.md).

A brief early independent programming section follows the university achievements and methods on the two homepages. It describes Lua scripting in mini technology, begun in 2020. Downloads (2,226,777) and plays (2,595,700) are aggregate creator-page counts across published works, not unique-user counts or separate game downloads. The owner's original screenshot is linked on demand; it is not embedded in the homepage.

The full CV and application materials remain private. Do not commit the original CV PDF, preparation notes, private phone number, transcripts, or unsanitized certificates. Only `lh481@student.le.ac.uk` is public. Keep the universities' GPA scales and UoL-only rank distinct; graduation and First Class Honours are expected, not awarded.

The new layout does not request empty Analytics, Scholar statistics, MathJax, or missing icon resources. The original [MIT license](LICENSE), including **Copyright (c) 2022 Yi Ren**, is preserved byte-for-byte; retained theme/vendor license notices remain in their source files.

The two additional-training cards use original NUS and Neoscholar institution logos on the right. The ITSTP Data Analysis course is described as taught by MIT faculty, with Prof. Gunther Roland's affiliation, 48 class hours, and a verified 92/100 (A+) assessment. Neoscholar is identified as the program/transcript provider; the private full transcript is not published. The ozone project links to its public code repository and a privacy-reviewed report PDF.

The NIPT entry describes the CUMCM 2025 mathematical-modeling project, with the owner's confirmed Team leader role, personal contributions, public code, and modeling-report links. Its left-hand figure is a faithful screenshot of the original report's three-model comparison (Fig. 14); the caption identifies these as original report results. The homepage makes no clinical-validation or new reproduction-performance claim.
