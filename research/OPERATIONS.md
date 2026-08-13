# BatterijWijzer — Operations Log & Runbook

Autonomous execution of the NL/BE market-research plan (see `NL-BE-MARKET-RESEARCH.md`).
Niche: **thuisbatterijen + zonnepanelen na het einde van salderen** (top pick from the research).
Working brand: **BatterijWijzer** (placeholder until a domain is bought).

## Status

### Done (by Claude)
- [x] Market research report (`research/NL-BE-MARKET-RESEARCH.md`)
- [x] Site v1 in `site/`: homepage, 2 interactive calculators (thuisbatterij, zonnepanelen post-saldering), 2 cornerstone articles, AVG-compliant lead form (`offerte.html`), privacy policy
- [x] GitHub Pages deploy workflow (`.github/workflows/deploy-site.yml`)
- [x] Daily routine scheduled: Claude wakes up daily to spend the token budget on the next backlog item

### Blocked on human (money/identity gates — Claude cannot legally/technically do these)
1. **Enable GitHub Pages**: repo Settings → Pages → Source: "GitHub Actions". After that every push auto-deploys the site to a live URL. (~1 minute)
2. **Buy the domain** (~€10/yr): suggestions, check availability at any registrar:
   `batterijwijzer.nl`, `batterijcheck.nl`, `thuisbatterijwijzer.nl`, `salderencheck.nl`.
   Then: repo Settings → Pages → Custom domain, and point DNS (CNAME) at GitHub Pages.
3. **Form endpoint** (free tier is fine): create a Formspree (or similar) form, put the endpoint URL in `LEAD_ENDPOINT` in `site/offerte.html`. Until then the form shows "tijdelijk niet beschikbaar".
4. **Affiliate signups** (needs your identity + IBAN): Daisycon (energy/insurance/telecom) and Bol.com Partner Program. Once approved, give Claude the tracking links to place.
5. **Lead buyers**: to sell quote-requests, either sign up at a lead marketplace or let Claude draft outreach emails to regional installers (Claude can write them; you send/approve).
6. **When revenue starts**: KVK registration (NL) or bijberoep (BE); see tax section of the research report.

## Daily-session runbook (for the scheduled Claude session)

Each day, in order of priority, pick the top unblocked item, complete it, commit, push to
`claude/dutch-belgian-market-research-cmxwyh`, and update this file:

1. If human unblocked something above → integrate it (tracking links, form endpoint, domain).
2. Content backlog (one page/day, Dutch, must contain something an AI answer can't give —
   a table with current numbers, a calculation, or a decision checklist):
   - [x] Terugleverkosten per leverancier: vergelijkingstabel (update monthly! — laatst: aug 2026)
   - [x] Dynamisch energiecontract + thuisbatterij: hoe werkt het, voor wie
   - [x] Thuisbatterij subsidie: stand van zaken NL (en BE premies per gewest) — refresh after
         Prinsjesdag 17 sep 2026 (btw-besluit losse batterijen!)
   - [x] Beste thuisbatterijen 2026: vergelijking op €/kWh, garantie, chemie
   - [x] Thuisaccu en verzekering/brandveiligheid: waar je op moet letten
   - [ ] Belgische variant-pagina's (premies, digitale meter, capaciteitstarief)
   - [x] FAQ-pagina (schema.org FAQ markup) per calculator
3. Technical backlog:
   - [x] sitemap.xml + robots.txt (paths relative — make absolute once domain exists)
   - [x] Schema.org markup (WebApplication voor calculators, FAQPage)
   - [ ] Open Graph tags + social preview
   - [ ] Cookieless analytics (e.g. GoatCounter free tier — needs human signup, ask once)
   - [ ] Nieuwsbrief-signup blok (needs provider signup — ask once)
4. Never: fake reviews, fabricated "test results", scaled thin AI pages (March 2026 spam
   update kills exactly that), or claims about prices/subsidies without a check.

## Log

- **2026-08-07**: Research report delivered. Site v1 built (7 pages, 2 calculators, lead funnel,
  privacy). Pages workflow added. Daily routine created. Human checklist published (6 items).
- **2026-08-08** (daily session 1): Added `terugleverkosten-per-leverancier.html` — comparison
  table (Eneco ±€0,18/kWh, Essent staffel ±€276/jr, Vattenfall ±€215/jr, Budget Energie
  ±€0,11/kWh, dynamische leveranciers €0) + mini cost calculator + 7 savings tips; linked from
  homepage and salderen article. Added sitemap.xml + robots.txt. Note: direct fetches of Dutch
  comparison sites are blocked by the egress proxy — figures sourced via search results; refresh
  monthly. All 6 human blockers still open (Pages, domain, form endpoint, Daisycon/Solvari/
  Slimster signups, lead buyers, KVK). Next up: dynamisch contract + thuisbatterij article.
- **2026-08-09** (daily session 2): Added `dynamisch-contract-thuisbatterij.html` — explains the
  two battery revenue models (solar-shift vs price-trading), 1 May 2026 example (€0,74/kWh
  intraday spread), realistic yields (€200–280/jr no solar; €400–700/jr with solar post-2027;
  debunks €1.200 vendor claims), negative-price misconception, plus a trading-income mini
  calculator. Cross-linked from homepage, zin-of-onzin article and sitemap. All 6 human blockers
  still open. Next up: thuisbatterij subsidie NL + BE premies page.
- **2026-08-10** (daily session 3): Added `subsidie-thuisbatterij.html` — NL: new ISDE battery
  subsidy per 1-1-2026 (€250/kWh, max €1.500, requires ≥3.000 Wp new panels), 0% btw with
  panels, pending Prinsjesdag decision on 0% btw for standalone batteries (motion 10 jun 2026);
  BE: no premies anywhere (Fluvius closed), 6% btw renovation rate, Homegrade loans (BR),
  prosumententarief refund ±54% (WA), groenestroomcertificaten (BR). Includes interactive
  region/situation checker. Cross-linked + sitemap. IMPORTANT date: refresh page after
  17 sep 2026 (Prinsjesdag). All 6 human blockers still open. Next up: beste thuisbatterijen
  2026 comparison (€/kWh, garantie, chemie).
- **2026-08-11** (daily session 4): Added `beste-thuisbatterijen.html` — situation-based
  comparison (premium: Sigenergy/Tesla PW3/SolarEdge/Enphase; dynamic-trading: Sessy/Zonneplan/
  AlphaESS; modular budget: BYD/Huawei/Marstek/LG at €300–600/kWh; plug-in: Marstek Venus E
  ±€254/kWh), criteria table (LFP, ≥6.000 cycli, €400–650/kWh incl. install benchmark), 5 offer
  pitfalls, and an interactive offerte-checker (price-per-kWh verdict + warranty flags) feeding
  the quote funnel. Explicitly framed as public-spec comparison, no fabricated tests.
  Cross-linked + sitemap. All 6 human blockers still open. Next up: brandveiligheid/verzekering
  article or FAQ pages with schema.org markup.
- **2026-08-12** (daily session 5): Added `brandveiligheid-verzekering.html` — opstal vs
  inboedel (vast vs plug-in, huurwoning), the 3 insurer requirements (NEN 1010, erkend
  installateur, installatierapport), legal registration duty via Energieleveren.nl (insurers
  ask for proof), placement do's/don'ts (no bedroom/gas/wooden attic; concrete floor, dry,
  frost-free, ventilated), LFP preference, BE note (AREI/Fluvius). Includes interactive
  6-point coverage checklist. Cross-linked + sitemap. All 6 human blockers still open.
  Content backlog remaining: Belgische variant-pagina's, FAQ + schema.org markup;
  tech backlog: Open Graph tags, analytics (needs human signup), nieuwsbrief (needs human
  signup).
- **2026-08-13** (daily session 6): Added `veelgestelde-vragen.html` — 12 FAQs in 3 clusters
  (salderen / thuisbatterij / subsidie & regels), collapsible details-elements, all answers
  distilled from existing verified pages with internal links; JSON-LD FAQPage markup (8 core
  Q&As). Added WebApplication JSON-LD to both calculators. Cross-linked + sitemap. All 6 human
  blockers still open (day 6). Remaining content backlog: Belgische variant-pagina's;
  remaining tech: Open Graph tags. NOTE for next sessions: consider drafting installer
  outreach emails (Tier 3 lead sales) — doable without human accounts, human only sends.
