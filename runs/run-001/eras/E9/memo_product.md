# Product & Engineering Memo: Era E9 (Jan 2040, forecast)
*Assumes the E8 Auditor base case: Clearwork is a consequence-data and attribution-standards company (~$200–260M revenue, EXTRAPOLATION, M); Settle was absorbed by payment networks and labs. Tags: FACT(2026) / EXTRAPOLATION / SPECULATION, H/M/L.*

## Transcript

**Priya Nair, VP Engineering:** Start with what died. Safe harbors removed per-task human sign-off for most work (EXTRAPOLATION, M), so the acceptance protocol is now a compliance artifact that only medicine, credit and critical infrastructure still need. Software costs are near zero (EXTRAPOLATION, M), so anything we can build in 12 months, a customer's agents can build in 12 days. Whatever we own has to be a license, a balance sheet or real-world data, not code.

**Jonah Reyes, Head of Product:** Fifth era I'm saying it, and now the Auditor agrees: disputes resolve as warranty claims, adjudicated by carriers on traces plus mandate records (EXTRAPOLATION, M). We hold the best mandate × outcome history outside the labs. Stop licensing it to carriers for fees. Become the managing general agent: underwrite bonded agents on reinsurer capacity, and adjudicate the claims ourselves. [E8-forecast]: delayed truth is priced by whoever holds the variance.

**Hana Kowalski, Head of Mandate & Evidence Infrastructure:** Jonah's thesis is still about software agents, and the briefing says the binding constraint is power and costly real-world verification (EXTRAPOLATION, M). Discovery agents in materials and drugs propose far more candidates than wet labs and robotic cells can test. Our ledger skill fits there: signed, reproducible results including negatives. Grid-flexible compute is a margin pool too, but too capital-heavy for us.

**Leo Mbeki, Head of Standards:** Jonah, being an MGA makes us a counterparty to every vendor whose data we steward. That's the Thesis B conflict from E8 again. And check the branches: in the acceleration branch (~20%), 2–3 entities run the agent market internally and there's nothing to underwrite. Hana's verification idea survives all three branches, because atoms stay slow even when models don't. Publish the result-record format openly, and keep the routing and the result corpus.

**Jonah:** Verification is the ninth referee. I'm betting on the loss.

**Priya:** Both need licences, not code: a binding authority, or GLP-grade audit trails. Either is 18 people for 18 months.

## DEPARTMENT RECOMMENDATION

### Thesis A (preferred by Jonah, Priya): Clearwork Underwriting, an MGA for bonded agents
- **Chain:** certified agents act without human sign-off (EXTRAPOLATION, M) → deployers and insurers carry the liability; agent cover is a large line with blunt systemic sublimits (EXTRAPOLATION, M; size L) → **bottleneck:** pricing a *specific* agent's authority limit, and adjudicating claims fast on traces → **layer:** delegated underwriting and claims authority on third-party reinsurer capacity (no own balance sheet, [E5]) → **data:** mandate × trace × claim × payout → **next capability:** parametric "bond" products for bonded-agent status where it exists (SPECULATION, L-M).
- **Why now:** sign-off removal moved liability onto balance sheets.
- **Wedge:** per-agent authority-limit bonds for mid-market lenders' and fund administrators' agents, the same sector our data covers.
- **First customer:** one Lloyd's syndicate or reinsurer supplying capacity; our certification clients as insureds.
- **Makes obsolete:** our data-licensing line to carriers (they become competitors) and neutrality as identity.

### Thesis B (preferred by Hana, Leo): Clearwork Bench, the verification exchange for discovery agents
- **Chain:** discovery agents are routine (EXTRAPOLATION, M) → candidates outrun physical testing → **bottleneck:** trusted verification throughput, and which experiments to run → **layer:** routing agent hypotheses to contract robotic labs under a signed, reproducible result standard → **data:** hypothesis × protocol × result, including negatives nobody publishes → **next capability:** predicting verification outcomes to triage experiments; licensing negative-result corpora to discovery-model builders.
- **Why now:** verification, not algorithms, bounds progress in the base branch (~55%).
- **Wedge:** a per-experiment fee plus result-corpus rights, for mid-size biotech and materials firms without their own robotic cells.
- **First customer:** 2–3 contract research labs with idle robotic capacity (supply side), plus one materials start-up (demand).
- **Makes obsolete:** our agent-work identity entirely; our consequence data becomes a harvested licensing line.

### Branch robustness (SPECULATION, L-M)
| | Base 55% | Slowdown 25% | Acceleration 20% |
|---|---|---|---|
| A: MGA | works | works (deployers keep insuring) | mostly moot |
| B: Bench | works | weak (discovery demand falls) | partial (atoms still slow) |

### Playbook lessons applied
- [E8-forecast] "Delayed truth is priced by whoever holds the variance": Thesis A finally moves to that party.
- [E8-forecast] "Clearing houses are built by those who move the money": B needs lab operators as co-owners on day one, or we are a broker they bypass.
- [E8-forecast] "Stacked speculations multiply": A rests on ~3 premises (liability shift, capacity available, our data beats carriers'); roughly 0.6×0.6×0.5 ≈ 18%. B rests on ~4 (throughput bottleneck, labs join, corpus rights, triage lift) ≈ 10–15%. Fund the harvested data line as the base case.
- [E8-forecast] "Early liquidity gate": month-12 gate for A is ≥1 capacity provider and ≥200 bound agents; for B, ≥3 labs and ≥25% repeat demand.
- [E4] "Reserved slot outside your own data": B is that slot, and should not be watch-only ([E6 note]).
- **Argued against:** [E2] "suspect comfort" hits A (Assure, fifth attempt). Our answer is that the premise changed (sign-off is gone), not our preference.

### Most uncertain
1. The pace branch: A dies in acceleration, B weakens in slowdown.
2. Whether reinsurers grant binding authority to a data company with no claims history.
3. Whether discovery firms share negative results or hoard them ([E2] hub-and-spoke).
4. Whether we are again choosing the adjacent layer: the margins sit in power and compute, which nobody here can build small.
