#!/usr/bin/env python3
"""Builds the EVOLVED static site. Run from the repo root: python3 tools/build.py

Every page shares one header/footer. Page bodies live in tools/pages.py,
blog posts in tools/posts.py. Output is plain HTML in the repo root.
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from pages import PAGES
from posts import POSTS

SITE = "https://evolvedproducts.us"
EMAIL = "Tyler@evolvedproducts.us"
# Set to False at launch: preview builds tell search engines not to index.
NOINDEX = True
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

NAV = [
    ("index.html", "Home"),
    ("personal-vehicle.html", "Personal Vehicle"),
    ("fleet-bulk.html", "Fleet &amp; Bulk"),
    ("how-to-mix.html", "How to Mix"),
    ("about.html", "About"),
    ("faq.html", "FAQ"),
    ("blog/index.html", "Blog"),
]

ORG = {
    "@context": "https://schema.org",
    "@type": "Organization",
    "name": "Evolved Innovations",
    "alternateName": "EVOLVED",
    "url": SITE,
    "logo": SITE + "/images/evolved-logo.webp",
    "email": EMAIL,
    "telephone": "+1-866-727-9411",
    "address": {"@type": "PostalAddress", "addressLocality": "Sioux Falls",
                "addressRegion": "SD", "addressCountry": "US"},
}


def page(path, title, desc, body, schema=None, active=None):
    depth = path.count("/")
    pre = "../" * depth
    nav = "".join(
        f'<a href="{pre}{href}"{" aria-current=page" if href == (active or path) else ""}>{label}</a>'
        for href, label in NAV)
    canonical = SITE + "/" + ("" if path == "index.html" else path.replace("index.html", ""))
    robots = '<meta name="robots" content="noindex,nofollow">' if NOINDEX else ""
    ld = [ORG] + (schema or [])
    ld_html = "".join(f'<script type="application/ld+json">{json.dumps(x)}</script>' for x in ld)
    body = body.replace("{pre}", pre).replace("{email}", EMAIL)
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
{robots}
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{SITE}/images/rainaway-32oz-front.webp">
<link rel="icon" type="image/png" href="{pre}images/favicon.png">
<link rel="apple-touch-icon" href="{pre}images/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@700;800;900&family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{pre}css/site.css">
{ld_html}
</head>
<body>
<header class="site-header">
  <div class="wrap">
    <a class="brand" href="{pre}index.html" aria-label="EVOLVED home"><img src="{pre}images/evolved-logo.webp" alt="EVOLVED bio-based washer fluid" width="900" height="257"></a>
    <button class="menu-btn" aria-label="Menu" aria-expanded="false" onclick="var n=document.getElementById('nav');n.classList.toggle('open');this.setAttribute('aria-expanded',n.classList.contains('open'))">&#9776;</button>
    <nav class="nav" id="nav">{nav}<a class="btn green sm" href="{pre}contact.html">Order / Quote</a></nav>
  </div>
</header>
<main>
{body}
</main>
<footer class="site-footer">
  <div class="wrap">
    <div class="foot-grid">
      <div>
        <div class="foot-logo"><img src="{pre}images/evolved-logo.webp" alt="EVOLVED" width="900" height="257"></div>
        <p>Bio-based windshield washer fluid concentrate. You add the water, so we don't ship it.</p>
        <p>Sioux Falls, South Dakota</p>
      </div>
      <div><h4>Products</h4><ul>
        <li><a href="{pre}personal-vehicle.html">Personal Vehicle</a></li>
        <li><a href="{pre}fleet-bulk.html">Fleet &amp; Bulk</a></li>
        <li><a href="{pre}how-to-mix.html">How to Mix</a></li>
      </ul></div>
      <div><h4>Company</h4><ul>
        <li><a href="{pre}about.html">About</a></li>
        <li><a href="{pre}faq.html">FAQ</a></li>
        <li><a href="{pre}blog/index.html">Blog</a></li>
      </ul></div>
      <div><h4>Contact</h4><ul>
        <li><a href="tel:+18667279411">1-866-727-9411</a></li>
        <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
        <li><a href="{pre}contact.html">Order or get a quote</a></li>
        <li><a href="{pre}privacy-policy.html">Privacy Policy</a></li>
      </ul></div>
    </div>
    <div class="legal">&copy; 2026 Evolved Innovations. EVOLVED INNOVATIONS&trade; is a trademark of Evolved Innovations. All rights reserved.</div>
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

    cards = ""
    for post in POSTS:
        cards += f"""<article class="card post-card"><a href="{post['slug']}.html">
<span class="tag sky">{post['tag']}</span><h3>{post['h1']}</h3>
<p class="muted">{post['desc']}</p><span class="post-meta">{post['date_human']} &middot; Read more &rarr;</span></a></article>"""
    blog_index = f"""<section class="page-hero"><div class="wrap">
<span class="eyebrow">Blog</span><h1>Washer fluid, explained</h1>
<p class="lead">Straight answers about windshield washer fluid, concentrates, and keeping your view clear.</p></div></section>
<section><div class="wrap"><div class="grid3">{cards}</div></div></section>"""
    write("blog/index.html", page("blog/index.html", "Washer Fluid Blog | EVOLVED",
                                  "Plain-English articles about windshield washer fluid, concentrates, winter driving and bio-based products.",
                                  blog_index, active="blog/index.html"))
    urls.append("blog/")
    for post in POSTS:
        path = f"blog/{post['slug']}.html"
        body = f"""<section class="page-hero"><div class="wrap post">
<span class="eyebrow">{post['tag']}</span><h1>{post['h1']}</h1>
<p class="post-meta">{post['date_human']} &middot; Evolved Innovations</p></div></section>
<section style="padding-top:20px"><div class="wrap post">{post['body']}
<p class="muted" style="margin-top:2.5em">Questions? Email us at <a href="mailto:{{email}}">{{email}}</a>.</p>
<p><a href="index.html">&larr; All articles</a></p></div></section>"""
        schema = [{"@context": "https://schema.org", "@type": "BlogPosting", "headline": post["h1"],
                   "datePublished": post["date"], "author": {"@type": "Organization", "name": "Evolved Innovations"},
                   "mainEntityOfPage": f"{SITE}/{path}"}]
        write(path, page(path, post["title"], post["desc"], body, schema, active="blog/index.html"))
        urls.append(path)

    sm = "".join(f"<url><loc>{SITE}/{'' if u == 'index.html' else u}</loc></url>" for u in urls)
    write("sitemap.xml", f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{sm}</urlset>\n')
    robots = "User-agent: *\nDisallow: /\n" if NOINDEX else f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n"
    write("robots.txt", robots)
    print(f"built {len(urls)} pages (noindex={NOINDEX})")


if __name__ == "__main__":
    main()
