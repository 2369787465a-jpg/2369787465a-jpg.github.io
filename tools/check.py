"""Check generated HTML, site-relative links, fragment targets, and public assets."""
from __future__ import annotations

import json
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

from build import ROOT, OUTPUTS, render


class Document(HTMLParser):
    def __init__(self, path: Path):
        super().__init__(convert_charrefs=True)
        self.path = path
        self.ids: set[str] = set()
        self.links: list[str] = []
        self.errors: list[str] = []
        self.h1s = 0
        self.lang = ""
        self.feed(path.read_text(encoding="utf-8"))

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if tag == "html":
            self.lang = values.get("lang", "")
        if tag == "h1":
            self.h1s += 1
        if "id" in values:
            identifier = values["id"]
            if identifier in self.ids:
                self.errors.append(f"Duplicate ID: {identifier}")
            self.ids.add(identifier)
        if tag == "img" and not values.get("alt"):
            self.errors.append("Image has no descriptive alternative text")
        for key in ("href", "src"):
            if key in values:
                self.links.append(values[key] or "")


def main() -> None:
    documents = {name: Document(ROOT / name) for _, _, name in OUTPUTS}
    errors = []
    generated = render()
    for name, document in documents.items():
        errors.extend(f"{name}: {error}" for error in document.errors)
        if document.h1s != 1:
            errors.append(f"{name}: expected one H1")
        if document.lang not in ("en", "zh-CN"):
            errors.append(f"{name}: missing page language")
        html = document.path.read_text(encoding="utf-8")
        if html != generated[name]:
            errors.append(f"{name}: generated page is stale")
        if any(marker in html for marker in ("{{", "{%", "wentao-wang.jpg", "google-analytics.com", "google_scholar")):
            errors.append(f"{name}: template placeholder or retired resource")
        for link in document.links:
            if not link or link == "#":
                errors.append(f"{name}: empty link")
                continue
            parsed = urlsplit(link)
            if parsed.scheme or parsed.netloc:
                continue
            relative = unquote(parsed.path).lstrip("/")
            target = ROOT / relative if parsed.path.startswith("/") else document.path.parent / relative
            if not parsed.path:
                target = document.path
            elif target.is_dir():
                target = target / "index.html"
            if not target.is_file():
                errors.append(f"{name}: missing local target {link}")
                continue
            if parsed.fragment:
                target_name = target.relative_to(ROOT).as_posix()
                target_doc = documents.get(target_name)
                if target_doc is None and target.suffix == ".html":
                    target_doc = Document(target)
                if target_doc is None or unquote(parsed.fragment) not in target_doc.ids:
                    errors.append(f"{name}: missing fragment {link}")
    manifest = json.loads((ROOT / "site.webmanifest").read_text(encoding="utf-8"))
    for icon in manifest["icons"]:
        if not (ROOT / icon["src"].lstrip("/")).is_file():
            errors.append(f"Manifest: missing icon {icon['src']}")
    if errors:
        raise SystemExit("\n".join(errors))
    print("Four generated pages passed: local links, fragments, images, IDs, languages, and manifest.")


if __name__ == "__main__":
    main()
