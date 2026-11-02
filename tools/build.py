#!/usr/bin/env python3
"""Builds the EVOLVED static site. Run from the repo root: python3 tools/build.py

Design copies the original GoDaddy site (Nov 2026). Shared header/footer here;
page bodies in tools/pages.py; blog posts in tools/posts.py.
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from pages import PAGES
from posts import POSTS

SITE = "https://evolvedproducts.us"
EMAIL = "Tyler@evolvedproducts.us"
PHONE = "1-866-727-9411"
# Set to False at launch: preview builds tell search engines not to index.
NOINDEX = True
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ORG = {
    "@context": "https://schema.org", "@type": "Organization",
    "name": "Evolved Innovations", "alternateName": "EVOLVED", "url": SITE,
    "logo": SITE + "/images/evolved-logo.webp", "email": EMAIL, "telephone": "+1-866-727-9411",
    "address": {"@type": "PostalAddress", "addressLocality": "Sioux Falls",
                "addressRegion": "SD", "postalCode": "57104", "addressCountry": "US"},
}

CART_SVG = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M7 18a2 2 0 1 0 0 4 2 2 0 0 0 0-4zm10 0a2 2 0 1 0 0 4 2 2 0 0 0 0-4zM5.2 4H2V2h4.6l.9 2H22l-3.6 8.4a2 2 0 0 1-1.8 1.2H8.1l-1 1.9V16H19v2H5v-2.4l1.5-2.8L5.2 4z"/></svg>'
PHONE_SVG = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.25 11.4 11.4 0 0 0 3.6.57 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1c0 1.25.2 2.45.57 3.57a1 1 0 0 1-.25 1z"/></svg>'


def page(path, title, desc, body, schema=None, active=None):
    pre = "../" * path.count("/")
    act = active or path
    cur = lambda h: ' aria-current="page"' if h == act else ""
    canonical = SITE + "/" + ("" if path == "index.html" else path.replace("index.html", "").replace(".html", ""))
    robots = '<meta name="robots" content="noindex,nofollow">\n' if NOINDEX else ""
    ld = "".join(f'<script type="application/ld+json">{json.dumps(x)}</script>' for x in [ORG] + (schema or []))
    body = body.replace("{pre}", pre).replace("{email}", EMAIL).replace("{phone}", PHONE)
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
{robots}<link rel="canonical" href="{canonical}">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{SITE}/images/tile-bugaway.webp">
<meta name="theme-color" content="#ffffff">
<link rel="icon" type="image/png" href="{pre}images/favicon.png">
<link rel="apple-touch-icon" href="{pre}images/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cabin:ital,wght@0,400;0,600;1,400&family=League+Spartan:wght@700&family=Barlow+Condensed:ital,wght@1,800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{pre}css/site.css">
{ld}
</head>
<body>
<header class="site-header">
  <div class="hdr">
    <button class="burger" aria-label="Menu" aria-expanded="false" onclick="var d=document.getElementById('drawer');d.classList.toggle('open');this.setAttribute('aria-expanded',d.classList.contains('open'))"><span></span><span></span><span></span></button>
    <nav aria-label="Main">
      <a href="{pre}index.html"{cur('index.html')}>Home</a>
      <a href="{pre}about.html"{cur('about.html')}>About</a>
      <div class="dd"><button type="button" aria-haspopup="true" onclick="this.parentNode.classList.toggle('open')">Products</button>
        <div class="dd-menu">
          <a href="{pre}washer-fluid-concentrates.html">Washer Fluid Concentrates</a>
          <a href="{pre}fleet-bulk.html">Fleet &amp; Bulk</a>
          <a href="{pre}personal-vehicle.html">Personal vehicle</a>
        </div></div>
    </nav>
    <a class="logo" href="{pre}index.html" aria-label="EVOLVED home"><img src="{pre}images/evolved-logo.webp" alt="EVOLVED bio-based washer fluid" width="900" height="257"></a>
    <div class="right">
      <a class="txt" href="{pre}blog/index.html"{cur('blog/index.html')}>Blog</a>
      <a class="icon txt" href="tel:+18667279411" aria-label="Call {PHONE}">{PHONE_SVG}</a>
      <a class="icon" href="{pre}washer-fluid-concentrates.html" aria-label="Shop">{CART_SVG}</a>
    </div>
  </div>
  <div class="drawer" id="drawer">
    <a href="{pre}index.html">Home</a><a href="{pre}about.html">About</a>
    <a href="{pre}washer-fluid-concentrates.html" class="sub">Washer Fluid Concentrates</a>
    <a href="{pre}fleet-bulk.html" class="sub">Fleet &amp; Bulk</a>
    <a href="{pre}personal-vehicle.html" class="sub">Personal vehicle</a>
    <a href="{pre}blog/index.html">Blog</a><a href="{pre}contact-us.html">Contact Us</a>
    <a href="tel:+18667279411">Call {PHONE}</a>
  </div>
</header>
<main>
{body}
</main>
<footer class="site-footer">
  <div class="wrap">
    <div class="foot"><span>Copyright &copy; 2026 EVOLVED - All Rights Reserved.</span><span><a href="tel:+18667279411" style="text-decoration:none">{PHONE}</a> &middot; <a href="mailto:{EMAIL}" style="text-decoration:none">{EMAIL}</a></span></div>
    <div class="foot-links"><a href="{pre}privacy-policy.html">Privacy Policy</a><a href="{pre}contact-us.html">Contact Us</a></div>
  </div>
</footer>
<script src="{pre}js/site.js" defer></script>
</body>
</html>
"""


def write(path, html):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w") as f:
        f.write(html)


def main():
    urls = []
    for p in PAGES:
        write(p["path"], page(p["path"], p["title"], p["desc"], p["body"], p.get("schema")))
        urls.append(p["path"])

    rows = "".join(f"""<div class="post-row"><a href="{p['slug']}.html"><img src="../images/{p['thumb']}" alt="" width="200" height="200" loading="lazy"></a>
<div><div class="date">{p['date_human']}</div><h4><a href="{p['slug']}.html">{p['h1']}</a></h4><p>{p['desc']}</p><a class="go" href="{p['slug']}.html">Continue Reading</a></div></div>""" for p in POSTS)
    body = f"""<section><div class="wrap narrow"><h1 class="title">My Blog</h1>{rows}</div></section>"""
    write("blog/index.html", page("blog/index.html", "Blog | EVOLVED Washer Fluid",
                                  "Tips and plain-English articles about windshield washer fluid, concentrates and bio-based products from EVOLVED.",
                                  body, active="blog/index.html"))
    urls.append("blog/index.html")
    for p in POSTS:
        path = f"blog/{p['slug']}.html"
        body = f"""<section><div class="wrap post"><div class="date" style="text-align:center;color:var(--small)">{p['date_human']}</div>
<h1 class="title">{p['h1']}</h1>{p['body']}
<p style="margin-top:40px">Questions? Email <a href="mailto:{{email}}">{{email}}</a> or call <a href="tel:+18667279411">{{phone}}</a>.</p>
<p><a href="index.html">&larr; Back to blog</a></p></div></section>"""
        schema = [{"@context": "https://schema.org", "@type": "BlogPosting", "headline": p["h1"],
                   "datePublished": p["date"], "author": {"@type": "Organization", "name": "Evolved Innovations"},
                   "mainEntityOfPage": f"{SITE}/{path[:-5]}"}]
        write(path, page(path, p["title"], p["desc"], body, schema, active="blog/index.html"))
        urls.append(path)

    sm = "".join(f"<url><loc>{SITE}/{'' if u == 'index.html' else u.replace('index.html', '').replace('.html', '')}</loc></url>" for u in urls)
    write("sitemap.xml", f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{sm}</urlset>\n')
    write("robots.txt", "User-agent: *\nDisallow: /\n" if NOINDEX else f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")
    print(f"built {len(urls)} pages (noindex={NOINDEX})")


if __name__ == "__main__":
    main()
