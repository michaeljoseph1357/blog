# Michael Boyle — AI Journey (Pelican)

A minimalist, blog-first static site built with **Pelican** (Python). Posts, tags, RSS, clean URLs, and a simple theme you can restyle by editing **`theme_overrides/static/custom.css`**.

## Quickstart

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# develop with live reload
pelican -lr -s pelicanconf.py

# build to ./output
pelican content -o output -s pelicanconf.py
```

## Deploy

- GitHub Pages, Netlify, or Cloudflare Pages (serve `output/`)
- For GitHub Pages, you can push `output/` to `gh-pages` or use an action.

## Styling

Edit **`theme_overrides/static/custom.css`** to change colors, fonts, radius, and spacing.
You can also tweak templates in **`theme_overrides/templates/`**.
