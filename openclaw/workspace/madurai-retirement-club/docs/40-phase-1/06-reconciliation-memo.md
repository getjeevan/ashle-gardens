---
tags: [ashle-gardens, reconciliation, action-items, ceo-review]
status: open
created: 2026-07-07
source: full vault audit, 2026-07-07
---

# 🔧 Reconciliation Memo — Open Contradictions

> [!summary] Full-vault audit found 9 unresolved contradictions and a lapsed sprint with no retro. This memo lists each as a decision item: what conflicts, where, who owns it, and what "done" looks like. Nothing here should block Phase 1 further without a call on at least items 1–4.

## How to use this
Each item needs one of: **(a) pick a number and update every file**, **(b) merge/rewrite conflicting docs**, or **(c) explicitly defer with a reason**. Check the box when closed and note the resolution inline.

---

## 1. Land acreage — 7 different figures, no single source of truth
- [ ] **Conflict:** 30–40 acres (vision, [[CLAUDE.md]]) vs. **4.595 acres legally documented** ([[Land Documents Summary]]) vs. 40 acres treated as settled ([[Water Budget]]) vs. 15 acres organic farm ([[Organic Farm Design]]) vs. 15 acres Phase 1 footprint ([[Phase-1-Master-Site-Plan]]) vs. 10 acres Phase 1 footprint ([[Phase-1-Sprint-CEO-Coordination]]) vs. 1.5 acres farm within Phase 1 ([[Phase-1-Circular-Economy-Integration]]) vs. 8 acres farm ([[Unit Economics]]) vs. 2–3 acres vs. 2.5 acres for the Temple attraction (two different files).
- **Owner:** Rajan-Anna (land status) + Meera (site plan)
- **Decision needed:** Is 4.595 acres the only land currently owned/actionable, with 30–40 acres purely aspirational (future acquisition)? If so, every Phase-1 planning doc built around 10–15 acres is currently unbuildable on owned land and needs a footnote or a land-acquisition milestone gating it.
- **Also flags:** unresolved "D2002/6" legal notation in [[Land Documents Summary]] needing Tahsildar-office investigation before any registration proceeds.

## 2. AAI airport-distance conflict (regulatory-material)
- [ ] **Conflict:** 12.7 km from IXM Airport ([[CLAUDE.md]], [[Project Overview]]) vs. ~45 km ([[Approvals Master List]]).
- **Owner:** Rajan-Anna
- **Decision needed:** AAI NOC is only mandatory within 20 km. This isn't cosmetic — it determines whether the AAI NOC workstream (currently active for the Temple structure) is required at all. Confirm the real distance from a single authoritative source (site coordinates 9.7212°N, 78.0852°E vs. IXM coordinates) and correct whichever file is wrong.

## 3. Business unit count — 10, 11, 12, or 13?
- [ ] **Conflict:** CLAUDE.md/[[Project Overview]] say 12 (includes Pet Spa). [[🏡 Ashle Gardens MOC]] says 11 (Pet Spa omitted — added May 16, never backfilled). [[Unit Economics]] uses a 10-unit taxonomy with non-overlapping names ("Cottage Residences," "Spa & Wellness Centre"). The **Cambodian Temple Attraction** (added June 6, has its own CAPEX/revenue/sprint ownership) isn't in any of the three lists.
- **Owner:** CEO (you) — this is a naming/canon decision, not research
- **Decision needed:** Pick one canonical numbered list (recommend: 12 units + Temple as an explicit 13th, since it now has independent P&L). Update the MOC and Unit Economics.md to match. Ayurveda Spa and NRI Concierge have zero dedicated files — either commission them or mark explicitly "not yet scoped."

## 4. Two irreconcilable master financial models
- [ ] **Conflict:** [[Agile CAPEX Plan]] totals ₹10–14 Cr. [[Unit Economics]]'s own consolidated table sums to ₹46.2–55 Cr. Neither references the other.
- **Owner:** Karthik (CFO)
- **Decision needed:** These aren't close enough to be rounding — one is missing whole line items or one is double-counting phases. Needs a single reconciled CAPEX table with a visible bridge (what's in the 46–55 Cr figure that isn't in the 10–14 Cr figure, e.g. full 30–40 acre buildout vs. Phase 1 only).

## 5. Laundry TAM math error (internal, not just cross-file)
- [ ] **Conflict:** [[Laundry — Market Sizing]] executive summary claims 19,200–21,500 kg/day / ₹1.40–1.57 Cr/yr revenue. The file's own detailed table sums to 7,404 kg/day / ~₹54L — ~3x off from its own supporting data.
- **Owner:** Anbu (Laundry) + Karthik
- **Decision needed:** Recompute the executive summary from the detailed table, or show what additional demand source justifies the higher figure. This number feeds the hospital SLA pitch — don't let 3x-inflated demand go into a contract conversation.

## 6. Laundry CAPEX — 3x spread across files
- [ ] **Conflict:** ₹1.2 Cr ([[Unit Economics]]) vs. ₹60–92L ([[Phase-1-CFO-Brief]]) vs. ₹1.92–3.44 Cr ([[Laundry — Equipment]]).
- **Owner:** Karthik + Anbu
- **Decision needed:** Likely a phase-scope mismatch (full build vs. Phase 1 partial) — confirm and label each figure with its scope explicitly rather than leaving bare numbers.

## 7. COE philosophy directly contradicts its own operational docs
- [ ] **Conflict:** [[COE — Philosophy]] (May 16) explicitly **rejects** a stipend-based apprenticeship model. [[COE — PMKVY Funding]], [[COE — ITI Partnerships]], and [[COE — Entity Structure]] (same week) build 500+ lines of operational planning **around exactly that stipend/PMKVY/NSDC model**.
- **Owner:** Sundaram (COE)
- **Decision needed:** This is the starkest direct contradiction in the vault — not a numbers mismatch but a rejected-then-adopted model. Either the Philosophy doc needs a superseding update explaining why stipend-based funding was adopted despite the earlier rejection, or the PMKVY/ITI/Entity docs need to be rewritten around a non-stipend structure. Cannot ship both as currently written.

## 8. Kitchen capacity and TNRERA unit counts
- [ ] **Conflict (kitchen):** 500 meals/day ([[Phase-1-CFO-Brief]], [[Phase-1-Sprint-CEO-Coordination]]) vs. 1,500 meals/day ([[Kitchen — FSSAI]], [[Kitchen — Layout]]).
- [ ] **Conflict (TNRERA units):** 54 units ([[TNRERA Registration]]) vs. 68 units ([[Heritage Room Program]]) vs. 20 units for Phase 1 ([[Phase-1-Sprint-CEO-Coordination]]).
- **Owner:** Selvi (Kitchen) / Meenakshi (Legal) + Meera
- **Decision needed:** Same phase-scope-labeling fix as #6 likely resolves both — confirm whether these are Phase 1 vs. full-build numbers and label accordingly.

## 9. Unverified climate citations
- [ ] **Conflict:** [[Climate Summary]] cites weatherbox.io, weatherworld.com, en.climate-data.org — but the file itself notes these were paywalled/restricted, meaning the cited figures were never actually confirmed against source data.
- **Owner:** Meera
- **Decision needed:** Low priority relative to 1–8, but flag any climate figure used in irrigation/water-budget sizing as provisional until re-sourced from IMD or a non-paywalled dataset.

---

## 10. Phase 1 Sprint (June 6 – July 4) has lapsed with no retro
- [ ] **Status:** Sprint end date passed 3 days ago. Every box in [[Phase-1-Sprint-CEO-Coordination]]'s 10-item success-criteria checklist is still unchecked. No completion/outcome note exists anywhere in the vault.
- [ ] **Related lapsed deadlines, same root cause:** [[Phase-1-CFO-Brief]] (MSME filing was due June 30), [[Phase-1-Master-Site-Plan]] (due June 20), [[Phase-1-Circular-Economy-Integration]] (due June 27), [[Phase-1-Brand-Strategy]] (due June 27), [[PROJECT_REQUEST_Temple_Costing_Opportunity]] (URGENT, due June 20).
- **Owner:** CEO (you) — needs a retro sync with all 10 agents before starting anything new
- **Decision needed:** Before any further planning work, get an actual status read from each Tier lead (Karthik/Deepa/Meera; Anbu/Selvi/Sundaram/Velu; Rajan-Anna/Priya/Meenakshi) on which of the 10 success criteria are actually done vs. stalled vs. abandoned. Given no evidence the agent infrastructure (OpenClaw/Ollama) was ever actually invoked (see [[🏡 Ashle Gardens MOC]] audit note), this retro may need to happen as direct human work rather than assuming agents already produced it.

---

## Priority order (suggested)
1. **#10** — get the sprint retro done first; it may make several other items moot or reveal they were already resolved verbally/elsewhere.
2. **#1, #3** — land acreage and BU count are foundational; every downstream financial and site doc inherits these.
3. **#4, #7** — the two model contradictions (financial, COE) are structural, not just labeling.
4. **#2** — AAI distance, quick to verify, regulatory-material.
5. **#5, #6, #8, #9** — labeling/scope fixes, lower effort once #1 and #3 are settled.
