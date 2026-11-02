# evolvedproducts.us

Static site for EVOLVED bio-based washer fluid (Evolved Innovations).

- Build: `python3 tools/build.py` (page copy in `tools/pages.py`, blog in `tools/posts.py`)
- Hosting plan: Cloudflare Pages (preview on pages.dev first; GoDaddy stays live until launch)
- Preview builds are noindex. At launch: set `NOINDEX = False` in `tools/build.py`, remove the `X-Robots-Tag` line from `_headers`, rebuild.
