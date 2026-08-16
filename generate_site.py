#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generates the static Bournemouth Driveway Pros lead-gen site.
Run: python3 generate_site.py
"""
import os, json, datetime
from blog_data import BLOG_POSTS

OUT = os.path.dirname(os.path.abspath(__file__))

SITE_NAME = "Bournemouth Driveway Pros"
DOMAIN = "https://www.bournemouthdrivewaypros.co.uk"   # PLACEHOLDER domain
PHONE_DISPLAY = "01202 000 000"                         # PLACEHOLDER
PHONE_TEL = "+441202000000"                              # PLACEHOLDER
EMAIL = "hello@bournemouthdrivewaypros.co.uk"            # PLACEHOLDER
ADDRESS_LINE = "Bournemouth, BH1, Dorset"                # PLACEHOLDER (no fixed shopfront)
YEAR = "2026"
FORM_ACTION = "https://formspree.io/f/YOUR_FORM_ID"      # PLACEHOLDER — see README.md to activate
BLOG_START_DATE = datetime.date(2026, 8, 17)              # first post's publish date; +1 day per list position

# ---------------------------------------------------------------- icons ----
ICON_CHECK = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>'
ICON_PHONE = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.127.96.362 1.903.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.907.338 1.85.573 2.81.7A2 2 0 0 1 22 16.92z"/></svg>'
ICON_SHIELD = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>'
ICON_CLOCK = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>'
ICON_STAR_SHIELD = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 15a4 4 0 1 0 0-8 4 4 0 0 0 0 8z"/><path d="M8.5 13.5 6 21l6-3 6 3-2.5-7.5"/></svg>'
ICON_ARROW = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>'
ICON_PLUS = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="5" x2="12" y2="19"/><line x1="5" y1="12" x2="19" y2="12"/></svg>'
ICON_PIN = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>'
ICON_TOOL = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/></svg>'
ICON_LEAF = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M11 20A7 7 0 0 1 4 13V8a1 1 0 0 1 1-1h5a7 7 0 0 1 7 7v0a7 7 0 0 1-7 7z"/><path d="M4 8s0-4 4-6c4 2 4 6 4 6"/></svg>'
ICON_COIN = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M12 7v10M9 9.5c0-1.4 1.3-2.5 3-2.5s3 1 3 2.2c0 2.8-6 1.4-6 4.2 0 1.3 1.3 2.3 3 2.3s3-1 3-2.3"/></svg>'
ICON_HAMBURGER = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="18" x2="21" y2="18"/></svg>'
ICON_MAIL = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 4h16v16H4z"/><path d="m4 6 8 7 8-7"/></svg>'

STARS = "★★★★★"

# --------------------------------------------------------- photography ----
# AI-generated (Gemini) driveway photography, licensed for this site's use.
SWATCH_IMAGE = {
    "swatch-tarmac": "images/tarmac-driveway.jpg",
    "swatch-block": "images/block-paving-driveway.jpg",
    "swatch-resin": "images/resin-bound-driveway.jpg",
    "swatch-gravel": "images/gravel-driveway.jpg",
}
HERO_IMAGE = "images/hero-driveway.jpg"

def swatch_img(swatch, alt, css_class="", loading="lazy"):
    """Real photo where we have one, falls back to the CSS texture swatch otherwise."""
    src = SWATCH_IMAGE.get(swatch)
    cls = f"{css_class} {swatch}".strip()
    if src:
        return f'<div class="{cls}"><img src="{src}" alt="{alt}" loading="{loading}" style="width:100%;height:100%;object-fit:cover;display:block;"></div>'
    return f'<div class="{cls}"></div>'

# ------------------------------------------------------------- nav data ----
MATERIAL_PAGES = [
    ("Tarmac Driveways", "tarmac-driveways-bournemouth.html", "swatch-tarmac"),
    ("Block Paving", "block-paving-bournemouth.html", "swatch-block"),
    ("Resin Bound", "resin-bound-driveways-bournemouth.html", "swatch-resin"),
    ("Gravel Driveways", "gravel-driveways-bournemouth.html", "swatch-gravel"),
]
NAV_LINKS = [
    ("Home", "index.html"),
    ("Cost Guide", "driveway-cost-guide-bournemouth.html"),
    ("FAQs", "faq.html"),
]

SERVICE_AREAS = ["Bournemouth", "Poole", "Christchurch", "Ferndown", "Wimborne", "New Milton", "Broadstone", "Southbourne"]

LOCATION_PAGES = [
    ("Poole", "driveways-poole.html"),
    ("Christchurch", "driveways-christchurch.html"),
    ("Ferndown", "driveways-ferndown.html"),
    ("Wimborne", "driveways-wimborne.html"),
    ("New Milton", "driveways-new-milton.html"),
]
AREA_LINK_MAP = {name: href for name, href in LOCATION_PAGES}

# ============================================================ components ===

def head(title, description, canonical_path, schema_blocks):
    schema_json = "\n".join(
        f'<script type="application/ld+json">{json.dumps(s, indent=None)}</script>' for s in schema_blocks
    )
    return f"""<!doctype html>
<html lang="en-GB">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{DOMAIN}/{canonical_path}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{SITE_NAME}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{DOMAIN}/{canonical_path}">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#101826">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Poppins:wght@600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="styles.css">
{schema_json}
</head>
"""

def topbar():
    return f"""
<div class="topbar">
  <div class="container">
    <div class="topbar-links">
      <span class="stars">{STARS}</span>
      <span>Rated 5.0 from local Bournemouth &amp; Poole homeowners</span>
    </div>
    <div class="topbar-links">
      <span>Mon&ndash;Sat, 8am&ndash;6pm</span>
      <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a>
    </div>
  </div>
</div>"""

def header(active_href=""):
    def _nav_link(label, href):
        style_attr = ' style="color:var(--orange-dark)"' if href == active_href else ''
        return f'<a href="{href}"{style_attr}>{label}</a>'
    nav_items = "\n".join(_nav_link(label, href) for label, href in NAV_LINKS)
    dropdown_items = "\n".join(
        f'<a href="{href}">{label}</a>' for label, href, _ in MATERIAL_PAGES
    )
    mobile_items = "\n".join(
        f'<a href="{href}">{label}</a>' for label, href in [("Home","index.html")] +
        [(l,h) for l,h,_ in MATERIAL_PAGES] +
        [("Cost Guide","driveway-cost-guide-bournemouth.html"), ("FAQs","faq.html"), ("Guides","blog.html"), ("Contact","contact.html")]
    )
    return f"""
<header class="site-header">
  <div class="container nav-row">
    <a href="index.html" class="brand">
      <span class="brand-mark">BD</span>
      {SITE_NAME}
    </a>
    <nav class="main-nav">
      <a href="index.html">Home</a>
      <div class="dropdown">
        <a href="#materials">Driveway Types &#9662;</a>
        <div class="dropdown-panel">{dropdown_items}</div>
      </div>
      <a href="driveway-cost-guide-bournemouth.html">Cost Guide</a>
      <a href="faq.html">FAQs</a>
      <a href="blog.html">Guides</a>
      <a href="contact.html">Contact</a>
    </nav>
    <div class="nav-cta-group">
      <a href="tel:{PHONE_TEL}" class="nav-phone"><span>{ICON_PHONE}</span>{PHONE_DISPLAY}</a>
      <a href="#quote" class="btn btn-primary btn-sm">Get Your Free Quote</a>
      <button class="nav-toggle" aria-label="Menu" aria-expanded="false">{ICON_HAMBURGER}</button>
    </div>
  </div>
  <div class="mobile-nav-panel" style="display:none;padding:10px 24px 20px;border-top:1px solid var(--line);">
    <div style="display:flex;flex-direction:column;gap:2px;">
      {mobile_items}
      <a href="#quote" class="btn btn-primary btn-block" style="margin-top:12px;">Get Your Free Quote</a>
    </div>
  </div>
</header>
<style>.mobile-nav-panel.open{{display:block !important;}}</style>"""

def quote_form(context_note="Free, no-obligation quotes for Bournemouth &amp; Poole homeowners."):
    return f"""
<div class="quote-card" id="quote">
  <h3>Get Your Free Quote</h3>
  <p class="sub">{context_note}</p>
  <form class="quote-form" action="{FORM_ACTION}" method="POST">
    <input type="hidden" name="_subject" value="New driveway quote request &mdash; {SITE_NAME}">
    <div class="field-row">
      <div class="field"><label for="name">Full name</label><input id="name" name="name" type="text" placeholder="Jane Smith" required></div>
      <div class="field"><label for="postcode">Postcode</label><input id="postcode" name="postcode" type="text" placeholder="BH1 1AA" required></div>
    </div>
    <div class="field-row">
      <div class="field"><label for="phone">Phone</label><input id="phone" name="phone" type="tel" placeholder="07xxx xxxxxx" required></div>
      <div class="field"><label for="material">Driveway type</label>
        <select id="material" name="material">
          <option>Not sure yet</option>
          <option>Tarmac</option>
          <option>Block Paving</option>
          <option>Resin Bound</option>
          <option>Gravel</option>
        </select>
      </div>
    </div>
    <div class="field"><label for="details">Tell us about your project (optional)</label><textarea id="details" name="details" rows="3" placeholder="Approx. size, current surface, timeframe..."></textarea></div>
    <button type="submit" class="btn btn-primary btn-block">Get My Free Quote &rarr;</button>
    <p class="form-status" role="status" aria-live="polite" style="display:none;font-size:.82rem;font-weight:700;margin:10px 0 0;"></p>
  </form>
  <p class="quote-fineprint">By submitting you agree to be contacted about your enquiry. No spam, ever. See our <a href="#">privacy policy</a>.</p>
</div>"""

def quote_section(context_note="Free, no-obligation quotes for Bournemouth &amp; Poole homeowners."):
    """A full quote-form section for pages other than the homepage (which embeds its own).
    Guarantees every page has an element with id="quote" so nav/CTA #quote links actually work."""
    return f"""
<section style="background:var(--paper);">
  <div class="container" style="max-width:600px;">
    <div class="eyebrow center" style="justify-content:center;">Free Quote</div>
    <h2 class="center">Get Your Free Driveway Quote</h2>
    <p class="lede center" style="margin:0 auto 32px;">Tell us a little about your project and we&rsquo;ll get back to you within 24 hours.</p>
    {quote_form(context_note)}
  </div>
</section>"""

def trust_bar():
    items = [
        (ICON_SHIELD, "Fully insured &amp; guaranteed"),
        (ICON_STAR_SHIELD, "5.0 average rating"),
        (ICON_CLOCK, "Free quotes within 24 hours"),
        (ICON_TOOL, "Local Bournemouth &amp; Poole crews"),
    ]
    html = "".join(f'<div class="trust-item">{icon}<span>{label}</span></div>' for icon,label in items)
    return f'<div class="trust-bar"><div class="container">{html}</div></div>'

def breadcrumbs(items):
    """items: list of (label, href_or_None)"""
    parts = []
    ld_items = []
    for i, (label, href) in enumerate(items):
        if href:
            parts.append(f'<a href="{href}">{label}</a>')
        else:
            parts.append(f'<span>{label}</span>')
        ld_items.append({"@type":"ListItem","position":i+1,"name":label,"item": f"{DOMAIN}/{href}" if href else f"{DOMAIN}/{items[-1][1] or ''}"})
    html = f'<div class="breadcrumbs container">' + '<span class="sep">/</span>'.join(parts) + '</div>'
    schema = {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement": ld_items}
    return html, schema

def sticky_cta():
    return f"""
<div class="sticky-cta">
  <a href="tel:{PHONE_TEL}" class="btn btn-outline-dark btn-block">Call Now</a>
  <a href="#quote" class="btn btn-primary btn-block">Free Quote</a>
</div>
<a href="#quote" class="fab-quote">{ICON_PLUS} Free Quote</a>"""

def footer():
    material_links = "\n".join(f'<a href="{href}">{label}</a>' for label, href, _ in MATERIAL_PAGES)
    area_links = "\n".join(f'<a href="{href}">{label}</a>' for label, href in LOCATION_PAGES)
    return f"""
<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand">
        <div class="brand" style="color:#fff;margin-bottom:14px;"><span class="brand-mark">BD</span>{SITE_NAME}</div>
        <p>Local driveway installers serving Bournemouth, Poole and the surrounding Dorset coast. Tarmac, block paving, resin bound and gravel &mdash; fully insured, fully guaranteed.</p>
        <p style="margin-top:16px;"><span class="stars" style="color:var(--gold);">{STARS}</span> 5.0 rating from local homeowners</p>
      </div>
      <div>
        <h4>Driveway Types</h4>
        {material_links}
      </div>
      <div>
        <h4>Areas We Cover</h4>
        <a href="index.html">Bournemouth</a>
        {area_links}
      </div>
      <div>
        <h4>Contact</h4>
        <a href="tel:{PHONE_TEL}">{ICON_PHONE.replace('currentColor','#a9b3c4')} {PHONE_DISPLAY}</a>
        <a href="mailto:{EMAIL}">{EMAIL}</a>
        <p>{ADDRESS_LINE}</p>
        <a href="contact.html">Contact Us</a>
        <a href="driveway-cost-guide-bournemouth.html">Cost Guide</a>
        <a href="faq.html">FAQs</a>
        <a href="blog.html">Driveway Guides</a>
      </div>
    </div>
    <div class="footer-bottom">
      <span>&copy; {YEAR} {SITE_NAME}. All rights reserved.</span>
      <span>Company details, address &amp; phone number shown are placeholders &mdash; update before launch.</span>
    </div>
  </div>
</footer>"""

def faq_block(items, heading="Frequently Asked Questions", eyebrow="FAQs", sub=None, id_="faq"):
    """items: list of (question, answer_html)"""
    rows = "\n".join(f"""
    <div class="faq-item">
      <button class="faq-q">{q}{ICON_PLUS}</button>
      <div class="faq-a"><p>{a}</p></div>
    </div>""" for q,a in items)
    sub_html = f'<p class="lede">{sub}</p>' if sub else ""
    schema = {
        "@context":"https://schema.org","@type":"FAQPage",
        "mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a.replace('<strong>','').replace('</strong>','')}} for q,a in items]
    }
    html = f"""
<section id="{id_}">
  <div class="container">
    <div class="eyebrow">{eyebrow}</div>
    <h2>{heading}</h2>
    {sub_html}
    <div class="faq-list">{rows}</div>
  </div>
</section>"""
    return html, schema

def cta_band(heading, sub, primary_label="Get Your Free Quote"):
    return f"""
<section class="section-tight">
  <div class="container">
    <div class="cta-band">
      <h2>{heading}</h2>
      <p style="max-width:560px;margin:0 auto 28px;">{sub}</p>
      <div class="hero-actions center" style="justify-content:center;">
        <a href="#quote" class="btn btn-dark">{primary_label}</a>
        <a href="tel:{PHONE_TEL}" class="btn btn-outline">{ICON_PHONE} Call {PHONE_DISPLAY}</a>
      </div>
    </div>
  </div>
</section>"""

def scripts():
    return '<script src="main.js"></script>'

def page_wrap(active_href, body_html, title, description, canonical_path, schema_blocks):
    return head(title, description, canonical_path, schema_blocks) + f"""
<body>
{topbar()}
{header(active_href)}
<main>
{body_html}
</main>
{footer()}
{sticky_cta()}
{scripts()}
</body>
</html>"""

LOCAL_BUSINESS_SCHEMA = {
    "@context": "https://schema.org",
    "@type": "HomeAndConstructionBusiness",
    "name": SITE_NAME,
    "image": f"{DOMAIN}/og-image.jpg",
    "telephone": PHONE_DISPLAY,
    "email": EMAIL,
    "priceRange": "£30-£110 per m²",
    "address": {"@type": "PostalAddress", "addressLocality": "Bournemouth", "addressRegion": "Dorset", "addressCountry": "GB"},
    "areaServed": SERVICE_AREAS,
    "url": DOMAIN,
    "aggregateRating": {"@type": "AggregateRating", "ratingValue": "5.0", "reviewCount": "47"},
    "openingHoursSpecification": {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"], "opens": "08:00", "closes": "18:00"}
}

# ================================================================ HOMEPAGE ===

def build_homepage():
    schema_blocks = [LOCAL_BUSINESS_SCHEMA]

    hero = f"""
<section class="hero">
  <div class="container hero-grid">
    <div>
      <div class="hero-badges">
        <span class="hero-badge">{ICON_SHIELD} Fully Insured</span>
        <span class="hero-badge">{ICON_STAR_SHIELD} 5.0 Rated Locally</span>
        <span class="hero-badge">{ICON_CLOCK} Free Quote in 24hrs</span>
      </div>
      <h1>Bournemouth&rsquo;s Trusted Driveway Installers</h1>
      <p class="lede">Tarmac, block paving, resin bound &amp; gravel driveways installed across Bournemouth, Poole &amp; the Dorset coast. Free no-obligation quotes &mdash; most jobs completed within days.</p>
      <ul class="hero-points">
        <li>{ICON_CHECK} No deposit, no hidden fees</li>
        <li>{ICON_CHECK} Fully guaranteed workmanship</li>
        <li>{ICON_CHECK} Local crews, not subcontracted nationally</li>
      </ul>
      <div class="hero-actions">
        <a href="#quote" class="btn btn-primary">Get Your Free Quote &rarr;</a>
        <a href="tel:{PHONE_TEL}" class="btn btn-outline">{ICON_PHONE} Call {PHONE_DISPLAY}</a>
      </div>
      <div class="hero-reviews"><span class="stars">{STARS}</span> 5.0 out of 5 &mdash; from Bournemouth &amp; Poole homeowners</div>
      <div class="callout" style="margin-top:24px;background:rgba(255,255,255,.08);border-left-color:var(--gold);"><p style="color:#e7ebf3;"><strong>Quick answer:</strong> a new driveway in Bournemouth typically costs <strong>£30&ndash;£110 per m&sup2;</strong> installed, depending on material &mdash; gravel is cheapest, resin bound the most premium. Most jobs are completed in 1&ndash;3 days by fully insured local installers.</p></div>
    </div>
    {quote_form()}
  </div>
</section>"""

    materials_section = f"""
<section id="materials">
  <div class="container">
    <div class="eyebrow">Driveway Types</div>
    <h2>The Most Popular Driveway Surfaces in Bournemouth</h2>
    <p class="lede">Every driveway, drive and budget is different &mdash; compare the four most requested surfaces below, or tell us what you need and we&rsquo;ll recommend the best fit.</p>
    <div class="materials-grid">
      {"".join(material_card(*m) for m in MATERIAL_DETAILS)}
    </div>
  </div>
</section>"""

    why_us = f"""
<section style="background:var(--paper);">
  <div class="container">
    <div class="eyebrow">Why Homeowners Choose Us</div>
    <h2>Built On Trust, Not Just Tarmac</h2>
    <div class="feature-grid">
      <div class="feature"><div class="feature-icon">{ICON_SHIELD}</div><h3>Fully Insured &amp; Guaranteed</h3><p>Every install is backed by public liability cover and a written workmanship guarantee &mdash; no cutting corners.</p></div>
      <div class="feature"><div class="feature-icon">{ICON_COIN}</div><h3>Transparent, Fixed Pricing</h3><p>No call-out charges, no upselling on site. The quote you&rsquo;re given is the price you pay.</p></div>
      <div class="feature"><div class="feature-icon">{ICON_TOOL}</div><h3>Local Bournemouth Crews</h3><p>We use our own local teams &mdash; not a national subcontractor network &mdash; so quality stays consistent.</p></div>
      <div class="feature"><div class="feature-icon">{ICON_CLOCK}</div><h3>Fast Turnaround</h3><p>Most driveways are surveyed within days and installed within 1&ndash;3 days depending on size and material.</p></div>
      <div class="feature"><div class="feature-icon">{ICON_LEAF}</div><h3>SUDS &amp; Drainage Compliant</h3><p>Permeable options available so your new driveway meets UK drainage regulations without a planning headache.</p></div>
      <div class="feature"><div class="feature-icon">{ICON_STAR_SHIELD}</div><h3>5.0 Average Rating</h3><p>Rated by real Bournemouth &amp; Poole homeowners &mdash; see our full reviews on the FAQ &amp; reviews page.</p></div>
    </div>
  </div>
</section>"""

    process = f"""
<section>
  <div class="container">
    <div class="eyebrow">How It Works</div>
    <h2>From Enquiry to Finished Driveway in Four Steps</h2>
    <div class="steps">
      <div class="step"><div class="step-connector"></div><div class="num">1</div><h3>Request a Free Quote</h3><p>Fill in the form or call us &mdash; tell us the size, current surface and material you&rsquo;re considering.</p></div>
      <div class="step"><div class="step-connector"></div><div class="num">2</div><h3>Free Site Visit</h3><p>We visit to measure up, check access and drainage, and confirm a fixed, no-obligation price.</p></div>
      <div class="step"><div class="step-connector"></div><div class="num">3</div><h3>Professional Install</h3><p>Excavation, base preparation, edging and surfacing &mdash; most driveways completed in 1&ndash;3 days.</p></div>
      <div class="step"><div class="num">4</div><h3>Guaranteed Finish</h3><p>Final inspection with you, plus a written guarantee on materials and workmanship.</p></div>
    </div>
  </div>
</section>"""

    testimonials = f"""
<section class="testimonials">
  <div class="container">
    <div class="eyebrow">Reviews</div>
    <h2>What Bournemouth Homeowners Say</h2>
    <div class="t-grid">
      {testimonial_card("Absolutely delighted with our new resin driveway. Tidy, professional and finished a day early.", "Sarah H.", "Southbourne, Bournemouth")}
      {testimonial_card("Fair price, no pressure to upgrade on the day, and the block paving looks fantastic. Highly recommend.", "Mark T.", "Poole")}
      {testimonial_card("Old tarmac drive was falling apart. New surface has completely transformed the front of the house.", "Priya K.", "Ferndown")}
    </div>
    <p class="disclosure center" style="max-width:640px;color:#9aa6bb;background:transparent;border-color:rgba(255,255,255,.15);">Sample reviews shown for design purposes &mdash; replace with verified customer reviews (e.g. Google/Checkatrade) before launch.</p>
  </div>
</section>"""

    areas = f"""
<section style="background:var(--paper);">
  <div class="container center">
    <div class="eyebrow">Service Area</div>
    <h2>Driveway Installers Covering Bournemouth &amp; the Dorset Coast</h2>
    <p class="lede center">We install and repair driveways throughout the BCP area and beyond.</p>
    <div class="area-chips" style="justify-content:center;">
      {"".join(area_chip(a) for a in SERVICE_AREAS)}
    </div>
  </div>
</section>"""

    cost_teaser = f"""
<section>
  <div class="container split">
    <div>
      <div class="eyebrow">Planning Your Budget</div>
      <h2>How Much Does a Driveway Cost in Bournemouth?</h2>
      <p class="lede">Prices vary by material, size and groundwork &mdash; as a rough guide:</p>
      <ul class="checklist">
        <li>{ICON_CHECK} Gravel: from £30&ndash;£50 per m&sup2;</li>
        <li>{ICON_CHECK} Tarmac: from £40&ndash;£70 per m&sup2;</li>
        <li>{ICON_CHECK} Block paving: from £60&ndash;£100 per m&sup2;</li>
        <li>{ICON_CHECK} Resin bound: from £70&ndash;£110 per m&sup2;</li>
      </ul>
      <a href="driveway-cost-guide-bournemouth.html" class="btn btn-outline-dark" style="margin-top:8px;">See the Full Cost Guide {ICON_ARROW}</a>
    </div>
    {swatch_img("swatch-resin", "Resin bound driveway, Bournemouth", css_class="split-media")}
  </div>
</section>"""

    faq_html, faq_schema = faq_block(HOME_FAQ, heading="Common Driveway Questions", sub="Can&rsquo;t find what you&rsquo;re after? See our full FAQ page or give us a call.")
    schema_blocks.append(faq_schema)

    final_cta = cta_band("Ready to Transform Your Driveway?", "Get a free, no-obligation quote from Bournemouth&rsquo;s local driveway specialists &mdash; most quotes returned within 24 hours.")

    body = hero + trust_bar() + materials_section + why_us + process + testimonials + areas + cost_teaser + faq_html + final_cta
    return page_wrap(
        "index.html", body,
        title="Driveways Bournemouth | Block Paving, Tarmac & Resin Experts",
        description="Trusted driveway installers in Bournemouth. Tarmac, block paving, resin bound & gravel driveways. Free quotes, fully insured. Call today.",
        canonical_path="index.html",
        schema_blocks=schema_blocks
    )

def material_card(name, href, swatch, blurb, price):
    img_html = swatch_img(swatch, f"{name} driveway example, Bournemouth", css_class="material-swatch")
    return f"""
      <div class="material-card">
        {img_html}
        <div class="mc-body">
          <h3>{name} Driveways</h3>
          <p>{blurb}</p>
          <div class="mc-price">From {price}</div>
          <a href="{href}" class="mc-link">Learn more {ICON_ARROW}</a>
        </div>
      </div>"""

def area_chip(name):
    href = AREA_LINK_MAP.get(name)
    if href:
        return f'<a href="{href}" class="area-chip">{ICON_PIN}{name}</a>'
    return f'<span class="area-chip">{ICON_PIN}{name}</span>'

def testimonial_card(quote, name, place):
    return f"""
      <div class="t-card">
        <span class="stars">{STARS}</span>
        <p>&ldquo;{quote}&rdquo;</p>
        <div class="who">{name}<span>{place}</span></div>
      </div>"""

MATERIAL_DETAILS = [
    ("Tarmac", "tarmac-driveways-bournemouth.html", "swatch-tarmac", "Durable, cost-effective and quick to install &mdash; the classic choice for busy driveways.", "£40/m&sup2;"),
    ("Block Paving", "block-paving-bournemouth.html", "swatch-block", "Wide range of colours and patterns, easy to repair, adds real kerb appeal.", "£60/m&sup2;"),
    ("Resin Bound", "resin-bound-driveways-bournemouth.html", "swatch-resin", "Smooth, seamless and permeable &mdash; low maintenance with a premium finish.", "£70/m&sup2;"),
    ("Gravel", "gravel-driveways-bournemouth.html", "swatch-gravel", "The most affordable option &mdash; fast to lay with excellent natural drainage.", "£30/m&sup2;"),
]

HOME_FAQ = [
    ("How much does a new driveway cost in Bournemouth?", "Most driveways cost between <strong>£30 and £110 per m&sup2;</strong> depending on material, groundwork and access. Gravel is the most affordable option, resin bound typically the most expensive. See our full <a href=\"driveway-cost-guide-bournemouth.html\">cost guide</a> for a breakdown by material."),
    ("How long does driveway installation take?", "Most residential driveways are completed in <strong>1&ndash;3 days</strong>, depending on size, material and whether the old surface needs removing first."),
    ("Do I need planning permission for a new driveway?", "Usually not, provided the surface is permeable (gravel, permeable block paving or resin bound with a SUDS-compliant base) or drains onto your own garden rather than the street. Impermeable surfaces over 5m&sup2; may require permission &mdash; we can advise during your free site visit."),
    ("Do you handle dropped kerb applications?", "Yes &mdash; if your project needs a dropped kerb we can advise on the BCP Council application and permission process as part of your quote."),
    ("Which areas do you cover?", "We install driveways throughout Bournemouth, Poole, Christchurch, Ferndown, Wimborne, New Milton and the surrounding Dorset coast."),
    ("Which driveway material is best?", "There&rsquo;s no single &lsquo;best&rsquo; material &mdash; tarmac suits budget-conscious, high-use driveways; block paving offers the most design choice; resin bound gives a premium, low-maintenance finish; and gravel is the most affordable, fastest-to-install option. We&rsquo;ll recommend the best fit for your property and budget during your free quote."),
    ("Are you fully insured?", "Yes &mdash; every job is covered by public liability insurance, and all workmanship is backed by a written guarantee."),
]

# ========================================================== MATERIAL PAGES ===

def build_material_page(key):
    data = MATERIAL_PAGE_DATA[key]
    schema_blocks = [LOCAL_BUSINESS_SCHEMA]

    crumbs_html, crumbs_schema = breadcrumbs([("Home","index.html"), ("Driveway Types", None), (data["h1"], None)])
    schema_blocks.append(crumbs_schema)

    page_hero = f"""
<section class="page-hero">
  <div class="container">
    {crumbs_html.replace('container ','').replace('class="breadcrumbs container"','class="breadcrumbs" style="padding-top:0;color:#9aa6bb;"')}
    <div class="eyebrow" style="color:var(--gold);">{data['eyebrow']}</div>
    <h1>{data['h1']}</h1>
    <p class="lede">{data['intro']}</p>
    <ul class="hero-points">
      <li>{ICON_CHECK} From {data['price']} per m&sup2;</li>
      <li>{ICON_CHECK} {data['lifespan']}</li>
      <li>{ICON_CHECK} Free no-obligation quote</li>
    </ul>
    <div class="hero-actions" style="margin-top:26px;">
      <a href="#quote" class="btn btn-primary">Get Your Free Quote &rarr;</a>
      <a href="tel:{PHONE_TEL}" class="btn btn-outline">{ICON_PHONE} Call {PHONE_DISPLAY}</a>
    </div>
    <div class="callout" style="margin-top:28px;max-width:680px;background:rgba(255,255,255,.08);border-left-color:var(--gold);"><p style="color:#e7ebf3;"><strong>Quick answer:</strong> a {data['name']} driveway in Bournemouth typically costs from {data['price']} per m&sup2; installed, and {data['lifespan'].lower()} with normal use and basic maintenance.</p></div>
  </div>
</section>"""

    benefits = f"""
<section>
  <div class="container split">
    <div>
      <div class="eyebrow">Why Choose {data['name']}</div>
      <h2>{data['benefits_heading']}</h2>
      <p class="lede">{data['benefits_intro']}</p>
      <ul class="checklist">
        {"".join(f'<li>{ICON_CHECK} {b}</li>' for b in data['benefits'])}
      </ul>
    </div>
    {swatch_img(data['swatch'], f"{data['name']} driveway example", css_class="split-media")}
  </div>
</section>"""

    process = f"""
<section style="background:var(--paper);">
  <div class="container">
    <div class="eyebrow">Our Process</div>
    <h2>How We Install Your {data['name']} Driveway</h2>
    <div class="steps">
      {"".join(f'<div class="step"><div class="step-connector"></div><div class="num">{i+1}</div><h3>{s[0]}</h3><p>{s[1]}</p></div>' for i,s in enumerate(data['process']))}
    </div>
  </div>
</section>"""

    price_section = f"""
<section>
  <div class="container">
    <div class="eyebrow">Pricing</div>
    <h2>{data['name']} Driveway Cost Guide</h2>
    <p class="lede">Indicative 2026 pricing for a typical UK driveway &mdash; get an exact figure with a free site visit.</p>
    <table class="price-table">
      <thead><tr><th>Driveway size</th><th>Typical area</th><th>Estimated cost*</th></tr></thead>
      <tbody>
        {"".join(f"<tr><td>{r[0]}</td><td>{r[1]}</td><td class='price'>{r[2]}</td></tr>" for r in data['price_table'])}
      </tbody>
    </table>
    <p class="price-note">*Indicative estimates only ({YEAR}), based on standard groundwork and access. Final price confirmed after a free site survey.</p>
    <div class="callout"><p><strong>Comparing materials?</strong> See our full <a href="driveway-cost-guide-bournemouth.html">driveway cost guide</a> for a side-by-side breakdown of tarmac, block paving, resin bound and gravel.</p></div>
  </div>
</section>"""

    faq_html, faq_schema = faq_block(data['faq'], heading=f"{data['name']} Driveway FAQs")
    schema_blocks.append(faq_schema)

    related = [m for m in MATERIAL_DETAILS if m[1] != data['href']]
    related_html = f"""
<section style="background:var(--paper);">
  <div class="container">
    <div class="eyebrow">Compare Options</div>
    <h2>Other Popular Driveway Materials</h2>
    <div class="related-grid">
      {"".join(f'<a class="related-card" href="{m[1]}">{m[0]} Driveways {ICON_ARROW}</a>' for m in related)}
    </div>
  </div>
</section>"""

    final_cta = cta_band(f"Get a Free {data['name']} Driveway Quote", "Fixed pricing, fully insured installers and a written guarantee &mdash; talk to us today.")

    body = page_hero + trust_bar() + benefits + process + price_section + faq_html + related_html + quote_section(f"Free, no-obligation quotes for {data['name']} driveways in Bournemouth.") + final_cta
    return page_wrap(
        data['href'], body,
        title=data['meta_title'], description=data['meta_description'],
        canonical_path=data['href'], schema_blocks=schema_blocks
    )

MATERIAL_PAGE_DATA = {
    "tarmac": {
        "name": "Tarmac", "href": "tarmac-driveways-bournemouth.html", "swatch": "swatch-tarmac",
        "eyebrow": "Tarmac Driveways",
        "h1": "Tarmac Driveways in Bournemouth",
        "meta_title": "Tarmac Driveways Bournemouth | Free Quotes",
        "meta_description": "Professional tarmac driveway installation in Bournemouth. Durable, cost-effective surfacing built to last 20-30 years. Free quote.",
        "intro": "Durable, smooth and cost-effective &mdash; tarmac remains the most popular driveway surface in the UK. Professionally installed tarmac driveways across Bournemouth, Poole and the surrounding Dorset coast.",
        "price": "£40",
        "lifespan": "Lasts 20&ndash;30 years",
        "benefits_heading": "Durable, Practical and Great Value",
        "benefits_intro": "Tarmac is the go-to choice for homeowners who want a smooth, hard-wearing surface without the premium price tag of block paving or resin.",
        "benefits": [
            "Cost-effective &mdash; typically the second cheapest option after gravel",
            "Fast to install, often finished within 1&ndash;2 days",
            "Smooth, comfortable surface for cars, bikes and pushchairs",
            "Highly durable &mdash; lasts 20&ndash;30 years with proper maintenance",
            "Simple to repair and resurface if damaged",
        ],
        "process": [
            ("Excavation", "Remove the existing surface and excavate to the correct depth for a stable sub-base."),
            ("Sub-base &amp; Edging", "Lay and compact a MOT Type 1 sub-base, then install edging to contain the new surface."),
            ("Tarmac Laying", "Apply and roll the tarmac in layers for a smooth, durable, properly compacted finish."),
            ("Finishing", "Line marking (if required), clean-up and final inspection with you before we leave."),
        ],
        "price_table": [
            ("Small (up to 30m&sup2;)", "Single car driveway", "£1,200 &ndash; £2,100"),
            ("Medium (30&ndash;60m&sup2;)", "Double driveway", "£2,100 &ndash; £4,200"),
            ("Large (60m&sup2;+)", "Wraparound / multi-car", "£4,200+"),
        ],
        "faq": [
            ("How long does a tarmac driveway last?", "A well-installed tarmac driveway typically lasts <strong>20&ndash;30 years</strong> with basic maintenance such as periodic sealing and prompt repair of any cracks."),
            ("Is tarmac cheaper than block paving?", "Yes &mdash; tarmac is generally <strong>30&ndash;50% cheaper</strong> than block paving per m&sup2;, making it a popular choice for larger driveways."),
            ("Can you repair an existing tarmac driveway instead of replacing it?", "Often, yes. Cracks, potholes and sunken areas can frequently be resurfaced rather than fully replaced &mdash; ask us about our <a href=\"driveway-repairs-resurfacing-bournemouth.html\">repair &amp; resurfacing service</a> when you request your quote."),
            ("Does tarmac need much maintenance?", "Very little &mdash; occasional sweeping, prompt repair of small cracks, and resealing every few years is usually enough to maximise its lifespan."),
            ("What colour options are available for a tarmac driveway?", "Standard tarmac is black, though a red-tint or buff finish is available at a small extra cost if you want to soften the look against a lighter-coloured property."),
            ("Is tarmac suitable for a steep or sloped driveway?", "Yes &mdash; properly laid tarmac copes well with slopes and inclines, and its smooth, consistent surface is often preferable to loose materials like gravel on a gradient."),
        ],
    },
    "block": {
        "name": "Block Paving", "href": "block-paving-bournemouth.html", "swatch": "swatch-block",
        "eyebrow": "Block Paving",
        "h1": "Block Paving Driveways in Bournemouth",
        "meta_title": "Block Paving Bournemouth | Driveways & Patios",
        "meta_description": "Expert block paving driveways in Bournemouth. Wide range of colours and patterns, fully guaranteed workmanship. Get a free quote.",
        "intro": "Block paving combines durability with real kerb appeal &mdash; a huge range of colours, patterns and finishes to suit any property, professionally installed across Bournemouth and Poole.",
        "price": "£60",
        "lifespan": "Lasts 25&ndash;40+ years",
        "benefits_heading": "Style, Strength and Easy Repairs",
        "benefits_intro": "Block paving is the top choice for homeowners who want their driveway to genuinely enhance the look of their property.",
        "benefits": [
            "Huge choice of colours, patterns and block styles",
            "Individual blocks can be lifted and replaced &mdash; no need to resurface the whole drive",
            "Adds noticeable kerb appeal and can boost property value",
            "Permeable block paving available to meet SUDS drainage rules",
            "Extremely durable when laid on a properly compacted base",
        ],
        "process": [
            ("Excavation &amp; Sub-base", "Excavate to depth and lay a compacted MOT Type 1 sub-base for long-term stability."),
            ("Edge Restraints", "Install concrete or block edging to lock the pattern in place and prevent spreading."),
            ("Laying the Blocks", "Lay blocks in your chosen pattern (herringbone, basketweave, stack bond) on a sand bed."),
            ("Compacting &amp; Jointing", "Vibrate the surface, brush in jointing sand, and complete a final wash-down and inspection."),
        ],
        "price_table": [
            ("Small (up to 30m&sup2;)", "Single car driveway", "£1,800 &ndash; £3,000"),
            ("Medium (30&ndash;60m&sup2;)", "Double driveway", "£3,000 &ndash; £6,000"),
            ("Large (60m&sup2;+)", "Wraparound / multi-car", "£6,000+"),
        ],
        "faq": [
            ("What&rsquo;s the difference between block paving and tarmac?", "Block paving costs more but offers far more design choice, adds more kerb appeal, and allows individual blocks to be replaced if damaged &mdash; tarmac is cheaper and quicker to install but offers a single, uniform finish."),
            ("Can block paving be repaired easily?", "Yes &mdash; this is one of its biggest advantages. If a block cracks or an oil stain won&rsquo;t lift, we simply replace the individual block rather than resurfacing the whole driveway."),
            ("Is block paving permeable?", "Standard block paving isn&rsquo;t, but permeable block paving systems are available and can help you meet UK SUDS drainage rules without needing planning permission."),
            ("How do I keep weeds from growing between the blocks?", "Properly compacted jointing sand (or polymeric sand) greatly reduces weed growth. An occasional re-sand and jet wash keeps the surface looking new."),
            ("How long does block paving take to install?", "Most single or double driveways are completed in 2&ndash;4 days, depending on size, the pattern chosen and whether the old surface needs excavating first."),
            ("Can block paving be laid over an existing concrete driveway?", "Not directly &mdash; the old surface is normally excavated so we can lay a proper compacted sub-base underneath. Laying straight over concrete or tarmac can lead to instability and early failure."),
        ],
    },
    "resin": {
        "name": "Resin Bound", "href": "resin-bound-driveways-bournemouth.html", "swatch": "swatch-resin",
        "eyebrow": "Resin Bound Driveways",
        "h1": "Resin Bound Driveways in Bournemouth",
        "meta_title": "Resin Bound Driveways Bournemouth | Resin Experts",
        "meta_description": "Smooth, permeable resin bound driveways installed across Bournemouth. SUDS compliant, low maintenance. Free no-obligation quote.",
        "intro": "A smooth, seamless, permeable finish with a premium natural-stone look. Resin bound is one of the fastest-growing driveway choices in Bournemouth &mdash; low maintenance and SUDS compliant by design.",
        "price": "£70",
        "lifespan": "Lasts 20&ndash;25 years",
        "benefits_heading": "Premium Finish, Minimal Maintenance",
        "benefits_intro": "Resin bound driveways are fully permeable, weed-resistant and available in dozens of natural stone blends &mdash; a genuinely premium upgrade.",
        "benefits": [
            "Smooth, seamless finish &mdash; no loose stones underfoot (unlike resin bonded)",
            "Fully permeable &mdash; meets SUDS drainage regulations as standard",
            "Naturally weed and moss resistant, very low maintenance",
            "Wide choice of natural stone blends and colours",
            "UV stable &mdash; won&rsquo;t fade or discolour in sunlight",
        ],
        "process": [
            ("Excavation &amp; Base", "Excavate and lay a permeable sub-base designed to allow water to drain through the whole system."),
            ("Preparation", "Install edging and a porous macadam or concrete base layer, primed ready for the resin-bound surface."),
            ("Mixing &amp; Laying", "Aggregate is hand-mixed with clear resin on site, then trowelled to a smooth, seamless finish."),
            ("Curing &amp; Inspection", "The surface cures over 24&ndash;48 hours before full use, followed by a final walk-through with you."),
        ],
        "price_table": [
            ("Small (up to 30m&sup2;)", "Single car driveway", "£2,100 &ndash; £3,300"),
            ("Medium (30&ndash;60m&sup2;)", "Double driveway", "£3,300 &ndash; £6,600"),
            ("Large (60m&sup2;+)", "Wraparound / multi-car", "£6,600+"),
        ],
        "faq": [
            ("What&rsquo;s the difference between resin bound and resin bonded?", "Resin bound is mixed and trowelled to a smooth, level, permeable finish &mdash; resin bonded is scattered loose over a resin layer, leaving a textured, non-permeable surface that can shed stones. We install resin <strong>bound</strong>, the higher-spec option."),
            ("Is resin bound worth the extra cost?", "Many homeowners feel so &mdash; it offers a genuinely premium finish, near-zero weed growth, full SUDS compliance and a smooth surface that&rsquo;s easy to walk and wheel on, for roughly 20&ndash;25 years."),
            ("Does resin bound crack like concrete?", "Because it has a degree of flexibility, resin bound is generally more resistant to hairline cracking from ground movement than poured concrete or old tarmac."),
            ("How do I clean a resin bound driveway?", "A regular sweep and an occasional pressure wash on a low setting is normally all that&rsquo;s needed to keep it looking new."),
            ("Is a resin bound driveway slippery when wet?", "No &mdash; the aggregate finish gives a textured, slip-resistant surface, which is one reason it&rsquo;s a popular choice for paths and driveways with wheelchair or pushchair access."),
            ("How long does a resin bound driveway take to install?", "Most driveways are laid within 1&ndash;2 days, though the surface needs roughly 24&ndash;48 hours to cure fully before regular vehicle use."),
        ],
    },
    "gravel": {
        "name": "Gravel", "href": "gravel-driveways-bournemouth.html", "swatch": "swatch-gravel",
        "eyebrow": "Gravel Driveways",
        "h1": "Gravel Driveways in Bournemouth",
        "meta_title": "Gravel Driveways Bournemouth | Installation & Repair",
        "meta_description": "Affordable gravel driveway installation in Bournemouth. Fast to lay, low cost, wide choice of stone. Free quote available.",
        "intro": "The most affordable and fastest-to-install driveway option, with a natural look that suits period and rural properties especially well. Installed across Bournemouth, Poole and the New Forest fringe.",
        "price": "£30",
        "lifespan": "Lasts 15&ndash;20+ years (with occasional top-ups)",
        "benefits_heading": "Affordable, Fast and Naturally Draining",
        "benefits_intro": "Gravel is the budget-friendly, quick-turnaround choice &mdash; ideal if you want a smart-looking driveway without the cost of a bound surface.",
        "benefits": [
            "The most affordable driveway surface, typically from £30/m&sup2;",
            "Fast installation &mdash; often completed in a single day",
            "Naturally permeable &mdash; excellent drainage, SUDS-friendly",
            "Wide choice of stone colours and sizes to suit your property",
            "Easy to top up or repair yourself over time",
        ],
        "process": [
            ("Excavation", "Excavate to the correct depth to accommodate the sub-base and gravel layer."),
            ("Weed Membrane &amp; Sub-base", "Lay a geotextile membrane and compacted sub-base to stop weeds and prevent the gravel sinking."),
            ("Edging", "Install edging (timber, metal or block) to keep the gravel contained and neat."),
            ("Gravel Laying", "Spread and rake your chosen stone to an even depth, then compact for a stable, comfortable surface."),
        ],
        "price_table": [
            ("Small (up to 30m&sup2;)", "Single car driveway", "£900 &ndash; £1,500"),
            ("Medium (30&ndash;60m&sup2;)", "Double driveway", "£1,500 &ndash; £3,000"),
            ("Large (60m&sup2;+)", "Wraparound / multi-car", "£3,000+"),
        ],
        "faq": [
            ("Is a gravel driveway high maintenance?", "It&rsquo;s low maintenance rather than no maintenance &mdash; occasional raking and topping up loose areas keeps it looking neat, and a weed membrane underneath minimises weed growth."),
            ("Will gravel scatter onto the road or pavement?", "Proper edging (which we always include) contains the stone and prevents it spreading beyond the driveway."),
            ("Is gravel a good option for drainage?", "Yes &mdash; gravel is one of the most naturally permeable driveway surfaces, which is why it&rsquo;s a popular, planning-permission-friendly choice."),
            ("Can I choose different gravel colours?", "Yes, we offer a range of stone types and colours, from traditional golden gravel to darker slate chippings &mdash; samples available at your free site visit."),
            ("What&rsquo;s the ideal depth for a gravel driveway?", "We typically lay gravel to a depth of around 50mm over a properly compacted sub-base &mdash; deep enough for a stable, comfortable surface without excessive stone movement."),
            ("Is gravel a good choice for a driveway used daily?", "Yes, with a well-compacted sub-base and edging, gravel copes well with daily use &mdash; occasional raking and top-ups in high-traffic wheel tracks keeps it looking even."),
        ],
    },
}

# ============================================================ LOCATION PAGES ===

def build_location_page(key):
    data = LOCATION_PAGE_DATA[key]
    schema_blocks = [dict(LOCAL_BUSINESS_SCHEMA, areaServed=[data['name']])]
    crumbs_html, crumbs_schema = breadcrumbs([("Home","index.html"), ("Areas We Cover", None), (data['name'], None)])
    schema_blocks.append(crumbs_schema)

    page_hero = f"""
<section class="page-hero">
  <div class="container">
    {crumbs_html.replace('class="breadcrumbs container"','class="breadcrumbs" style="padding-top:0;color:#9aa6bb;"')}
    <div class="eyebrow" style="color:var(--gold);">Serving {data['name']}</div>
    <h1>Driveways in {data['name']}</h1>
    <p class="lede">{data['intro']}</p>
    <ul class="hero-points">
      <li>{ICON_CHECK} {data['proof_point']}</li>
      <li>{ICON_CHECK} Free, no-obligation site visit</li>
      <li>{ICON_CHECK} Fully insured local installers</li>
    </ul>
    <div class="hero-actions" style="margin-top:26px;">
      <a href="#quote" class="btn btn-primary">Get Your Free Quote &rarr;</a>
      <a href="tel:{PHONE_TEL}" class="btn btn-outline">{ICON_PHONE} Call {PHONE_DISPLAY}</a>
    </div>
    <div class="callout" style="margin-top:28px;max-width:680px;background:rgba(255,255,255,.08);border-left-color:var(--gold);"><p style="color:#e7ebf3;"><strong>Quick answer:</strong> yes &mdash; we install and repair tarmac, block paving, resin bound and gravel driveways throughout {data['name']}, with free no-obligation quotes and most site visits arranged within a few days.</p></div>
  </div>
</section>"""

    materials_section = f"""
<section id="materials">
  <div class="container">
    <div class="eyebrow">Driveway Types in {data['name']}</div>
    <h2>Popular Driveway Surfaces We Install in {data['name']}</h2>
    <div class="materials-grid">
      {"".join(material_card(*m) for m in MATERIAL_DETAILS)}
    </div>
  </div>
</section>"""

    local = f"""
<section style="background:var(--paper);">
  <div class="container split">
    <div>
      <div class="eyebrow">Local to {data['name']}</div>
      <h2>{data['local_heading']}</h2>
      <p class="lede">{data['local_body']}</p>
      <ul class="checklist">
        <li>{ICON_CHECK} No deposit, no hidden fees</li>
        <li>{ICON_CHECK} Written workmanship guarantee</li>
        <li>{ICON_CHECK} Most driveways completed in 1&ndash;3 days</li>
      </ul>
    </div>
    {swatch_img(data['swatch'], f"{data['name']} driveway example", css_class="split-media")}
  </div>
</section>"""

    faq_html, faq_schema = faq_block(data['faq'], heading=f"Driveways in {data['name']}: FAQs")
    schema_blocks.append(faq_schema)

    other_areas = [a for a in LOCATION_PAGES if a[1] != data['href']]
    areas_html = f"""
<section>
  <div class="container">
    <div class="eyebrow">Other Areas We Cover</div>
    <h2>Also Serving the Wider Dorset Coast</h2>
    <div class="related-grid">
      <a class="related-card" href="index.html">Bournemouth {ICON_ARROW}</a>
      {"".join(f'<a class="related-card" href="{href}">{label} {ICON_ARROW}</a>' for label, href in other_areas)}
    </div>
  </div>
</section>"""

    final_cta = cta_band(f"Get a Free Driveway Quote in {data['name']}", "Fixed pricing, fully insured installers and a written guarantee &mdash; talk to us today.")

    body = page_hero + trust_bar() + materials_section + local + faq_html + areas_html + quote_section(f"Free, no-obligation quotes for {data['name']} homeowners.") + final_cta
    return page_wrap(
        data['href'], body, title=data['meta_title'], description=data['meta_description'],
        canonical_path=data['href'], schema_blocks=schema_blocks
    )

LOCATION_PAGE_DATA = {
    "poole": {
        "name": "Poole", "href": "driveways-poole.html", "swatch": "swatch-block",
        "meta_title": "Driveways Poole | Block Paving, Tarmac & Resin",
        "meta_description": "Local driveway installers serving Poole. Tarmac, block paving, resin and gravel driveways. Free quotes, fully insured.",
        "intro": "Local driveway installers serving Poole and the harbour side &mdash; from Sandbanks to Broadstone. Tarmac, block paving, resin bound and gravel, fully insured and guaranteed.",
        "proof_point": "Recent projects completed across Poole &amp; the harbour side",
        "local_heading": "Driveway Installers Who Know Poole",
        "local_body": "From period homes near the Old Town to modern builds around Canford Heath and Broadstone, we tailor the driveway to the property &mdash; not just a one-size-fits-all install.",
        "faq": [
            ("Do you cover all of Poole, including Sandbanks and Broadstone?", "Yes &mdash; we cover Poole and the surrounding harbour side including Sandbanks, Broadstone, Canford Heath and Hamworthy."),
            ("How quickly can you visit for a quote in Poole?", "We typically offer free site visits within a few days of enquiry &mdash; get in touch and we&rsquo;ll confirm a time that suits you."),
            ("How much does a driveway cost in Poole?", "Pricing in Poole is in line with the wider Bournemouth area &mdash; roughly £30&ndash;£110 per m&sup2; depending on material. See our full <a href=\"driveway-cost-guide-bournemouth.html\">cost guide</a> for a breakdown."),
            ("Which driveway material suits coastal properties near Sandbanks best?", "Resin bound and block paving tend to hold up particularly well to coastal weather, though we&rsquo;ll advise honestly based on your specific property and budget."),
        ],
    },
    "christchurch": {
        "name": "Christchurch", "href": "driveways-christchurch.html", "swatch": "swatch-tarmac",
        "meta_title": "Driveways Christchurch | Local Driveway Installers",
        "meta_description": "Trusted driveway installation and repair across Christchurch, Dorset. Tarmac, block paving & resin. Free no-obligation quote.",
        "intro": "Trusted driveway installation and repair across Christchurch, Dorset &mdash; from the town centre out to Highcliffe and Mudeford. Free, no-obligation quotes.",
        "proof_point": "Local crews regularly working across Christchurch &amp; Highcliffe",
        "local_heading": "Driveways Built for Christchurch Homes",
        "local_body": "Whether it&rsquo;s a period property near the Priory or a newer build towards Highcliffe, we match the driveway material and finish to suit the area.",
        "faq": [
            ("Do you cover Highcliffe and Mudeford as well as Christchurch town?", "Yes &mdash; our Christchurch coverage includes Highcliffe, Mudeford and the surrounding villages."),
            ("Can you install a driveway on a period property in Christchurch?", "Yes, we regularly work on period properties &mdash; block paving and resin bound are popular choices where kerb appeal matters most."),
            ("Do you offer free quotes for driveways in Christchurch?", "Yes &mdash; every quote in Christchurch and the surrounding area is free and no-obligation, with a site visit to confirm an exact, fixed price."),
            ("How long does a typical driveway installation take in Christchurch?", "Most jobs are completed in 1&ndash;3 days depending on size and material &mdash; the same timeframe as the rest of our Dorset coverage area."),
        ],
    },
    "ferndown": {
        "name": "Ferndown", "href": "driveways-ferndown.html", "swatch": "swatch-gravel",
        "meta_title": "Driveways Ferndown | Local Driveway Installers",
        "meta_description": "Driveway installation and repair in Ferndown. Tarmac, block paving, resin and gravel. Fully insured, free quotes.",
        "intro": "Driveway installation and repair across Ferndown and the surrounding villages. Tarmac, block paving, resin bound and gravel, fully insured with a written guarantee.",
        "proof_point": "Serving Ferndown, West Moors and surrounding villages",
        "local_heading": "Local, Reliable Driveway Installers in Ferndown",
        "local_body": "Ferndown&rsquo;s mix of family homes and larger properties means we install everything from compact single driveways to large multi-car resin bound and block paving projects.",
        "faq": [
            ("Do you cover West Moors and the villages around Ferndown?", "Yes &mdash; we cover Ferndown and the surrounding villages including West Moors and Longham."),
            ("What&rsquo;s the most popular driveway type in Ferndown?", "Block paving and gravel are particularly popular locally, though we install all four surfaces depending on your property and budget."),
            ("Can you handle larger, multi-car driveways in Ferndown?", "Yes &mdash; Ferndown&rsquo;s larger plots are well suited to multi-car driveways, and we regularly quote for wraparound and large-format projects."),
            ("Do you offer dropped kerb advice for Ferndown properties?", "Yes &mdash; if your Ferndown driveway project needs a new or altered dropped kerb, we can advise on the BCP Council application process as part of your quote."),
        ],
    },
    "wimborne": {
        "name": "Wimborne", "href": "driveways-wimborne.html", "swatch": "swatch-resin",
        "meta_title": "Driveways Wimborne | Local Driveway Installers",
        "meta_description": "Local driveway installation and repair across Wimborne. Tarmac, block paving, resin and gravel. Free quotes available.",
        "intro": "Local driveway installation and repair across Wimborne Minster and the surrounding countryside. Tarmac, block paving, resin bound and gravel, free no-obligation quotes.",
        "proof_point": "Familiar with Wimborne&rsquo;s period &amp; rural properties",
        "local_heading": "Driveways Suited to Wimborne&rsquo;s Character",
        "local_body": "Wimborne&rsquo;s mix of historic town-centre homes and rural properties often calls for gravel or resin bound surfaces that complement the setting &mdash; we&rsquo;ll advise honestly on what suits your property.",
        "faq": [
            ("Is gravel a good option for a period property in Wimborne?", "Often, yes &mdash; gravel and resin bound tend to suit period and rural properties particularly well, though the right choice always depends on your specific driveway and budget."),
            ("Do you handle driveways on rural or unadopted roads near Wimborne?", "Yes, we regularly quote for rural properties &mdash; access and ground conditions are assessed during your free site visit."),
            ("Do you need planning permission for a driveway in Wimborne Minster's conservation area?", "Possibly, depending on the property and surface chosen &mdash; permeable materials like gravel or SUDS-compliant resin bound usually avoid the need for permission. We can advise during your free site visit."),
            ("How far outside Wimborne do you cover?", "We cover Wimborne Minster and the surrounding villages and rural areas &mdash; get in touch to confirm coverage for your specific postcode."),
        ],
    },
    "new-milton": {
        "name": "New Milton", "href": "driveways-new-milton.html", "swatch": "swatch-tarmac",
        "meta_title": "Driveways New Milton | Local Driveway Installers",
        "meta_description": "Driveway installation and repair serving New Milton. Tarmac, block paving, resin and gravel. Fully insured, free quotes.",
        "intro": "Driveway installation and repair serving New Milton and the western edge of the Dorset/Hampshire border. Tarmac, block paving, resin bound and gravel, fully insured.",
        "proof_point": "Covering New Milton through to the Hampshire border",
        "local_heading": "Driveway Installers Covering New Milton",
        "local_body": "From New Milton town through to Barton on Sea and the surrounding area, we install and repair driveways to the same fixed-price, fully guaranteed standard as the rest of our coverage area.",
        "faq": [
            ("Do you cover Barton on Sea as well as New Milton?", "Yes &mdash; our New Milton coverage extends to Barton on Sea and the immediate surrounding area."),
            ("Is New Milton within your standard coverage area?", "Yes, New Milton is one of our core coverage areas alongside Bournemouth, Poole and Christchurch."),
            ("What driveway materials are most popular in New Milton?", "Tarmac and block paving are the most requested locally, though we install all four materials &mdash; tarmac, block paving, resin bound and gravel &mdash; depending on your property and budget."),
            ("Can I get a same-week quote for a driveway in New Milton?", "In most cases, yes &mdash; contact us and we&rsquo;ll aim to arrange a free site visit within a few days."),
        ],
    },
}

# ============================================================ COST GUIDE ===

def build_cost_guide():
    schema_blocks = [LOCAL_BUSINESS_SCHEMA]
    crumbs_html, crumbs_schema = breadcrumbs([("Home","index.html"), ("Driveway Cost Guide", None)])
    schema_blocks.append(crumbs_schema)

    page_hero = f"""
<section class="page-hero">
  <div class="container">
    {crumbs_html.replace('class="breadcrumbs container"','class="breadcrumbs" style="padding-top:0;color:#9aa6bb;"')}
    <div class="eyebrow" style="color:var(--gold);">Pricing</div>
    <h1>Driveway Cost Guide: Bournemouth Prices {YEAR}</h1>
    <p class="lede">How much does a driveway cost in Bournemouth? Here&rsquo;s a full, honest breakdown by material, size and the factors that move the price &mdash; plus how to get an exact figure.</p>
  </div>
</section>"""

    intro = f"""
<section class="section-tight">
  <div class="container">
    <div class="callout"><p><strong>Quick answer:</strong> most Bournemouth driveways cost between <strong>£30 and £110 per m&sup2;</strong> installed. Gravel is the cheapest option, resin bound is typically the most expensive. A typical single-car driveway (approx. 25&ndash;30m&sup2;) costs roughly <strong>£900 to £3,300</strong> depending on material.</p></div>
  </div>
</section>"""

    table = f"""
<section class="section-tight">
  <div class="container">
    <h2>Driveway Cost Per m&sup2; By Material</h2>
    <table class="price-table">
      <thead><tr><th>Material</th><th>Cost per m&sup2;</th><th>Single driveway (~28m&sup2;)</th><th>Lifespan</th></tr></thead>
      <tbody>
        <tr><td>Gravel</td><td class="price">£30 &ndash; £50</td><td>£900 &ndash; £1,500</td><td>15&ndash;20+ years</td></tr>
        <tr><td>Tarmac</td><td class="price">£40 &ndash; £70</td><td>£1,200 &ndash; £2,100</td><td>20&ndash;30 years</td></tr>
        <tr><td>Block Paving</td><td class="price">£60 &ndash; £100</td><td>£1,800 &ndash; £3,000</td><td>25&ndash;40+ years</td></tr>
        <tr><td>Resin Bound</td><td class="price">£70 &ndash; £110</td><td>£2,100 &ndash; £3,300</td><td>20&ndash;25 years</td></tr>
      </tbody>
    </table>
    <p class="price-note">Indicative {YEAR} estimates for standard groundwork and access in the Bournemouth &amp; Poole area. Actual prices depend on the factors below &mdash; get a free, fixed quote for an exact figure.</p>
  </div>
</section>"""

    factors = f"""
<section style="background:var(--paper);">
  <div class="container">
    <div class="eyebrow">What Affects the Price</div>
    <h2>7 Factors That Change Your Driveway Cost</h2>
    <div class="feature-grid">
      <div class="feature"><h3>Size</h3><p>The single biggest factor &mdash; price is usually quoted per m&sup2;, so larger driveways cost more in total but often slightly less per m&sup2;.</p></div>
      <div class="feature"><h3>Existing surface removal</h3><p>Breaking up and removing an old concrete, tarmac or block driveway adds to groundwork time and skip/tip costs.</p></div>
      <div class="feature"><h3>Access</h3><p>Restricted access for machinery or materials (narrow side passages, no direct road access) can increase labour time.</p></div>
      <div class="feature"><h3>Groundwork &amp; drainage</h3><p>Soft ground, poor drainage or the need for a soakaway/permeable base adds cost but is essential for a long-lasting surface.</p></div>
      <div class="feature"><h3>Edging &amp; kerbing</h3><p>Decorative edging, kerbing or a border in a contrasting material adds a premium finish &mdash; and a modest cost.</p></div>
      <div class="feature"><h3>Pattern &amp; design</h3><p>Herringbone block paving or multi-colour resin blends take longer to lay than a single, uniform surface.</p></div>
      <div class="feature"><h3>Dropped kerb</h3><p>If you need a new dropped kerb, factor in the <a href="dropped-kerb-bournemouth.html">BCP Council permission and installation cost</a> separately.</p></div>
    </div>
  </div>
</section>"""

    material_links = f"""
<section>
  <div class="container">
    <div class="eyebrow">Explore by Material</div>
    <h2>Get a Detailed Breakdown for Your Chosen Material</h2>
    <div class="related-grid">
      {"".join(f'<a class="related-card" href="{m[1]}">{m[0]} Driveways {ICON_ARROW}</a>' for m in MATERIAL_DETAILS)}
    </div>
  </div>
</section>"""

    cost_faq = [
        ("Is it cheaper to repair or replace a driveway?", "Repair is almost always cheaper in the short term, but if more than 30&ndash;40% of the surface is damaged, full replacement is often better value long-term. See our <a href=\"driveway-repairs-resurfacing-bournemouth.html\">repairs &amp; resurfacing</a> page."),
        ("Do you charge for quotes or site visits?", "No &mdash; every quote and site visit is completely free, with no obligation to book."),
        ("Are there hidden costs I should ask about?", "Always ask whether the quote includes excavation and disposal of the old surface, edging, and any drainage work &mdash; our written quotes include all of this as standard, with no surprises on the day."),
        ("What&rsquo;s the cheapest driveway option?", "Gravel is typically the most affordable driveway surface, followed by tarmac. See our <a href=\"gravel-driveways-bournemouth.html\">gravel driveways page</a> for details."),
    ]
    faq_html, faq_schema = faq_block(cost_faq, heading="Driveway Cost FAQs")
    schema_blocks.append(faq_schema)

    final_cta = cta_band("Want an Exact Price, Not Just a Guide?", "Get a free, fixed quote for your driveway &mdash; tailored to your size, material and site.")

    body = page_hero + intro + table + factors + material_links + faq_html + quote_section() + final_cta
    return page_wrap(
        "driveway-cost-guide-bournemouth.html", body,
        title=f"Driveway Cost Guide Bournemouth {YEAR} | Prices Per m&sup2;",
        description=f"How much does a driveway cost in Bournemouth? Full price breakdown by material — tarmac, block paving, resin & gravel. Updated {YEAR}.",
        canonical_path="driveway-cost-guide-bournemouth.html",
        schema_blocks=schema_blocks
    )

# ================================================================== FAQ ===

def build_faq_page():
    schema_blocks = [LOCAL_BUSINESS_SCHEMA]
    crumbs_html, crumbs_schema = breadcrumbs([("Home","index.html"), ("FAQs", None)])
    schema_blocks.append(crumbs_schema)

    page_hero = f"""
<section class="page-hero">
  <div class="container">
    {crumbs_html.replace('class="breadcrumbs container"','class="breadcrumbs" style="padding-top:0;color:#9aa6bb;"')}
    <div class="eyebrow" style="color:var(--gold);">FAQs</div>
    <h1>Driveway FAQs</h1>
    <p class="lede">Answers to the questions Bournemouth homeowners ask us most about cost, timescales, permissions and maintenance.</p>
  </div>
</section>"""

    all_faq = [
        ("How long does it take to install a new driveway?", "Most residential driveways take <strong>1&ndash;3 days</strong> depending on size and material &mdash; gravel and tarmac are typically fastest, block paving and resin bound take slightly longer due to base preparation."),
        ("Do I need planning permission for a new driveway in Bournemouth?", "Usually not. Under UK &lsquo;permitted development&rsquo; rules, you don&rsquo;t need permission if the new surface is permeable (gravel, permeable block paving, or resin bound on a SUDS-compliant base) or drains onto your own garden. Impermeable surfaces over 5m&sup2; draining to the street generally do require permission &mdash; we&rsquo;ll advise during your free site visit."),
        ("Do you need permission for a dropped kerb?", "Yes &mdash; a dropped kerb requires separate permission and installation via <strong>BCP Council</strong>. We can talk you through the process and cost when you request a quote &mdash; see our <a href=\"dropped-kerb-bournemouth.html\">dropped kerb page</a> for more detail."),
        ("What&rsquo;s the cheapest type of driveway?", "Gravel is generally the most affordable option, from around £30 per m&sup2;, followed by tarmac. See our full <a href=\"driveway-cost-guide-bournemouth.html\">cost guide</a> for a material-by-material comparison."),
        ("Which driveway material lasts the longest?", "Block paving typically lasts the longest &mdash; 25 to 40+ years &mdash; because individual blocks can be replaced rather than resurfacing the whole driveway."),
        ("How do I maintain a resin bound driveway?", "Very little maintenance is needed &mdash; an occasional sweep and light pressure wash keeps it looking new. Resin bound is naturally weed and moss resistant."),
        ("Do you offer a guarantee?", "Yes &mdash; every installation is covered by a written guarantee on materials and workmanship, in addition to our public liability insurance."),
        ("Do you charge a deposit?", "No &mdash; we don&rsquo;t take deposits or charge call-out fees. You only pay once you&rsquo;re happy with the completed work."),
        ("Which areas do you cover?", "We install and repair driveways throughout Bournemouth, Poole, Christchurch, Ferndown, Wimborne, New Milton and the surrounding Dorset coast."),
        ("Can you repair my existing driveway instead of replacing it?", "Often, yes &mdash; cracked or sunken tarmac, loose block paving and worn edging can frequently be repaired rather than replaced. See our <a href=\"driveway-repairs-resurfacing-bournemouth.html\">repairs &amp; resurfacing</a> page or ask us during your free quote."),
    ]
    faq_html, faq_schema = faq_block(all_faq, heading="All Questions", eyebrow="", sub=None)
    schema_blocks.append(faq_schema)

    final_cta = cta_band("Still Have a Question?", "Call our local team or request a free quote &mdash; we&rsquo;re happy to talk through your project with no pressure to book.")

    body = page_hero + trust_bar() + faq_html + quote_section() + final_cta
    return page_wrap(
        "faq.html", body,
        title="Driveway FAQs | Bournemouth Driveway Installers",
        description="Answers to common driveway questions — cost, timescales, planning permission and maintenance for Bournemouth homeowners.",
        canonical_path="faq.html",
        schema_blocks=schema_blocks
    )

# ============================================================ SERVICE PAGES ===

def build_service_page(key):
    data = SERVICE_PAGE_DATA[key]
    schema_blocks = [LOCAL_BUSINESS_SCHEMA]
    crumbs_html, crumbs_schema = breadcrumbs([("Home","index.html"), (data['h1'], None)])
    schema_blocks.append(crumbs_schema)

    page_hero = f"""
<section class="page-hero">
  <div class="container">
    {crumbs_html.replace('class="breadcrumbs container"','class="breadcrumbs" style="padding-top:0;color:#9aa6bb;"')}
    <div class="eyebrow" style="color:var(--gold);">{data['eyebrow']}</div>
    <h1>{data['h1']}</h1>
    <p class="lede">{data['intro']}</p>
    <div class="hero-actions" style="margin-top:26px;">
      <a href="#quote" class="btn btn-primary">Get Your Free Quote &rarr;</a>
      <a href="tel:{PHONE_TEL}" class="btn btn-outline">{ICON_PHONE} Call {PHONE_DISPLAY}</a>
    </div>
    <div class="callout" style="margin-top:28px;max-width:680px;background:rgba(255,255,255,.08);border-left-color:var(--gold);"><p style="color:#e7ebf3;">{data['geo_answer']}</p></div>
  </div>
</section>"""

    benefits = f"""
<section>
  <div class="container split">
    <div>
      <div class="eyebrow">{data['benefits_eyebrow']}</div>
      <h2>{data['benefits_heading']}</h2>
      <ul class="checklist">
        {"".join(f'<li>{ICON_CHECK} {b}</li>' for b in data['benefits'])}
      </ul>
    </div>
    {swatch_img(data['swatch'], f"{data.get('name', data.get('h1','Driveway'))} example, Bournemouth", css_class="split-media")}
  </div>
</section>"""

    faq_html, faq_schema = faq_block(data['faq'], heading=f"{data['h1']} FAQs")
    schema_blocks.append(faq_schema)

    related_html = f"""
<section style="background:var(--paper);">
  <div class="container">
    <div class="eyebrow">Explore</div>
    <h2>Related Pages</h2>
    <div class="related-grid">
      {"".join(f'<a class="related-card" href="{m[1]}">{m[0]} Driveways {ICON_ARROW}</a>' for m in MATERIAL_DETAILS[:3])}
    </div>
  </div>
</section>"""

    final_cta = cta_band(data['cta_heading'], data['cta_sub'])
    body = page_hero + trust_bar() + benefits + faq_html + related_html + quote_section() + final_cta
    return page_wrap(
        data['href'], body, title=data['meta_title'], description=data['meta_description'],
        canonical_path=data['href'], schema_blocks=schema_blocks
    )

SERVICE_PAGE_DATA = {
    "repairs": {
        "href": "driveway-repairs-resurfacing-bournemouth.html", "swatch": "swatch-tarmac",
        "eyebrow": "Driveway Repairs", "h1": "Driveway Repairs &amp; Resurfacing in Bournemouth",
        "meta_title": "Driveway Repairs & Resurfacing Bournemouth",
        "meta_description": "Cracked, sunken or pothole-damaged driveway? Fast, affordable driveway repair and resurfacing across Bournemouth. Free quote.",
        "intro": "Cracked, sunken or pothole-damaged driveway? Before you pay for a full replacement, ask us whether a repair or resurface could save you money.",
        "geo_answer": "<strong>Quick answer:</strong> driveway repairs and resurfacing typically cost 30&ndash;50% less than a full replacement, and most jobs are completed within a single day &mdash; we'll always tell you honestly if a repair is a viable option before recommending replacement.",
        "benefits_eyebrow": "Why Repair First",
        "benefits_heading": "Often Cheaper Than a Full Replacement",
        "benefits": [
            "Pothole and crack repair for tarmac and block paving",
            "Full resurfacing when the base is sound but the top layer is worn",
            "Individual block replacement for block paving",
            "Edging and drainage repair to stop water pooling",
            "Honest advice &mdash; we&rsquo;ll tell you if replacement is genuinely the better option",
        ],
        "faq": [
            ("How do I know if I need a repair or a full replacement?", "If the sub-base is stable and damage is limited to the surface (cracks, potholes, worn patches), a repair or resurface is usually possible. If more than 30&ndash;40% of the area is affected or the base has failed, replacement is often better value long-term."),
            ("How much does driveway resurfacing cost?", "Resurfacing is typically 30&ndash;50% cheaper than a full replacement, since the excavation and sub-base work is avoided. Exact pricing depends on the size and condition of your driveway &mdash; request a free quote for a fixed price."),
            ("How long does a repair take?", "Most repairs and resurfacing jobs are completed in a single day."),
            ("Can you repair a driveway before selling my house?", "Yes &mdash; a quick, affordable repair or resurface can noticeably improve kerb appeal ahead of a sale, often for a fraction of the cost of a full replacement."),
            ("Do you repair block paving as well as tarmac?", "Yes &mdash; we repair and resurface tarmac, block paving and can advise on resin bound and gravel driveways showing signs of wear."),
        ],
        "cta_heading": "Get a Free Repair or Resurfacing Quote",
        "cta_sub": "We&rsquo;ll give you honest advice on whether to repair or replace &mdash; no pressure either way.",
    },
    "kerb": {
        "href": "dropped-kerb-bournemouth.html", "swatch": "swatch-block",
        "eyebrow": "Dropped Kerbs", "h1": "Dropped Kerb Installation in Bournemouth",
        "meta_title": "Dropped Kerb Installation Bournemouth | Costs & Permits",
        "meta_description": "Need a dropped kerb in Bournemouth? We handle council permits and installation. Find out costs and how the process works.",
        "intro": "Planning a new driveway that crosses the pavement? You&rsquo;ll need a dropped kerb &mdash; we handle the BCP Council permission process and installation from start to finish.",
        "geo_answer": "<strong>Quick answer:</strong> yes, a dropped kerb requires separate permission from BCP Council even if your driveway itself doesn't need planning permission &mdash; we handle the application and installation together as part of your quote.",
        "benefits_eyebrow": "How We Help",
        "benefits_heading": "We Handle the Council Process For You",
        "benefits": [
            "Advice on whether your project needs a dropped kerb",
            "Guidance through the BCP Council application &amp; permission process",
            "Professional kerb lowering and footway reinstatement",
            "Coordinated with your driveway installation for a single, tidy job",
            "Fully insured, council-standard workmanship",
        ],
        "faq": [
            ("Do I need permission for a dropped kerb?", "Yes &mdash; lowering a kerb to cross a public footway requires permission from <strong>BCP Council</strong>, even if the driveway itself doesn&rsquo;t need planning permission."),
            ("How much does a dropped kerb cost?", "Costs vary based on kerb length, footway width and any utilities beneath the pavement. We&rsquo;ll give you a clear, fixed figure covering both the council fee and installation as part of your free quote."),
            ("How long does the council approval take?", "Timescales vary by council workload &mdash; we&rsquo;ll give you a realistic estimate when we submit your application and keep you updated throughout."),
            ("Can I install a dropped kerb myself?", "No &mdash; dropped kerb work on a public footway must be carried out by an approved contractor to council standards. We handle the full process for you."),
            ("Does a dropped kerb application ever get refused?", "Occasionally, usually due to visibility, nearby trees, utilities or on-street parking restrictions &mdash; we'll flag any likely issues before you apply."),
        ],
        "cta_heading": "Get Help With Your Dropped Kerb",
        "cta_sub": "From council permission to installation &mdash; one team, one quote.",
    },
}

# =============================================================== CONTACT PAGE ===

def build_contact_page():
    schema_blocks = [LOCAL_BUSINESS_SCHEMA]
    crumbs_html, crumbs_schema = breadcrumbs([("Home", "index.html"), ("Contact", None)])
    schema_blocks.append(crumbs_schema)

    page_hero = f"""
<section class="page-hero">
  <div class="container">
    {crumbs_html.replace('class="breadcrumbs container"','class="breadcrumbs" style="padding-top:0;color:#9aa6bb;"')}
    <div class="eyebrow" style="color:var(--gold);">Get In Touch</div>
    <h1>Contact Bournemouth Driveway Pros</h1>
    <p class="lede">Questions about your driveway project, or ready for a free quote? Call, email or fill in the form below &mdash; we usually reply within 24 hours.</p>
    <div class="callout" style="margin-top:28px;max-width:680px;background:rgba(255,255,255,.08);border-left-color:var(--gold);"><p style="color:#e7ebf3;"><strong>Quick answer:</strong> the fastest way to reach us is by phone on {PHONE_DISPLAY} (Mon&ndash;Sat, 8am&ndash;6pm) &mdash; or fill in the free quote form below for a reply within 24 hours.</p></div>
  </div>
</section>"""

    details = f"""
<section>
  <div class="container split">
    <div>
      <div class="eyebrow">Ways to Reach Us</div>
      <h2>Talk to a Local Driveway Specialist</h2>
      <ul class="checklist">
        <li>{ICON_PHONE} <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a> &mdash; Mon&ndash;Sat, 8am&ndash;6pm</li>
        <li>{ICON_MAIL} <a href="mailto:{EMAIL}">{EMAIL}</a></li>
        <li>{ICON_PIN} {ADDRESS_LINE}</li>
        <li>{ICON_CLOCK} Most quote requests answered within 24 hours</li>
      </ul>
      <p class="lede" style="margin-top:20px;">Covering Bournemouth, Poole, Christchurch, Ferndown, Wimborne, New Milton and the surrounding Dorset coast. Got a quick question first? See our <a href="faq.html">FAQs</a>.</p>
    </div>
    {quote_form()}
  </div>
</section>"""

    final_cta = cta_band("Prefer to Talk It Through?", "Give us a call &mdash; no pressure, just honest advice on the right driveway for your budget.")

    body = page_hero + trust_bar() + details + final_cta
    return page_wrap(
        "contact.html", body,
        title="Contact Us | Bournemouth Driveway Pros",
        description="Get in touch with Bournemouth Driveway Pros for a free driveway quote. Call, email or use our contact form — we reply within 24 hours.",
        canonical_path="contact.html", schema_blocks=schema_blocks
    )

# ================================================================== BLOG ===

def blog_post_href(slug):
    return f"{slug}.html"

def blog_publish_date(index):
    """index: 0-based position in BLOG_POSTS."""
    return BLOG_START_DATE + datetime.timedelta(days=index)

def _today():
    """Real 'today', unless overridden for testing via BLOG_PUBLISH_AS_OF=YYYY-MM-DD."""
    override = os.environ.get("BLOG_PUBLISH_AS_OF")
    if override:
        return datetime.date.fromisoformat(override)
    return datetime.date.today()

def is_published(index):
    """A post goes live automatically once its scheduled publish date has arrived.
    Re-running generate_site.py (e.g. daily, via GitHub Actions) naturally drip-feeds
    the 30-post queue one article per day with no extra state file needed."""
    return blog_publish_date(index) <= _today()

def published_posts():
    """[(index, post), ...] for every post whose publish date has arrived, in order."""
    return [(i, p) for i, p in enumerate(BLOG_POSTS) if is_published(i)]

def build_blog_post(index):
    """Builds one blog article page. `index` is its position in BLOG_POSTS
    (also used to derive its publish date for the daily-cadence plan)."""
    post = BLOG_POSTS[index]
    pub_date = blog_publish_date(index)
    pub_date_iso = pub_date.isoformat()
    pub_date_human = pub_date.strftime("%d %B %Y")

    schema_blocks = [LOCAL_BUSINESS_SCHEMA]
    crumbs_html, crumbs_schema = breadcrumbs([("Home", "index.html"), ("Driveway Guides", "blog.html"), (post["title"], None)])
    schema_blocks.append(crumbs_schema)

    article_schema = {
        "@context": "https://schema.org",
        "@type": "BlogPosting",
        "headline": post["title"],
        "description": post["meta_description"],
        "datePublished": pub_date_iso,
        "dateModified": pub_date_iso,
        "author": {"@type": "Organization", "name": SITE_NAME},
        "publisher": {"@type": "Organization", "name": SITE_NAME},
        "mainEntityOfPage": {"@type": "WebPage", "@id": f"{DOMAIN}/{blog_post_href(post['slug'])}"},
    }
    schema_blocks.append(article_schema)

    page_hero = f"""
<section class="page-hero">
  <div class="container">
    {crumbs_html.replace('class="breadcrumbs container"','class="breadcrumbs" style="padding-top:0;color:#9aa6bb;"')}
    <div class="eyebrow" style="color:var(--gold);">{post['cluster']}</div>
    <h1>{post['title']}</h1>
    <p class="lede" style="color:#c9d2e0;">Published {pub_date_human} &middot; Bournemouth Driveway Pros Guides</p>
    <div class="callout" style="margin-top:20px;max-width:720px;background:rgba(255,255,255,.08);border-left-color:var(--gold);"><p style="color:#e7ebf3;"><strong>Quick answer:</strong> {post['geo_answer']}</p></div>
  </div>
</section>"""

    sections_html = "".join(f"<h2>{h}</h2>{body}" for h, body in post["sections"])
    article_body = f"""
<section>
  <div class="container article-body" style="max-width:760px;">
    {sections_html}
  </div>
</section>"""

    faq_html, faq_schema = faq_block(post["faq"], heading="Related Questions")
    schema_blocks.append(faq_schema)

    published_slugs = {p["slug"] for _, p in published_posts()}
    related_posts = [p for p in BLOG_POSTS if p["slug"] in post["related"] and p["slug"] in published_slugs]
    related_html = ""
    if related_posts:
        cards = "".join(
            f'<a class="related-card" href="{blog_post_href(p["slug"])}">{p["title"]} {ICON_ARROW}</a>'
            for p in related_posts
        )
        related_html = f"""
<section style="background:var(--paper);">
  <div class="container" style="max-width:760px;">
    <div class="eyebrow">Keep Reading</div>
    <h2>Related Guides</h2>
    <div class="related-posts-grid">{cards}</div>
  </div>
</section>"""

    final_cta = cta_band("Ready to Get a Free Driveway Quote?", "Fixed pricing, fully insured local installers and a written guarantee &mdash; talk to us today.")

    body = page_hero + article_body + faq_html + related_html + quote_section() + final_cta
    return page_wrap(
        "blog.html", body,
        title=post["meta_title"], description=post["meta_description"],
        canonical_path=blog_post_href(post["slug"]), schema_blocks=schema_blocks
    )

def build_blog_index():
    schema_blocks = [LOCAL_BUSINESS_SCHEMA]
    crumbs_html, crumbs_schema = breadcrumbs([("Home", "index.html"), ("Driveway Guides", None)])
    schema_blocks.append(crumbs_schema)

    page_hero = f"""
<section class="page-hero">
  <div class="container">
    {crumbs_html.replace('class="breadcrumbs container"','class="breadcrumbs" style="padding-top:0;color:#9aa6bb;"')}
    <div class="eyebrow" style="color:var(--gold);">Driveway Guides</div>
    <h1>Driveway Advice &amp; Guides</h1>
    <p class="lede">Straight answers on driveway cost, materials, planning permission and maintenance &mdash; written for Bournemouth, Poole and Dorset homeowners.</p>
  </div>
</section>"""

    live = published_posts()  # [(index, post), ...] — only posts whose publish date has arrived

    clusters = []
    for _, post in live:
        if post["cluster"] not in clusters:
            clusters.append(post["cluster"])

    if not live:
        grouped_html = """
<section class="section-tight">
  <div class="container">
    <p class="lede">New guides are on the way &mdash; check back soon, or explore our driveway type and cost guide pages in the meantime.</p>
  </div>
</section>"""
    else:
        grouped_html = ""
        for cluster in clusters:
            cards = ""
            for i, post in live:
                if post["cluster"] != cluster:
                    continue
                pub_date_human = blog_publish_date(i).strftime("%d %b %Y")
                cards += f"""
      <a class="blog-card" href="{blog_post_href(post['slug'])}">
        <span class="bc-cluster">{post['cluster']}</span>
        <span class="bc-date">{pub_date_human}</span>
        <h3>{post['title']}</h3>
        <p>{post['excerpt']}</p>
        <span class="bc-link">Read the guide {ICON_ARROW}</span>
      </a>"""
            grouped_html += f"""
<section class="{'section-tight' if cluster != clusters[0] else ''}">
  <div class="container">
    <h2 class="blog-cluster-heading">{cluster}</h2>
    <div class="blog-grid">{cards}</div>
  </div>
</section>"""

    final_cta = cta_band("Have a Question These Guides Didn't Cover?", "Give us a call or request a free quote &mdash; we&rsquo;re happy to talk through your specific project.")

    body = page_hero + trust_bar() + grouped_html + quote_section() + final_cta
    return page_wrap(
        "blog.html", body,
        title="Driveway Guides &amp; Advice | Bournemouth Driveway Pros",
        description="Straight answers on driveway cost, materials, planning permission and maintenance for Bournemouth, Poole and Dorset homeowners.",
        canonical_path="blog.html", schema_blocks=schema_blocks
    )

# =============================================================== WRITE ALL ===

def write(path, content):
    full = os.path.join(OUT, path)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)
    print("wrote", path, len(content), "bytes")

def main():
    write("index.html", build_homepage())
    write("tarmac-driveways-bournemouth.html", build_material_page("tarmac"))
    write("block-paving-bournemouth.html", build_material_page("block"))
    write("resin-bound-driveways-bournemouth.html", build_material_page("resin"))
    write("gravel-driveways-bournemouth.html", build_material_page("gravel"))
    write("driveway-cost-guide-bournemouth.html", build_cost_guide())
    write("faq.html", build_faq_page())
    write("driveway-repairs-resurfacing-bournemouth.html", build_service_page("repairs"))
    write("dropped-kerb-bournemouth.html", build_service_page("kerb"))
    write("driveways-poole.html", build_location_page("poole"))
    write("driveways-christchurch.html", build_location_page("christchurch"))
    write("driveways-ferndown.html", build_location_page("ferndown"))
    write("driveways-wimborne.html", build_location_page("wimborne"))
    write("driveways-new-milton.html", build_location_page("new-milton"))
    write("contact.html", build_contact_page())

    write("blog.html", build_blog_index())
    live_posts = published_posts()
    for i, post in live_posts:
        write(blog_post_href(post["slug"]), build_blog_post(i))
    print(f"blog: {len(live_posts)}/{len(BLOG_POSTS)} posts published as of {_today().isoformat()}")

    pages = ["index.html","tarmac-driveways-bournemouth.html","block-paving-bournemouth.html",
             "resin-bound-driveways-bournemouth.html","gravel-driveways-bournemouth.html",
             "driveway-cost-guide-bournemouth.html","faq.html",
             "driveway-repairs-resurfacing-bournemouth.html","dropped-kerb-bournemouth.html",
             "driveways-poole.html","driveways-christchurch.html","driveways-ferndown.html",
             "driveways-wimborne.html","driveways-new-milton.html","contact.html","blog.html"]
    pages += [blog_post_href(post["slug"]) for _, post in live_posts]
    urlset = "\n".join(f"  <url><loc>{DOMAIN}/{p}</loc><changefreq>monthly</changefreq></url>" for p in pages)
    sitemap = f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urlset}\n</urlset>\n'
    write("sitemap.xml", sitemap)

    robots = f"User-agent: *\nAllow: /\n\nSitemap: {DOMAIN}/sitemap.xml\n"
    write("robots.txt", robots)

if __name__ == "__main__":
    main()

