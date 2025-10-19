AUTHOR = "Michael Boyle"
SITENAME = "Michael Boyle — AI Journey"
SITEURL = ""                     # ← empty for dev
RELATIVE_URLS = False             # ← relative links in dev

PATH = "content"
TIMEZONE = "Europe/London"
DEFAULT_LANG = "en"
DEFAULT_DATE_FORMAT = "%Y-%m-%d"

PAGE_PATHS = ["pages"]

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

FEED_ALL_RSS = "rss.xml"
CATEGORY_FEED_RSS = "category/{slug}.xml"
TRANSLATION_FEED_RSS = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 10

THEME_TEMPLATES_OVERRIDES = ["theme_overrides/templates"]

# Copy static assets from content/static → output/static
STATIC_PATHS = ["images", "extra", "static"]

# (favicon example)
EXTRA_PATH_METADATA = {
    "extra/favicon.ico": {"path": "favicon.ico"},
}

# Tell templates where the custom CSS will be served
CUSTOM_CSS = "static/custom.css"

SOCIAL = (
    ("GitHub", "https://github.com/yourname"),
    ("LinkedIn", "https://www.linkedin.com/in/yourprofile/"),
)

JINJA_ENVIRONMENT = {"trim_blocks": True, "lstrip_blocks": True}
