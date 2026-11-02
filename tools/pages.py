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
      <span class="pill driver">Everyday Driver Series</span><h4>Make it by the gallon</h4>
      <p class="clamp"><b>Windshield washer fluid concentrate made for everyday drivers.</b> The Personal Vehicle line gives car, truck, and SUV owners a compact alternative to bulky ready-to-use washer fluid jugs. Each 8 oz bottle makes up to 32 gallons of finished windshield washer fluid, making it easy to mix, store, and refill at home or on the go. Designed for daily drivers, road trips, seasonal refills, and cleaner windshield visibility, this line delivers powerful performance in a small, easy-to-use bottle.</p>
      <button class="more" type="button">+ Show More</button>
    </div>
    <div class="card">
      <a href="{pre}fleet-bulk.html"><img src="{pre}images/card-fleet-bulk.webp" alt="Fleet and Bulk Series" width="339" height="339" loading="lazy"></a>
      <span class="pill fleet"><span>Fleet &amp; Bulk Series</span></span><h4>Make 55 Gallon Drums</h4>
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
    ("rain-655", "Evolved 6-55 Rain Away Bio-Based Windshield Washer Fluid Concentrate – 6 oz (Makes One 55-Gallon Drum)", "20.00", "p-655-rain", "p-655-rain-back", "fleet rainaway"),
    ("bug-655", "Evolved 6-55 Bug Away Bio-Based Windshield Washer Fluid Concentrate – 6 oz (Makes One 55-Gallon Drum)", "20.00", "p-655-bug", "p-655-bug-back", "fleet bugaway"),
]


def order_link(title):
    from urllib.parse import quote
    return "{pre}contact-us.html?product=" + quote(title)


def shop_page():
    def cards(series):
        out = ""
        for pid, t, price, front, back, cats in PRODUCTS:
            if series not in cats:
                continue
            out += f"""<div class="prod" id="{pid}" data-cat="{cats}">
<img src="{{pre}}images/{front}.webp" data-back="{{pre}}images/{back}.webp" alt="{t}" width="800" height="800" loading="lazy">
<h3>{t}</h3><div class="price">${price} USD</div><a class="btn sm" href="{order_link(t)}">Order</a></div>"""
        return out
    body = f"""<section><div class="wrap shop">
<aside id="cats">
  <a class="on" data-f="all">All Products</a>
  <a data-f="fleet">Fleet and Bulk Series Washer Fluid Concentrates</a>
  <a data-f="personal">Personal Vehicle Series Washer Fluid Concentrates</a>
  <a data-f="bugaway" id="bugaway">BugAway Bio-Based Washer Fluid Concentrate</a>
  <a data-f="rainaway" id="rainaway">RainAway Bio-Based Washer Fluid Concentrate</a>
</aside>
<div><div class="shop-head"><h4 id="cat-title">All Products</h4></div>
<div class="series driver">
  <div class="series-head driver"><div><h2>Everyday Driver Series</h2><p>8 oz bottles for cars, SUVs and pickups. Each makes 32 gallons.</p></div><span class="pill driver">8-32</span></div>
  <div class="grid3">{cards("personal")}</div></div>
<div class="series fleet">
  <div class="series-head fleet"><div><h2>Fleet &amp; Bulk Series</h2><p>Super concentrates for fleets, shops and bulk buyers. Makes 55-gallon drums.</p></div><span class="pill fleet"><span>6-55 &middot; 32-1760</span></span></div>
  <div class="grid3">{cards("fleet")}</div></div>
</div>
</div></section>"""
    schema = [{"@context": "https://schema.org", "@type": "Product", "name": t, "brand": {"@type": "Brand", "name": "EVOLVED"},
               "image": f"https://evolvedproducts.us/images/{front}.webp",
               "offers": {"@type": "Offer", "price": price, "priceCurrency": "USD", "availability": "https://schema.org/InStock"}}
              for pid, t, price, front, back, cats in PRODUCTS]
    return body, schema


def stat_band(cls, tiles):
    imgs = "".join(f'<img src="{{pre}}images/{f}.webp" alt="{a}" width="242" height="242" loading="lazy">' for f, a in tiles)
    return f'<section class="stat-band {cls}">{WAVE}<div class="wrap stats4">{imgs}</div></section>'


ICONS = {
    "bug": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4a3 3 0 0 1 3 3H9a3 3 0 0 1 3-3zM7 9h10v1.5l3-1.5.9 1.8-3.9 2V14h4v2h-4v.5a5 5 0 0 1-.6 2.4l3.5 2-1 1.7-3.6-2.1a5 5 0 0 1-6.6 0l-3.6 2.1-1-1.7 3.5-2A5 5 0 0 1 7 16.5V16H3v-2h4v-1.2l-3.9-2L4 9l3 1.5z"/></svg>',
    "drop": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2s7 7.6 7 12.5a7 7 0 0 1-14 0C5 9.6 12 2 12 2zm-3.5 12a.9.9 0 0 0-.9.9 4.4 4.4 0 0 0 4.4 4.4.9.9 0 0 0 0-1.8 2.6 2.6 0 0 1-2.6-2.6.9.9 0 0 0-.9-.9z"/></svg>',
    "cup": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 2h12l-1.6 18.2A2 2 0 0 1 14.4 22H9.6a2 2 0 0 1-2-1.8zm2.2 2 .4 5h6.8l.4-5zm.6 7 .8 9h4.8l.8-9z"/></svg>',
    "leaf": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M20 3s1 9-4.5 13.5C12 19.4 7.6 18.6 6.3 17.7L4.4 21l-1.7-1 2.2-3.6C3.8 14.6 3.6 11 6.6 8 10.9 3.7 20 3 20 3zM8.2 15.6c2.6-3.4 5.4-5.6 8.4-7.3-3.4 1-6.6 3.4-9.6 6.6z"/></svg>',
}

ORDER_BUG8 = "{pre}contact-us.html?product=Evolved%208-32%20Bug%20Away%20(8%20oz)"
ORDER_RAIN8 = "{pre}contact-us.html?product=Evolved%208-32%20Rain%20Away%20(8%20oz)"


def fleet_card(pid, img, name, makes, price):
    return f"""<a href="{{pre}}washer-fluid-concentrates.html#{pid}"><img src="{{pre}}images/{img}.webp" alt="Evolved {name}" width="242" height="300" loading="lazy"><div class="nm">{name}</div><div class="mk">{makes}</div><div class="pr">{price}</div></a>"""


FLEET = """<div class="t-fleet">
<section class="flt-hero"><div class="wrap split">
  <div>
    <span class="pill fleet"><span>Fleet &amp; Bulk Series</span></span>
    <h1 class="flt-display">Built for fleets.<br><span>Made to go further.</span></h1>
    <div class="limebar flt-display"><span>1 bottle makes 32&times; 55-gallon drums</span></div>
    <p class="lead">Bio-based washer fluid super concentrates for trucking fleets, dealerships, service shops and bulk operations. Stop paying to ship water.</p>
    <div class="btns"><a class="btn lime" href="{pre}contact-us.html?product=Fleet%20%26%20Bulk%20pricing">Get fleet pricing</a><a class="btn ghost" href="#bulk">See bulk sizes</a></div>
  </div>
  <div class="hexes">
    <div class="hex"><img src="{pre}images/hx-truck.webp" alt="Semi truck on a mountain highway" width="400" height="400"></div>
    <div class="hex lime"><img src="{pre}images/hx-vans.webp" alt="Row of fleet vans" width="400" height="400"></div>
    <div class="hex"><img src="{pre}images/hx-driver.webp" alt="Smiling truck driver in the cab" width="400" height="400"></div>
    <div class="hex"><img src="{pre}images/hx-bugs.webp" alt="Bug-covered windshield on the interstate" width="400" height="400"></div>
  </div>
</div></section>

<section class="spec-strip"><div class="wrap stats">
  <div><div class="n">1 oz</div><div class="l">of 32-1760 makes 55 gallons</div></div>
  <div><div class="n">1,760</div><div class="l">gallons per 32 oz bottle</div></div>
  <div><div class="n">32&times;</div><div class="l">fewer drums to ship</div></div>
  <div><div class="n">100%</div><div class="l">bio-based</div></div>
</div></section>

<section class="flt-dark" id="bulk"><div class="wrap">
  <h1 class="title">Bulk and Fleet Washer Fluid Concentrates</h1>
  <div class="fleet-cards">
    """ + fleet_card("bug-655", "p-655-bug", "6-55 BugAway", "6 oz bottle &middot; makes one 55-gallon drum", "$20") + """
    """ + fleet_card("rain-655", "p-655-rain", "6-55 RainAway", "6 oz bottle &middot; makes one 55-gallon drum", "$20") + """
    """ + fleet_card("bug-321760", "p-321760-bug", "32-1760 BugAway", "32 oz bottle &middot; makes thirty-two 55-gallon drums", "$99") + """
    """ + fleet_card("rain-321760", "p-321760-rain", "32-1760 RainAway", "32 oz bottle &middot; makes thirty-two 55-gallon drums", "$99") + """
  </div>
  <div class="sizes">
    <div><b>6-55</b><span>A separate formula. Pour the whole 6 oz bottle into one 55-gallon drum and fill with water. Nothing to measure. Best for one drum at a time, or to try EVOLVED.</span></div>
    <div><b>32-1760</b><span>The more concentrated formula. Measure 1 oz with the built-in chamber for each 55-gallon drum. One bottle does 32 drums at the lowest cost per gallon.</span></div>
  </div>
</div></section>

<section><div class="wrap">
  <h2 class="title">One bottle = thirty-two drums</h2>
  <div class="split">
    <img src="{pre}images/f-warehouse-wide.webp" alt="1 bottle makes 32 55-gallon drums of windshield washer fluid. That's 1,760 gallons total." width="1400" height="700" loading="lazy">
    <ul class="bullets">
      <li>32-1760: 1 oz of concentrate &rarr; one 55-gallon drum of finished fluid</li>
      <li>32-1760: one 32 oz bottle &rarr; thirty-two 55-gallon drums (1,760 gallons)</li>
      <li>Built-in 1 oz measuring chamber, so every drum gets the same dose</li>
      <li>Smaller bottles, lower freight, easier reordering</li>
      <li>Less plastic, less warehouse space, less waste</li>
    </ul>
  </div>
</div></section>

<section style="background:#eef4fd"><div class="wrap">
  <h2 class="title">Who it's built for</h2>
  <div class="who">
    <div><div class="hex"><img src="{pre}images/hx-vans.webp" alt="" width="400" height="400" loading="lazy"></div><b>Fleets</b><span>Trucking, delivery, rental and municipal fleets</span></div>
    <div><div class="hex"><img src="{pre}images/hx-wheel.webp" alt="" width="400" height="400" loading="lazy"></div><b>Service shops</b><span>Quick lubes, repair shops and dealerships</span></div>
    <div><div class="hex"><img src="{pre}images/hx-rain.webp" alt="" width="400" height="400" loading="lazy"></div><b>Car washes</b><span>Top off every vehicle that comes through</span></div>
    <div><div class="hex"><img src="{pre}images/hx-truck.webp" alt="" width="400" height="400" loading="lazy"></div><b>Bulk buyers</b><span>Farms, schools and anyone filling drums</span></div>
  </div>
</div></section>

<section><div class="wrap">
  <h2 class="title">Two formulas. Every season.</h2>
  <div class="flyer2">
    <img src="{pre}images/f-fleet-bug-built.webp" alt="BugAway 32 oz: built for fleets, made to go further. Removes bugs and grime." width="1254" height="1254" loading="lazy">
    <img src="{pre}images/f-fleet-rain-built.webp" alt="RainAway 32 oz: built for fleets, made to go further. Cleans and repels rain." width="1254" height="1254" loading="lazy">
  </div>
</div></section>

<section class="flt-cta"><div class="wrap">
  <h2 class="flt-display">Running 5 trucks or 500?</h2>
  <p>Tell us how many vehicles you run and how much washer fluid you go through. We'll send pricing and shipping for your volume.</p>
  <div class="btns" style="justify-content:center"><a class="btn lime" href="{pre}contact-us.html?product=Fleet%20%26%20Bulk%20pricing">Get fleet pricing</a><a class="btn ghost" href="tel:+18667279411">Call {phone}</a></div>
</div></section>
""" + faq_block() + """
</div>"""


def badge(icon, title, sub):
    return f'<div class="badge"><div class="ic">{ICONS[icon]}</div><b>{title}</b><span>{sub}</span></div>'


PERSONAL = """<div class="t-driver">
<section class="drv-hero"><div class="wrap split">
  <div>
    <span class="pill driver">Everyday Driver Series</span>
    <h1><em>Clean</em> for summer.<br><b>Clarity</b> for rain.</h1>
    <p class="lead">Bio-based washer fluid concentrates for cars, SUVs and pickups. One 8 oz bottle makes 32 gallons, so you never haul another heavy jug home.</p>
    <div class="btns"><a class="btn green" href="#formulas">Shop BugAway</a><a class="btn blue" href="#formulas">Shop RainAway</a></div>
  </div>
  <img src="{pre}images/card-everyday-driver.webp" alt="Everyday Driver Series for cars, SUVs and pickups" width="696" height="696">
</div></section>

<section><div class="wrap badges">
  """ + badge("bug", "Removes bugs", "and road grime") + badge("drop", "Repels rain", "water-beading action") + badge("cup", "1/4 oz = 1 gallon", "built-in measuring chamber") + badge("leaf", "Bio-based", "plant-derived formula") + """
</div></section>

<section class="sky" id="formulas"><div class="wrap">
  <h2 class="title">Choose Your Formula</h2>
  <div class="formula2">
    <div class="fcard" id="bugaway"><img src="{pre}images/f-bug-power.webp" alt="BugAway: bug removal power. Removes bugs and road grime. Before and after." width="1254" height="1254" loading="lazy">
      <div class="in"><h3>BugAway</h3><div class="price">$24 &middot; 8 oz makes 32 gallons</div>
      <ul><li>Removes bugs and road grime</li><li>Loosens stubborn residue</li><li>Streak-free clarity for summer driving</li></ul>
      <a class="btn green" href=\"""" + ORDER_BUG8 + """\">Order BugAway</a></div></div>
    <div class="fcard rain" id="rainaway"><img src="{pre}images/f-rain-action.webp" alt="RainAway: rain repellent action. Repels rain and improves visibility. Before and after." width="1254" height="1254" loading="lazy">
      <div class="in"><h3>RainAway</h3><div class="price">$24 &middot; 8 oz makes 32 gallons</div>
      <ul><li>Water-beading action</li><li>Clearer views in rainy conditions</li><li>Streak-free clarity</li></ul>
      <a class="btn blue" href=\"""" + ORDER_RAIN8 + """\">Order RainAway</a></div></div>
  </div>
</div></section>

<section><div class="wrap split">
  <img class="round" src="{pre}images/f-chamber.webp" alt="Built-in measuring chamber: measure 1/4 oz directly from the bottle, no extra measuring cup needed" width="1254" height="1254" loading="lazy">
  <div><h2>Mixing takes 30 seconds</h2>
    <ol class="steps">
      <li><b>Fill the chamber</b>Fill the built-in measuring chamber to the 1/4 oz line. No measuring cup needed.</li>
      <li><b>Pour it in</b>Pour the dose into an empty 1-gallon jug.</li>
      <li><b>Add water</b>Top it off with water, cap it and give it a shake. Your washer fluid is ready.</li>
    </ol></div>
</div></section>

<section class="drv-band"><div class="wrap stats">
  <div><div class="n">1/4 oz</div><div class="l">makes 1 gallon</div></div>
  <div><div class="n">32</div><div class="l">gallons per 8 oz bottle</div></div>
  <div><div class="n">32</div><div class="l">plastic jugs kept out of the landfill</div></div>
  <div><div class="n">100%</div><div class="l">bio-based</div></div>
</div></section>

<section><div class="wrap split">
  <div><h2>Less plastic. Less storage.</h2>
    <p style="margin-top:16px">One 8 oz bottle replaces 32 one-gallon jugs. It fits in a garage shelf, a glove box or a road-trip bag, and you only add the water you already have at home.</p>
    <div class="btns"><a class="btn green" href="#formulas">Pick your formula</a></div></div>
  <img class="round" src="{pre}images/f-less-storage.webp" alt="Less plastic, less storage. One 8 oz bottle replaces 32 one-gallon jugs." width="1254" height="1254" loading="lazy">
</div></section>

<section class="sky"><div class="wrap">
  <h2 class="title">Photo Gallery</h2>
  <div class="gallery round">
    <img src="{pre}images/f-podium-bug.webp" alt="BugAway 8 oz bottle with its features" width="1080" height="1080" loading="lazy">
    <img src="{pre}images/g12-rain.webp" alt="Clearer views in the rain" width="725" height="725" loading="lazy">
    <img src="{pre}images/g13-grime.webp" alt="Real road grime. Real cleaning power. Tough on bugs, clear on glass" width="725" height="725" loading="lazy">
  </div>
</div></section>
""" + faq_block() + """
</div>"""


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
