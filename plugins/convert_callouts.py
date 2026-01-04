# admonition_details_simple.py
from pelican import signals
from bs4 import BeautifulSoup

def convert_callouts(instance):
    html = getattr(instance, "_content", None)
    if not html:
        return
    # Quick precheck to avoid parsing pages with no callouts
    if 'class="callout' not in html and "class='callout" not in html:
        return

    soup = BeautifulSoup(html, "html.parser")

    for div in soup.select("div.callout"):
        # 1) Make <details> and copy attributes
        details = soup.new_tag("details")
        for k, v in div.attrs.items():
            details.attrs[k] = v

        # Move original children into <details>
        for child in list(div.contents):
            details.append(child.extract())

        # Replace the <div> with <details>
        div.replace_with(details)

        # 2) Find first .callout-title and convert to <summary>
        title_el = details.select_one(".callout-title")
        if title_el:
            summary = soup.new_tag("summary")
            # Move the title's contents into <summary>
            for c in list(title_el.contents):
                summary.append(c.extract())
            # Replace the title element with <summary>
            title_el.replace_with(summary)
            # Ensure <summary> is the first child (as HTML expects)
            summary.extract()
            details.insert(0, summary)

    instance._content = str(soup)

def register():
    signals.content_object_init.connect(convert_callouts)
