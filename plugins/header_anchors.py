from bs4 import BeautifulSoup
from pelican import signals

def add_header_anchors(instance):
    if not instance._content:
        return

    soup = BeautifulSoup(instance._content, "html.parser")

    for header in soup.find_all(["h2", "h3", "h4", "h5", "h6"]):
        if "id" in header.attrs:
            # Create an <a> element linking to this id
            anchor = soup.new_tag("a", href=f"#{header['id']}") # , **{"class": "header-link"}
            anchor.string = header.get_text()
            # Replace header’s text with the anchor
            header.clear()
            header.append(anchor)

    instance._content = str(soup)

def register():
    signals.content_object_init.connect(add_header_anchors)
