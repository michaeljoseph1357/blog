import os, sys
sys.path.insert(0, os.path.dirname(__file__))  # ensure we can import pelicanconf
from pelicanconf import *



SITEURL = "https://michaelboyle-ai.netlify.app" # <-- change to your domain
RELATIVE_URLS = False
FEED_ALL_RSS = "rss.xml"
DELETE_OUTPUT_DIRECTORY = True
