"""Generate four Jekyll page sources. Run from any directory with Python 3.10+."""
from __future__ import annotations

import argparse
import json
from datetime import date
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, StrictUndefined, select_autoescape

ROOT = Path(__file__).resolve().parent.parent
OUTPUTS = (("en", False, "_pages/about.md"), ("zh", False, "_pages/about_zh.md"),
           ("en", True, "_pages/publications.md"),
           ("zh", True, "_pages/publications_zh.md"))


def render() -> dict[str, str]:
    content = json.loads((ROOT / "tools/content.json").read_text(encoding="utf-8"))
    env = Environment(loader=FileSystemLoader(ROOT / "tools/templates"),
                      autoescape=select_autoescape(["html"]),
                      undefined=StrictUndefined, trim_blocks=True, lstrip_blocks=True)
    # Optional links are deliberately absent rather than replaced with dummy URLs.
    for paper in content["publications"]:
        paper.setdefault("equal_author_count", 2 if paper["cofirst"] else 0)
        for key in ("pdf", "code", "preprint", "doi", "evidence"):
            paper.setdefault(key, None)
    for project in content["projects"] + content.get("competitions", []):
        project.setdefault("publication", None)
        for key in ("image", "image_source", "contribution", "evidence"):
            project.setdefault(key, None)
    for project in content["featured"]:
        project.setdefault("contribution", None)
        project.setdefault("layout", "split")
    for item in content["awards"] + content["experience"]:
        item.setdefault("evidence", None)
    for award in content["awards"]:
        award.setdefault("role", None)
    template = env.get_template("page.html")
    pages = {}
    for lang, publications_page, destination in OUTPUTS:
        home_url = "/zh/" if lang == "zh" else "/"
        publications_url = home_url + "publications/"
        other_home = "/" if lang == "zh" else "/zh/"
        other_url = other_home + "publications/" if publications_page else other_home
        copy = content["copy"][lang]
        page_title = (copy["publications_heading"] + " | " + content["site"]["name"]
                      if publications_page else copy["title"])
        metadata = {
            "layout": "default", "permalink": publications_url if publications_page else home_url,
            "title": page_title, "excerpt": copy["description"], "lang": lang,
            "lang_switch_label": copy["language"], "lang_switch_url": other_url,
            "author_profile": True,
            "author_name": content["site"]["name_zh"] if lang == "zh" else content["site"]["name"],
            "author_avatar": content["site"]["portrait"] or "/images/lifeng-han-avatar.svg",
            "author_avatar_width": content["site"].get("portrait_width", 175),
            "author_avatar_height": content["site"].get("portrait_height", 210),
            "author_bio": ("Mathematics & Foundations of Mathematical Science undergraduate"
                           if lang == "en" else "数学与数理基础科学专业本科生"),
            "sidebar_intro": copy["sidebar_universities"].replace("\n", " · ") + ". " + copy["sidebar_graduation"],
        }
        if lang == "en" and not publications_page:
            metadata["redirect_from"] = ["/about/", "/about.html"]
        frontmatter = "---\n" + "\n".join(
            f"{key}: {json.dumps(value, ensure_ascii=False)}" for key, value in metadata.items()) + "\n---\n\n"
        pages[destination] = frontmatter + template.render(
            **{key: value for key, value in content.items() if key != "copy"},
            publication_by_id={p["id"]: p for p in content["publications"]},
            t=copy, lang=lang, publications_page=publications_page,
            home_url=home_url, publications_url=publications_url,
            other_url=other_url, path=publications_url if publications_page else home_url,
            page_title=page_title, year=date.today().year)
    return pages


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Fail if committed pages need regeneration")
    args = parser.parse_args()
    stale = []
    for name, html in render().items():
        path = ROOT / name
        if args.check:
            if not path.exists() or path.read_text(encoding="utf-8") != html:
                stale.append(name)
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(html, encoding="utf-8", newline="\n")
            print(f"Generated {name}")
    if stale:
        raise SystemExit("Regenerate pages with tools/build.py: " + ", ".join(stale))
    if args.check:
        print("All four generated pages are current.")


if __name__ == "__main__":
    main()
