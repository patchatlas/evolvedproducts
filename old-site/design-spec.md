# evolvedproducts.us: Design Spec (captured Nov 1, 2026)

Source: the live GoDaddy Website Builder site (now branded "GoDaddy Airo"). Values come from computed styles in headless Edge at 1366px desktop, unless marked "approx." (read off the screenshots).
Screenshots in this folder were taken with the site's cookie banner hidden locally. Nothing was clicked or accepted.

---

## 1. Global design tokens

### Fonts (both from Google Fonts)
| Use | Family | Weight | Size (desktop) | Notes |
|---|---|---|---|---|
| H1 / H2 section titles | **League Spartan** | 400 (renders heavy, it's a geometric bold-looking face) | 44px | centered; mobile ≈ 32px (approx.) |
| H4 card / sub titles | **Cabin** | 400 | 22px | |
| Body / paragraphs | **Cabin** | 400 | 16px | line-height 24px |
| Nav links | **Cabin** | 400 (active page = 600) | 14px | UPPERCASE, letter-spacing 0.994px (~0.071em), line-height 24px |
| Nav dropdown items | Cabin | 400 | 16px | normal case, color #5e5e5e, padding 4px 0 |
| Buttons | **Cabin** | 600 | 14px | UPPERCASE, letter-spacing 0.994px |
| Small print (footer, reCAPTCHA, blog dates) | Cabin | 400 | 14px (12px reCAPTCHA) | |
| Shop "All Products" heading | Cabin | 400 | 22px | left-aligned (not League Spartan) |
| Fallback stack used by the site | `Cabin, Georgia, serif` / `"League Spartan", arial, helvetica, sans-serif` | | | |

Google Fonts import to reproduce: `League Spartan:wght@400` and `Cabin:wght@400;600` (Cabin italic 400 is also loaded).

### Colors
| Token | Hex | Where |
|---|---|---|
| Brand navy (primary accent) | **#20507a** | Home section titles ("Choose Your Washer Fluid Formula", "Small Bottles. Big Impact", "100% BIODEGRADABLE…", "Our Mission"); Fleet & Bulk stat band background |
| Deep navy | **#153047** | Personal Vehicle stat band background; "Photo Gallery" title; Home mission paragraph text |
| Dark navy text | #172d42 | Home "gallon or drum" card paragraphs |
| Near-black (headings / buttons) | **#161616** | Non-accent H1/H2, button background, price text, footer "Powered by" link |
| Nav / H4 text | #1b1b1b | Nav links, H4 headings, header icons, footer links |
| H4 on light beige section | #181616 | |
| Body text grey | **#5e5e5e** | paragraphs, FAQ answers, dropdown items |
| Small-print grey | #595959 | copyright, blog dates, reCAPTCHA note, shop category links |
| Input text / labels | #474747 | form fields |
| Personal Vehicle hero text | #605353 | warm grey paragraph text |
| Button text | **#dbdbdb** | text on the #161616 buttons |
| White | #ffffff | page background, header, most sections, white headings on image sections |
| Off-white beige section | **#faf7f7** | Home "Make washer fluid by the gallon or by the drum" |
| Light warm grey section | **#f7f5f5** | Personal Vehicle hero |
| Dark video band | **#1b1b1b** | Home "How to use the concentrates" section (H4 #fefefe, sub text #aaaaaa) |
| Hairline / borders | **#e2e2e2** | heading divider, input borders, FAQ row lines, shop category border |
| Heading divider on beige section | #e7d8d8 | |
| Image overlay | rgba(0,0,0,0.24) | linear-gradient laid over the background photos (Testimonials, Reviews, Fleet hero) |
| Logo colors (inside the image) | approx. leaf green #8dc63f, water blue #5bc8e8, black wordmark | "BIO-BASED" in green, "WASHER FLUID" in blue |

### Spacing, shapes, effects
- Content container: **1160px max**, 24px side padding (inner width ≈ 1112px). Header spans full 1366px with 24px/48px padding.
- Section padding: **56px top/bottom** for content sections; footer 32px top/bottom.
- **Heading divider:** under every centered section title there's a short line, **50px wide, 2px tall, #e2e2e2** (`border-bottom: 2px solid`), margin-top 24px, centered.
- Buttons: **border-radius 4px**, padding **8px 32px** (≈ 40-56px tall visually), bg #161616, text #dbdbdb, no shadow, no border.
- Images: square corners (radius 0), no shadows anywhere.
- Form inputs: white, **1px solid #e2e2e2, radius 4px**, padding 23px 16px 7px (floating-label style: label sits inside top-left), height 51px, width 725px; textarea 202px tall, padding 16px.
- Wave divider (Fleet & Bulk and Personal Vehicle stat bands): a 68px-tall SVG wave on top of the band, same color as the band:
  `<svg viewBox="0 0 1200 120" preserveAspectRatio="none"><path d="M0,60 C200,90 400,30 600,60 C800,90 1000,30 1200,60 L1200,120 L0,120 Z" fill="currentColor"/></svg>`
- No sticky header (position: static), no header border or shadow.

---

## 2. Header (all pages)
- Height **161px**, white background.
- **3-zone layout:** nav links left · logo centered · BLOG link + icons right.
  - Left (x≈48px): `HOME` `ABOUT` `PRODUCTS ▾` (dropdown caret 16px icon). Cabin 14px uppercase, letter-spacing ~1px, color #1b1b1b; active page in weight 600.
  - PRODUCTS dropdown items: *Washer Fluid Concentrates* (/washer-fluid-concentrates), *Fleet & Bulk* (/fleet-%26-bulk), *Personal vehicle* (/personal-vehicle). Cabin 16px #5e5e5e.
  - Center: logo image `images/Updated Evolved Logo.jpg` displayed at **396 × 113px**, top at 24px. (The source logo has a very faint grey box behind it, visible in screenshots.)
  - Right: `BLOG` text link (x≈1121px), then three 40px icon buttons, #1b1b1b: **search (magnifier), cart, account (person)**.
- **Mobile (390px):** hamburger menu left, logo centered (smaller), cart icon right. Nav moves into a slide-out drawer.

## 3. Footer (all pages)
- White background, 32px padding.
- Row 1: left "Copyright © 2026 EVOLVED - All Rights Reserved." (Cabin 14px #595959); right "Powered by" + GoDaddy Airo logo (drop this on the new site).
- Row 2 centered: `PRIVACY POLICY` (/privacy-policy) · `CONTACT US` (/contact-us). Cabin 14px uppercase, letter-spacing ~1px, #1b1b1b.
- Mobile: everything stacks centered.

---

## 4. Pages, section by section

### 4.1 Home `/` (title "EVOLVED")
1. **Header** (above).
2. **"Choose Your Washer Fluid Formula"** (white, 56px padding, section height 710px)
   - H1 League Spartan 44px **#20507a**, centered, with the divider below.
   - **Two side-by-side image tiles**, each ≈435 × 470px, centered with a gap of about 50px. Each is a CSS background image (`cover`, center) under a transparent gradient: left = `blob-848896c.jpg` (BugAway "Bug Removal Power"), right = `blob-cdd1f4e.jpg` (RainAway "Rain Repellent Action"). Each tile is a link (currently `#`) with an empty white H2 overlay (no visible text).
   - Mobile: tiles stack full-width and are cropped into short wide strips.
3. **"Make washer fluid by the gallon or by the drum"** (bg **#faf7f7**, height 906px)
   - H2 44px **#161616** centered, divider in #e7d8d8.
   - **2-column card grid**, centered (columns ≈339px wide, gap ≈48px):
     - Card 1: image `ChatGPT Image Sep 24 2026 05_37_15 PM.jpg` (339×339 square, cover) → H4 "Make it by the gallon" (Cabin 22px #181616) → paragraph (16px #172d42, centered): *"Windshield washer fluid concentrate made for everyday drivers. The Personal Vehicle line gives car, truck, and SUV owners a compact alternative to bulky ready-to-use washer fluid jugs. Each 8 oz bottle makes up to 32 gallons of finished windshield washer fluid, making it easy to mix, store, and refill at home or on the go. Designed for…"* → "+ Show More" toggle.
     - Card 2: image `ChatGPT Image Sep 24 2026 05_24_53 PM.jpg` → H4 "Make 55 Gallon Drums" → *"Bulk windshield washer fluid concentrate for fleets, shops, and commercial use. The Fleet & Bulk line is designed for businesses that need dependable washer fluid in high volumes without the cost, space, and waste of shipping water. With concentrated formulas that make 55-gallon drums or up to 1,760 gallons of finished washer fluid. Flee…"* → "+ Show More".
   - Text is clamped at about 8 lines; "Show More" expands it.
4. **Video band** (bg **#1b1b1b**, height 411px)
   - Split 50/50: left = HTML5 video player 532×299 with controls (file saved as `video/how-to-use-concentrates.mp4`); right = centered H4 "How to use the concentrates" (Cabin 22px #fefefe) + "Explainer video and description" (16px #aaaaaa).
5. **"Small Bottles. Big Impact"** (white, 772px)
   - H2 44px **#20507a** centered + divider.
   - Split 2 columns: left image `Brown Photo Collage Instagram Post 1.jpg` (532×532 square); right, vertically centered: H4 "Our Mission" (22px **#20507a**), paragraph (16px **#153047**, centered): *"It started with smaller bottles, smarter formulas, and better decisions at the design level. We're committed to building products that help people see clearer, clean smarter, and delivering bio-based solutions that outperform traditional formulas."* → button **LEARN MORE** → /about (#161616 bg, #dbdbdb text, 4px radius).
6. **"100% BIODEGRADABLE. ZERO COMPROMISE."** (white, 930px)
   - H2 44px **#20507a** centered.
   - **Full-width image carousel / slider**: 600×600 slides (one 480×600) in a horizontal strip with the center slide fully visible and neighbours peeking in from each side; arrow on the right. Below it is a **thumbnail strip of 70×70 thumbnails** (16 thumbnails).
   - Slide/thumbnail order: `Bugs Happen-7e24d88`, `Summertime Washer Fluid 2`, `ChatGPT Image Oct 7 2026 10_16_50 PM`, `ChatGPT Image Sep 24 2026 05_37_15 PM`, `blob-848896c`, `ChatGPT Image Sep 24 2026 06_27_32 PM`, `ChatGPT Image Sep 24 2026 05_24_53 PM`, `ChatGPT Image Sep 24 2026 05_45_19 PM`, `ChatGPT Image Sep 24 2026 09_45_13 PM`, `ChatGPT Image Sep 24 2026 09_32_19 PM`, `ChatGPT Image Oct 7 2026 10_16_43 PM`, `ChatGPT Image Sep 23 2026 08_22_06 PM`, `ChatGPT Image Sep 23 2026 08_10_40 PM`, `Roadtrip fuel-5d942cd`, `Blue Modern Amazon Product Image-1e1cf92`, `Blue White Modern 8-32 3-96b02cc` (all .jpg in images/).
7. **"Testimonials that speak for us!"** (full-bleed background photo, 279px tall)
   - Background `getty-2185826541.jpg`, `cover`, centered, with a **rgba(0,0,0,0.24)** dark overlay.
   - H2 44px **white** centered; below it a wide (≈725px) translucent grey bar with "Reviews coming soon!" (16px white, centered).
8. **"Frequently Asked Questions"** (white, 509px)
   - H2 44px #161616 + divider; intro "Please reach us at tylerpatch.evolved@gmail.com if you cannot find an answer to your question." (16px #5e5e5e, email underlined). **Update the email to tyler@evolvedproducts.us** to match the other pages.
   - Accordion, 725px wide, centered: rows "First Question / Second Question / Third Question" (placeholders, answers "Add an answer to this item."). Row text Cabin 16px black, left; ▾ caret on the right; 1px #e2e2e2 line between rows.
9. **"Contact Us"** (white, 793px)
   - H2 44px #161616 + divider, H4 "We love our customers. Feel free to drop us a line!" (22px #1b1b1b).
   - Form 725px wide: Name, Email*, Message (textarea), then a centered **SEND** button (same button style), then the reCAPTCHA note (12px #595959).
10. **Footer.**

### 4.2 About `/about` (title "About EVOLVED: Eco-Friendly Cleaning Solutions")
1. **"About EVOLVED"** H1 44px #161616 centered + divider.
2. **4 alternating zig-zag rows** (image 532×266, i.e. 2:1, next to centered text; rows ≈314px apart):
   - Row 1: image left `blob-933f73e.png` (woman in car + water drop) | text right: H4 "Our Mission" (22px #1b1b1b) + *"For decades, **washer fluid** has been built around single-use plastic jugs tossed after one use. / At **Evolved Innovations**, we believe it's time for something better."*
   - Row 2: text left: H4 "Why we exist" + *"We exist to **eliminate unnecessary waste** without asking people to compromise on performance. / Sustainability shouldn't feel like a downgrade. It should feel like an upgrade—smarter, more efficient, and more intentional. That belief drives every formula we create and every product we release."* | image right `Untitled design 7-52b2efb.jpg`.
   - Row 3: image left `blob-7c55820.png` | text: H4 "How we do it" + *"We spent years engineering **high-performance concentrates** that put control back in your hands. / Instead of paying to ship water and plastic, we design products that let you add what you already have—**water**—at home. The result is dramatically less waste, lower costs, and better performance per ounce."*
   - Row 4: text left: H4 "Built for the long-haul" + *"We're not a trend brand or a one-product experiment. We're building a platform of **environmentally responsible concentrates**, designed with the same philosophy: fewer materials, smarter formulas, better results. / We design products the way they *should have been made all along*."* | image right `blob-fa2f165.png` (EI EVOLVED Environmental Innovations nature banner).
   - Body text 16px #5e5e5e centered; bold phrases in a darker weight.
3. **"Reviews"** full-bleed background band: `stock-10467.jpg` (squeegee on glass), cover, rgba(0,0,0,0.24) overlay; H2 "Reviews" white 44px; translucent grey bar "Reviews coming soon!".
4. Footer.

### 4.3 Washer Fluid Concentrates `/washer-fluid-concentrates` (GoDaddy online store page)
- **2-column shop layout:** left sidebar (≈230px) with category links (Cabin 16px #1b1b1b; current category in 600): **All Products**, Fleet and Bulk Series Washer Fluid Concentrates, Personal Vehicle Series Washer Fluid Concentrates, BugAway Bio-Based Washer Fluid Concentrate, RainAway Bio-Based Washer Fluid Concentrate.
- Right: "All Products" (Cabin 22px #1b1b1b, left) and a "Most popular ▾" sort dropdown on the right.
- **3-column product grid**: square product image (≈242px, cover, light-blue/white product shot backgrounds) → title (Cabin 16px #1b1b1b, left-aligned) → price (Cabin 16px #161616). "+ Quick View" appears on hover.
  | Product | Price | Image (front / back) |
  |---|---|---|
  | Evolved 8-32 Rain Away Windshield Washer Fluid Concentrate – 8 oz (Makes 32 Gallons) | $26.99 USD | `8-32 Rain Front-b9f7e7b.jpg` / `8-32 Rain Back-aa5c2a5.jpg` |
  | Evolved 8-32 Bug Away Windshield Washer Fluid Concentrate – 8 oz (Makes 32 Gallons) | $26.99 USD | `8-32 Bug Front.jpg` / `8-32 Bug Back.jpg` |
  | Evolved 32-1760 Bug Away Bio-Based Windshield Washer Fluid Concentrate – 32 oz (Makes 1,760 Gallons) | $99.00 USD | `32-1760 Bug Front.jpg` / `32-1760 Bug Back.jpg` |
  | Evolved 32-1760 Rain Away Bio-Based Windshield Washer Fluid Concentrate – 32 oz (Makes 1,760 Gallons) | $99.00 USD | `32-1760 Rain Front.jpg` / `32-1760 Rain Back.jpg` |
  | Evolved 6-55 Rain Away Bio-Based Windshield Washer Fluid Concentrate | $20.00 USD | `6-55 Rain Front.jpg` / `6-55 Rain back.jpg` |
  | Evolved 6-55 Bug Away Bio-Based Windshield Washer Fluid Concentrate | $20.00 USD | `6-55 Bug Front.jpg` / `6-55 Bug Back.jpg` |
- No section title or divider on this page. Footer follows.

### 4.4 Fleet & Bulk `/fleet-%26-bulk`
1. **Full-bleed hero image**, 778px tall: background `ChatGPT Image Sep 24 2026 09_45_13 PM.jpg` (cover, centered, 0.24 dark overlay). The headline "INNOVATION IN EVERY DROP. Super concentrates for fleets and bulk operations." and the bottles are **baked into the image**; there's no live text.
2. **"Bulk and Fleet Washer Fluid Concentrates"** H1 44px #161616 + divider. **4-column product cards** (242×323 images, cover): `6-55 Bug Front` "Makes 1 - 55 Gallon Drum" · `6-55 Rain Front` "Makes 1 - 55 Gallon Drum" · `32-1760 Bug Front` "Makes 32 - 55 Gallon Drums" · `32-1760 Rain Front` "Makes 32 - 55 Gallon Drums". Labels in Cabin 22px #1b1b1b centered.
3. **Stat band**: bg **#20507a**, 354px tall, **wave divider on top**. Four 242×242 square stat tiles (images; the text is baked in): `ChatGPT Image May 19 2026 03_09_03 PM 1.jpg` ("1 oz makes a 55-gallon drum"), `…03_09_04 PM 2.jpg` ("32 oz makes 1,760 gallons"), `…03_09_04 PM 3.jpg` ("32× fewer drums to ship"), `…03_09_04 PM 4.jpg` ("100% Bio-Based"). The tiles are dark navy squares with teal/aqua numerals.
4. **"One Bottle = Thirty-Two Drums"** H2 + divider; a wide image `ChatGPT Image Sep 24 2026 09_32_19 PM.jpg` (1112×556, 2:1); then a bulleted list (16px #5e5e5e): "1 oz of concentrate → 55 gallon drum of finished fluid", "32 oz bottle → thirty-two 55-gallon drums", "Smaller bottles, lower freight, easier reordering", "Less plastic, less warehouse space, less waste".
5. **FAQ** (same style as Home): intro uses tyler@evolvedproducts.us. Q: "Can I use this in the winter?" A: "Yes, for freezing temperatures and winter use, follow the methanol mixing chart for your desired freeze protec[tion]…"; "Are the formulas bio-based?"; "What makes Evovled better than other washer fluid concentrates." (**fix the typo "Evovled"**).
6. Footer.

### 4.5 Personal Vehicle `/personal-vehicle`
1. **Split hero**, bg **#f7f5f5**, 856px tall: left column (left-aligned): H1 "Bio-Based Concentrates" (League Spartan 44px #151515), paragraphs 16px **#605353**: "BugAway removes bugs, grime and stubborn residue." / "RainAway delivers water-beading action for clearer wet-weather visibility." / "Proven results that speak for themselves." Right: image `blob-d337bc3.jpg` (696×696, "Personal Vehicle Series").
2. **"Choose Your Formula"** H2 + divider; 2 cards (339×339 images): `ChatGPT Image Sep 24 2026 06_27_05 PM.jpg` (BugAway) with placeholder H4 "Generate excitement" + "What's something exciting your business offers? Say it here." and `…06_27_32 PM.jpg` (RainAway) with "Feature something" + "What's a product or service you'd like to show." (**These are GoDaddy placeholder texts; replace them.**)
3. **Stat band**: bg **#153047**, wave top, 4 tiles: `ChatGPT Image May 19 2026 03_12_34 PM 2.jpg` ("1/4 oz makes 1 gallon"), `…03_12_34 PM 1.jpg` ("8 oz makes 32 gallons"), `…03_12_34 PM 3.jpg` ("32 gallon jugs saved from the landfill"), `…03_09_04 PM 4.jpg` ("100% Bio-Based").
4. **"Photo Gallery"** H2 (#153047) + divider; three stacked square images 725×725, centered: `ChatGPT Image Sep 24 2026 10_29_53 PM` ("Less plastic. Less storage."), `ChatGPT Image Sep 23 2026 08_22_06 PM` ("Clearer views in the rain"), `ChatGPT Image Sep 23 2026 08_10_40 PM` ("Real road grime. Real cleaning power.").
5. **FAQ**: "Can I use this in the winter?" (A: "The formulas are designed for above-freezing use. For freezing temperatures, follow the methanol mixing chart…"), "Are the concentrates made from plants?", "What makes Evovled better…" (typo).
6. Footer.

### 4.6 Blog `/blog`
- H1 "My Blog" + divider.
- Post list, ≈725px wide, centered. Each row: 200×200 thumbnail on the left (CSS background, `auto`, top-center) and text on the right: date (14px #595959) → title (Cabin 22px #1b1b1b) → excerpt (16px #5e5e5e) → "Continue Reading" link (16px #1b1b1b). 1px #e2e2e2 line between posts.
  - May 5, 2026: "Bulk Windshield Washer Fluid: Evolved 6-55 vs 32-1760" / "Unlocking Efficiency: Why Bulk Windshield Washer Fluids Matter" (thumbnail `getty-157506595.jpg`, blue jug).
  - February 21, 2026: "Evolved 8-32 Windshield Washer Fluid: The Smart Choice for Summer" / "Revolutionizing Your Summer Drive" (thumbnail `Washer Fluid Flyer.jpg`).
- Footer.

### 4.7 Contact Us `/contact-us` (title "Contact US | EVOLVED")
- H1 "Contact Us" + divider; H4 "We love our customers. Feel free to drop us a line!"; the same form as Home (Name, Email*, Message, SEND, reCAPTCHA note); then H4 "EVOLVED Innovations" and "Sioux Falls, SD 57104" (16px #5e5e5e), centered.
- Footer.

---

## 5. Responsive behavior (390px)
- Header: hamburger left / logo center / cart right.
- All multi-column grids (cards, zig-zag rows, split sections, stat tiles, product grid) stack to one column, full width with ~24px gutters; text stays centered.
- Hero image tiles on Home are cropped to short wide strips.
- H1/H2 shrink to about 32px; the long headings wrap to 2–3 lines.

## 6. SEO meta (for reuse)
- About: "Discover EVOLVED's environmentally responsible cleaning products, featuring eco-friendly solutions and high-performance concentrates for sustainable cleaning."
- Washer Fluid Concentrates: "Discover premium washer fluid concentrates for optimal automotive cleaning. Shop now for effective car wash solutions and windshield washer fluid!"
- Fleet & Bulk: "Shop our bio-based washer fluid concentrates for fleet and bulk needs. Maximize efficiency with less waste and improved cleaning power."
- Personal Vehicle: "Eco-friendly washer fluid concentrate that makes 32 gallons from one bottle. Perfect for vehicle cleaning without bulky jugs."
- Blog: "Explore the EVOLVED blog for insights, tips, and updates. Stay informed with our posts on products and cookie policy."
- Home and Contact: none set.

## 7. Notes and gaps
- **Image formats:** GoDaddy's image server returns JPEG even for files named .png, so most images are saved as `.jpg` at full original resolution. None of the images had transparency, so nothing was lost (WebP versions were checked). Three files (blob-933f73e, blob-7c55820, blob-fa2f165) came back as true PNGs.
- **Two images missing:** the washer-fluid page referenced "Blue White Modern 8-32 (4)…" and "Blue Modern Amazon Product Image (1)…" (likely product-gallery extras), but their full addresses never appeared in the page. Re-export them from GoDaddy or Tyler's design files if needed.
- **Product detail pages** (/shop/…) were not captured.
- Placeholder or stale content to fix on the rebuild: Home FAQ placeholder questions, old Gmail address on Home, Personal Vehicle "Generate excitement / Feature something" text, the "Evovled" typo.
- `getty-*` and `stock-*` images are GoDaddy-licensed stock photos. They may only be licensed for use inside GoDaddy sites, so swap them for owned or free-licensed photos on the new static site.
