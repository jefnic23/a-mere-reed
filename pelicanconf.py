AUTHOR = "Jeff Nicholas"
SITENAME = "A Mere Reed"
SITEURL = "merereed.com"

PATH = "content"
ARTICLE_PATHS = ["articles", "drafts", "pages"]

AUTHOR_SAVE_AS = ""
AUTHORS_SAVE_AS = ""
CATEGORY_SAVE_AS = ""
CATEGORIES_SAVE_AS = ""
FEEDS_SAVE_AS = ""
TAG_SAVE_AS = ""
TAGS_SAVE_AS = ""

LOAD_CONTENT_CACHE = False
SHOW_DRAFTS = True

THEME = "theme"

TIMEZONE = "America/New_York"

DEFAULT_LANG = "en"

PLUGIN_PATHS = ["plugins"]
PLUGINS = [
    "pandoc_reader",
    "add_dropcap",
    "format_time",
    "extract_toc",
    "header_anchors",
    "external_favicons",
    "external_links_blank",
    "add_toc_titles",
    "add_header_titles",
    "convert_callouts"
]

MENUITEMS = [
    ("Blog", "/archives.html"),
]

MAINITEMS = [
    ("About", "/about.html"),
    ("Projects", "/projects.html")
]

TYPOGRIFY = True

# Arguments passed into pandoc
PANDOC_ARGS = ["--toc", "--toc-depth=4"]

# Non-Pandoc Extensions that are not enabled by default in pandoc
#   https://pandoc.org/MANUAL.html#non-pandoc-extensions
PANDOC_EXTENSIONS = [
    "+abbreviations",
    "+backtick_code_blocks",
    "+emoji",
    "+inline_code_attributes",
    "+smart",
    "+auto_identifiers",
    "+implicit_header_references",
]

CALCULATE_READING_TIME = True
READING_SPEED = 238

FAVICON_DIR = "theme/assets/external_favicons"  # folder under OUTPUT_PATH for saved icons (URL path too)
FAVICON_CACHE_DIR = None  # set to custom path; default is OUTPUT_PATH/FAVICON_DIR
FAVICON_DOWNLOAD = True  # disable if you want to only use pre-cached icons
FAVICON_TIMEOUT = 5  # seconds for network fetch
FAVICON_USE_GOOGLE_FALLBACK = True  # use Google S2 if /favicon.ico not found
FAVICON_IMG_SIZE = 16  # px width/height for appended icon
FAVICON_IMG_CLASS = "ext-favicon"

# Behavior knobs (sane defaults shown)
BLANK_FORCE = False                # If True, overwrite any existing target with "_blank"
BLANK_REL_TOKENS = ["noopener", "noreferrer"]  # Always merge these into rel=""
BLANK_ADD_EXTERNAL_REL = True      # Also add "external" to rel
BLANK_SKIP_MAILTO_TEL = True       # Skip mailto:, tel:, javascript:
BLANK_SKIP_DOWNLOAD = True         # Skip <a download>
BLANK_LINK_CLASS = "ext-blank"     # Add a class to modified links (or set to None)

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("GitHub", "https://github.com/jefnic23"),
    ("goodreads", "https://www.goodreads.com/user/show/96530631-jeff-nicholas")
)

# Social widget
SOCIAL = (
    ("Twitter", "https://twitter.com/JeffFNicholas"),
    ("LinkedIn", "https://www.linkedin.com/in/jeff-n-9463651a5/"),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
