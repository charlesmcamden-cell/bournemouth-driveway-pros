# Bournemouth Driveway Pros — Site

A 14-page static lead-generation site for a driveways "rank & rent" build targeting Bournemouth, Poole, Christchurch, Ferndown, Wimborne and New Milton. Pure HTML/CSS/JS, no build step, no framework — open `index.html` in a browser or deploy as-is.

## Pages

- `index.html` — homepage / pillar page
- `tarmac-driveways-bournemouth.html`, `block-paving-bournemouth.html`, `resin-bound-driveways-bournemouth.html`, `gravel-driveways-bournemouth.html` — material pages
- `driveway-cost-guide-bournemouth.html` — pricing/comparison (link-magnet page)
- `faq.html` — FAQPage schema
- `driveway-repairs-resurfacing-bournemouth.html`, `dropped-kerb-bournemouth.html` — service pages
- `driveways-poole.html`, `driveways-christchurch.html`, `driveways-ferndown.html`, `driveways-wimborne.html`, `driveways-new-milton.html` — location pages
- `styles.css`, `main.js` — shared design system + interactions (mobile nav, FAQ accordion, quote form)
- `sitemap.xml`, `robots.txt` — SEO plumbing
- `generate_site.py` — the generator. All copy, meta tags, schema and pricing live in this one file as Python data structures. **Edit this file and rerun `python3 generate_site.py`, don't hand-edit the HTML** — every page shares the same header/footer/CTA components, so hand edits will drift and get overwritten on the next regen.

## Before this goes live — placeholders to replace

Everything below is fake/sample data, clearly marked in `generate_site.py`:

- **Business name, phone, email, address** (`SITE_NAME`, `PHONE_DISPLAY`, `PHONE_TEL`, `EMAIL`, `ADDRESS_LINE` — top of the file)
- **Domain** (`DOMAIN` — used in canonical URLs, Open Graph tags and sitemap.xml)
- **Testimonials** on the homepage — three sample quotes, flagged in the HTML with a visible disclosure note. Replace with real, verifiable reviews (Google/Checkatrade) before launch — fabricated testimonials are a genuine legal/trust risk, not just a nice-to-have fix.
- **Pricing** in the cost guide and material pages — realistic 2026 UK ranges, but not sourced from a live local quote. Verify against actual job costs before publishing as fact.

## Activating the quote form (lead capture)

The form currently points at a placeholder Formspree endpoint and will show "Form isn't connected yet" if submitted as-is — it deliberately does **not** fake a success message for an unconfigured form.

1. Create a free account at [formspree.io](https://formspree.io) (free tier covers 50 submissions/month).
2. Create a new form, copy its endpoint (`https://formspree.io/f/xxxxxxxx`).
3. In `generate_site.py`, replace `FORM_ACTION`'s placeholder value with your real endpoint.
4. Rerun `python3 generate_site.py`.

That's it — the form already does a proper AJAX POST with an inline success/error message (see `main.js`), no further code changes needed. Any Formspree-compatible or generic form backend (Netlify Forms, Basin, your own endpoint) works the same way as long as it accepts a standard `multipart/form-data` POST.

## Photography

The material "photos" are currently CSS-only textures (no images to license, nothing fake) rather than real photography — image generation and stock-photo downloads were both blocked in the environment this was built in (trial-plan restrictions on the AI image tool; network/security restrictions on pulling stock photos programmatically). To add real photos:

1. Source images (AI-generated or licensed stock — Unsplash/Pexels license permits commercial use).
2. Save them into this folder, e.g. `images/hero.jpg`, `images/tarmac.jpg`, etc.
3. Swap the relevant `.swatch-*` `<div>` elements in `generate_site.py` for `<img>` tags, or add `background-image` rules to the swatch classes in `styles.css`.

## Deployment

Static files, so any static host works:

- **GitHub Pages**: Settings → Pages → Deploy from branch → `main` / root.
- **Netlify / Vercel**: drag-and-drop the folder or connect the repo — zero config needed. If you deploy to Netlify specifically, you can swap the form for Netlify Forms instead of Formspree (add `data-netlify="true"` to the `<form>`).

## SEO/GEO notes

- Every page: single H1, unique meta title/description, canonical tag, Open Graph tags.
- Structured data: `HomeAndConstructionBusiness` (site-wide), `BreadcrumbList` and `FAQPage` (per relevant page) — all JSON-LD, validated.
- The cost guide has an explicit "quick answer" callout near the top, written to be directly quotable by AI/GEO search summaries.
- `sitemap.xml` and `robots.txt` are wired up but reference the placeholder `DOMAIN` — update once the real domain is live.
- Content strategy / keyword research this site was built from lives in the accompanying `content_brief.xlsx`.
