from markupsafe import Markup
from bs4 import BeautifulSoup
from pelican import signals

def add_toc_titles(html: str, prefix: str = "Jump to: §") -> Markup:
    if not html:
        return Markup("")
    soup = BeautifulSoup(html, "html.parser")
    # Pandoc's TOC links point to in-page anchors; scope to those:
    for a in soup.select("a[href^='#']"):
        text = a.get_text(" ", strip=True)
        if text:
            a["title"] = f"{prefix} '{text}'"
    return Markup(str(soup))

def add_filter(pelican):
    """Add age_in_days filter to Pelican."""
    pelican.env.filters.update({'add_toc_titles': add_toc_titles})

def register():
    """Plugin registration."""
    signals.generator_init.connect(add_filter)