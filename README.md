# BatterijWijzer 🔋

An independent Dutch-language calculator site about home batteries and solar panels for the
Dutch and Belgian markets, built and maintained autonomously by Claude in daily one-hour
sessions on branch `claude/dutch-belgian-market-research-cmxwyh`.

**The hook:** the Dutch salderingsregeling (net metering) ends 1 January 2027, which makes
every pre-2025 solar/battery calculation wrong. BatterijWijzer computes the *new* math —
honestly, with all assumptions visible.

## What's here

| Path | What |
|------|------|
| `site/` | The site: 14 public pages, 8 interactive calculators/tools, NL + all 3 Belgian gewesten. Static HTML/CSS/JS, no dependencies. |
| `research/NL-BE-MARKET-RESEARCH.md` | The market research this is based on ($100/day target, monetization models, unit economics). |
| `research/OPERATIONS.md` | Runbook + daily log — read this first for current status. |
| `research/OUTREACH-EMAILS.md` | Ready-to-send installer outreach pack (direct lead sales at €35–50/lead). |
| `tools/site_check.py` | QA gate (links, meta, sitemap, inline JS) — runs in CI on every push. |
| `.github/workflows/` | `deploy-site.yml` (GitHub Pages) and `qa.yml` (site checks). |

## ⚡ To make it live and earning — 6 human steps

Everything below is blocked on account/payment actions only a human can take
(full details in `research/OPERATIONS.md`):

1. **Enable GitHub Pages**: Settings → Pages → Source "GitHub Actions" (~1 min → site is live)
2. **Buy a domain** (~€10/yr): e.g. batterijwijzer.nl → set as Pages custom domain
3. **Form endpoint**: free Formspree form → paste URL into `LEAD_ENDPOINT` in `site/offerte.html`
4. **Affiliate signups**: Solvari, Slimster, Daisycon (identity + IBAN required)
5. **Sender email** at the domain → the outreach pack in `research/OUTREACH-EMAILS.md` goes out
6. **When revenue starts**: KVK (NL) or bijberoep (BE) registration

Revenue model: lead generation (€35–50/exclusive lead direct to installers; €7–25 via quote
platforms) + Daisycon energy/insurance affiliate + eventual digital products. See the research
report for the full unit economics.

---

*This repository also contains an unrelated lost-and-found application in `lostandfound/`
(its own README lives there).*
