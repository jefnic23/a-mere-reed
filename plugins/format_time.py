import re

from pelican import signals

# Regex pattern to match times (e.g., 4pm, 5:30am, 12:45PM)
TIME_PATTERN = re.compile(r"(\b\d{1,2}(:\d{2})?\s?[ap]m\b)", re.IGNORECASE)


def format_time(content):
    """Wrap times in <span> for styling."""
    if content._content:  # Ensure content is not empty
        content._content = TIME_PATTERN.sub(
            r'<span class="time">\1</span>', content._content
        )


def register():
    signals.content_object_init.connect(format_time)
