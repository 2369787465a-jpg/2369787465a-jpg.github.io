# Lifeng Han · Academic homepage

A bilingual academic portfolio at [2369787465a-jpg.github.io](https://2369787465a-jpg.github.io/), hosted by GitHub Pages from the `main` branch, repository root.

## Pages

| English | 中文 |
| --- | --- |
| `/` | `/zh/` |
| `/publications/` | `/zh/publications/` |

The four pages are committed static HTML. GitHub Pages can copy them through its existing Jekyll build; visitors and local previews do not need Ruby, a JavaScript framework, or third-party scripts. `/about/` and `/about.html` redirect to the homepage. Existing section anchors are retained.

## Edit and preview

Use Python 3.10 or later. The only build dependency is Jinja2:

```sh
python -m pip install -r tools/requirements.txt
python tools/build.py
python tools/build.py --check
python tools/check.py
python -m http.server 8000 --bind 127.0.0.1
```

Open `http://127.0.0.1:8000/`. If `python` is a Windows Store alias, use the absolute path of an installed Python executable instead.

- `tools/content.json`: shared facts, links, and English/Chinese copy. Update both languages together. Publication titles and author order follow the manuscripts/CV.
- `tools/templates/page.html`: one template for all four pages.
- `assets/css/site.css`: typography, responsive layout, keyboard focus, reduced motion, and printing.
- `assets/js/site.js`: optional mobile-navigation behavior. Content, links, and disclosure sections work without JavaScript.
- `assets/research/`: original architecture figures from the two research manuscripts.

After editing content or the template, regenerate and commit all four HTML files with the source changes. GitHub Pages does **not** run the Python generator. The check command detects generated files that need an update. `tools/` is excluded from deployment.

## Portrait

The initial design uses an LH monogram. To use a real portrait, add an approved, optimized image to `assets/portrait/`, set `site.portrait` in `tools/content.json` to its site path (for example, `/assets/portrait/lifeng-han.jpg`), and regenerate. Use a square crop; the template already provides image alternative text and responsive styling. The former `images/wentao-wang.jpg` belongs to another person and must never be used for Lifeng Han.

## Publications, code, and later evidence

The two project code links and manuscript PDFs point to their actual public GitHub repositories. The arXiv link is a preprint and is labeled separately from the Applied Intelligence manuscript's **under revision** status. ICONIP 2026 is **accepted**; CIPAE 2025 is **published**. Update these statuses only after an author-confirmed change or a verified publication record. Keep complete author lists and the co-first-author markers.

When the owner provides more material, add only approved public files and real links. Potential additions include a portrait, accepted/published paper records, award certificates, a verified Kaggle profile, and a verified academic identifier. Check permissions and remove private identifiers from public certificate copies. Add evidence links beside the corresponding award or publication; do not use placeholder links or fabricate missing records. The current award entries do not imply that proof has been uploaded.

The full CV and supporting application materials remain private. Do not commit the original CV PDF, preparation notes, private phone number, transcripts, or unsanitized certificates. Only the professional email `lh481@student.le.ac.uk` is public. The two universities' GPA scales and the UoL-only rank must remain distinct; graduation and First Class Honours are expected, not awarded.

## GitHub Pages and retained theme

`_config.yml` excludes `tools/`, retired Jekyll theme files, and the former `images/` directory. The old `_pages` files have `published: false` and are excluded, avoiding duplicate output at the four public routes. Old theme source remains in the repository for provenance and rollback; the new pages do not load its scripts, analytics, Scholar statistics requests, fonts, or old icons. No hosting-provider migration is required.

The original [MIT license](LICENSE), including **Copyright (c) 2022 Yi Ren**, is preserved. Retained vendor/theme license notices remain in their original files.
