# --- make sure we can import pelicanconf no matter the CWD ---
import os, sys
BASE_DIR = os.path.dirname(__file__)
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from pelicanconf import *

# ---- production overrides ----
SITEURL = "https://michaelboyle.blog"  # ← use your custom domain
RELATIVE_URLS = False
DELETE_OUTPUT_DIRECTORY = True

# (Optional but good practice)
FEED_DOMAIN = SITEURL
