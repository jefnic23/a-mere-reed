from bs4 import BeautifulSoup
from pelican import signals

# Defaults
HEADER_TITLE_PREFIX = "Link to: §"

def _collect_toc_ids(toc_html: str | None) -> set[str]:
    ids = set()
    if not toc_html:
        return ids
    soup = BeautifulSoup(toc_html, "html.parser")
    for a in soup.select("a[href^='#']"):
        href = a.get("href", "")
        if href.startswith("#") and len(href) > 1:
            ids.add(href[1:])
    return ids

def add_header_titles(content):
    """
    Runs for Articles/Pages after they’re read.
    """
    # only process HTML-like content
    if not getattr(content, "_content", None):
        return

    toc_ids = _collect_toc_ids(getattr(content, "toc", None))

    soup = BeautifulSoup(content._content, "html.parser")
    changed = False

    for h in soup.select("h2[id], h3[id], h4[id]"):
        hid = h.get("id")
        if hid not in toc_ids:
            continue
        if h.has_attr("title"):
            continue

        text = h.get_text(" ", strip=True)
        if not text:
            continue

        h["title"] = f"{HEADER_TITLE_PREFIX} '{text}'"
        changed = True

    if changed:
        content._content = str(soup)

def register():
    signals.content_object_init.connect(add_header_titles)
