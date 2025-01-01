from bs4 import BeautifulSoup
from pelican import signals


def add_dropcap_attribute(content):
    if getattr(content, "dropcap", False):  # Check if 'dropcap' is True
        soup = BeautifulSoup(content._content, "html.parser")
        first_paragraph = soup.find("p")
        if first_paragraph:
            first_paragraph["data-first-letter"] = first_paragraph.text[0]
            content._content = str(soup)


def register():
    signals.content_object_init.connect(add_dropcap_attribute)
