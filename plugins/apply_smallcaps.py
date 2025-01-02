import re

from pelican import signals

# Regex pattern to match 3 or more consecutive characters
CONSECUTIVE_CHARS_PATTERN = re.compile(r"(\b[A-Z]{3,}\b)")


def apply_smallcaps(content):
    """Wrap 3 or more consecutive characters in <span> for styling."""
    if content._content:  # Ensure content is not empty
        content._content = CONSECUTIVE_CHARS_PATTERN.sub(
            r'<span class="small-caps">\1</span>', content._content
        )


def register():
    signals.content_object_init.connect(apply_smallcaps)
