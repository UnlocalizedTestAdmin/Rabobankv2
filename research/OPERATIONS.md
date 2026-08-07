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
   - [ ] Terugleverkosten per leverancier: vergelijkingstabel (update monthly!)
   - [ ] Dynamisch energiecontract + thuisbatterij: hoe werkt het, voor wie
   - [ ] Thuisbatterij subsidie: stand van zaken NL (en BE premies per gewest)
   - [ ] Beste thuisbatterijen 2026: vergelijking op €/kWh, garantie, chemie
   - [ ] Thuisaccu en verzekering/brandveiligheid: waar je op moet letten
   - [ ] Belgische variant-pagina's (premies, digitale meter, capaciteitstarief)
   - [ ] FAQ-pagina (schema.org FAQ markup) per calculator
3. Technical backlog:
   - [ ] sitemap.xml + robots.txt
   - [ ] Schema.org markup (WebApplication voor calculators, FAQPage)
   - [ ] Open Graph tags + social preview
   - [ ] Cookieless analytics (e.g. GoatCounter free tier — needs human signup, ask once)
   - [ ] Nieuwsbrief-signup blok (needs provider signup — ask once)
4. Never: fake reviews, fabricated "test results", scaled thin AI pages (March 2026 spam
   update kills exactly that), or claims about prices/subsidies without a check.

## Log

- **2026-08-07**: Research report delivered. Site v1 built (7 pages, 2 calculators, lead funnel,
  privacy). Pages workflow added. Daily routine created. Human checklist published (6 items).
