"""Generate the four public pages. Run from any directory with Python 3.10+."""
from __future__ import annotations

import argparse
import json
from datetime import date
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, StrictUndefined, select_autoescape

ROOT = Path(__file__).resolve().parent.parent
OUTPUTS = (("en", False, "index.html"), ("zh", False, "zh/index.html"),
           ("en", True, "publications/index.html"),
           ("zh", True, "zh/publications/index.html"))


def render() -> dict[str, str]:
    content = json.loads((ROOT / "tools/content.json").read_text(encoding="utf-8"))
    env = Environment(loader=FileSystemLoader(ROOT / "tools/templates"),
                      autoescape=select_autoescape(["html"]),
                      undefined=StrictUndefined, trim_blocks=True, lstrip_blocks=True)
    # Optional links are deliberately absent rather than replaced with dummy URLs.
    for paper in content["publications"]:
        for key in ("pdf", "code", "preprint", "doi"):
            paper.setdefault(key, None)
    for project in content["projects"]:
        project.setdefault("publication", None)
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
        pages[destination] = template.render(
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
