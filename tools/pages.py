"""Page bodies. {pre} = relative path prefix, {email} = contact email.

Claim rules (Nov 2, 2026): no "certified" bio-based until USDA BioPreferred
decides; no "100% biodegradable" or "outperforms" without test data; current
formulas are warm-weather and WILL FREEZE, so say so plainly.
"""

FREEZE_NOTICE = """<div class="notice"><div class="ico">&#10052;</div><p><b>Warm-weather formula.</b> Mixed fluid will freeze. Use it when temperatures stay above 32&deg;F, and switch to a winter-rated washer fluid before freezing weather. Winter mixing instructions are coming soon.</p></div>"""

HOME = """
<section class="hero"><div class="wrap">
  <div>
    <span class="eyebrow">Bio-based washer fluid concentrate</span>
    <h1>Clean glass. No jugs. Just add water.</h1>
    <p class="lead">EVOLVED is windshield washer fluid in concentrate form. One 32 oz bottle makes up to 1,760 gallons. You add the water at home or at the shop, so nobody ships it across the country in plastic jugs.</p>
    <div class="btns"><a class="btn green" href="{pre}personal-vehicle.html">For my vehicle</a><a class="btn ghost" href="{pre}fleet-bulk.html">For my fleet or shop</a></div>
  </div>
  <div class="hero-bottles">
    <img src="{pre}images/bugaway-32oz-front.webp" alt="EVOLVED Bug Away 32 oz washer fluid concentrate bottle" width="900" height="900">
    <img src="{pre}images/rainaway-32oz-front.webp" alt="EVOLVED Rain Away 32 oz washer fluid concentrate bottle" width="900" height="910">
  </div>
</div></section>

<div class="wrap"><div class="stats">
  <div class="stat"><b>1 oz</b><span>makes a 55-gallon drum</span></div>
  <div class="stat"><b>1,760 gal</b><span>from one 32 oz bottle</span></div>
  <div class="stat"><b>32 gal</b><span>from one 8 oz bottle</span></div>
</div></div>

<section><div class="wrap">
  <div class="center" style="max-width:720px;margin:0 auto 36px"><span class="eyebrow">Two formulas</span><h2>Pick the job you need done</h2>
  <p class="lead">Both formulas come in the same concentrate bottle and mix the same way.</p></div>
  <div class="grid2">
    <div class="card logo-card center"><img src="{pre}images/bugaway-logo.webp" alt="Bug Away logo" width="700" height="458" loading="lazy">
      <h3>Bug Away</h3><p class="muted">Made for bug season and summer road trips, when the windshield collects bugs and road grime.</p>
      <span class="tag">Removes bugs</span></div>
    <div class="card logo-card center"><img src="{pre}images/rainaway-logo.webp" alt="Rain Away logo" width="700" height="452" loading="lazy">
      <h3>Rain Away</h3><p class="muted">Made for rainy days, so water beads up and your view stays clear.</p>
      <span class="tag sky">Repels rain</span></div>
  </div>
</div></section>

<section class="alt"><div class="wrap">
  <div class="center" style="max-width:720px;margin:0 auto 36px"><span class="eyebrow">How it works</span><h2>Three steps, about a minute</h2></div>
  <div class="steps">
    <div class="step"><h3>Measure</h3><p>Measure the concentrate. The 32 oz bottle has a built-in 1 oz measuring chamber, so there's no cup to clean.</p></div>
    <div class="step"><h3>Pour</h3><p>Pour the measured concentrate into a gallon jug, a tank or a 55-gallon drum.</p></div>
    <div class="step"><h3>Add water</h3><p>Fill with water and it's ready for the washer reservoir.</p></div>
  </div>
  <p class="center" style="margin-top:28px"><a class="btn" href="{pre}how-to-mix.html">See full mixing directions</a></p>
</div></section>

<section><div class="wrap split">
  <div>
    <span class="eyebrow">Why concentrate</span>
    <h2>Stop paying to ship water</h2>
    <p>Ready-to-use washer fluid is mostly water. It gets bottled in plastic jugs, loaded on trucks and driven to a store, and then you haul it home. Water weighs about 8.3 pounds a gallon.</p>
    <p>EVOLVED skips that. The bottle holds only the concentrate. You add the water where you use it.</p>
    <ul class="checks">
      <li>One 32 oz bottle makes as much fluid as 1,760 one-gallon jugs</li>
      <li>Far less plastic to buy, store and throw away</li>
      <li>One small bottle on the shelf instead of pallets of jugs</li>
    </ul>
  </div>
  <div><img src="{pre}images/rainaway-32oz-front.webp" alt="Rain Away 32 oz bottle, makes 1,760 gallons" width="900" height="910" loading="lazy"></div>
</div></section>

<section class="alt2"><div class="wrap">""" + FREEZE_NOTICE + """</div></section>

<section class="dark"><div class="wrap split">
  <div><span class="eyebrow">Fleets, shops &amp; dealerships</span><h2>Built for 55-gallon drums</h2>
  <p class="lead">Service centers, dealerships, trucking companies, municipalities and fleets can make a full drum from a single ounce.</p></div>
  <div class="btns" style="justify-content:flex-end"><a class="btn green" href="{pre}fleet-bulk.html">Fleet &amp; bulk details</a><a class="btn ghost" style="color:#fff;border-color:#fff" href="{pre}contact.html?topic=quote">Get a quote</a></div>
</div></section>

<section><div class="wrap" style="max-width:820px">
  <div class="center"><span class="eyebrow">FAQ</span><h2>Common questions</h2></div>
  <details><summary>How much water do I add?</summary><div class="ans">For the 32 oz bottle, add 1 oz of concentrate to 55 gallons of water. For the 8 oz bottle, add 1/4 oz to each gallon of water. Full directions are on the <a href="{pre}how-to-mix.html">How to Mix</a> page.</div></details>
  <details><summary>Can I use it in winter?</summary><div class="ans">Not yet. The current formulas are warm-weather formulas, and the mixed fluid will freeze. Switch to a winter-rated washer fluid before temperatures drop below 32&deg;F.</div></details>
  <details><summary>Is it certified bio-based?</summary><div class="ans">We've applied to the USDA BioPreferred&reg; Program and are waiting on their decision. We'll post an update here when we hear back.</div></details>
  <p class="center"><a href="{pre}faq.html">More questions &rarr;</a></p>
</div></section>
"""

PERSONAL = """
<section class="page-hero"><div class="wrap">
  <span class="eyebrow">Personal vehicle</span>
  <h1>Make washer fluid by the gallon</h1>
  <p class="lead">For car, truck and SUV owners. One 8 oz bottle of EVOLVED concentrate makes up to 32 gallons of washer fluid. That's a lot of fill-ups from one small bottle in the garage.</p>
  <div class="btns"><a class="btn green" href="{pre}contact.html?topic=order">Order now</a><a class="btn ghost" href="{pre}how-to-mix.html">How to mix</a></div>
</div></section>

<section><div class="wrap">
  <div class="grid2">
    <div class="card logo-card center"><img src="{pre}images/bugaway-logo.webp" alt="Bug Away logo" width="700" height="458" loading="lazy">
      <h3>Bug Away &middot; 8 oz</h3><p class="muted">Makes up to 32 gallons. Made for bug season and highway miles.</p>
      <a class="btn green sm" href="{pre}contact.html?topic=order&amp;product=Bug%20Away%208%20oz">Order Bug Away</a></div>
    <div class="card logo-card center"><img src="{pre}images/rainaway-logo.webp" alt="Rain Away logo" width="700" height="452" loading="lazy">
      <h3>Rain Away &middot; 8 oz</h3><p class="muted">Makes up to 32 gallons. Made for rainy-day driving.</p>
      <a class="btn sky sm" href="{pre}contact.html?topic=order&amp;product=Rain%20Away%208%20oz">Order Rain Away</a></div>
  </div>
</div></section>

<section class="alt"><div class="wrap split">
  <div>
    <h2>Good for</h2>
    <ul class="checks">
      <li>Daily drivers and commuters</li>
      <li>Road trips and bug season</li>
      <li>Topping off every vehicle in the family</li>
      <li>Keeping a backup in the garage instead of a stack of jugs</li>
    </ul>
  </div>
  <div class="card">
    <h3>Mix rate</h3>
    <div class="table-wrap"><table>
      <tr><th>Concentrate</th><th>Water</th><th>Makes</th></tr>
      <tr><td>1/4 oz</td><td>1 gallon</td><td>1 gallon</td></tr>
      <tr><td>1 oz</td><td>4 gallons</td><td>4 gallons</td></tr>
      <tr><td>8 oz (full bottle)</td><td>32 gallons</td><td>32 gallons</td></tr>
    </table></div>
  </div>
</div></section>

<section><div class="wrap">""" + FREEZE_NOTICE + """</div></section>
"""

FLEET = """
<section class="page-hero"><div class="wrap">
  <span class="eyebrow">Fleet &amp; bulk</span>
  <h1>One ounce. One 55-gallon drum.</h1>
  <p class="lead">For service centers, quick lubes, dealerships, trucking companies, municipalities and fleet operators. One 32 oz bottle of EVOLVED concentrate makes up to 1,760 gallons of washer fluid. That's 32 full drums.</p>
  <div class="btns"><a class="btn green" href="{pre}contact.html?topic=quote">Get a fleet quote</a><a class="btn ghost" href="{pre}how-to-mix.html">How to mix</a></div>
</div></section>

<section><div class="wrap">
  <div class="grid2">
    <div class="card pad0"><div class="product-img"><img src="{pre}images/bugaway-32oz-front.webp" alt="Bug Away 32 oz concentrate, makes 1,760 gallons" width="900" height="900" loading="lazy"></div>
      <div class="body"><span class="tag">Removes bugs</span><h3>Bug Away &middot; 32 oz</h3><p class="muted">Makes up to 1,760 gallons. Built-in 1 oz measuring chamber.</p>
      <a class="btn green sm" href="{pre}contact.html?topic=order&amp;product=Bug%20Away%2032%20oz">Order Bug Away</a></div></div>
    <div class="card pad0"><div class="product-img"><img src="{pre}images/rainaway-32oz-front.webp" alt="Rain Away 32 oz concentrate, makes 1,760 gallons" width="900" height="910" loading="lazy"></div>
      <div class="body"><span class="tag sky">Repels rain</span><h3>Rain Away &middot; 32 oz</h3><p class="muted">Makes up to 1,760 gallons. Built-in 1 oz measuring chamber.</p>
      <a class="btn sky sm" href="{pre}contact.html?topic=order&amp;product=Rain%20Away%2032%20oz">Order Rain Away</a></div></div>
  </div>
</div></section>

<section class="alt"><div class="wrap split">
  <div>
    <span class="eyebrow">Plan your supply</span>
    <h2>How many bottles do you need?</h2>
    <p>Enter how many gallons of washer fluid you go through in a year. We'll show the drums, ounces of concentrate and 32 oz bottles that covers.</p>
    <ul class="checks">
      <li>Store one case of bottles instead of pallets of jugs</li>
      <li>Mix on-site, only as much as you need</li>
      <li>Less plastic and cardboard to break down and haul away</li>
    </ul>
  </div>
  <div class="calc">
    <label for="gal">Gallons of washer fluid per year</label>
    <input id="gal" type="number" min="0" step="10" value="1000" inputmode="numeric">
    <div class="calc-out">
      <div><b id="drums">19</b><span>55-gal drums</span></div>
      <div><b id="oz">19</b><span>oz of concentrate</span></div>
      <div><b id="bottles">1</b><span>32 oz bottles</span></div>
    </div>
    <p class="muted" style="margin:14px 0 0;font-size:.9rem">Based on the label mix rate of 1 oz per 55 gallons.</p>
  </div>
</div></section>

<section><div class="wrap split">
  <div><h2>Talk to us about volume</h2><p class="lead">Running a shop, a dealership or a fleet? Tell us roughly how much fluid you use and we'll put together pricing.</p></div>
  <div class="btns" style="justify-content:flex-end"><a class="btn green" href="{pre}contact.html?topic=quote">Request a quote</a></div>
</div></section>

<section class="alt2"><div class="wrap">""" + FREEZE_NOTICE + """</div></section>
"""

MIX = """
<section class="page-hero"><div class="wrap">
  <span class="eyebrow">Directions</span>
  <h1>How to mix EVOLVED concentrate</h1>
  <p class="lead">A little concentrate goes a long way. The 32 oz bottle has a built-in measuring chamber, so you don't need a cup.</p>
</div></section>

<section><div class="wrap split">
  <div>
    <h2>32 oz bottle &middot; 55-gallon drum</h2>
    <p class="muted">Mix rate: 1 oz makes 55 gallons.</p>
    <div class="steps" style="grid-template-columns:1fr;gap:14px">
      <div class="step"><p>Remove the cap of the small measuring reservoir.</p></div>
      <div class="step"><p>Squeeze the bottle to fill the small reservoir with 1 oz of concentrate.</p></div>
      <div class="step"><p>Pour the contents of the small reservoir into a 55-gallon drum.</p></div>
      <div class="step"><p>Fill the drum with water.</p></div>
    </div>
  </div>
  <div><img src="{pre}images/bugaway-32oz-front.webp" alt="Bug Away 32 oz bottle with built-in 1 oz measuring chamber" width="900" height="900" loading="lazy"></div>
</div></section>

<section class="alt"><div class="wrap">
  <h2>8 oz bottle &middot; by the gallon</h2>
  <p class="muted">Mix rate: 1/4 oz makes 1 gallon. One bottle makes up to 32 gallons.</p>
  <div class="steps">
    <div class="step"><p>Measure 1/4 oz of concentrate (about 1.5 teaspoons).</p></div>
    <div class="step"><p>Pour it into a clean, empty one-gallon jug.</p></div>
    <div class="step"><p>Fill the jug with water, cap it and give it a gentle shake. Then fill your washer reservoir.</p></div>
  </div>
</div></section>

<section><div class="wrap">
  <h2>Quick reference</h2>
  <div class="table-wrap"><table>
    <tr><th>Bottle</th><th>Concentrate</th><th>Water</th><th>Full bottle makes</th></tr>
    <tr><td>8 oz</td><td>1/4 oz</td><td>1 gallon</td><td>32 gallons</td></tr>
    <tr><td>32 oz</td><td>1 oz</td><td>55 gallons</td><td>1,760 gallons</td></tr>
  </table></div>
  <h3 style="margin-top:36px">Tips</h3>
  <ul class="checks">
    <li>Use clean water. Distilled or softened water helps prevent mineral spots on the glass.</li>
    <li>Label any jug or drum you mix into so nobody mistakes it for drinking water.</li>
    <li>Store the concentrate capped, out of reach of children, and away from freezing temperatures.</li>
  </ul>
</div></section>

<section class="alt2"><div class="wrap">
  <div class="notice"><div class="ico">&#9888;</div><p><b>Warning: product will freeze.</b> Harmful if swallowed. Avoid contact with eyes, skin and clothing. Keep out of reach of children. If swallowed, get medical attention right away. Winter mixing instructions are coming soon.</p></div>
</div></section>
"""

ABOUT = """
<section class="page-hero"><div class="wrap">
  <span class="eyebrow">About</span>
  <h1>Small bottles. Big impact.</h1>
  <p class="lead">Evolved Innovations makes EVOLVED, a bio-based windshield washer fluid sold as a concentrate. We're based in Sioux Falls, South Dakota.</p>
</div></section>

<section><div class="wrap split">
  <div>
    <h2>Why we started</h2>
    <p>For decades, washer fluid has been sold the same way: mostly water, in a single-use plastic jug, shipped by the truckload. Then you carry it home, pour it in, and throw the jug away.</p>
    <p>We thought there was a better way. Ship only the part that does the work, and let people add their own water. You get a smaller bottle, less plastic, less freight and less to store.</p>
    <h2>What we believe</h2>
    <ul class="checks">
      <li>Better for the planet should still work great on the windshield.</li>
      <li>Less waste and lower cost per gallon can go together.</li>
      <li>We say only what we can back up. That's why our USDA BioPreferred&reg; application shows as "applied for" until the USDA decides.</li>
    </ul>
  </div>
  <div class="grid2" style="gap:10px">
    <img src="{pre}images/bugaway-32oz-front.webp" alt="Bug Away 32 oz bottle" width="900" height="900" loading="lazy">
    <img src="{pre}images/rainaway-32oz-front.webp" alt="Rain Away 32 oz bottle" width="900" height="910" loading="lazy">
  </div>
</div></section>

<section class="dark"><div class="wrap split">
  <div><h2>Selling to shops or retailers?</h2><p class="lead">We work with auto parts stores, service centers and fleets. Reach out and we'll talk.</p></div>
  <div class="btns" style="justify-content:flex-end"><a class="btn green" href="{pre}contact.html?topic=wholesale">Contact us</a></div>
</div></section>
"""

FAQ_ITEMS = [
    ("What is EVOLVED?",
     "EVOLVED is a bio-based windshield washer fluid concentrate. You mix it with water to make ready-to-use washer fluid."),
    ("How much water do I add?",
     "32 oz bottle: 1 oz of concentrate per 55 gallons of water. 8 oz bottle: 1/4 oz per gallon of water. See the How to Mix page for step-by-step directions."),
    ("How much washer fluid does one bottle make?",
     "The 8 oz bottle makes up to 32 gallons. The 32 oz bottle makes up to 1,760 gallons, which is 32 full 55-gallon drums."),
    ("Will it freeze?",
     "Yes. The current Bug Away and Rain Away formulas are warm-weather formulas, and mixed fluid will freeze. Use them when temperatures stay above 32&deg;F, and switch to a winter-rated washer fluid before freezing weather. Winter mixing instructions are coming soon."),
    ("What's the difference between Bug Away and Rain Away?",
     "Bug Away is made for bug season and highway driving. Rain Away is made to help water bead up on the glass in rainy weather. Both mix the same way."),
    ("What does bio-based mean?",
     "The USDA describes biobased products as products made from plants and other renewable agricultural, marine and forestry materials, instead of petroleum. We've applied to the USDA BioPreferred&reg; Program and are waiting on their decision."),
    ("Is EVOLVED USDA certified?",
     "Not yet. Our application to the USDA BioPreferred&reg; Program is in review. We won't call it certified until it is."),
    ("What water should I use?",
     "Clean tap water works. Distilled or softened water helps prevent mineral spots on the glass, especially if you have hard water."),
    ("Do you sell to shops, fleets and retailers?",
     "Yes. Fleet and bulk customers can request a quote, and we're open to talking with auto parts stores and other retailers."),
    ("How do I order?",
     "Use the order form on the Contact page, or email us. We'll confirm the price and shipping with you."),
]


def faq_page():
    items = "".join(f'<details><summary>{q}</summary><div class="ans">{a}</div></details>' for q, a in FAQ_ITEMS)
    body = f"""<section class="page-hero"><div class="wrap"><span class="eyebrow">FAQ</span>
<h1>Frequently asked questions</h1><p class="lead">Can't find your answer? Email <a href="mailto:{{email}}">{{email}}</a>.</p></div></section>
<section style="padding-top:20px"><div class="wrap" style="max-width:820px">{items}</div></section>"""
    import re
    schema = [{"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": re.sub("&[a-z]+;", "", a)}}
        for q, a in FAQ_ITEMS]}]
    return body, schema


CONTACT = """
<section class="page-hero"><div class="wrap">
  <span class="eyebrow">Contact</span>
  <h1>Order, get a quote or ask a question</h1>
  <p class="lead">Fill this out and your email app will open with the message ready to send. Or email us directly at <a href="mailto:{email}">{email}</a>.</p>
</div></section>
<section style="padding-top:20px"><div class="wrap split" style="align-items:start">
  <form class="form card" id="contact-form">
    <div><label for="topic">I want to</label>
      <select id="topic" name="topic">
        <option value="order">Place an order</option>
        <option value="quote">Get a fleet or bulk quote</option>
        <option value="wholesale">Talk about wholesale or retail</option>
        <option value="question">Ask a question</option>
      </select></div>
    <div><label for="product">Product (if ordering)</label>
      <select id="product" name="product">
        <option value="">Not sure yet</option>
        <option>Bug Away 8 oz</option><option>Rain Away 8 oz</option>
        <option>Bug Away 32 oz</option><option>Rain Away 32 oz</option>
      </select></div>
    <div><label for="qty">Quantity or yearly gallons</label><input id="qty" name="qty" placeholder="e.g. 2 bottles, or 5,000 gallons a year"></div>
    <div><label for="name">Name</label><input id="name" name="name" required autocomplete="name"></div>
    <div><label for="company">Company (optional)</label><input id="company" name="company" autocomplete="organization"></div>
    <div><label for="msg">Message</label><textarea id="msg" name="msg" placeholder="Shipping address, questions, anything else"></textarea></div>
    <button class="btn green" type="submit">Create email</button>
  </form>
  <div>
    <div class="card"><h3>Email</h3><p><a href="mailto:{email}">{email}</a></p>
    <h3>Location</h3><p>Sioux Falls, South Dakota</p>
    <h3>Fleets &amp; shops</h3><p class="muted">Tell us roughly how many gallons you use a year and we'll put together pricing.</p></div>
  </div>
</div></section>
"""

PRIVACY = """
<section class="page-hero"><div class="wrap"><span class="eyebrow">Legal</span><h1>Privacy Policy</h1><p class="muted">Last updated November 2, 2026</p></div></section>
<section style="padding-top:20px"><div class="wrap post">
<p>This website is run by Evolved Innovations in Sioux Falls, South Dakota.</p>
<h2>What we collect</h2>
<p>This site does not use advertising trackers and does not set cookies. The contact form doesn't store anything on our servers. It opens your own email app with your message filled in, and you decide whether to send it.</p>
<p>If you email us, we receive your email address and whatever you write. We use that only to answer you and fill your order.</p>
<h2>Sharing</h2>
<p>We don't sell your information. We share it only when needed to fill your order, such as giving a shipping address to a carrier, or when the law requires it.</p>
<h2>Website hosting</h2>
<p>Our hosting provider may keep standard server logs, such as IP addresses and the pages requested, for security and reliability.</p>
<h2>Contact</h2>
<p>Questions about privacy? Email <a href="mailto:{email}">{email}</a>.</p>
</div></section>
"""

_faq_body, _faq_schema = faq_page()

PRODUCT_SCHEMA = [{
    "@context": "https://schema.org", "@type": "Product", "name": n, "brand": {"@type": "Brand", "name": "EVOLVED"},
    "description": d, "image": "https://evolvedproducts.us/images/" + img} for n, d, img in [
    ("EVOLVED Bug Away Washer Fluid Concentrate 32 oz", "Bio-based windshield washer fluid concentrate. 1 oz makes 55 gallons; bottle makes up to 1,760 gallons.", "bugaway-32oz-front.webp"),
    ("EVOLVED Rain Away Washer Fluid Concentrate 32 oz", "Bio-based windshield washer fluid concentrate. 1 oz makes 55 gallons; bottle makes up to 1,760 gallons.", "rainaway-32oz-front.webp"),
]]

PAGES = [
    {"path": "index.html", "title": "EVOLVED | Bio-Based Windshield Washer Fluid Concentrate",
     "desc": "EVOLVED bio-based windshield washer fluid concentrate. One 32 oz bottle makes up to 1,760 gallons. Just add water. Bug Away and Rain Away formulas.",
     "body": HOME, "schema": PRODUCT_SCHEMA},
    {"path": "personal-vehicle.html", "title": "Washer Fluid Concentrate for Cars, Trucks & SUVs | EVOLVED",
     "desc": "One 8 oz bottle of EVOLVED washer fluid concentrate makes up to 32 gallons. Bug Away and Rain Away for your car, truck or SUV.",
     "body": PERSONAL},
    {"path": "fleet-bulk.html", "title": "Fleet & Bulk Washer Fluid Concentrate | 1 oz Makes 55 Gallons | EVOLVED",
     "desc": "Washer fluid concentrate for fleets, shops and dealerships. 1 oz makes a 55-gallon drum; one 32 oz bottle makes 1,760 gallons. Request a quote.",
     "body": FLEET, "schema": PRODUCT_SCHEMA},
    {"path": "how-to-mix.html", "title": "How to Mix Washer Fluid Concentrate | EVOLVED",
     "desc": "Step-by-step mixing directions for EVOLVED washer fluid concentrate: 1 oz per 55-gallon drum, or 1/4 oz per gallon.",
     "body": MIX},
    {"path": "about.html", "title": "About Evolved Innovations | Sioux Falls, SD",
     "desc": "Evolved Innovations makes EVOLVED bio-based washer fluid concentrate in Sioux Falls, South Dakota. Less plastic, less freight, just add water.",
     "body": ABOUT},
    {"path": "faq.html", "title": "Washer Fluid Concentrate FAQ | EVOLVED",
     "desc": "Answers about EVOLVED washer fluid concentrate: mix rates, freezing, bio-based, ordering and fleet pricing.",
     "body": _faq_body, "schema": _faq_schema},
    {"path": "contact.html", "title": "Order or Get a Quote | EVOLVED Washer Fluid",
     "desc": "Order EVOLVED washer fluid concentrate or request fleet and bulk pricing.",
     "body": CONTACT},
    {"path": "privacy-policy.html", "title": "Privacy Policy | EVOLVED",
     "desc": "Privacy policy for evolvedproducts.us.", "body": PRIVACY},
]
