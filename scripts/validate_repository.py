#!/usr/bin/env python3
"""Validate local references in Art Gallery's static repository.

Uses only the Python standard library. It does not fetch external URLs or execute
page JavaScript. Run from any working directory with:
    python scripts/validate_repository.py
"""
from __future__ import annotations

import re
import sys
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_PAGES = ("index.html", "about.html", "youtube.html")
MARKDOWN_LINK_RE = re.compile(r"!?\\[[^\\]]*\\]\\(([^)]+)\\)")
CSS_URL_RE = re.compile(r"url\\(\\s*(['\\\"]?)(.*?)\\1\\s*\\)", re.IGNORECASE)


class PageParser(HTMLParser):
    """Collect local resource references, links, and element IDs."""

    def __init__(self) -> None:
        super().__init__()
        self.resources: list[str] = []
        self.links: list[str] = []
        self.ids: set[str] = set()

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if values.get("id"):
            self.ids.add(str(values["id"]))
        if tag in {"img", "script", "iframe", "source"} and values.get("src"):
            self.resources.append(str(values["src"]))
        if tag == "link" and values.get("href"):
            self.resources.append(str(values["href"]))
        if tag == "a" and values.get("href"):
            self.links.append(str(values["href"]))


def is_external_reference(raw: str) -> bool:
    """Return True for references that should not be resolved on disk."""
    value = raw.strip().strip("'\\\"")
    parsed = urlparse(value)
    return bool(parsed.scheme or parsed.netloc or value.startswith(
        ("#", "data:", "mailto:", "tel:", "javascript:")
    ))


def resolve_local_reference(base: Path, raw: str) -> tuple[Path | None, str]:
    """Resolve a relative URL path and return its optional fragment."""
    value = raw.strip().strip("'\\\"")
    if is_external_reference(value):
        return None, ""
    parsed = urlparse(value)
    target = unquote(parsed.path)
    if not target:
        return None, parsed.fragment
    return (base / target).resolve(), parsed.fragment


def markdown_links(content: str) -> list[str]:
    """Extract inline Markdown links and images outside fenced code blocks."""
    lines: list[str] = []
    in_fence = False
    fence_char = ""
    fence_length = 0
    for line in content.splitlines():
        match = re.match(r"^\\s*(\\x60{3,}|~{3,})", line)
        if match:
            token = match.group(1)
            if not in_fence:
                in_fence = True
                fence_char = token[0]
                fence_length = len(token)
            elif token[0] == fence_char and len(token) >= fence_length:
                in_fence = False
            continue
        if not in_fence:
            lines.append(line)
    result = []
    for match in MARKDOWN_LINK_RE.finditer("\\n".join(lines)):
        target = match.group(1).strip()
        if target.startswith("<") and ">" in target:
            target = target[1:target.index(">")]
        else:
            target = target.split()[0] if target else ""
        if target:
            result.append(target)
    return result


def check_html(page: Path, failures: list[str]) -> None:
    parser = PageParser()
    try:
        parser.feed(page.read_text(encoding="utf-8"))
    except (OSError, UnicodeError) as exc:
        failures.append(f"{page.relative_to(ROOT)}: unable to read HTML: {exc}")
        return
    for raw in parser.resources + parser.links:
        target, fragment = resolve_local_reference(page.parent, raw)
        if target is not None and not target.exists():
            failures.append(f"{page.relative_to(ROOT)}: missing local reference {raw}")
        elif target is not None and fragment and target.suffix.lower() in {".html", ".htm"} and target.is_file():
            other = PageParser()
            other.feed(target.read_text(encoding="utf-8"))
            if fragment not in other.ids:
                failures.append(f"{page.relative_to(ROOT)}: missing anchor #{fragment} in {target.relative_to(ROOT)}")


def check_css(css_file: Path, failures: list[str]) -> None:
    try:
        content = css_file.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        failures.append(f"{css_file.relative_to(ROOT)}: unable to read CSS: {exc}")
        return
    for match in CSS_URL_RE.finditer(content):
        raw = match.group(2).strip()
        target, _ = resolve_local_reference(css_file.parent, raw)
        if target is not None and not target.exists():
            failures.append(f"{css_file.relative_to(ROOT)}: missing CSS url() target {raw}")


def check_markdown(md_file: Path, failures: list[str]) -> None:
    try:
        content = md_file.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        failures.append(f"{md_file.relative_to(ROOT)}: unable to read Markdown: {exc}")
        return
    fence_pattern = r"^\\s*(\\x60{3,}|~{3,})"
    fence_count = len(re.findall(fence_pattern, content, re.MULTILINE))
    if fence_count % 2:
        failures.append(f"{md_file.relative_to(ROOT)}: unclosed Markdown code fence")
    for raw in markdown_links(content):
        target, _ = resolve_local_reference(md_file.parent, raw)
        if target is not None and not target.exists():
            failures.append(f"{md_file.relative_to(ROOT)}: broken Markdown link {raw}")


def check_svg(svg_file: Path, failures: list[str]) -> None:
    try:
        ET.parse(svg_file)
    except (ET.ParseError, OSError) as exc:
        failures.append(f"{svg_file.relative_to(ROOT)}: invalid SVG/XML: {exc}")


def main() -> int:
    failures: list[str] = []
    for relative in REQUIRED_PAGES:
        page = ROOT / relative
        if not page.is_file():
            failures.append(f"Missing required page: {relative}")
        else:
            check_html(page, failures)

    for css_file in ROOT.rglob("*.css"):
        if ".git" not in css_file.parts:
            check_css(css_file, failures)

    for md_file in ROOT.rglob("*.md"):
        if ".git" not in md_file.parts:
            check_markdown(md_file, failures)

    for svg_file in ROOT.rglob("*.svg"):
        if ".git" not in svg_file.parts:
            check_svg(svg_file, failures)

    if failures:
        print("Repository validation failed:")
        for failure in failures:
            print(f" - {failure}")
        return 1

    print("Repository validation passed.")
    print(f" - Required pages: {len(REQUIRED_PAGES)}")
    print(f" - CSS files: {len(list(ROOT.rglob('*.css')))}")
    print(f" - Markdown files: {len(list(ROOT.rglob('*.md')))}")
    print(f" - SVG assets: {len(list(ROOT.rglob('*.svg')))}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
