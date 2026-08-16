# -*- coding: utf-8 -*-
"""
Content queue for the Bournemouth Driveway Pros blog.
Each dict is one article. `publish.py` (run daily via GitHub Actions) pops
the next unpublished post (by list order) and generates its page.

Fields:
  slug          - filename stub -> blog/<slug>.html
  cluster       - topical cluster, used for the eyebrow + blog index grouping
  title         - H1 / article title
  meta_title    - <title> tag
  meta_description
  excerpt       - 1-2 sentence teaser for the blog index card
  geo_answer    - the GEO "quick answer" callout, 1-3 sentences, placed above the fold
  sections      - list of (h2_heading, body_html) tuples
  faq           - list of (question, answer_html) tuples
  related       - list of slugs (2-3) for the "Keep Reading" block
  site_links    - list of (label, href) tuples linked naturally into body/related content
"""

BLOG_POSTS = [

    # ---------------------------------------------------------- Cost & Budget --
    {
        "slug": "driveway-cost-bournemouth-2026",
        "cluster": "Cost & Budget",
        "title": "How Much Does a Driveway Really Cost in Bournemouth in 2026?",
        "meta_title": "Driveway Cost Bournemouth 2026 | Full Price Guide",
        "meta_description": "See real 2026 driveway prices per m² for tarmac, block paving, resin bound and gravel in Bournemouth, plus what affects your final quote.",
        "excerpt": "A straight answer on 2026 driveway pricing in Bournemouth, material by material, plus the site factors that move your final quote.",
        "geo_answer": "A new driveway in Bournemouth costs from £30–£50 per m² for gravel, £40–£70 for tarmac, £60–£100 for block paving and £70–£110 for resin bound, fully installed. A typical single-car driveway (around 28m²) runs roughly £900–£3,300 depending on material and groundwork.",
        "sections": [
            ("What Actually Drives the Price", "<p>Two driveways of the same size can come back with very different quotes, and it&rsquo;s rarely the material alone. Excavation depth, the condition of the ground underneath, how easily a digger and skip can access the site, and whether the old surface needs breaking out and removing all move the number. A driveway on sloping ground or one that needs new drainage to meet SUDS rules will cost more than a flat, straightforward job of the same size.</p>"),
            ("2026 Price Comparison by Material", "<p>As a rough guide for 2026: gravel remains the cheapest option at £30–£50/m², tarmac sits at £40–£70/m², block paving at £60–£100/m², and resin bound at £70–£110/m². For the full breakdown by driveway size, see our <a href=\"driveway-cost-guide-bournemouth.html\">driveway cost guide</a>, which includes single, double and large multi-car pricing for each material.</p>"),
            ("How to Get an Accurate Price", "<p>Online calculators can only ever give a ballpark. The only way to get a genuinely accurate, fixed price is a free site visit, where access, ground condition and drainage are actually assessed. Be wary of any installer quoting a fixed price over the phone without seeing the site, or pushing a same-day discount &mdash; both are classic pressure tactics rather than genuine savings.</p>"),
        ],
        "faq": [
            ("Is VAT included in driveway quotes?", "Reputable installers should always confirm whether a quote is VAT inclusive. Always ask for this in writing before you agree to any work."),
            ("Do I need to pay a deposit?", "Be cautious of large upfront deposits. A fair, transparent installer typically asks for little to nothing before starting the physical work."),
            ("How can I keep costs down without sacrificing quality?", "Gravel and tarmac are the most budget-friendly durable options. Keeping the design simple, avoiding unnecessary excavation depth, and getting a fixed quote up front also help control costs."),
            ("Do prices vary much across the Bournemouth area?", "Pricing is broadly consistent across Bournemouth, Poole and the wider BCP area &mdash; access and ground conditions affect price more than location itself."),
        ],
        "related": ["driveway-cost-per-square-metre-2026", "hidden-driveway-costs"],
    },
    {
        "slug": "resin-bound-vs-block-paving-cost",
        "cluster": "Cost & Budget",
        "title": "Resin Bound vs Block Paving: Which Costs More Long-Term?",
        "meta_title": "Resin Bound vs Block Paving Cost Compared",
        "meta_description": "Resin bound costs more upfront but less over 20 years than block paving. Full cost, maintenance and lifespan comparison.",
        "excerpt": "Resin bound wins on upfront price comparisons less often than you&rsquo;d think once maintenance and lifespan are factored in. Here&rsquo;s the real long-term cost.",
        "geo_answer": "Block paving is cheaper to install (£60–£100/m² vs resin bound&rsquo;s £70–£110/m²), but resin bound typically costs less per year over a 20-year lifespan once you account for block paving&rsquo;s more frequent resanding, weeding and resealing.",
        "sections": [
            ("Upfront Cost", "<p>Block paving is the less expensive install of the two, typically £60–£100 per m² against resin bound&rsquo;s £70–£110 per m². For a standard 28m² driveway, that&rsquo;s a difference of roughly £300–£600 at installation.</p>"),
            ("Maintenance Cost Over Time", "<p>This is where the gap narrows. Block paving benefits from jointing sand top-ups, occasional weed treatment and a resand or reseal every 2&ndash;3 years to keep it looking sharp. Resin bound is naturally weed and moss resistant and typically only needs a re-coat every 8&ndash;12 years, with light sweeping and an occasional low-pressure wash in between.</p>"),
            ("Lifespan and Resale", "<p>Block paving lasts 25&ndash;40+ years and resin bound 20&ndash;25 years, but resin bound&rsquo;s lower upkeep and premium look mean many homeowners find the extra upfront cost pays for itself in reduced maintenance time and, per <a href=\"does-a-new-driveway-add-value.html\">our guide to driveway resale value</a>, comparable kerb-appeal returns.</p>"),
        ],
        "faq": [
            ("Which lasts longer, resin bound or block paving?", "Block paving typically lasts longer (25–40+ years) than resin bound (20–25 years before a re-coat), but individual block paving blocks are also easier to replace if damaged."),
            ("Does resin bound really need less maintenance?", "Yes &mdash; its smooth, sealed surface resists weed and moss growth far better than the jointed gaps in block paving."),
            ("Which adds more value to a home?", "Both improve kerb appeal; see our dedicated <a href=\"does-a-new-driveway-add-value.html\">resale value guide</a> for typical uplift figures for each material."),
        ],
        "related": ["is-resin-bound-driveway-worth-it", "driveway-cost-per-square-metre-2026"],
    },
    {
        "slug": "hidden-driveway-costs",
        "cluster": "Cost & Budget",
        "title": "Hidden Driveway Costs Nobody Tells You About",
        "meta_title": "Hidden Driveway Costs UK: What Quotes Miss",
        "meta_description": "Excavation, drainage, kerbs and skip hire can add thousands to a driveway quote. Here's what to check before you sign.",
        "excerpt": "The headline price-per-m² figure rarely tells the whole story. Here are the costs that catch homeowners out.",
        "geo_answer": "The most commonly missed driveway costs are excavation and old-surface removal (£300–£800+), skip hire, dropped kerb applications (typically £400–£1,500 depending on council and works), drainage upgrades for SUDS compliance, and access charges for narrow or restricted sites.",
        "sections": [
            ("Excavation and Removal", "<p>If your existing driveway needs breaking out and taking away before the new surface goes in, that&rsquo;s additional cost most bare per-m² prices don&rsquo;t include. Ask any installer explicitly whether removal of the old surface, and disposal, is included in the headline figure.</p>"),
            ("Dropped Kerbs and Drainage", "<p>If you need a new or altered dropped kerb, that&rsquo;s a separate council application and cost on top of the driveway itself &mdash; see our <a href=\"dropped-kerb-rules-bournemouth.html\">dropped kerb guide</a> for typical figures. Likewise, non-permeable driveways over 5m² may need extra drainage work to meet SUDS rules, covered in our <a href=\"permeable-vs-non-permeable-driveways.html\">permeable driveways guide</a>.</p>"),
            ("Access and Site Conditions", "<p>Restricted access for machinery, a long carry distance from the road, or ground that needs extra excavation depth because of poor drainage can all add cost that only becomes clear at a proper site visit &mdash; another reason to avoid quotes given without one.</p>"),
        ],
        "faq": [
            ("Should removal of my old driveway be included in the quote?", "Always ask explicitly &mdash; some quotes include it, others price it separately. Get this confirmed in writing before work starts."),
            ("Do I need to budget separately for a dropped kerb?", "Yes, in most cases. It&rsquo;s a separate council application and cost &mdash; see our full breakdown in the dropped kerb guide."),
            ("How can I avoid hidden costs appearing later?", "Insist on a fixed, written quote from a free site visit rather than a phone or online estimate, and ask directly what is and isn&rsquo;t included."),
        ],
        "related": ["driveway-cost-bournemouth-2026", "dropped-kerb-rules-bournemouth"],
    },
    {
        "slug": "cheapest-driveway-options-bournemouth",
        "cluster": "Cost & Budget",
        "title": "Cheapest Driveway Options in Bournemouth Without Sacrificing Quality",
        "meta_title": "Cheapest Driveway Options in Bournemouth 2026",
        "meta_description": "Gravel and tarmac are the most affordable driveway materials in Bournemouth. Compare real costs and what you give up for the saving.",
        "excerpt": "Budget doesn&rsquo;t have to mean a poor result. Here&rsquo;s where the real savings are, and where cutting corners actually costs more later.",
        "geo_answer": "Gravel (£30–£50/m²) and tarmac (£40–£70/m²) are the most affordable durable driveway materials in Bournemouth. Both can be installed in a day or two and, with a properly compacted sub-base, last 15–30 years.",
        "sections": [
            ("Gravel: The Lowest Upfront Cost", "<p>Gravel is genuinely the cheapest option that still holds up well &mdash; it&rsquo;s naturally permeable, fast to lay, and suits period and rural properties particularly well. See our full <a href=\"gravel-driveways-bournemouth.html\">gravel driveways page</a> for pricing by driveway size.</p>"),
            ("Tarmac: Budget-Friendly and Hard-Wearing", "<p>Where gravel isn&rsquo;t the right look for a property, tarmac is usually the next most affordable choice and offers a smoother, more durable surface for daily use &mdash; typically lasting 20&ndash;30 years with basic upkeep.</p>"),
            ("Where Not to Cut Corners", "<p>The genuine false economy is skipping a proper sub-base to save money &mdash; a driveway laid on a poorly compacted or too-shallow base will fail early regardless of material, meaning you pay twice. Always ask what depth of sub-base is included, whatever material you choose.</p>"),
        ],
        "faq": [
            ("Is gravel or tarmac cheaper?", "Gravel is usually the cheaper of the two, though both are among the most affordable driveway surfaces available."),
            ("Will a budget driveway still look good?", "Yes &mdash; both gravel and tarmac can look smart and well-kept when properly edged, compacted and maintained."),
            ("What's the biggest false economy on a budget driveway?", "Skipping a proper compacted sub-base to save money &mdash; it leads to early failure and higher long-term cost."),
        ],
        "related": ["driveway-cost-bournemouth-2026", "block-paving-vs-gravel-driveway"],
    },
    {
        "slug": "driveway-cost-per-square-metre-2026",
        "cluster": "Cost & Budget",
        "title": "Driveway Cost Per Square Metre 2026: Every Material Compared",
        "meta_title": "Driveway Cost Per m² 2026 | All Materials Compared",
        "meta_description": "Tarmac, block paving, resin bound and gravel driveway costs per square metre in 2026, compared side by side.",
        "excerpt": "A quick-reference price-per-m² comparison across all four driveway materials, updated for 2026.",
        "geo_answer": "2026 driveway costs per m²: gravel £30–£50, tarmac £40–£70, block paving £60–£100, resin bound £70–£110. Multiply by your driveway&rsquo;s area for a rough installed cost, though groundwork and access can move the final figure.",
        "sections": [
            ("The Four Materials, Side by Side", "<p>Gravel: £30&ndash;£50/m². Tarmac: £40&ndash;£70/m². Block paving: £60&ndash;£100/m². Resin bound: £70&ndash;£110/m². These figures assume standard groundwork on a reasonably accessible site &mdash; see the individual <a href=\"tarmac-driveways-bournemouth.html\">tarmac</a>, <a href=\"block-paving-bournemouth.html\">block paving</a>, <a href=\"resin-bound-driveways-bournemouth.html\">resin bound</a> and <a href=\"gravel-driveways-bournemouth.html\">gravel</a> pages for size-based pricing tables.</p>"),
            ("Working Out Your Driveway's Area", "<p>Measure the longest length and widest width in metres and multiply them for a rough area &mdash; irregular shapes are best measured in sections. Most single-car driveways are around 25&ndash;30m², doubles 45&ndash;60m².</p>"),
            ("Why Per-m² Prices Are Only a Starting Point", "<p>Per-m² pricing is useful for comparing materials, but excavation, drainage and access all affect the final number &mdash; which is why we always recommend a free site visit over a phone estimate.</p>"),
        ],
        "faq": [
            ("Which material is cheapest per m²?", "Gravel, at roughly £30–£50 per m² installed."),
            ("Which material is most expensive per m²?", "Resin bound, typically £70–£110 per m², reflecting its premium, low-maintenance finish."),
            ("Do these prices include VAT?", "Always confirm VAT treatment with your installer in writing before agreeing to a quote."),
        ],
        "related": ["driveway-cost-bournemouth-2026", "resin-bound-vs-block-paving-cost"],
    },

    # ------------------------------------------------------ Material Comparisons --
    {
        "slug": "tarmac-vs-resin-bound-driveway",
        "cluster": "Material Comparisons",
        "title": "Tarmac vs Resin Bound Driveways: Full Comparison",
        "meta_title": "Tarmac vs Resin Bound Driveway: Which Is Better?",
        "meta_description": "Tarmac is cheaper and faster to install; resin bound looks better and drains naturally. Full head-to-head comparison.",
        "excerpt": "Two of the most requested driveway surfaces in Bournemouth, compared on cost, looks, drainage and lifespan.",
        "geo_answer": "Tarmac (£40–£70/m², 20–30 year lifespan) is the cheaper, faster-to-install choice for a smooth, hard-wearing surface. Resin bound (£70–£110/m², 20–25 years) costs more but gives a premium, permeable, weed-resistant finish that meets SUDS drainage rules automatically.",
        "sections": [
            ("Cost and Installation Speed", "<p>Tarmac is roughly 30&ndash;50% cheaper than resin bound and is usually laid in 1&ndash;2 days. Resin bound takes a similar time to lay but needs 24&ndash;48 hours to cure before full vehicle use.</p>"),
            ("Looks and Finish", "<p>Tarmac gives a uniform black (or tinted) surface. Resin bound offers dozens of natural stone blends and a smooth, seamless, UV-stable finish that many homeowners feel gives a more premium look.</p>"),
            ("Drainage and Long-Term Durability", "<p>Resin bound is fully permeable as standard, meeting <a href=\"suds-permeable-paving-rules.html\">SUDS drainage rules</a> without extra work. Tarmac is not naturally permeable and can need additional drainage provision on larger, non-permeable areas. Both are durable, but tarmac has a slightly longer typical lifespan (20&ndash;30 years vs resin bound&rsquo;s 20&ndash;25).</p>"),
        ],
        "faq": [
            ("Which is cheaper, tarmac or resin bound?", "Tarmac, typically by 30–50% per m²."),
            ("Which drains better?", "Resin bound is fully permeable by design; tarmac is not, and may need additional drainage on larger areas."),
            ("Which lasts longer?", "Tarmac has a marginally longer typical lifespan (20–30 years) than resin bound (20–25 years before a re-coat)."),
        ],
        "related": ["is-resin-bound-driveway-worth-it", "resin-bound-vs-block-paving-cost"],
    },
    {
        "slug": "block-paving-vs-gravel-driveway",
        "cluster": "Material Comparisons",
        "title": "Block Paving vs Gravel Driveways: Pros, Cons and Best Uses",
        "meta_title": "Block Paving vs Gravel Driveway Compared",
        "meta_description": "Block paving suits high-traffic modern driveways; gravel suits period and rural properties. Compare cost, upkeep and durability.",
        "excerpt": "Different jobs, different homes. Here&rsquo;s how block paving and gravel actually compare once you look past the price tag.",
        "geo_answer": "Block paving (£60–£100/m²) suits high-traffic, modern driveways and offers the most design choice. Gravel (£30–£50/m²) is cheaper, drains naturally and suits period or rural properties, but needs more regular raking and top-ups.",
        "sections": [
            ("Cost and Installation", "<p>Gravel is significantly cheaper and can often be laid in a single day. Block paving costs more and typically takes 2&ndash;4 days, reflecting the extra base preparation and laying work involved.</p>"),
            ("Look and Property Fit", "<p>Block paving suits modern builds and properties where a crisp, uniform finish matters. Gravel has a softer, more natural look that tends to suit period, rural or coastal properties particularly well.</p>"),
            ("Maintenance and Durability", "<p>Block paving is extremely durable and individual blocks can be replaced if damaged. Gravel needs occasional raking and topping up in high-traffic wheel tracks but is otherwise low maintenance and naturally weed-resistant with a proper membrane underneath.</p>"),
        ],
        "faq": [
            ("Which is better for a busy family driveway?", "Block paving generally copes better with heavy, daily use and looks crisp for longer without raking."),
            ("Which drains better?", "Both can be specified as permeable; gravel is naturally permeable by default, while block paving needs a permeable system specifically chosen."),
            ("Can gravel and block paving be combined?", "Yes &mdash; some driveways use block paving borders with a gravel infill for a cost-effective, textured look."),
        ],
        "related": ["cheapest-driveway-options-bournemouth", "resin-bound-vs-resin-bonded"],
    },
    {
        "slug": "resin-bound-vs-resin-bonded",
        "cluster": "Material Comparisons",
        "title": "Resin Bound vs Resin Bonded: What's the Difference?",
        "meta_title": "Resin Bound vs Resin Bonded Driveways Explained",
        "meta_description": "Resin bound mixes stone through resin for a smooth, permeable surface; resin bonded sticks loose stone on top. Here's why it matters.",
        "excerpt": "The single most confused pair of terms in the driveway world &mdash; and the difference genuinely matters for durability and drainage.",
        "geo_answer": "Resin bound driveways mix aggregate through the resin and trowel it to a smooth, level, permeable finish. Resin bonded driveways scatter loose stone over a resin layer on top, leaving a textured surface that isn&rsquo;t permeable and can shed loose stones over time.",
        "sections": [
            ("How Each Is Made", "<p>Resin bound aggregate is hand-mixed with clear resin before laying, then trowelled to a smooth, level finish. Resin bonded involves pouring resin first and scattering stone on top, which bonds only at the base of each stone.</p>"),
            ("Finish and Feel Underfoot", "<p>Resin bound gives a smooth, seamless surface that&rsquo;s comfortable to walk and wheel on. Resin bonded has a rougher, more textured feel, and loose stones can work free over time, especially in high-traffic areas.</p>"),
            ("Drainage and Longevity", "<p>Resin bound is fully permeable, meeting SUDS drainage rules as standard. Resin bonded is not permeable and, because stones can shed, typically needs more upkeep to stay looking its best. We install resin bound &mdash; see our <a href=\"resin-bound-driveways-bournemouth.html\">resin bound driveways page</a> for full details.</p>"),
        ],
        "faq": [
            ("Which is more expensive?", "Resin bound is generally the higher-spec, more premium option and priced accordingly."),
            ("Which is more durable?", "Resin bound tends to hold up better over time since the aggregate is fully bound through the resin rather than sitting on top."),
            ("Do you install resin bonded driveways?", "We specialise in resin bound &mdash; the smoother, permeable, higher-spec option &mdash; rather than resin bonded."),
        ],
        "related": ["is-resin-bound-driveway-worth-it", "tarmac-vs-resin-bound-driveway"],
    },
    {
        "slug": "is-resin-bound-driveway-worth-it",
        "cluster": "Material Comparisons",
        "title": "Is a Resin Bound Driveway Worth the Extra Cost?",
        "meta_title": "Is a Resin Bound Driveway Worth It in 2026?",
        "meta_description": "Resin bound driveways cost more upfront but last 20-25 years and meet SUDS drainage rules. Here's the honest verdict.",
        "excerpt": "An honest look at whether resin bound&rsquo;s premium price tag is justified for most Bournemouth homeowners.",
        "geo_answer": "For most homeowners, yes: resin bound costs more upfront (£70–£110/m²) than tarmac or block paving, but its 20–25 year lifespan, near-zero weed growth, SUDS-compliant drainage and premium finish make it good value if you&rsquo;re staying in the property long-term.",
        "sections": [
            ("What You're Paying For", "<p>The extra cost over tarmac or gravel buys a smooth, seamless, natural-stone finish, full permeability without extra drainage work, and a surface that&rsquo;s naturally resistant to weeds and moss &mdash; meaning far less maintenance over its lifetime.</p>"),
            ("When It Makes the Most Sense", "<p>Resin bound is particularly worth it if you plan to stay in the property for years, want to minimise ongoing maintenance, or need a permeable surface to avoid planning permission on a larger driveway.</p>"),
            ("When a Cheaper Material Makes More Sense", "<p>If budget is the primary concern, or you&rsquo;re planning to sell soon and want the lowest-cost kerb-appeal improvement, tarmac or block paving may offer a better return &mdash; see our <a href=\"resin-bound-vs-block-paving-cost.html\">resin bound vs block paving cost comparison</a>.</p>"),
        ],
        "faq": [
            ("Does resin bound increase home value?", "It can improve kerb appeal, though block paving and resin bound tend to add broadly similar resale value &mdash; see our resale value guide for specifics."),
            ("Is resin bound low maintenance?", "Yes &mdash; a regular sweep and occasional gentle wash is normally all that&rsquo;s needed."),
            ("How long before it needs re-coating?", "Typically every 8–12 years, depending on use and exposure."),
        ],
        "related": ["tarmac-vs-resin-bound-driveway", "resin-bound-driveway-maintenance"],
    },
    {
        "slug": "best-driveway-material-coastal-weather",
        "cluster": "Material Comparisons",
        "title": "Best Driveway Material for Bournemouth's Clay Soil and Coastal Weather",
        "meta_title": "Best Driveway Material for Bournemouth Weather & Soil",
        "meta_description": "Coastal salt air and Dorset clay soil affect driveway durability. Here's which materials perform best locally.",
        "excerpt": "Bournemouth&rsquo;s coastal air and clay-heavy soil put specific demands on a driveway. Here&rsquo;s what actually holds up.",
        "geo_answer": "Resin bound and block paving tend to perform best in Bournemouth&rsquo;s coastal, clay-soil conditions &mdash; both resist salt-air weathering well and, with a properly compacted sub-base, cope with ground movement better than a thin, poorly prepared surface of any material.",
        "sections": [
            ("Why Local Conditions Matter", "<p>Coastal salt air can accelerate wear on some surfaces over time, and Bournemouth&rsquo;s clay-heavy soil can shift slightly with wet and dry seasons, putting pressure on a driveway&rsquo;s sub-base if it isn&rsquo;t properly compacted.</p>"),
            ("Materials That Hold Up Well", "<p>Resin bound&rsquo;s UV-stable, sealed surface resists salt-air discolouration, and its slight flexibility helps with minor ground movement. Block paving&rsquo;s individual units also cope well with movement since blocks can flex independently rather than cracking as a single slab might.</p>"),
            ("The Real Key: Sub-Base Preparation", "<p>Whichever material you choose, a properly excavated and compacted sub-base matters more for coastal, clay-soil driveways than the surface material itself &mdash; it&rsquo;s the single biggest factor in avoiding cracking, sinking or standing water down the line.</p>"),
        ],
        "faq": [
            ("Does salt air damage driveways?", "It can accelerate wear on some surfaces over many years, though resin bound and block paving both resist it reasonably well."),
            ("Is clay soil a problem for driveways?", "Only if the sub-base isn&rsquo;t properly prepared &mdash; a compacted MOT Type 1 sub-base largely mitigates the risk of ground movement."),
            ("Which areas of Bournemouth have the clay-heaviest soil?", "It varies by street and depth &mdash; our site surveys always check ground conditions before quoting."),
        ],
        "related": ["driveway-installation-poole-guide", "permeable-vs-non-permeable-driveways"],
    },
    {
        "slug": "permeable-vs-non-permeable-driveways",
        "cluster": "Material Comparisons",
        "title": "Permeable vs Non-Permeable Driveways: What You Need to Know",
        "meta_title": "Permeable vs Non-Permeable Driveways Explained",
        "meta_description": "Non-permeable driveways over 5m² need planning permission unless water drains to a permeable area. Here's what qualifies.",
        "excerpt": "The permeability of your driveway surface can decide whether you need planning permission at all. Here&rsquo;s what counts.",
        "geo_answer": "A non-permeable driveway larger than 5m² needs planning permission unless rainwater drains to a permeable area like a lawn or border. Permeable surfaces &mdash; gravel, permeable block paving, or resin bound with a SUDS-compliant base &mdash; are exempt from this rule regardless of size.",
        "sections": [
            ("What Counts as Permeable", "<p>Gravel is naturally permeable. Permeable block paving uses gapped joints and a porous sub-base to let water through. Resin bound, laid on the correct porous base, is also fully permeable. Standard tarmac and standard block paving are not.</p>"),
            ("Why It Matters for Planning Permission", "<p>Under permitted development rules, a non-permeable driveway over 5m² needs planning permission unless the water is directed to a permeable area of your own garden rather than the street. See our full <a href=\"driveway-planning-permission-bournemouth.html\">planning permission guide</a> for the details.</p>"),
            ("Choosing the Right Option", "<p>If avoiding planning permission matters to you, a permeable material is the simplest route &mdash; and has the added benefit of reducing surface flooding risk on your property and the wider street.</p>"),
        ],
        "faq": [
            ("Is tarmac ever permeable?", "Specialist porous tarmac systems exist but are less common; standard tarmac is not permeable."),
            ("Does a small non-permeable driveway need permission?", "Generally no, if it's under 5m², though it's worth confirming with your local council for your specific property."),
            ("Can I convert a non-permeable driveway to permeable later?", "In many cases, yes, though it usually involves excavating and relaying rather than adapting the existing surface."),
        ],
        "related": ["driveway-planning-permission-bournemouth", "suds-permeable-paving-rules"],
    },

    # -------------------------------------------------------------- Planning & Legal --
    {
        "slug": "driveway-planning-permission-bournemouth",
        "cluster": "Planning & Legal",
        "title": "Do You Need Planning Permission for a Driveway in Bournemouth?",
        "meta_title": "Driveway Planning Permission Bournemouth 2026 Guide",
        "meta_description": "Most driveways under 5m² of non-permeable surfacing don't need planning permission in Bournemouth. Full rules explained.",
        "excerpt": "The rule that decides whether your new driveway needs council sign-off, explained plainly.",
        "geo_answer": "Most driveways in Bournemouth don't need planning permission, provided the surface is permeable (gravel, permeable block paving, SUDS-compliant resin bound) or drains to your own garden. Non-permeable surfaces over 5m² that drain to the street generally do require permission.",
        "sections": [
            ("The Core Rule", "<p>Under permitted development rights, you can lay a new or replacement driveway of any size without planning permission if it uses permeable paving, or if rainwater drains to a permeable area of your own garden rather than onto the street. Only non-permeable driveways over 5m² that drain to the highway typically require an application.</p>"),
            ("What Doesn't Change This", "<p>Being in a conservation area, having protected trees nearby, or living in certain listed or Article 4 Direction properties can bring in extra requirements even for an otherwise permitted development driveway &mdash; see our guide to <a href=\"driveway-rules-trees-conservation-areas.html\">driveway rules near trees and conservation areas</a>.</p>"),
            ("What To Do If You're Unsure", "<p>We check the specifics of your property, including drainage direction and any local restrictions, during your free site visit and will flag clearly if an application is needed before any work starts.</p>"),
        ],
        "faq": [
            ("What's the 5m² rule?", "Non-permeable driveways over 5m² that drain onto the street generally need planning permission; permeable surfaces of any size usually don't."),
            ("Does a dropped kerb need separate permission?", "Yes &mdash; that's a separate council process. See our dropped kerb guide."),
            ("Will you handle the planning application for me?", "We can advise on the process and requirements as part of your quote, and point you to the right council resource."),
        ],
        "related": ["permeable-vs-non-permeable-driveways", "dropped-kerb-rules-bournemouth"],
    },
    {
        "slug": "dropped-kerb-rules-bournemouth",
        "cluster": "Planning & Legal",
        "title": "Dropped Kerb Rules and Costs in Bournemouth Explained",
        "meta_title": "Dropped Kerb Rules & Costs in Bournemouth",
        "meta_description": "Need a dropped kerb for your new driveway? Here's how BCP Council applications work, timelines and typical costs.",
        "excerpt": "If your new driveway needs vehicle access from the road, a dropped kerb application is usually the first step.",
        "geo_answer": "A dropped kerb in Bournemouth requires an application to BCP Council, whether or not your driveway itself needs planning permission. Costs and timelines vary by road type and works required &mdash; we can advise on the current process as part of your free quote.",
        "sections": [
            ("Why You Need One", "<p>If you want to drive on and off your new driveway from the road, and there isn&rsquo;t already a dropped kerb, this is a separate legal requirement from the driveway itself &mdash; even if your driveway surface doesn&rsquo;t need planning permission.</p>"),
            ("The Application Process", "<p>Applications go through BCP Council and typically involve confirming the road type, checking for nearby trees, drains or utility covers, and an inspection before works are approved. Timelines vary depending on council workload and road type.</p>"),
            ("What It Involves on Site", "<p>Once approved, the kerb is lowered and the pavement reinforced to safely bear vehicle weight &mdash; this is separate physical work from the driveway surface itself and is usually priced separately in a quote.</p>"),
        ],
        "faq": [
            ("Can I lower my own kerb without permission?", "No &mdash; altering a public kerb without approval is not permitted and can result in enforcement action."),
            ("How long does a dropped kerb application take?", "It varies by council workload and site specifics &mdash; we can advise on realistic timelines during your free quote."),
            ("Is a dropped kerb included in a driveway quote?", "Usually priced separately, since it's a distinct council process and different type of work &mdash; always confirm what's included."),
        ],
        "related": ["driveway-planning-permission-bournemouth", "hidden-driveway-costs"],
    },
    {
        "slug": "suds-permeable-paving-rules",
        "cluster": "Planning & Legal",
        "title": "SUDS and Permeable Paving Rules: Do You Need Drainage Approval?",
        "meta_title": "SUDS Driveway Rules: Do You Need Approval?",
        "meta_description": "Sustainable drainage (SUDS) rules affect most new UK driveways. Here's what's compliant without extra approval.",
        "excerpt": "SUDS rules exist to stop driveways adding to surface flooding. Here's what's automatically compliant.",
        "geo_answer": "SUDS (Sustainable Drainage Systems) rules require new hard surfacing to manage rainwater responsibly. Permeable materials &mdash; gravel, permeable block paving, and resin bound on a porous base &mdash; are SUDS compliant by design and don't need extra drainage approval in most cases.",
        "sections": [
            ("What SUDS Is For", "<p>Sustainable drainage rules exist to reduce the flooding risk created when rainwater that used to soak into a garden instead runs straight off a hard surface into the drains and street.</p>"),
            ("Compliant Options", "<p>Gravel, permeable block paving with gapped joints over a porous sub-base, and resin bound laid on a suitable porous base all allow water to soak through naturally, meeting SUDS requirements without extra work.</p>"),
            ("Non-Compliant Options and What They Need", "<p>Standard tarmac and standard block paving don't drain through the surface, so on larger driveways they may need water directed to a permeable area of your garden, or a separate soakaway or drainage channel, to meet the rules &mdash; we assess this at your free site visit.</p>"),
        ],
        "faq": [
            ("Is resin bound always SUDS compliant?", "Only when laid on a correctly specified porous base &mdash; this is standard practice for our resin bound installs."),
            ("Do I need council approval for a SUDS-compliant driveway?", "Generally no, since compliant permeable surfaces are usually exempt from the planning permission trigger that affects larger non-permeable driveways."),
            ("What happens if my driveway isn't SUDS compliant?", "It may need planning permission if over 5m² and draining to the street &mdash; see our planning permission guide."),
        ],
        "related": ["permeable-vs-non-permeable-driveways", "driveway-planning-permission-bournemouth"],
    },
    {
        "slug": "driveway-rules-trees-conservation-areas",
        "cluster": "Planning & Legal",
        "title": "Driveway Rules Near Trees, Boundaries and Conservation Areas in Dorset",
        "meta_title": "Driveway Rules Near Trees & Conservation Areas",
        "meta_description": "Conservation areas and protected trees can affect driveway planning in Dorset. What to check before you dig.",
        "excerpt": "Living somewhere protected or leafy? A few extra checks before work starts can save real headaches later.",
        "geo_answer": "Driveways near protected (TPO) trees or in conservation areas can require extra consent even where the driveway itself would normally be permitted development. Root protection zones and Article 4 Directions in some Dorset conservation areas are the two most common triggers.",
        "sections": [
            ("Tree Preservation Orders (TPOs)", "<p>If a tree on or near your property has a Tree Preservation Order, work within its root protection area &mdash; including excavation for a driveway &mdash; can require council consent, even for an otherwise permitted-development driveway.</p>"),
            ("Conservation Areas and Article 4 Directions", "<p>Some conservation areas in Dorset have Article 4 Directions removing the usual permitted development rights, meaning even a small, permeable driveway may need a full planning application. This varies street by street, so it&rsquo;s always worth checking directly with the council.</p>"),
            ("Boundary Considerations", "<p>Where a driveway runs close to a boundary, it&rsquo;s worth confirming exact ownership and any rights of access before excavation starts, to avoid disputes with neighbours later.</p>"),
        ],
        "faq": [
            ("How do I know if a tree near me has a TPO?", "Your local council's planning department maintains a public TPO register you can check by address."),
            ("Does living in a conservation area always mean I need permission?", "Not always &mdash; it depends on whether an Article 4 Direction is in place for your specific street."),
            ("Can you check this for me?", "We flag anything relevant during your free site visit and can point you to the right council resource to confirm."),
        ],
        "related": ["driveway-planning-permission-bournemouth", "driveway-installation-wimborne-guide"],
    },

    # ---------------------------------------------------------- Maintenance & Care --
    {
        "slug": "resin-bound-driveway-maintenance",
        "cluster": "Maintenance & Care",
        "title": "How to Maintain a Resin Bound Driveway: Complete Care Guide",
        "meta_title": "How to Maintain a Resin Bound Driveway",
        "meta_description": "Resin bound driveways need light monthly sweeping and an annual clean to last their full 20+ year lifespan. Full care guide.",
        "excerpt": "Resin bound is one of the lowest-maintenance surfaces available &mdash; but a little regular care goes a long way.",
        "geo_answer": "A resin bound driveway needs light sweeping every few weeks, an annual low-pressure wash, prompt attention to any oil or fuel spills, and a re-coat roughly every 8–12 years to maintain its full 20–25 year lifespan.",
        "sections": [
            ("Regular Light Care", "<p>A soft-bristle broom every few weeks clears leaves, dirt and debris before they can work into the surface. This alone prevents most of the discolouration issues homeowners see over time.</p>"),
            ("Annual Deep Clean", "<p>Once a year, a low-pressure wash (see our <a href=\"pressure-washing-driveway.html\">pressure washing guide</a> for the safe settings) removes ground-in dirt and any early moss or algae before it becomes established.</p>"),
            ("Dealing With Spills and Stains", "<p>Oil, fuel or fat spills should be blotted (not rubbed) and cleaned promptly with a mild detergent &mdash; resin bound is more resistant to staining than block paving, but quick action still gives the best result.</p>"),
        ],
        "faq": [
            ("Can I pressure wash a resin bound driveway?", "Yes, on a low-pressure setting held at a safe distance &mdash; high pressure can strip the resin surface over time."),
            ("How often should I reseal it?", "Roughly every 8–12 years, depending on use and exposure &mdash; see our full guide on resealing frequency."),
            ("What should I avoid using on it?", "Avoid rock salt in winter and harsh chemical cleaners &mdash; see our winter driveway care guide."),
        ],
        "related": ["pressure-washing-driveway", "winter-driveway-care"],
    },
    {
        "slug": "remove-moss-weeds-block-paving",
        "cluster": "Maintenance & Care",
        "title": "How to Remove Moss, Algae and Weeds From a Block Paving Driveway",
        "meta_title": "How to Remove Moss & Weeds From Block Paving",
        "meta_description": "Moss, algae and weeds between block paving are usually a drainage or joint-sand issue. Here's how to clear and prevent them.",
        "excerpt": "A step-by-step approach to clearing moss and weeds from block paving &mdash; and stopping them coming back.",
        "geo_answer": "To remove moss and weeds from block paving: 1) brush or scrape away loose growth, 2) treat remaining moss/algae with a suitable driveway-safe cleaner, 3) pressure wash on a moderate setting, 4) once dry, top up joints with fresh sand to prevent regrowth.",
        "sections": [
            ("Step 1: Clear Loose Growth", "<p>Start by brushing away any loose moss, weeds or debris with a stiff broom or a joint scraper for anything rooted in the sand between blocks.</p>"),
            ("Step 2: Treat and Wash", "<p>Apply a driveway-safe moss and algae treatment to any remaining growth, leave it to work as directed, then pressure wash on a moderate setting &mdash; see our <a href=\"pressure-washing-driveway.html\">pressure washing guide</a> for safe technique.</p>"),
            ("Step 3: Prevent Regrowth", "<p>Once the surface is fully dry, top up the joints with fresh kiln-dried or polymeric sand. Well-filled joints are one of the biggest factors in stopping weeds and moss re-establishing.</p>"),
        ],
        "faq": [
            ("Why does moss keep coming back?", "Usually because the joints have lost their sand, or the area doesn't get much sun and stays damp &mdash; both make it easy for moss to re-establish."),
            ("Is bleach safe to use on block paving?", "It's better to use a purpose-made driveway cleaner rather than bleach, which can discolour some block types."),
            ("How often should I do this?", "An annual clean and joint top-up is usually enough to keep block paving looking sharp."),
        ],
        "related": ["resin-bound-driveway-maintenance", "how-often-reseal-driveway"],
    },
    {
        "slug": "winter-driveway-care",
        "cluster": "Maintenance & Care",
        "title": "Winter Driveway Care: Protecting Against Frost and Salt Damage",
        "meta_title": "Winter Driveway Care: Avoiding Frost & Salt Damage",
        "meta_description": "Rock salt can damage resin bound driveways. Here's how to protect any driveway surface through a UK winter.",
        "excerpt": "A few small habit changes protect your driveway surface through the coldest months.",
        "geo_answer": "Avoid rock salt on resin bound driveways, as it can degrade the resin over time &mdash; use a resin-safe de-icer instead. Block paving and tarmac tolerate standard rock salt better, but all surfaces benefit from clearing standing water before a freeze to reduce frost damage.",
        "sections": [
            ("Which Surfaces Are Most at Risk", "<p>Resin bound is the most sensitive to standard rock salt, which can gradually break down the resin binder over repeated winters. Block paving and tarmac are more tolerant, though excessive salt use isn&rsquo;t ideal for any surface long-term.</p>"),
            ("De-Icing the Right Way", "<p>Use a resin-safe de-icer on resin bound driveways, and apply any salt or de-icer sparingly and evenly rather than piling it in one area.</p>"),
            ("Preventing Frost Damage", "<p>Standing water that freezes and expands is the main cause of frost damage on any surface &mdash; make sure drainage is clear of leaves and debris going into winter, and address any standing water issues (see our <a href=\"driveway-drainage-standing-water.html\">drainage guide</a>) before the cold sets in.</p>"),
        ],
        "faq": [
            ("Can I use rock salt on my resin driveway?", "It's best avoided &mdash; use a resin-safe de-icer instead to protect the surface long-term."),
            ("Does frost crack tarmac or block paving?", "It can, particularly where standing water has been allowed to sit and freeze repeatedly &mdash; good drainage reduces this risk significantly."),
            ("Is grit better than salt?", "Grit provides traction without the chemical effects of salt, and is a safe option for any driveway surface."),
        ],
        "related": ["driveway-drainage-standing-water", "resin-bound-driveway-maintenance"],
    },
    {
        "slug": "how-often-reseal-driveway",
        "cluster": "Maintenance & Care",
        "title": "How Often Should You Reseal a Resin or Block Paving Driveway?",
        "meta_title": "How Often to Reseal a Resin or Block Paving Driveway",
        "meta_description": "Resin bound driveways need re-coating every 8-12 years; block paving sealant every 2-3 years. Here's why it matters.",
        "excerpt": "Getting resealing timing right protects your driveway&rsquo;s look and lifespan &mdash; and it differs a lot by material.",
        "geo_answer": "Resin bound driveways typically need a re-coat every 8–12 years. Block paving benefits from a fresh sealant and jointing sand top-up every 2–3 years to keep colours sharp and joints weed-resistant. Gravel and tarmac don't require sealing in the same way.",
        "sections": [
            ("Resin Bound Re-Coating", "<p>The resin surface gradually loses some of its UV stability and gloss over years of sun and weather exposure. A professional re-coat every 8&ndash;12 years restores the finish and extends the driveway&rsquo;s overall lifespan.</p>"),
            ("Block Paving Sealant", "<p>Block paving sealant protects colour, reduces staining, and helps stabilise jointing sand against weeds &mdash; most manufacturers recommend reapplying every 2&ndash;3 years, more often in high-traffic areas.</p>"),
            ("Signs You're Overdue", "<p>Fading colour, increased weed growth between blocks, or a resin surface that feels rougher or duller than it used to are all signs it&rsquo;s worth booking a reseal or re-coat.</p>"),
        ],
        "faq": [
            ("Does gravel need resealing?", "No &mdash; gravel doesn't use a sealed surface, though occasional top-ups keep depth and coverage even."),
            ("Can I reseal block paving myself?", "It's possible with the right products, though a professional job typically gives a more even, longer-lasting result."),
            ("What happens if I never reseal?", "The surface will still function but will fade, stain more easily, and in block paving's case, weed more, faster."),
        ],
        "related": ["resin-bound-driveway-maintenance", "remove-moss-weeds-block-paving"],
    },
    {
        "slug": "pressure-washing-driveway",
        "cluster": "Maintenance & Care",
        "title": "Pressure Washing Your Driveway: Dos, Don'ts and How Often",
        "meta_title": "Pressure Washing a Driveway: Dos, Don'ts, Frequency",
        "meta_description": "Too much pressure can strip resin and loosen block paving joints. Here's the safe way to jet wash any driveway.",
        "excerpt": "Pressure washing is one of the easiest ways to damage a driveway if done wrong. Here's how to do it safely.",
        "geo_answer": "Use a low-to-moderate pressure setting and keep the nozzle at least 20-30cm from the surface. High pressure held too close can strip resin bound coatings and blast jointing sand out of block paving, both of which shorten the driveway's lifespan.",
        "sections": [
            ("Setting the Right Pressure", "<p>A wide fan nozzle on a low or moderate setting is safer than a narrow, high-pressure jet, which concentrates force into a small area and can damage the surface finish or joints.</p>"),
            ("Material-Specific Tips", "<p>On resin bound, keep pressure low to avoid stripping the resin coating. On block paving, avoid blasting directly into the joints, which can strip out the sand and open the door to weeds. Tarmac and gravel are more forgiving but should still avoid sustained close-range high pressure.</p>"),
            ("How Often to Do It", "<p>An annual clean is usually enough for most driveways &mdash; more often in shaded, damp areas prone to algae, less often for well-draining, sunny driveways.</p>"),
        ],
        "faq": [
            ("Can pressure washing damage a driveway?", "Yes, if the pressure is too high or the nozzle held too close &mdash; particularly on resin bound and block paving joints."),
            ("Should I reseal after pressure washing?", "For block paving, a fresh sand top-up and occasional reseal after washing helps maintain weed resistance."),
            ("Is a hose enough instead of a pressure washer?", "For light dirt, yes &mdash; save the pressure washer for an annual deeper clean."),
        ],
        "related": ["resin-bound-driveway-maintenance", "remove-moss-weeds-block-paving"],
    },
    {
        "slug": "driveway-drainage-standing-water",
        "cluster": "Maintenance & Care",
        "title": "Driveway Drainage Problems and How to Fix Standing Water",
        "meta_title": "Driveway Standing Water: Causes & Fixes",
        "meta_description": "Standing water on a driveway is usually poor fall, compaction or a blocked drain. Here's how to diagnose and fix it.",
        "excerpt": "Puddles that won't drain are more than a nuisance &mdash; left unchecked, they cause real long-term damage.",
        "geo_answer": "Standing water on a driveway is usually caused by insufficient fall (slope) during installation, ground compaction over time reducing permeability, or a blocked drainage channel. Left unaddressed, it accelerates frost damage and surface wear.",
        "sections": [
            ("Common Causes", "<p>A driveway needs a slight fall, typically away from the house, to shed water properly. Over years, ground can compact and reduce a permeable surface's ability to drain, and channel drains or soakaways can silt up and need clearing.</p>"),
            ("Why It Matters", "<p>Standing water that freezes in winter expands and accelerates cracking, and prolonged damp conditions encourage moss, algae and weed growth &mdash; so fixing drainage issues protects the whole driveway, not just the puddle itself.</p>"),
            ("Fixing the Problem", "<p>Solutions range from clearing and reinstating a blocked drainage channel, to relaying an area with insufficient fall, to installing a soakaway on persistently waterlogged sites. We diagnose the specific cause during a site visit before recommending a fix.</p>"),
        ],
        "faq": [
            ("Is standing water always a big problem?", "Minor, short-lived puddling after heavy rain is normal; water that sits for a day or more usually points to a drainage issue worth fixing."),
            ("Can permeable driveways still get standing water?", "Yes, if the permeable layer has become compacted or silted over time and needs restoring."),
            ("Will you check drainage as part of a quote?", "Yes &mdash; drainage and ground condition are always assessed at your free site visit."),
        ],
        "related": ["winter-driveway-care", "suds-permeable-paving-rules"],
    },

    # -------------------------------------------------------------- Local Guides --
    {
        "slug": "driveway-installation-poole-guide",
        "cluster": "Local Guides",
        "title": "Driveway Installation in Poole: Local Guide, Costs and Considerations",
        "meta_title": "Driveway Installation in Poole | Local Guide",
        "meta_description": "Planning a new driveway in Poole? Local costs, popular materials and what BCP Council requires, explained.",
        "excerpt": "What Poole homeowners need to know before starting a driveway project, from cost to coastal considerations.",
        "geo_answer": "Driveway costs in Poole are in line with the wider Bournemouth area, roughly £30–£110 per m² depending on material. Resin bound and block paving tend to perform particularly well against Poole's coastal weather. See our full <a href=\"driveways-poole.html\">Poole driveways page</a> for local details.",
        "sections": [
            ("Local Pricing", "<p>Pricing in Poole follows the same broad ranges as the rest of the BCP area &mdash; gravel from £30/m² through to resin bound at up to £110/m². Coastal properties near Sandbanks and the harbour can sometimes involve trickier access, which a free site visit accounts for.</p>"),
            ("Materials That Suit Poole Properties", "<p>From period homes near the Old Town to modern builds around Canford Heath and Broadstone, we tailor material recommendations to the property. See our <a href=\"best-driveway-material-coastal-weather.html\">coastal weather materials guide</a> for more detail on what holds up best locally.</p>"),
            ("Planning and Council Considerations", "<p>Poole falls under BCP Council for both planning permission and dropped kerb applications &mdash; the same core rules covered in our <a href=\"driveway-planning-permission-bournemouth.html\">planning permission guide</a> apply here.</p>"),
        ],
        "faq": [
            ("Do you cover all of Poole, including Sandbanks and Broadstone?", "Yes &mdash; we cover Poole and the surrounding harbour side including Sandbanks, Broadstone, Canford Heath and Hamworthy."),
            ("How quickly can you visit for a quote in Poole?", "We typically offer free site visits within a few days of enquiry."),
            ("Which driveway material suits coastal properties near Sandbanks best?", "Resin bound and block paving tend to hold up particularly well to coastal weather."),
        ],
        "related": ["best-driveway-material-coastal-weather", "driveway-cost-bournemouth-2026"],
    },
    {
        "slug": "driveway-installation-christchurch-guide",
        "cluster": "Local Guides",
        "title": "Driveway Installation in Christchurch: What Homeowners Need to Know",
        "meta_title": "Driveway Installation in Christchurch | Local Guide",
        "meta_description": "New driveway in Christchurch? Local pricing, popular materials and planning rules for Dorset homeowners.",
        "excerpt": "A local look at driveway costs, materials and planning considerations for Christchurch homeowners.",
        "geo_answer": "Driveway installation in Christchurch follows the same pricing (roughly £30–£110/m²) and planning rules as the wider Bournemouth area. Block paving and resin bound are popular locally, particularly for period properties near the Priory. See our <a href=\"driveways-christchurch.html\">Christchurch driveways page</a>.",
        "sections": [
            ("Local Pricing and Popular Materials", "<p>Whether it&rsquo;s a period property near the Priory or a newer build towards Highcliffe, block paving and resin bound are popular choices where kerb appeal matters most, though all four materials are installed regularly across the area.</p>"),
            ("Coverage Across the Area", "<p>Our Christchurch coverage extends to Highcliffe, Mudeford and the surrounding villages, with the same fixed-price, fully insured standard applied throughout.</p>"),
            ("Planning Considerations", "<p>Christchurch properties near the Priory or in conservation areas may have additional planning considerations &mdash; see our guide to <a href=\"driveway-rules-trees-conservation-areas.html\">driveway rules near trees and conservation areas</a>.</p>"),
        ],
        "faq": [
            ("Do you cover Highcliffe and Mudeford as well as Christchurch town?", "Yes &mdash; our coverage includes Highcliffe, Mudeford and the surrounding villages."),
            ("Can you install a driveway on a period property in Christchurch?", "Yes, we regularly work on period properties across the area."),
            ("How long does a typical installation take in Christchurch?", "Most jobs are completed in 1–3 days depending on size and material."),
        ],
        "related": ["driveway-rules-trees-conservation-areas", "driveway-cost-bournemouth-2026"],
    },
    {
        "slug": "driveway-installation-ferndown-guide",
        "cluster": "Local Guides",
        "title": "Driveway Installation in Ferndown: Costs, Materials and Considerations",
        "meta_title": "Driveway Installation in Ferndown | Local Guide",
        "meta_description": "New driveway in Ferndown? Local costs, materials and what to expect from quote to completion.",
        "excerpt": "What to expect when planning a new driveway in Ferndown, from popular materials to typical timelines.",
        "geo_answer": "Ferndown driveway installations follow standard BCP-area pricing (£30–£110/m²). Block paving and gravel are particularly popular locally, and Ferndown's larger plots are well suited to multi-car and wraparound driveway projects. See our <a href=\"driveways-ferndown.html\">Ferndown driveways page</a>.",
        "sections": [
            ("What's Popular Locally", "<p>Block paving and gravel are particularly popular in Ferndown, though we install all four materials depending on the property and budget. Ferndown's mix of family homes and larger properties means projects range from compact single driveways to large multi-car installs.</p>"),
            ("Multi-Car and Wraparound Projects", "<p>Ferndown's larger plots are well suited to multi-car driveways, and our team regularly quotes for wraparound and large-format projects &mdash; see our <a href=\"driveway-installation-process-explained.html\">installation process guide</a> for what to expect on a bigger job.</p>"),
            ("Dropped Kerbs in Ferndown", "<p>If your Ferndown project needs a new or altered dropped kerb, we advise on the BCP Council application process as part of your quote &mdash; see our full <a href=\"dropped-kerb-rules-bournemouth.html\">dropped kerb guide</a>.</p>"),
        ],
        "faq": [
            ("Do you cover West Moors and the villages around Ferndown?", "Yes &mdash; we cover Ferndown and surrounding villages including West Moors and Longham."),
            ("What's the most popular driveway type in Ferndown?", "Block paving and gravel are particularly popular locally."),
            ("Can you handle larger, multi-car driveways in Ferndown?", "Yes, we regularly quote for wraparound and large-format projects."),
        ],
        "related": ["driveway-installation-process-explained", "dropped-kerb-rules-bournemouth"],
    },
    {
        "slug": "driveway-installation-wimborne-guide",
        "cluster": "Local Guides",
        "title": "Driveway Installation in Wimborne: A Homeowner's Guide",
        "meta_title": "Driveway Installation in Wimborne | Local Guide",
        "meta_description": "New driveway in Wimborne? Local costs, material choices for period homes, and planning considerations.",
        "excerpt": "Wimborne's period and rural character shapes which materials tend to work best. Here's our local guide.",
        "geo_answer": "Wimborne's mix of period town-centre homes and rural properties often calls for gravel or resin bound driveways that complement the setting. Standard BCP-area pricing (£30–£110/m²) and planning rules apply. See our <a href=\"driveways-wimborne.html\">Wimborne driveways page</a>.",
        "sections": [
            ("Materials That Suit Wimborne", "<p>Gravel and resin bound tend to suit period and rural properties particularly well, complementing Wimborne's historic character, though the right choice always depends on your specific driveway and budget.</p>"),
            ("Conservation Area Considerations", "<p>Wimborne Minster's conservation area may bring in additional planning considerations depending on the property and surface chosen &mdash; permeable materials like gravel or SUDS-compliant resin bound usually avoid the need for extra permission. See our <a href=\"driveway-rules-trees-conservation-areas.html\">conservation area guide</a>.</p>"),
            ("Rural and Unadopted Roads", "<p>We regularly quote for rural properties around Wimborne &mdash; access and ground conditions are always assessed during your free site visit.</p>"),
        ],
        "faq": [
            ("Is gravel a good option for a period property in Wimborne?", "Often, yes &mdash; gravel and resin bound tend to suit period and rural properties particularly well."),
            ("Do you need planning permission in Wimborne Minster's conservation area?", "Possibly, depending on the property and surface &mdash; permeable materials usually avoid the need for permission."),
            ("How far outside Wimborne do you cover?", "We cover Wimborne Minster and surrounding villages and rural areas &mdash; get in touch to confirm your postcode."),
        ],
        "related": ["driveway-rules-trees-conservation-areas", "permeable-vs-non-permeable-driveways"],
    },
    {
        "slug": "driveway-installation-new-milton-guide",
        "cluster": "Local Guides",
        "title": "Driveway Installation in New Milton: Coastal Considerations and Costs",
        "meta_title": "Driveway Installation in New Milton | Local Guide",
        "meta_description": "New driveway in New Milton? Coastal weather considerations, local costs and material recommendations.",
        "excerpt": "New Milton's coastal position makes material choice matter more than usual. Here's what to consider.",
        "geo_answer": "Tarmac and block paving are the most requested driveway materials in New Milton, though all four materials suit the area depending on budget. Coastal weather makes durability against salt air worth discussing during your free quote. See our <a href=\"driveways-new-milton.html\">New Milton driveways page</a>.",
        "sections": [
            ("Popular Materials Locally", "<p>Tarmac and block paving are the most requested locally, though resin bound and gravel are also installed regularly depending on property style and budget.</p>"),
            ("Coastal Weather Considerations", "<p>From New Milton town through to Barton on Sea, coastal exposure is worth factoring into material choice &mdash; see our <a href=\"best-driveway-material-coastal-weather.html\">coastal weather materials guide</a> for what tends to perform best.</p>"),
            ("Getting a Quote", "<p>In most cases we can arrange a free site visit within a few days for New Milton and the surrounding area, with the same fixed-price, fully guaranteed standard as the rest of our coverage.</p>"),
        ],
        "faq": [
            ("Do you cover Barton on Sea as well as New Milton?", "Yes &mdash; our coverage extends to Barton on Sea and the immediate surrounding area."),
            ("What driveway materials are most popular in New Milton?", "Tarmac and block paving are the most requested locally."),
            ("Can I get a same-week quote in New Milton?", "In most cases, yes &mdash; contact us and we'll aim to arrange a free site visit within a few days."),
        ],
        "related": ["best-driveway-material-coastal-weather", "driveway-cost-bournemouth-2026"],
    },

    # -------------------------------------------------------- Buying Guide & Trust --
    {
        "slug": "how-to-choose-a-driveway-installer",
        "cluster": "Buying Guide & Trust",
        "title": "How to Choose a Driveway Installer: 10 Questions to Ask",
        "meta_title": "How to Choose a Driveway Installer: 10 Questions",
        "meta_description": "Ask these 10 questions before hiring a driveway installer to avoid rogue traders and costly mistakes.",
        "excerpt": "The right questions, asked before you sign anything, are the best protection against a poor driveway installation.",
        "geo_answer": "Before hiring a driveway installer, ask: are you fully insured, is the quote fixed and in writing, what sub-base depth is included, is old-surface removal included, what's the payment schedule, is there a written guarantee, can I see recent local work, who handles building/planning issues, what's the projected timeline, and what happens if I'm not satisfied?",
        "sections": [
            ("The 10 Questions", "<p>1) Are you fully insured with public liability cover? 2) Is this quote fixed, in writing, and from a site visit? 3) What sub-base depth and specification is included? 4) Is removal of the old surface included? 5) What's the payment schedule, and is a large deposit required? 6) Is there a written workmanship guarantee? 7) Can I see examples of recent local work? 8) Who handles any dropped kerb or planning permission needs? 9) What's the realistic timeline for my job? 10) What happens if I'm not satisfied with the finished result?</p>"),
            ("Red Flags to Watch For", "<p>Vague or verbal-only quotes, pressure to decide same-day, requests for a large cash deposit upfront, and reluctance to confirm insurance details are all worth treating with caution &mdash; see our full <a href=\"rogue-driveway-traders-red-flags.html\">rogue trader red flags guide</a>.</p>"),
            ("What a Good Answer Looks Like", "<p>A trustworthy installer will happily confirm insurance, provide a written fixed quote after seeing the site, explain sub-base specification without being asked twice, and won't pressure you to decide on the spot.</p>"),
        ],
        "faq": [
            ("Should I get more than one quote?", "It's generally worth comparing at least two or three quotes from a proper site visit before deciding."),
            ("Is a written guarantee standard?", "It should be &mdash; ask specifically what it covers and for how long."),
            ("What if an installer won't answer these questions?", "Treat that as a warning sign and consider getting quotes elsewhere."),
        ],
        "related": ["rogue-driveway-traders-red-flags", "driveway-installation-process-explained"],
    },
    {
        "slug": "rogue-driveway-traders-red-flags",
        "cluster": "Buying Guide & Trust",
        "title": "Red Flags: How to Spot Rogue Driveway Traders in Dorset",
        "meta_title": "Rogue Driveway Traders: Red Flags to Watch For",
        "meta_description": "Cold callers, cash-only deals and no written quote are classic rogue trader signs. Here's how to protect yourself.",
        "excerpt": "Rogue traders follow recognisable patterns. Here's what to watch for before you commit to a driveway project.",
        "geo_answer": "Common rogue driveway trader red flags: unsolicited cold-calling or door-knocking, cash-only payment requests, no fixed address or verifiable insurance, high-pressure same-day discounts, no written quote, and requests for a large upfront deposit before any work has started.",
        "sections": [
            ("Cold Calling and Door-Knocking", "<p>Legitimate local installers rarely rely on unsolicited door-to-door sales, especially offering to use \"leftover materials\" from a nearby job &mdash; a classic and long-running rogue trader tactic.</p>"),
            ("Payment and Pricing Red Flags", "<p>Be wary of cash-only requests, prices that seem unusually low, large deposits demanded before work starts, or pressure to decide immediately for a \"special\" discount.</p>"),
            ("How to Protect Yourself", "<p>Insist on a written, fixed quote from a proper site visit, verify insurance and any trade association membership independently, and take time to compare quotes rather than deciding under pressure &mdash; see our <a href=\"how-to-choose-a-driveway-installer.html\">10 questions to ask</a> before hiring.</p>"),
        ],
        "faq": [
            ("Should I ever pay cash upfront in full?", "It's safest to avoid paying the full amount upfront, and especially avoid cash-only arrangements with no paper trail."),
            ("Are all door-to-door driveway offers scams?", "Not necessarily, but unsolicited high-pressure offers are a classic pattern worth treating with real caution."),
            ("What should I do if I suspect a rogue trader?", "Don't sign anything or hand over money under pressure &mdash; take time to verify their details and get an independent quote instead."),
        ],
        "related": ["how-to-choose-a-driveway-installer", "driveway-installation-process-explained"],
    },
    {
        "slug": "driveway-installation-process-explained",
        "cluster": "Buying Guide & Trust",
        "title": "Driveway Installation Process: What to Expect From Quote to Completion",
        "meta_title": "Driveway Installation Process Explained",
        "meta_description": "From first survey to final finish: what actually happens during a driveway installation, and how long each stage takes.",
        "excerpt": "Knowing what should happen at each stage helps you spot a job that's on track &mdash; or one that isn't.",
        "geo_answer": "A typical driveway installation runs: free site survey and fixed quote, excavation and old-surface removal (if needed), sub-base laying and compaction, edging installation, surface laying (material-specific), and a final inspection walk-through. Most residential jobs complete in 1–4 days depending on material and size.",
        "sections": [
            ("Survey and Quote", "<p>A proper installer visits to measure, check access and drainage, and confirms a fixed, written price &mdash; this stage should never be skipped in favour of a phone-only estimate.</p>"),
            ("Excavation Through to Sub-Base", "<p>The existing surface is removed if needed, the area excavated to the correct depth, and a compacted MOT Type 1 sub-base laid &mdash; this stage matters more for the driveway's long-term durability than almost anything else.</p>"),
            ("Surfacing and Finishing", "<p>The final surface is laid according to the material &mdash; tarmac rolled in layers, block paving laid and jointed, resin mixed and trowelled, or gravel spread and compacted &mdash; followed by a final clean-up and walk-through inspection with you.</p>"),
        ],
        "faq": [
            ("How long does a typical driveway take?", "Most residential driveways are completed in 1–4 days depending on size and material."),
            ("What happens if it rains during installation?", "Some stages, particularly resin laying, are weather-sensitive and may need to be rescheduled &mdash; a good installer will explain this upfront."),
            ("Will I get a final walkthrough?", "Yes &mdash; a proper installer reviews the finished job with you before considering it complete."),
        ],
        "related": ["how-to-choose-a-driveway-installer", "hidden-driveway-costs"],
    },
    {
        "slug": "does-a-new-driveway-add-value",
        "cluster": "Buying Guide & Trust",
        "title": "Does a New Driveway Add Value to Your Home?",
        "meta_title": "Does a New Driveway Add Value to Your Home?",
        "meta_description": "Block paving can add £2,000-5,000 to resale value, resin bound £1,500-3,500. Here's what actually pays off.",
        "excerpt": "Kerb appeal genuinely moves the needle on resale value &mdash; here's what the numbers actually look like.",
        "geo_answer": "A new driveway can meaningfully boost resale value: block paving typically adds roughly £2,000–£5,000, and resin bound roughly £1,500–£3,500, largely through improved kerb appeal and off-street parking, which buyers consistently rate highly.",
        "sections": [
            ("Why Kerb Appeal Matters So Much", "<p>The driveway is often the first thing a buyer sees, and off-street parking is a genuinely high-priority feature for many buyers &mdash; both combine to make a tidy, well-installed driveway one of the better-value home improvements available.</p>"),
            ("What the Numbers Look Like", "<p>Block paving tends to add the most, roughly £2,000&ndash;£5,000, reflecting its premium, customisable look. Resin bound adds a comparable but slightly lower uplift, roughly £1,500&ndash;£3,500, still a strong return relative to installation cost.</p>"),
            ("Getting the Best Return", "<p>Choosing a material that suits the property's style, keeping the design clean rather than overly elaborate, and ensuring a professional, durable installation all help maximise the resale uplift &mdash; a poorly installed driveway can have the opposite effect.</p>"),
        ],
        "faq": [
            ("Which material adds the most value?", "Block paving tends to add the most on average, though resin bound offers a strong return too."),
            ("Is a new driveway worth it if I'm selling soon?", "Often, yes &mdash; kerb appeal and off-street parking are high-priority features for many buyers."),
            ("Does driveway condition affect how a home is valued?", "Yes &mdash; a cracked, dated or poorly maintained driveway can detract from a buyer's first impression."),
        ],
        "related": ["resin-bound-vs-block-paving-cost", "driveway-cost-bournemouth-2026"],
    },
]

assert len(BLOG_POSTS) == 30, f"expected 30 blog posts, got {len(BLOG_POSTS)}"

# Publish order == list order. Used by publish.py to know what's already live
# vs still queued (cross-referenced against blog_published.json in the repo).
PUBLISH_ORDER = [p["slug"] for p in BLOG_POSTS]
