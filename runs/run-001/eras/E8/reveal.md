# The Auditor: Audit and Forecast Score, Era E8 (Jan 2032 → Dec 2039)
*Call under review: **Clearwork**, "the neutral clearing house for delegated agent work." Its wedge is Clearwork Settle: mandate capture, a revision and acceptance log, and escrowed release against t+30/90/365 outcomes through a licensed partner, priced at 50–150 bps plus a per-mandate fee. It is sold vendor-side to agent vendors serving EU fund administrators and mid-market lenders. Certification is harvested, not sold. The exposure registry is licensed to a cat modeler. There is no answer key for this era, so every outcome below is a forecast. Tags: FACT(2026) / EXTRAPOLATION / SPECULATION, confidence H/M/L.*

## 1. Premise check (what the board stood on)
- **FACT(2026), H:** delegated-authority formats already exist, and payment networks own them. Google's AP2 (Sep 2025) uses signed intent and cart mandates. OpenAI and Stripe launched the Agentic Commerce Protocol (Sep 2025). Visa Intelligent Commerce and Mastercard Agent Pay (2025) tokenize agent payments. Microsoft Entra Agent ID (2025) issues agent identities. Victor's absorption warning points at real, shipping rails, not hypotheticals.
- **EXTRAPOLATION carried from the E8 briefing (M):** outcome pricing is the default, and multi-week agents are in use. Both are reasonable.
- **Stacked SPECULATION.** The thesis needs all of these at once: (a) multi-vendor plurality survives (the board's own estimate is 40%); (b) delayed-outcome clauses become common; (c) buyer and vendor dispute outcomes often enough to pay a third party; (d) outcomes can be attributed across chained agents (Lena: L-M); (e) human acceptance stays a legal or commercial requirement. Treating these as roughly independent at 0.4–0.7 each, the joint probability that the full wedge works as designed is **~10–15%**. The thesis is sturdier than that only because its fallbacks (data licensing, certification) are pre-wired.

## 2. Scorecard
| Criterion | Score | Why |
|---|---|---|
| Playbook consistency | **8** | Applies [E6] "a referee needs a mandate" (the contract is the mandate), [E7] "don't sell the funnel" (certification is harvested), [E2] voluntary vendor-side sale with a hub tripwire, and [E5] no balance-sheet risk. The absorption tripwire points at the likeliest substitute, as [E7] asks. |
| Plausibility | **5** | Mandate capture is buildable. Escrow on delayed outcomes is not a software problem. It needs buyers to accept locked-up payments, vendors to accept holdbacks, and both to accept a third party's attribution. $300M settled in year one assumes adoption at payment-rail speed for something that behaves like a trade-finance product. |
| Non-consensus-ness | **7** | Few people in 2026 frame agent work as a clearing problem. This is the org's most original thesis since E4. |
| Layer choice | **5** | Clearing houses are franchises (FACT, H, historical), but DTCC and CLS were built *by the incumbents who move the money*. A fee layer without float sits beside the rails, not on them. Value is more likely to pool with payment networks (conditional release), carriers (who hold the variance), and lab platforms (who hold the traces). |
| Science-fiction risk (10 = grounded) | **6** | No undemonstrated technology, but chained-agent attribution at t+365 is an unsolved measurement problem, and the whole revenue line depends on it. |

**Overall forecast score: 57/100**

## 3. Core-bottleneck confidence and kill case
**Confidence that "unprovable authority and disputed delayed outcomes" is a real, important, *separately monetizable* bottleneck by end-2039: ~30%.** The problem itself very likely exists (~70%). The doubt is whether it is sold as a neutral clearing service.

**Strongest kill case:** delayed truth is priced by whoever carries the variance, not by whoever records it. Buyers don't want escrow; they want a **warranty**. The vendor, or a carrier behind it, pays out if the migration fails at t+90. Once warranties are standard, the dispute becomes a claim, and claims are adjudicated by carriers on their own evidence standard (the OTel trace plus the vendor log). Meanwhile, payment networks add "conditional release" to AP2/ACP-style mandates as a free feature (an [E3] absorption: the network owner absorbs the measurement). Clearwork is left holding a better record than anyone needs. That is Carmen's and Elise's dissent together: the board walked away from the party that holds the loss.

## 4. Simulated outcome
**Base (~55%):** Settle signs 5 vendors in 2032, but settled value is lumpy. One large migration vendor provides ~45% of volume, so the hub tripwire fires in 2033. By end-2033: 7 vendors, ~$380M settled run-rate, and **criterion #1 is missed** (≥8 vendors, ≥$500M). Delayed-outcome clauses appear in ~8% of target contracts, so the need test passes narrowly. In 2034 a card network pilots cross-merchant conditional release on agent mandates and a top-2 lab bundles "outcome holdback" into its enterprise contracts. **The absorption tripwire half-fires.** The board executes it: Clearwork becomes a consequence-data and attribution-standards company. It licenses mandate × outcome data to two carriers and one lab, and it runs the acceptance protocol a Big-4 firm uses as the de facto audit standard. Certification revenue declines slowly. **2039:** ~$200–260M revenue, ~$3–4B value, a likely acquisition by an insurance-data or exchange group (Verisk-, ICE- or LSEG-type). The [E2] pattern repeats: useful, acquirable, not era-defining. This is the best-capitalized version yet.

**Bear (~30%):** plurality collapses into 3 lab-platforms (Ines's Consolidated scenario), outcome contracts settle on vendor telemetry backed by bundled E&O, and fewer than 5% of contracts carry delayed-outcome clauses. The need test fires in 2033. Settle is shut down after ~$70M of cumulative burn, and certification drifts to checklist prices. Sold 2035–36 for ~$0.8–1.5B. Human sign-off being dropped from safe-harbor rules (see E9 briefing) accelerates this.

**Bull (~15%):** a large correlated agent-loss event in 2033–34 (a model regression across thousands of finance deployments) leads regulators and carriers to require independent mandate and outcome records for high-risk agent work. Clearwork is the only neutral operator with history and becomes the DTCC-like utility, co-owned with carriers. Valued at $10–20B.

## 5. Lessons (full text in playbook.md, [E8-forecast])
1. A clearing house is built by the parties who move the money.
2. Stacked speculations multiply.
3. Delayed truth is priced by whoever holds the variance.
4. A 24-month kill gate is too slow for a network product.
