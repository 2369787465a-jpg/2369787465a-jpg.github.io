"""Check Jekyll sources, or a native Jekyll output directory with --site PATH."""
from __future__ import annotations

import argparse
import json
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

from build import ROOT, OUTPUTS, render


def page_source(path: Path) -> tuple[dict, str]:
    text = path.read_text(encoding="utf-8")
    front, body = text[4:].split("\n---\n", 1)
    metadata = {}
    for line in front.splitlines():
        key, value = line.split(":", 1)
        metadata[key] = json.loads(value)
    return metadata, body


class Document(HTMLParser):
    def __init__(self, html: str):
        super().__init__(convert_charrefs=True)
        self.ids: set[str] = set()
        self.links: list[str] = []
        self.errors: list[str] = []
        self.h1s = 0
        self.lang = ""
        self.feed(html)

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
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--site", type=Path, help="Check the native Jekyll output, e.g. _site")
    args = parser.parse_args()
    site_root = args.site.resolve() if args.site else ROOT
    documents, errors = {}, []
    generated = render()
    for _, _, name in OUTPUTS:
        source = ROOT / name
        metadata, body = page_source(source)
        route = metadata["permalink"]
        if source.read_text(encoding="utf-8") != generated[name]:
            errors.append(f"{name}: generated page is stale")
        if metadata.get("published") is False or metadata.get("layout") != "default":
            errors.append(f"{name}: Jekyll page is disabled or has the wrong layout")
        if metadata.get("lang") not in ("en", "zh"):
            errors.append(f"{name}: missing page language")
        if args.site:
            output = site_root / route.lstrip("/") / "index.html"
            if not output.is_file():
                errors.append(f"{name}: missing Jekyll output {output}")
                continue
            body = output.read_text(encoding="utf-8")
        document = Document(body)
        documents[route] = document
        errors.extend(f"{name}: {error}" for error in document.errors)
        if document.h1s != 1:
            errors.append(f"{name}: expected one H1")
        if args.site and document.lang not in ("en", "zh-CN"):
            errors.append(f"{name}: built HTML has no page language")
        if any(marker in body for marker in ("{{", "{%", "wentao-wang.jpg", "google-analytics.com", "google_scholar")):
            errors.append(f"{name}: unresolved template or retired resource")
    for route, document in documents.items():
        for link in document.links:
            if not link or link == "#":
                errors.append(f"{route}: empty link")
                continue
            parsed = urlsplit(link)
            if parsed.scheme or parsed.netloc:
                continue
            target_route = unquote(parsed.path) or route
            target_document = documents.get(target_route)
            if target_document:
                if parsed.fragment and unquote(parsed.fragment) not in target_document.ids:
                    errors.append(f"{route}: missing fragment {link}")
                continue
            target = site_root / target_route.lstrip("/")
            if target.is_dir():
                target = target / "index.html"
            if not target.is_file():
                errors.append(f"{route}: missing local target {link}")
    manifest = json.loads((ROOT / "site.webmanifest").read_text(encoding="utf-8"))
    for icon in manifest["icons"]:
        if not (site_root / icon["src"].lstrip("/")).is_file():
            errors.append(f"Manifest: missing icon {icon['src']}")
    if args.site:
        for retired in ("images/wentao-wang.jpg", "tools/content.json"):
            if (site_root / retired).exists():
                errors.append(f"Excluded file was published: {retired}")
        for redirect in ("about/index.html", "about.html"):
            if not (site_root / redirect).is_file():
                errors.append(f"Missing legacy redirect: {redirect}")
    if errors:
        raise SystemExit("\n".join(errors))
    mode = "native Jekyll output" if args.site else "Jekyll source"
    print(f"Four pages passed ({mode}): links, fragments, images, IDs, languages, and manifest.")


if __name__ == "__main__":
    main()
