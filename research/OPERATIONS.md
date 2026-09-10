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
   - [x] Belgische variant-pagina's (premies, digitale meter, capaciteitstarief) — Vlaanderen,
         Wallonië en Brussel all done; full BE coverage
   - [x] FAQ-pagina (schema.org FAQ markup) per calculator
3. Technical backlog:
   - [x] sitemap.xml + robots.txt (paths relative — make absolute once domain exists)
   - [x] Schema.org markup (WebApplication voor calculators, FAQPage)
   - [x] Open Graph tags (all pages; social preview image still to make once branding is set)
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
- **2026-08-14** (daily session 7): Created `research/OUTREACH-EMAILS.md` — the Tier-3 direct
  lead-sales pack: 4 Dutch email templates (installer pilot pitch with 3-free-leads hook,
  follow-up, lead-marketplace supplier application, Flemish variant), pricing anchors
  (€35 intro / €45 standard exclusive, €20–25 shared), targeting criteria, AVG
  verwerkersovereenkomst core clause, and usage rules (never send before the funnel is live;
  never claim volume we don't have). Also injected Open Graph tags on all 13 pages
  (og:title/description/locale/site_name derived from existing meta). All 6 human blockers
  still open (day 7). Remaining content backlog: Belgische variant-pagina's. When human
  unblocks: sending outreach needs a sender address at the domain.
- **2026-08-15** (daily session 8): Added `thuisbatterij-vlaanderen.html` — the Flemish market
  page: capaciteitstarief explained (±€56,6/kW/jaar 2026, gezinnen €90–245/jr op maandpiek),
  the three Flemish revenue models (zelfverbruik vs lage injectievergoeding, piekafvlakking
  €70–200/jr, dynamische prijshandel), total €400–800/jr and 7–10 jr payback benchmarks, AREI/
  Fluvius/6% btw notes, analoge-teller warning, and a dedicated Flemish calculator with
  peak-shaving input and per-stream breakdown (nl-BE locale, og:locale nl_BE). Cross-linked
  from homepage + subsidie page + sitemap. CONTENT BACKLOG NOW EMPTY except optional
  Wallonië/Brussel variants and the monthly terugleverkosten refresh (due ±2026-09-08).
  All 6 human blockers still open (day 8). Suggested next sessions: monthly data refresh,
  Wallonië/Brussel variant, nieuwsbrief-ready content, or maintenance passes pending human
  unblocks (Prinsjesdag refresh due after 17 sep).
- **2026-08-16** (daily session 9): QA hardening day. Added `tools/site_check.py` — repeatable
  site QA (broken internal links, missing title/description/og/viewport/favicon, sitemap
  coverage both directions; noindex pages exempt from description/og). Ran it: links/meta/
  sitemap were clean; favicons were missing → injected inline-SVG 🔋 favicon on all pages.
  Added 404.html (noindex, links to calculators; GitHub Pages serves it automatically).
  Final state: 15 pages checked, 0 problems + JS brace sanity check OK. RULE for future
  sessions: run `python3 tools/site_check.py` before every push. All 6 human blockers still
  open (day 9).
- **2026-08-17** (daily session 10): Added `thuisbatterij-wallonie-brussel.html` — completes
  Belgian coverage. Wallonië: prosumententarief 2026 forfaitair ±€76–86/kWe (ORES €85,84 ·
  RESA €85,93 · AIEG €76,45; CWaPE-approved), only for installations keured before 1-1-2024;
  proportional-tariff option with smart meter (€300–400 i.p.v. ±€550); post-2024 installations
  fall under injectieregime. Key insight documented: battery is worthless in the forfait
  regime, valuable in proportional/injection regimes. Brussel: groenestroomcertificaten
  (10 jaar), Homegrade loans, low injection. Interactive regime-checker (gewest + keuringsdatum
  + slimme meter → regime + battery advice). Cross-linked (index, Vlaanderen page, sitemap);
  QA: 16 pages, 0 problems. All 6 human blockers still open (day 10). Content backlog fully
  empty. Upcoming dated work: terugleverkosten refresh ±2026-09-08; Prinsjesdag btw-update
  after 2026-09-17.
- **2026-08-18** (daily session 11): QA automation. Extended `tools/site_check.py` with the
  inline-JS sanity check (balanced braces/parens per script block, JSON-LD excluded) and added
  `.github/workflows/qa.yml` so the full check runs in CI on every push touching site/ or
  tools/. Verified locally: 16 pages, 0 problems. All 6 human blockers still open (day 11).
  Sessions until ±sep 8 will be light holds unless the human unblocks — next substantive dated
  work is the terugleverkosten refresh (±2026-09-08), then the Prinsjesdag btw-update (after
  2026-09-17).
- **2026-08-19** (daily session 12): Light hold, as announced. Added a root `README.md` — the
  repo previously had none at top level (the existing one belongs to the lost-and-found app),
  so the project overview and the 6-step human unblock checklist are now the first thing
  visible on GitHub instead of buried in this file. QA green (16 pages, 0 problems). All 6
  human blockers still open (day 12). Nothing else touched — holding token budget for the
  ±sep 8 data refresh and the sep 17 Prinsjesdag update.
- **2026-08-20** (daily session 13): Data-integrity spot-check on the ISDE battery subsidy —
  the site's highest-stakes claim. Verified: subsidy still exists (€250/kWh, max €1.500;
  homeowner budget €416M for 2026; not exhausted per May/June sources; no August status
  findable via search — RVO site is behind the egress proxy). Real gap found and fixed:
  subsidie page now warns that the ISDE pot is first-come-first-served and jun–sep is peak
  season ("op = op") with advice to check RVO's budget page before signing. QA green
  (16 pages). All 6 human blockers still open (day 13).
- **2026-08-21** (daily session 14): Light hold. Extended `tools/site_check.py` with a
  non-fatal data-freshness detector: it parses each page's Dutch "peildatum" month-year
  mentions, takes the newest per page, and warns when it is >1 month old — so the ±sep 8
  refresh session (and every one after) gets an automatic list of stale pages instead of
  relying on log memory. Verified detector logic; QA green, zero warnings today (all pages
  dated aug 2026). All 6 human blockers still open (day 14).
- **2026-08-22** (daily session 15): Light hold. Added JSON-LD validation to
  `tools/site_check.py` — every application/ld+json block must parse as JSON and carry
  @context/@type, since a silent typo there kills rich results (the FAQ page and both
  calculators depend on this markup). All existing blocks valid; QA green, 16 pages,
  0 problems, 0 freshness warnings. All 6 human blockers still open (day 15). Next dated
  work unchanged: terugleverkosten refresh ±sep 8 (freshness detector will flag it),
  Prinsjesdag btw-update after sep 17.
- **2026-08-23** (daily session 16): Wrote `research/PRINSJESDAG-PLAYBOOK.md` — pre-drafted
  execution plan for the 17 sep btw-besluit on standalone batteries: three scenarios
  (approved / rejected / postponed) with headlines, key content, the exact pages and JSON-LD
  blocks to touch, a grep checklist ("Prinsjesdag|17 september"), and the rule to verify the
  real outcome before publishing anything. Makes the sep 17+ session execute-only — same-day
  coverage of the decision is the site's best SEO shot this year. All 6 human blockers still
  open (day 16).
- **2026-08-24** (daily session 17): CI health audit. Verified via the Actions API: Site QA
  workflow runs and passes on every push (4/4 success) — the QA gate is real. Pages deploy has
  failed on all 13 runs. Attempted self-service fix: added `enablement: true` to
  actions/configure-pages (workflow has pages:write). Result: it got further — tried to CREATE
  the Pages site — but GitHub refused with "Resource not accessible by integration": site
  creation needs repo-admin rights the workflow token doesn't get. CONCLUSION: Pages
  enablement is definitively human-only (blocker #1 confirmed, one click in repo Settings →
  Pages → Source "GitHub Actions"; deploy then auto-heals on next push thanks to the
  enablement flag staying in place). All 6 human blockers still open (day 17).
- **2026-08-25** (daily session 18): Light hold. Wrote `research/NIEUWSBRIEF-DRAFTS.md` —
  newsletter starter pack (welcome automation mail with the 3 core calculations, monthly
  saldering-countdown template, news-alert template for Prinsjesdag/ISDE/tariff moments,
  activation checklist incl. double opt-in/AVG). Third instantly-activatable asset next to
  the outreach pack and Prinsjesdag playbook. QA green. All 6 human blockers still open
  (day 18). Holding until terugleverkosten refresh ±sep 8.
- **2026-08-26** (daily session 19): Quiet hold — verified branch up to date, QA green
  (16 pages, 0 problems, 0 freshness warnings). No new work created by design: all
  activation assets exist and the next substance is dated (terugleverkosten refresh ±sep 8,
  Prinsjesdag playbook 17–18 sep). All 6 human blockers still open (day 19).
- **2026-08-27** (daily session 20): Quiet hold #2 — branch current, QA green (16 pages,
  0 problems). No changes. Next substance: terugleverkosten refresh ±sep 8, Prinsjesdag
  playbook 17–18 sep. All 6 human blockers still open (day 20).
- **2026-08-28** (daily session 21): Quiet hold #3 — branch current, QA green (16 pages,
  0 problems). No changes. All 6 human blockers still open (day 21).
- **2026-08-29** (daily session 22): Quiet hold #4 — branch current, QA green. No changes.
  In ~10 days the freshness detector starts flagging pages for the September data refresh.
  All 6 human blockers still open (day 22).
- **2026-08-30** (daily session 23): Quiet hold #5 — branch current, QA green. No changes.
  All 6 human blockers still open (day 23).
- **2026-08-31** (daily session 24): Quiet hold #6 — branch current, QA green. No changes.
  Last day of August: the terugleverkosten refresh is due ±sep 8. All 6 human blockers
  still open (day 24).
- **2026-09-01** (daily session 25): Quiet hold #7 — branch current, QA green. September has
  started: the monthly terugleverkosten refresh runs ±sep 8 as planned. All 6 human blockers
  still open (day 25).
- **2026-09-02** (daily session 26): Quiet hold #8 — branch current, QA green. No changes.
  All 6 human blockers still open (day 26).
- **2026-09-03** (daily session 27): Quiet hold #9 — branch current, QA green. No changes.
  Terugleverkosten refresh in ~5 days. All 6 human blockers still open (day 27).
- **2026-09-04** (daily session 28): Quiet hold #10 — branch current, QA green. No changes.
  All 6 human blockers still open (day 28).
- **2026-09-05** (daily session 29): Quiet hold #11 — branch current, QA green. No changes.
  Terugleverkosten refresh in ~3 days. All 6 human blockers still open (day 29).
- **2026-09-06** (daily session 30): Quiet hold #12 — branch current, QA green. No changes.
  Terugleverkosten refresh in ~2 days. All 6 human blockers still open (day 30).
- **2026-09-07** (daily session 31): Quiet hold #13 — branch current, QA green. No changes.
  TOMORROW: terugleverkosten data refresh (verify supplier tariffs, update peildatum on
  terugleverkosten-per-leverancier.html + check ISDE budget status). All 6 human blockers
  still open (day 31).
- **2026-09-08** (daily session 32): SEPTEMBER DATA REFRESH + MAJOR CORRECTION.
  (1) CORRECTION: the ISDE battery-subsidy claim published in August (€250/kWh, max €1.500,
  "per 1-1-2026") was MISINFORMATION circulating widely on affiliate sites — RVO states
  explicitly that thuisbatterijen do NOT fall under ISDE 2026 (which covers warmtepompen,
  zonneboilers, isolatie, ventilatie; budget €500M). Corrected on all 4 affected pages:
  subsidie-thuisbatterij.html rewritten as a debunk page with a visible rectificatie notice
  (title/meta/lead/table/warnings/checker JS all updated), FAQ answer + FAQPage JSON-LD
  fixed, zin-of-onzin bullet fixed, beste-thuisbatterijen pitfall #5 + Marstek row fixed,
  index link text updated. LESSON logged: affiliate-site consensus is not a source for
  subsidy claims — verify against RVO/official pages (via search snippets of the official
  domain when egress-blocked). The 0% btw-met-panelen claim and the Prinsjesdag motion were
  re-checked and still supported (VAT-refund route confirmed as a real alternative);
  Prinsjesdag playbook will verify outcomes against primary reporting before publishing.
  (2) ROUTINE REFRESH: terugleverkosten page updated to peildatum september 2026 —
  Eneco lowered from ±€0,18 to ±€0,134/kWh medio 2026; Budget Energie ±€78/jr at 2.500 kWh
  (staffel); Essent €276 and Vattenfall €215 unchanged; per-kWh range now €0,10–0,18 with
  movement note. QA green (16 pages). All 6 human blockers still open (day 32).
- **2026-09-09** (daily session 33): Small quality fix — moved the ISDE-mythe warning on
  thuisbatterij-zin-of-onzin.html out of the "wanneer zin" bullet list (a warning didn't
  belong there) into its own notice block. QA green (16 pages). Holding until Prinsjesdag
  playbook execution 17-18 sep. All 6 human blockers still open (day 33).
- **2026-09-10** (daily session 34): Quiet hold — branch current, QA green (16 pages,
  0 problems). No changes. Prinsjesdag playbook executes 17-18 sep. All 6 human blockers
  still open (day 34).
