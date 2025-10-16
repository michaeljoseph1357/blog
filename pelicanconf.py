AUTHOR = "Michael Boyle"
SITENAME = "Michael Boyle — AI Journey"
SITEURL = ""  # set to your production URL in publishconf.py

PATH = "content"
TIMEZONE = "Europe/London"
DEFAULT_LANG = "en"
DEFAULT_DATE_FORMAT = "%Y-%m-%d"

# Treat Markdown files under content/pages/ as Pages (no Date required)
PAGE_PATHS = ["pages"]

# URL / save paths (clean, SEO-friendly)
ARTICLE_URL = "blog/{date:%Y}/{date:%m}/{slug}/"
ARTICLE_SAVE_AS = "blog/{date:%Y}/{date:%m}/{slug}/index.html"
PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"
CATEGORY_SAVE_AS = ""
TAG_SAVE_AS = "tag/{slug}/index.html"
TAGS_SAVE_AS = "tags/index.html"
ARCHIVES_SAVE_AS = "blog/index.html"
YEAR_ARCHIVE_SAVE_AS = "blog/{date:%Y}/index.html"
MONTH_ARCHIVE_SAVE_AS = "blog/{date:%Y}/{date:%m}/index.html"

# Feeds (keep for production; harmless warning in dev when SITEURL is empty)
FEED_ALL_RSS = "rss.xml"
CATEGORY_FEED_RSS = "category/{slug}.xml"
TRANSLATION_FEED_RSS = None
AUTHOR_FEED_RSS = None

# Pagination
DEFAULT_PAGINATION = 10

# ================================
# THEME & STATIC SETTINGS
# ================================


THEME_TEMPLATES_OVERRIDES = ["theme_overrides/templates"]

# Pelican expects static files under the content directory
STATIC_PATHS = [
    "images",
    "extra",
    "static",
]

# Map source -> destination inside /output
EXTRA_PATH_METADATA = {
    "extra/favicon.ico": {"path": "favicon.ico"},
    "static/custom.css": {"path": "static/custom.css"},
}

CUSTOM_CSS = "static/custom.css"


# Social/links
SOCIAL = (
    ("GitHub", "https://github.com/yourname"),
    ("LinkedIn", "https://www.linkedin.com/in/yourprofile/"),
)

# Jinja
JINJA_ENVIRONMENT = {"trim_blocks": True, "lstrip_blocks": True}
