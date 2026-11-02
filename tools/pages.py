"""Page bodies, copied from the original GoDaddy site (Nov 2026) with only
small fixes: placeholder text replaced, Gmail -> Tyler@evolvedproducts.us,
"Evovled" typo fixed, prices per Tyler (8 oz $24, 32 oz $99, 6 oz $20 = old store price).
{pre} = relative path prefix, {email}, {phone}.
"""
import re

WAVE = '<svg class="wave" viewBox="0 0 1200 120" preserveAspectRatio="none" aria-hidden="true"><path d="M0,60 C200,90 400,30 600,60 C800,90 1000,30 1200,60 L1200,120 L0,120 Z" fill="currentColor"/></svg>'

FAQ = [
    ("Can I use this in the winter?",
     "The formulas are designed for above-freezing use. For freezing temperatures, follow the methanol mixing chart for your desired freeze protection."),
    ("Are the formulas bio-based?",
     "Yes, both BugAway and RainAway are built with plant-derived cleaning agents."),
    ("What makes Evolved better than other washer fluid concentrates?",
     "All of our products have special ingredients to keep your washer fluid system clean and corrosion free. Other concentrates and tablets cause clogged nozzles and can ruin your washer fluid pumps."),
]


def faq_block(title_cls=""):
    items = "".join(f'<details><summary>{q}</summary><div class="ans">{a}</div></details>' for q, a in FAQ)
    return f"""<section><div class="wrap narrow faq">
<h2 class="title{title_cls}">Frequently Asked Questions</h2>
<p class="faq-intro">Please reach us at <a href="mailto:{{email}}">{{email}}</a> if you cannot find an answer to your question.</p>
{items}</div></section>"""


FAQ_SCHEMA = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
    {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ]}

CONTACT_FORM = """<form class="cform" id="contact-form">
  <input name="name" placeholder="Name" autocomplete="name" aria-label="Name">
  <input name="email" type="email" placeholder="Email*" required autocomplete="email" aria-label="Email">
  <input name="product" type="hidden">
  <textarea name="msg" placeholder="Message" aria-label="Message"></textarea>
  <button class="btn" type="submit">Send</button>
  <p class="note">Send opens your email app with your message ready to go.</p>
</form>"""

GALLERY = [
    ("g01-bugs-happen", "Bugs happen. BugAway removes bugs and road grime"),
    ("g02-summertime", "Summertime washer fluid concentrate"),
    ("g03", "EVOLVED washer fluid concentrate"),
    ("card-everyday-driver", "Everyday Driver Series for cars, SUVs and pickups"),
    ("g05-bug-removal", "BugAway bug removal power"),
    ("g06", "RainAway rain repellent concentrate"),
    ("card-fleet-bulk", "Fleet and Bulk Series"),
    ("g08", "EVOLVED Personal Vehicle Series"),
    ("fleet-hero", "Innovation in every drop. Concentrates for fleets and bulk operations"),
    ("g10-drums", "One bottle equals thirty-two 55-gallon drums"),
    ("g11", "EVOLVED built-in measuring chamber"),
    ("g12-rain", "Clearer views in the rain"),
    ("g13-grime", "Real road grime. Real cleaning power"),
    ("g14-roadtrip", "Road trip ready"),
    ("g15-amazon", "EVOLVED washer fluid concentrate"),
    ("g16-832", "EVOLVED 8-32 concentrate"),
]


def carousel():
    slides = "".join(f'<img src="{{pre}}images/{f}.webp" alt="{a}" width="600" height="600" loading="lazy">' for f, a in GALLERY)
    thumbs = "".join(f'<img src="{{pre}}images/{f}.webp" alt="" width="70" height="70" loading="lazy">' for f, a in GALLERY)
    return f"""<div class="carousel" id="carousel"><button class="arrow prev" aria-label="Previous">&#8249;</button><div class="track">{slides}</div><button class="arrow next" aria-label="Next">&#8250;</button></div>
<div class="thumbs" id="thumbs">{thumbs}</div>"""


HOME = """
<section><div class="wrap">
  <h1 class="title navy">Choose Your Washer Fluid Formula</h1>
  <div class="tiles">
    <a href="{pre}washer-fluid-concentrates.html#bugaway"><img src="{pre}images/tile-bugaway.webp" alt="BugAway: bug removal power. Removes bugs and road grime" width="435" height="470"></a>
    <a href="{pre}washer-fluid-concentrates.html#rainaway"><img src="{pre}images/tile-rainaway.webp" alt="RainAway: rain repellent action. Repels rain and improves visibility" width="435" height="470"></a>
  </div>
</div></section>

<section class="beige"><div class="wrap">
  <h2 class="title">Make washer fluid by the gallon or by the drum</h2>
  <div class="cards2">
    <div class="card">
      <a href="{pre}personal-vehicle.html"><img src="{pre}images/card-everyday-driver.webp" alt="Everyday Driver Series for cars, SUVs and pickups" width="339" height="339" loading="lazy"></a>
      <h4>Make it by the gallon</h4>
      <p class="clamp"><b>Windshield washer fluid concentrate made for everyday drivers.</b> The Personal Vehicle line gives car, truck, and SUV owners a compact alternative to bulky ready-to-use washer fluid jugs. Each 8 oz bottle makes up to 32 gallons of finished windshield washer fluid, making it easy to mix, store, and refill at home or on the go. Designed for daily drivers, road trips, seasonal refills, and cleaner windshield visibility, this line delivers powerful performance in a small, easy-to-use bottle.</p>
      <button class="more" type="button">+ Show More</button>
    </div>
    <div class="card">
      <a href="{pre}fleet-bulk.html"><img src="{pre}images/card-fleet-bulk.webp" alt="Fleet and Bulk Series" width="339" height="339" loading="lazy"></a>
      <h4>Make 55 Gallon Drums</h4>
      <p class="clamp"><b>Bulk windshield washer fluid concentrate for fleets, shops, and commercial use.</b> The Fleet &amp; Bulk line is designed for businesses that need dependable washer fluid in high volumes without the cost, space, and waste of shipping water. With concentrated formulas that make 55-gallon drums or up to 1,760 gallons of finished washer fluid, Fleet &amp; Bulk helps service centers, dealerships, trucking companies, municipalities, and fleet operators reduce storage needs while keeping vehicles ready for the road.</p>
      <button class="more" type="button">+ Show More</button>
    </div>
  </div>
</div></section>

<section class="video-band"><div class="wrap split">
  <video controls preload="none" poster="{pre}images/video-poster.webp" playsinline><source src="{pre}media/how-to-use-concentrates.mp4" type="video/mp4"></video>
  <div><h4>How to use the concentrates</h4><p>Measure the concentrate with the built-in measuring chamber, pour it into your jug or drum, and add water. That's it.</p></div>
</div></section>

<section class="mission"><div class="wrap">
  <h2 class="title navy">Small Bottles. Big Impact</h2>
  <div class="split">
    <img src="{pre}images/mission-collage.webp" alt="Every step of the journey. Follow us @evolved.innovations" width="532" height="532" loading="lazy">
    <div class="txt">
      <h4>Our Mission</h4>
      <p>It started with smaller bottles, smarter formulas, and better decisions at the design level. We're committed to building products that help people see clearer, clean smarter, and delivering bio-based solutions that outperform traditional formulas.</p>
      <p style="margin-top:24px"><a class="btn" href="{pre}about.html">Learn More</a></p>
    </div>
  </div>
</div></section>

<section><div class="wrap">
  <h2 class="title navy">100% BIODEGRADABLE. ZERO COMPROMISE.</h2>
  """ + carousel() + """
</div></section>

<section class="photo-band" style="background-image:url('{pre}images/bg-testimonials.webp')"><div class="wrap">
  <h2>Testimonials that speak for us!</h2>
  <div class="bar">Reviews coming soon!</div>
</div></section>

""" + faq_block() + """

<section><div class="wrap narrow">
  <h2 class="title">Contact Us</h2>
  <h4 class="center">We love our customers. Feel free to drop us a line!</h4>
  """ + CONTACT_FORM + """
</div></section>
"""

ABOUT = """
<section><div class="wrap">
  <h1 class="title">About EVOLVED</h1>
  <div class="zig">
    <img src="{pre}images/about-mission.webp" alt="Driver looking through a clear windshield" width="532" height="266">
    <div class="txt"><h4>Our Mission</h4><p>For decades, <b>washer fluid</b> has been built around single-use plastic jugs tossed after one use.<br>At <b>Evolved Innovations</b>, we believe it's time for something better.</p></div>
  </div>
  <div class="zig">
    <div class="txt"><h4>Why we exist</h4><p>We exist to <b>eliminate unnecessary waste</b> without asking people to compromise on performance.<br>Sustainability shouldn't feel like a downgrade. It should feel like an upgrade: smarter, more efficient, and more intentional. That belief drives every formula we create and every product we release.</p></div>
    <img src="{pre}images/about-why.webp" alt="Bug-spattered windshield on an open road" width="532" height="266" loading="lazy">
  </div>
  <div class="zig">
    <img src="{pre}images/about-how.webp" alt="View through a clean windshield on a mountain road" width="532" height="266" loading="lazy">
    <div class="txt"><h4>How we do it</h4><p>We spent years engineering <b>high-performance concentrates</b> that put control back in your hands.<br>Instead of paying to ship water and plastic, we design products that let you add what you already have, <b>water</b>, at home. The result is dramatically less waste, lower costs, and better performance per ounce.</p></div>
  </div>
  <div class="zig">
    <div class="txt"><h4>Built for the long-haul</h4><p>We're not a trend brand or a one-product experiment. We're building a platform of <b>environmentally responsible concentrates</b>, designed with the same philosophy: fewer materials, smarter formulas, better results.<br>We design products the way they <i>should have been made all along</i>.</p></div>
    <img src="{pre}images/about-longhaul.webp" alt="EI EVOLVED Environmental Innovations" width="532" height="266" loading="lazy">
  </div>
</div></section>
<section class="photo-band" style="background-image:url('{pre}images/bg-reviews.webp')"><div class="wrap">
  <h2>Reviews</h2><div class="bar">Reviews coming soon!</div>
</div></section>
"""

PRODUCTS = [
    # id, title, price, front, back, categories
    ("rain-832", "Evolved 8-32 Rain Away Windshield Washer Fluid Concentrate – 8 oz (Makes 32 Gallons)", "24.00", "p-832-rain", "p-832-rain-back", "personal rainaway"),
    ("bug-832", "Evolved 8-32 Bug Away Windshield Washer Fluid Concentrate – 8 oz (Makes 32 Gallons)", "24.00", "p-832-bug", "p-832-bug-back", "personal bugaway"),
    ("bug-321760", "Evolved 32-1760 Bug Away Bio-Based Windshield Washer Fluid Concentrate – 32 oz (Makes 1,760 Gallons)", "99.00", "p-321760-bug", "p-321760-bug-back", "fleet bugaway"),
    ("rain-321760", "Evolved 32-1760 Rain Away Bio-Based Windshield Washer Fluid Concentrate – 32 oz (Makes 1,760 Gallons)", "99.00", "p-321760-rain", "p-321760-rain-back", "fleet rainaway"),
    ("rain-655", "Evolved 6-55 Rain Away Bio-Based Windshield Washer Fluid Concentrate", "20.00", "p-655-rain", "p-655-rain-back", "fleet rainaway"),
    ("bug-655", "Evolved 6-55 Bug Away Bio-Based Windshield Washer Fluid Concentrate", "20.00", "p-655-bug", "p-655-bug-back", "fleet bugaway"),
]


def order_link(title):
    from urllib.parse import quote
    return "{pre}contact-us.html?product=" + quote(title)


def shop_page():
    cards = ""
    for pid, t, price, front, back, cats in PRODUCTS:
        cards += f"""<div class="prod" id="{pid}" data-cat="{cats}">
<img src="{{pre}}images/{front}.webp" data-back="{{pre}}images/{back}.webp" alt="{t}" width="800" height="800" loading="lazy">
<h3>{t}</h3><div class="price">${price} USD</div><a class="btn sm" href="{order_link(t)}">Order</a></div>"""
    body = f"""<section><div class="wrap shop">
<aside id="cats">
  <a class="on" data-f="all">All Products</a>
  <a data-f="fleet">Fleet and Bulk Series Washer Fluid Concentrates</a>
  <a data-f="personal">Personal Vehicle Series Washer Fluid Concentrates</a>
  <a data-f="bugaway" id="bugaway">BugAway Bio-Based Washer Fluid Concentrate</a>
  <a data-f="rainaway" id="rainaway">RainAway Bio-Based Washer Fluid Concentrate</a>
</aside>
<div><div class="shop-head"><h4 id="cat-title">All Products</h4></div>
<div class="grid3">{cards}</div></div>
</div></section>"""
    schema = [{"@context": "https://schema.org", "@type": "Product", "name": t, "brand": {"@type": "Brand", "name": "EVOLVED"},
               "image": f"https://evolvedproducts.us/images/{front}.webp",
               "offers": {"@type": "Offer", "price": price, "priceCurrency": "USD", "availability": "https://schema.org/InStock"}}
              for pid, t, price, front, back, cats in PRODUCTS]
    return body, schema


def stat_band(cls, tiles):
    imgs = "".join(f'<img src="{{pre}}images/{f}.webp" alt="{a}" width="242" height="242" loading="lazy">' for f, a in tiles)
    return f'<section class="stat-band {cls}">{WAVE}<div class="wrap stats4">{imgs}</div></section>'


FLEET = """
<div class="hero-img"><img src="{pre}images/fleet-hero.webp" alt="Innovation in every drop. Super concentrates for fleets and bulk operations." width="1920" height="1080"></div>
<section><div class="wrap">
  <h1 class="title">Bulk and Fleet Washer Fluid Concentrates</h1>
  <div class="cards4">
    <a class="c" href="{pre}washer-fluid-concentrates.html#bug-655" style="text-decoration:none"><img src="{pre}images/p-655-bug.webp" alt="Evolved 6-55 Bug Away" width="242" height="323" loading="lazy"><h4>Makes 1 - 55 Gallon Drum</h4><div class="price">$20</div></a>
    <a class="c" href="{pre}washer-fluid-concentrates.html#rain-655" style="text-decoration:none"><img src="{pre}images/p-655-rain.webp" alt="Evolved 6-55 Rain Away" width="242" height="323" loading="lazy"><h4>Makes 1 - 55 Gallon Drum</h4><div class="price">$20</div></a>
    <a class="c" href="{pre}washer-fluid-concentrates.html#bug-321760" style="text-decoration:none"><img src="{pre}images/p-321760-bug.webp" alt="Evolved 32-1760 Bug Away" width="242" height="323" loading="lazy"><h4>Makes 32 - 55 Gallon Drums</h4><div class="price">$99</div></a>
    <a class="c" href="{pre}washer-fluid-concentrates.html#rain-321760" style="text-decoration:none"><img src="{pre}images/p-321760-rain.webp" alt="Evolved 32-1760 Rain Away" width="242" height="323" loading="lazy"><h4>Makes 32 - 55 Gallon Drums</h4><div class="price">$99</div></a>
  </div>
</div></section>
""" + stat_band("navy-bg", [("stat-1oz", "1 oz makes a 55-gallon drum"), ("stat-32oz", "32 oz makes 1,760 gallons"), ("stat-32x", "32x fewer drums to ship"), ("stat-100", "100% Bio-Based")]) + """
<section><div class="wrap">
  <h2 class="title">One Bottle = Thirty-Two Drums</h2>
  <img src="{pre}images/g10-drums.webp" alt="RainAway 32 oz bottle in front of rows of 55-gallon drums" width="1112" height="556" loading="lazy" style="width:100%">
  <ul class="bullets">
    <li>1 oz of concentrate &rarr; 55 gallon drum of finished fluid</li>
    <li>32 oz bottle &rarr; thirty-two 55-gallon drums</li>
    <li>Smaller bottles, lower freight, easier reordering</li>
    <li>Less plastic, less warehouse space, less waste</li>
  </ul>
</div></section>
""" + faq_block()

PERSONAL = """
<section class="pv-hero"><div class="wrap split">
  <div><h1>Bio-Based Concentrates</h1>
    <p>BugAway removes bugs, grime and stubborn residue.</p>
    <p>RainAway delivers water-beading action for clearer wet-weather visibility.</p>
    <p>Proven results that speak for themselves.</p></div>
  <img src="{pre}images/pv-hero.webp" alt="Personal Vehicle Series. Clean for summer. Clarity for rain." width="696" height="696">
</div></section>
<section><div class="wrap">
  <h2 class="title">Choose Your Formula</h2>
  <div class="cards2">
    <div class="card"><a href="{pre}washer-fluid-concentrates.html#bug-832"><img src="{pre}images/pv-bugaway.webp" alt="BugAway 8 oz makes 32 gallons" width="339" height="339" loading="lazy"></a>
      <h4>BugAway &middot; $24</h4><p>Removes bugs and road grime and loosens stubborn residue. Great for summer driving. One 8 oz bottle makes 32 gallons.</p>
      <a class="btn sm" href="{pre}contact-us.html?product=Evolved%208-32%20Bug%20Away%20(8%20oz)">Order</a></div>
    <div class="card"><a href="{pre}washer-fluid-concentrates.html#rain-832"><img src="{pre}images/pv-rainaway.webp" alt="RainAway 8 oz makes 32 gallons" width="339" height="339" loading="lazy"></a>
      <h4>RainAway &middot; $24</h4><p>Repels rain with water-beading action for great visibility in rainy conditions. One 8 oz bottle makes 32 gallons.</p>
      <a class="btn sm" href="{pre}contact-us.html?product=Evolved%208-32%20Rain%20Away%20(8%20oz)">Order</a></div>
  </div>
</div></section>
""" + stat_band("deep-bg", [("stat-quarter-oz", "1/4 oz makes 1 gallon"), ("stat-8oz", "8 oz makes 32 gallons"), ("stat-32jugs", "32 gallon jugs saved from the landfill"), ("stat-100", "100% Bio-Based")]) + """
<section><div class="wrap">
  <h2 class="title" style="color:var(--navy-deep)">Photo Gallery</h2>
  <div class="gallery">
    <img src="{pre}images/pv-less-plastic.webp" alt="Less plastic. Less storage. One 8 oz bottle replaces 32 one-gallon jugs" width="725" height="725" loading="lazy">
    <img src="{pre}images/g12-rain.webp" alt="Clearer views in the rain" width="725" height="725" loading="lazy">
    <img src="{pre}images/g13-grime.webp" alt="Real road grime. Real cleaning power. Tough on bugs, clear on glass" width="725" height="725" loading="lazy">
  </div>
</div></section>
""" + faq_block()

CONTACT = """
<section><div class="wrap narrow">
  <h1 class="title">Contact Us</h1>
  <h4 class="center">We love our customers. Feel free to drop us a line!</h4>
  """ + CONTACT_FORM + """
  <div class="center" style="margin-top:48px">
    <h4>EVOLVED Innovations</h4>
    <p>Sioux Falls, SD 57104</p>
    <p><a href="tel:+18667279411">{phone}</a><br><a href="mailto:{email}">{email}</a></p>
  </div>
</div></section>
"""

PRIVACY = """
<section><div class="wrap post">
<h1 class="title">Privacy Policy</h1>
<p>Last updated November 2, 2026. This website is run by Evolved Innovations in Sioux Falls, South Dakota.</p>
<h2>What we collect</h2>
<p>This site does not use advertising trackers and does not set cookies. The contact form doesn't store anything on our servers. It opens your own email app with your message filled in, and you decide whether to send it. If you email or call us, we use your information only to answer you and fill your order.</p>
<h2>Sharing</h2>
<p>We don't sell your information. We share it only when needed to fill your order, such as giving a shipping address to a carrier, or when the law requires it.</p>
<h2>Website hosting</h2>
<p>Our hosting provider may keep standard server logs, such as IP addresses and pages requested, for security and reliability.</p>
<h2>Contact</h2>
<p>Questions? Email <a href="mailto:{email}">{email}</a>.</p>
</div></section>
"""

_shop_body, _shop_schema = shop_page()

PAGES = [
    {"path": "index.html", "title": "EVOLVED | Bio-Based Windshield Washer Fluid Concentrate",
     "desc": "EVOLVED bio-based windshield washer fluid concentrates. BugAway and RainAway. Make washer fluid by the gallon or by the 55-gallon drum.",
     "body": HOME, "schema": [FAQ_SCHEMA]},
    {"path": "about.html", "title": "About EVOLVED: Eco-Friendly Cleaning Solutions",
     "desc": "Discover EVOLVED's environmentally responsible cleaning products, featuring eco-friendly solutions and high-performance concentrates for sustainable cleaning.",
     "body": ABOUT},
    {"path": "washer-fluid-concentrates.html", "title": "Washer Fluid Concentrates | EVOLVED",
     "desc": "Shop EVOLVED windshield washer fluid concentrates: BugAway and RainAway in 8 oz (makes 32 gallons), 32 oz (makes 1,760 gallons) and 6-55 sizes.",
     "body": _shop_body, "schema": _shop_schema},
    {"path": "fleet-bulk.html", "title": "Fleet & Bulk Washer Fluid Concentrates | EVOLVED",
     "desc": "Shop our bio-based washer fluid concentrates for fleet and bulk needs. Maximize efficiency with less waste and improved cleaning power.",
     "body": FLEET, "schema": [FAQ_SCHEMA]},
    {"path": "personal-vehicle.html", "title": "Personal Vehicle Washer Fluid Concentrate | EVOLVED",
     "desc": "Eco-friendly washer fluid concentrate that makes 32 gallons from one bottle. Perfect for vehicle cleaning without bulky jugs.",
     "body": PERSONAL, "schema": [FAQ_SCHEMA]},
    {"path": "contact-us.html", "title": "Contact Us | EVOLVED",
     "desc": "Contact EVOLVED Innovations in Sioux Falls, SD. Order washer fluid concentrate or ask a question.",
     "body": CONTACT},
    {"path": "privacy-policy.html", "title": "Privacy Policy | EVOLVED",
     "desc": "Privacy policy for evolvedproducts.us.", "body": PRIVACY},
]
