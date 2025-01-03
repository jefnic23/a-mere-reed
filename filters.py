from bs4 import BeautifulSoup


def toc(content):
    soup = BeautifulSoup(content, "html.parser")
    headings = []
    for tag in soup.find_all(["h2", "h3", "h4", "h5", "h6"]):
        anchor = tag.find("a")
        if anchor and anchor.get("id"):
            headings.append({"text": tag.get_text(), "id": anchor["id"]})
        else:
            headings.append({"text": tag.get_text(), "id": ""})
    return headings
