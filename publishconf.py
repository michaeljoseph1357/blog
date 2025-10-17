# --- make sure we can import pelicanconf no matter the CWD ---
import os, sys
BASE_DIR = os.path.dirname(__file__)
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

# import all dev settings
from pelicanconf import *

# ---- production overrides ----
SITEURL = "https://michaelboyle-ai.netlify.app"
RELATIVE_URLS = False
DELETE_OUTPUT_DIRECTORY = True
