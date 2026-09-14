# Prinsjesdag-playbook — btw-besluit losse thuisbatterijen (15 sep 2026)

Context: the Tweede Kamer motion of 10 June 2026 asked the government to investigate 0% btw
for standalone home batteries (currently 21%; batteries installed with panels already get 0%).
The minister promised clarity by Prinsjesdag, **15 September 2026** (date verified 13 sep
against koninklijkhuis.nl — third Tuesday of September; the earlier "17 september" in this
repo was wrong and has been corrected site-wide). This is the niche's biggest news moment
of the year. Timing: the daily session fires 07:00 UTC (09:00 CEST) but the Miljoenennota/
Belastingplan publishes ~15:15 CEST — so the 15 sep session can only pre-check leaks, and
the **16 sep session executes this playbook**. Verify the actual outcome first (search
"Prinsjesdag 2026 btw thuisbatterij besluit"); do not publish any scenario without
confirmation from primary reporting (Rijksoverheid/Belastingplan coverage), never from
affiliate sites.

## Pre-Prinsjesdag intelligence (checked 13–14 sep 2026)
- The decision moment is a **Kamerbrief/onderzoeksuitkomst**: the minister (Klimaat en Groene
  Groei) must inform the Kamer by Prinsjesdag about the 0%-btw investigation (motie 10 jun).
  Solar Magazine (trade press): the study puts the cost of scrapping btw at **€1–2 mld**
  in an optimistic scenario (basisscenario ~600.000 batterijen in 2027); two routes were
  studied — btw-teruggave (like pre-2023 panels) vs a true nultarief (simpler for consumers,
  structurally hundreds of millions more expensive). The high price tag makes an unconditional
  Scenario A less likely; a conditional, postponed, or teruggave-route outcome is plausible.
- **WARNING**: affiliate sites (thuisbatterij-gids.nl and others) are ALREADY presenting
  "kabinet stuurt wetsvoorstel, 0% per 1-1-2027" as settled fact. That is the ISDE pattern.
  Do not source the outcome from any affiliate/installer site. Acceptable sources: search
  snippets of rijksoverheid.nl / tweedekamer.nl / belastingdienst.nl (has a "Thuisbatterij
  en btw" page — check it post-besluit), NOS/FD/Solar Magazine reporting that quotes the
  Kamerbrief or Belastingplan directly. If sources conflict, publish Scenario C language
  (onderzoek loopt / besluit volgt) — never a premature "het is rond".

## Pages to touch in every scenario
1. `subsidie-thuisbatterij.html` — the "Losse batterij" table row + warning #2 ("Wacht je op
   de btw-uitspraak?") + the checker's `nee`-branch tip. Update peildatum to september 2026.
2. `veelgestelde-vragen.html` — FAQ "Hoeveel btw betaal ik op een thuisbatterij?" (both the
   visible answer and the JSON-LD block — keep them in sync; QA validates JSON).
3. New news article `btw-thuisbatterij-besluit.html` (add to index "Verder lezen" + sitemap).
   Skeleton below; headline per scenario.
4. `research/OPERATIONS.md` log entry.

## Scenario A — 0% btw approved for standalone batteries
- Headline: "0% btw op losse thuisbatterijen: dit scheelt je honderden euro's"
- Key content: effective date (check! likely 1 jan 2027 or immediate), saving ±€800 on an
  average battery, interaction with ISDE (probably unchanged: still requires new panels),
  advice flips from "wachten kan lonen" to "de rem is eraf — maar check de ingangsdatum
  vóór je tekent; installatie vóór de ingangsdatum = alsnog 21%".
- Calculator hint update in `thuisbatterij-calculator.html` price field ("Richtprijs 2026:
  €400–650/kWh" → adjust if incl. btw guidance changes).

## Scenario B — 0% btw rejected
- Headline: "Geen 0% btw op losse thuisbatterijen: dit betekent het voor je aankoop"
- Key content: 21% blijft; the battery-with-new-panels route (0% + ISDE) becomes relatively
  MORE attractive — worked example comparing loose battery vs battery+panels package;
  remove all "wachten kan lonen" language site-wide (grep for "Prinsjesdag").
- Tone: no drama — the base case in all our calculators already assumed 21%.

## Scenario C — postponed / investigation continues
- Headline: "Btw-besluit thuisbatterijen uitgesteld: wat nu?"
- Key content: new expected date if named; advice: don't postpone a purchase indefinitely
  for an uncertain discount — compute the break-even ("waiting X months costs you Y in
  missed savings vs ±€800 potential btw-voordeel", use €400–700/yr savings figure).
- Keep the "Prinsjesdag" mentions but update them to the new date.

## Grep checklist (all scenarios)
`grep -rn "Prinsjesdag\|15 september" site/` — every hit must be updated or consciously kept.
Run `python3 tools/site_check.py` before push (JSON-LD sync check will catch FAQ mismatches).
