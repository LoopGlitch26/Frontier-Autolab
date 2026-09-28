# Board Decision: Era E9 (January 2040, forecast, final era)
*Present: Castell, Rao, Okafor, Weil, Hale. Tags: FACT(2026)/EXT/SPEC, confidence H/M/L. Start: E8 Auditor base case (EXT, M): Clearwork, consequence data and standards, ~$200–260M revenue, ~$300M cash (EXT, L).*

## 1. Transcript highlights

**Victor (Convergence Audit):** All three departments put the same two theses first: (A) agent surety/bonding as an MGA and (B) a replication and ground-truth exchange. [E4] says unanimity right after a reveal is a leakage alarm. The leak here is circular. The E8 Auditor wrote the kill case (warranties, carrier evidence standards), then wrote an E9 world that vindicates it. We are being graded on agreeing with our grader.

**Victor on (A), the perennial idea:** This is the guarantee idea for the fourth time. E6 deferred "guarantees" to end-2022. E7 made Assure an option "only if a carrier mandate materialises." E8 made it the "next capability" after Settle. [E2] says to suspect comfort. Is it finally time, or is it what we reach for whenever the referee loses?

**Jonah (invited):** The premise changed, not my preference. Safe harbors removed per-task sign-off (EXT, M).

**Victor:** "Premise changed" is what comfort always says. First, **crowding** ([E7-forecast]): the briefing says 1–2 specialist modelers already dominate agent liability, and in E8 we licensed our inventory data to a cat modeler and our outcome data to two carriers. What do we have that they didn't already buy? Second, **a fee MGA is not the variance holder**. On fronted paper the carrier holds the loss and we take commission. That is a referee holding a binder. Third, **stability**: per-agent loss rates across monthly model updates may not be stationary enough to price (Lena's concern).

**Kofi (invited):** On crowding: the licensees got snapshots aggregated by deployer. We kept the live t+30/90/365 feed per agent *configuration*, and the perpetual contribution rights. Carriers still price per deployer, not per unit of authority (EXT, M).

**Lena:** If a model update resets the loss curve, per-agent pricing is worth no more than per-deployer pricing (SPEC, M).

**Tomas:** Victor's second point decides it. If we take no first loss, it *is* comfort. With a capped first-loss slice beside a co-owning carrier, we finally sit where [E5], [E6] and [E8] all point. And (A) is strongest in the slowdown branch (~25%): cheap open-weight agents at thousands of deployers with no risk function.

**Arjun:** Capped first loss at ≤15% of cash, a reinsurer sidecar for the rest, and a pre-agreed sale trigger for the acceleration branch.

**Victor on (B):** This is the ninth referee and the third clearing house. Labs and big pharma will integrate robotic cells. [E8-forecast] says clearing houses are built by the parties who move the money. Likely end state: a ~15%-margin CRO (EXT, L); premises ≈13%.

**Hana:** It is the only thesis that survives the acceleration branch (SPEC, L), and it is outside our data, which the [E4] reserved-slot rule demands. Lab operators co-own it from day one.

**Dev:** Neither thesis is code. (A) needs binding authority, a claims licence and adjudication on traces, which is ≤18 people in 18 months. (B) needs GLP-grade audit trails, which our ledger provides.

## 2. DECISION (CEO)

**Mira:** Here is the test. Comfort is (A) on the old terms: fees, no loss. Time means the E7 condition (a carrier mandate) is met in the projection (EXT, M) *and* we accept terms that scared us off in every earlier era. We take the second version; if first loss fails, we walk.

**Name:** **Clearbond** (renamed from Clearwork).
**Identity:** "The bonding house for agents that act without a human signature: we write the per-agent authority limit, take the first loss, and pay when the work fails."

**Reinvention thesis:**
- **Capability:** quarter-long autonomous agents (EXT, M).
- **Adoption:** safe harbors remove per-task sign-off and put liability on deployers and their insurers (EXT, M). Agent liability is a large premium line (EXT, M; size L).
- **Bottleneck:** nobody can size or transfer the loss *per agent configuration* as authority grows. Carriers use blunt per-deployer sublimits.
- **Layer we own:** delegated underwriting and claims authority, as an MGA with capped first loss. Capacity comes from one co-owning carrier plus a reinsurer sidecar.
- **Data:** bond × authority used × model version × claims × payout. Our own loss triangles, unlicensable.
- **Next capability:** dynamic authority pricing, meaning a live credit line per agent that tightens after a model update or drift. The bond becomes the agent's credit rating (SPEC, L-M).

**Premise count ([E8]):** safe harbors (0.6) × carrier grants authority and co-owns (0.5) × per-configuration pricing wins (0.6) ≈ **18%**. Fallback (data licensing to the co-owner) is funded as the base case.

**KILL:** Clearwork Settle and escrow; the acceptance protocol as a product (open standard under Leo, regulated niches only); data-licence renewals to rival carriers and the cat modeler ([E7] "don't sell the funnel"); neutrality as identity.

**KEEP:** signed ledger and OTel trace-schema stewardship; per-configuration consequence history with perpetual contribution rights; re-test pipeline (→ re-rating trigger); consequence-science and reward-hack team (→ claims forensics); ~40 protocol vendors (→ distribution).

**Wedge:** *Clearbond Authority*. Per-agent authority-limit bonds plus E&O, bundled with the safe-harbor certificate. It is sold **vendor-side** to agent vendors in mid-market lending ops and fund administration, with the deployer as beneficiary. Voluntary ([E2]).

**First customer:** 3 vendors from the protocol, serving a regional lender under a finance safe harbor whose incumbent carrier quotes only a blanket sublimit. Capacity comes from our larger carrier licensee as fronting co-owner, with 15–20% equity in the vehicle ([E8] "flow-holders co-own").

**Reserved slot (15% of new-bet burn, funded, not watch-only):** *Clearbond Bench*, the replication-certificate exchange for agent-discovered materials claims. 2–3 robotic-lab operators co-own it. The first customer is a materials licensor.

**3-year plan:**
- **2040:** binding authority, 200 bound configurations, $50M of bonded authority.
- **2041:** $1B of bonded authority, a second capacity provider, loss ratio inside the pricing band.
- **2042:** dynamic re-rating live, and a second vertical (procurement or claims ops).

**Capital:** ~$300M cash (EXT, L). The MGA build is ~$25M/yr. First loss capped at $45M (≤15% of cash) in trust; no float. Bench is ~$6M/yr. We keep the data-licence harvest to the co-owner carrier (~$40M/yr, declining). No raise, and a 24-month floor.

**Kill criteria:**
1. **Month 6:** no signed binding authority with first-loss terms. If so, we remain a data licensor. A fee-only MGA is **prohibited** (the comfort tripwire).
2. **Month 12 liquidity gate:** at least $50M of bonded authority, at least 200 configurations, and no single vendor above 35% of premium.
3. Loss ratio above 85% for two consecutive quarters, or a model-update loss shock exceeding the re-rating model's band twice. Either one halts new binding.
4. **Acceleration trigger:** a lab-state compact self-insures more than 50% of target-sector agent work. If so, we run the pre-agreed sale process.
5. **Crowding:** our win rate against the specialist modelers stays under 20% by month 18.
6. **Bench:** fewer than 3 co-owning labs, or repeat demand under 25%, by month 12. If so, we close it.

**Org changes:** Jonah Reyes → CEO, Clearbond Underwriting, with two licensed external hires (Chief Underwriting Officer, Head of Claims). Kofi Mensah → Head of Authority Pricing. Elise Laurent → loss-ratio owner. Arjun Mehta → capacity, trust account, sale trigger. Carmen Ortiz → vendor distribution and carrier co-owner. Hana Kowalski → GM, Bench (Yuki Harada as science lead). Priya Nair → claims engineering and certification harvest. Leo Mbeki → open standards. Samuel Brandt and Ines Varga → Branch Desk (quarterly pace indicators). Victor Hale → Absorption Watch plus a new **Comfort Audit** with veto on any drift to fee-only.

**Dissent log:**
- **Victor:** "Time, conditionally. It's the first era with the E7 condition met, but met in our Auditor's projection. Score us on whether we actually took a loss by 2041."
- **Lena:** "Non-stationary per-agent losses could make us an expensive per-deployer pricer."
- **Hana and Leo:** Bench should lead in the base branch, because atoms bind progress and bonds don't.
- **Samuel:** "Lloyd's Register, the recorder, also endured. We may be leaving the durable seat."
- **Elise:** margin pools in power and compute, which we cannot enter small.
