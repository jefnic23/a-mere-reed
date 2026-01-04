# external_links_blank.py
# Add target=_blank to external links, with safe rel tokens.
# Uses BeautifulSoup if available; otherwise regex fallback.

from __future__ import annotations

import urllib.parse
from bs4 import BeautifulSoup
from pelican import signals

# ---------- helpers ----------


def _domain_key(netloc: str) -> str:
    """Normalize a netloc to compare domains (strip auth/ports/www, naive eTLD+1)."""
    host = netloc.split("@")[-1].split(":")[0].strip().lower()
    if host.startswith("www."):
        host = host[4:]
    parts = host.split(".")
    if len(parts) >= 3:
        host = ".".join(parts[-2:])
    return host


def _is_external(href: str, our_domain: str | None) -> bool:
    try:
        u = urllib.parse.urlparse(href)
    except Exception:
        return False
    if u.scheme not in ("http", "https"):
        return False
    if not u.netloc:
        return False
    if our_domain and _domain_key(u.netloc) == _domain_key(our_domain):
        return False
    return True


def _should_skip(href: str, a_attrs: dict, settings: dict) -> bool:
    # Per-link opt out
    if "data-no-blank" in a_attrs:
        return True
    # Skip mailto/tel/javascript by default
    skip_tel_mailto = bool(settings.get("BLANK_SKIP_MAILTO_TEL", True))
    if skip_tel_mailto and href and href.startswith(("mailto:", "tel:", "javascript:")):
        return True
    # Skip downloads by default
    skip_download = bool(settings.get("BLANK_SKIP_DOWNLOAD", True))
    if skip_download and "download" in a_attrs:
        return True
    return False


def _merge_rel(existing: str | None, tokens: list[str], add_external: bool) -> str:
    rel = set((existing or "").split())
    rel.update(tokens)
    if add_external:
        rel.add("external")
    return " ".join(sorted(rel))


# ---------- BeautifulSoup path ----------


def _process_with_bs4(html: str, settings: dict, our_domain: str | None) -> str:
    force = bool(settings.get("BLANK_FORCE", False))
    rel_tokens = settings.get("BLANK_REL_TOKENS") or ["noopener", "noreferrer"]
    add_external = bool(settings.get("BLANK_ADD_EXTERNAL_REL", True))
    link_class = settings.get("BLANK_LINK_CLASS", None)

    soup = BeautifulSoup(html, "html.parser")
    for a in soup.find_all("a", href=True):
        href = a.get("href", "")
        if not _is_external(href, our_domain):
            continue
        if _should_skip(href, a.attrs, settings):
            continue

        # target
        if force or "target" not in a.attrs:
            a["target"] = "_blank"

        # rel merge
        a["rel"] = _merge_rel(
            (a.get("rel") if isinstance(a.get("rel"), str) else " ".join(a.get("rel", []))),
            rel_tokens,
            add_external,
        )

        # optional class
        if link_class:
            classes = a.get("class", [])
            if link_class not in classes:
                a["class"] = classes + [link_class]

    return str(soup)


# ---------- Entry point ----------


def _process_content(content):
    if not getattr(content, "_content", None):
        return

    settings = getattr(content, "settings", {}) or {}
    siteurl = (settings.get("SITEURL") or "").strip()
    our_domain = urllib.parse.urlparse(siteurl).netloc if siteurl else None

    html = content._content
    if "<a " not in html.lower():
        return

    content._content = _process_with_bs4(html, settings, our_domain)


def register():
    signals.content_object_init.connect(_process_content)
