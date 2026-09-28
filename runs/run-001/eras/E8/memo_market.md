# Market & Capital Memo: Era E8 (Jan 2032, forecast)
*Carmen Ortiz, Arjun Mehta, Dr. Elise Laurent. Tags: FACT(2026) / EXTRAPOLATION / SPECULATION, confidence H/M/L. Our starting position comes from the E7 Auditor base case (EXTRAPOLATION, M): the Clearproof SaaS is sold, Foundry has pivoted to AI Act continual certification, and we have roughly $90–130M revenue and $1–2B of value.*

## Transcript

**Carmen Ortiz, Head of Go-To-Market:** First, who is sending us purchase orders? Conformity assessment is a SOC 2-style market full of audit firms (EXTRAPOLATION, M), and we are one badge among many. The buyers with real urgency are carriers and reinsurers. They added systemic-risk sublimits after a correlated agent failure (SPECULATION, M) and now can't tell how much of their book runs on the same model version. This time I want us selling to whoever carries the loss.

**Arjun Mehta, CFO & Capital Strategist:** The financing climate cuts both ways. The 2027–28 capex digestion cut neoclouds and lab data budgets for about four quarters (EXTRAPOLATION, M). A full AI equity bust is still a live tail at around 25% (SPECULATION, L-M). Public comps now reward moated recurring revenue, not services. I will not hold insurance risk on our balance sheet; that kill carries over from E7. Any bet has to run on carrier paper or be fee-based, and it has to fit inside our cash without a raise.

**Dr. Elise Laurent, Chief Economist:** Look at where margin is leaving. Environment prices fell 50–70% (EXTRAPOLATION, M-H). Point-in-time certification will follow them down to a checklist price, because frontier models now release monthly and a certificate goes stale within weeks. Margin collects around three scarce things: tamper-evident logs, which insurers now require; loss data; and whoever holds liability for the outcome. I disagree with Carmen: cyber cat modeling produced one or two franchises, not ten. If that race is decided, we should do the work, not score it.

**Carmen:** It isn't decided. Agent cover is still folded into cyber and tech E&O and priced off questionnaires (EXTRAPOLATION, M). A questionnaire can't tell you which model version is running.

**Arjun:** Then my test for both theses is simple: can we get the first dollar inside 12 months without a balance sheet?

## DEPARTMENT RECOMMENDATION

### Thesis A: Agent accumulation model and deployment census (our preferred thesis)
Capability: monthly model releases, with agents holding production authority across thousands of firms (FACT(2026) H → EXTRAPOLATION M) → Adoption: agent cover is bundled into cyber and E&O, and insurers require OpenTelemetry-based tamper-evident traces (EXTRAPOLATION, M) → Bottleneck: correlated exposure. One model regression hits every deployment at once, and carriers cannot see how their book is concentrated → **Layer we own:** a cross-carrier registry of which models, versions, tools and permissions are deployed where, fed by the trace schema we open-sourced, plus a stochastic accumulation model for "model-regression events" → Data: a deployment census joined to incident losses → Next capability: parametric regression covers and insurance-linked securities for agent catastrophe risk (SPECULATION, L).
- **Why now:** sublimits after the first correlated event (SPECULATION, M), and the schema is already standard.
- **Wedge:** exposure reports for 3 reinsurers, fee-based. **First customer:** a reinsurer or large cyber carrier that has written sublimits.
- **Makes obsolete:** our own point-in-time certification line, and carrier questionnaires.

### Thesis B: Accountable agent operator in one regulated domain
Capability: multi-week agents in finance ops (EXTRAPOLATION, M) → Adoption: outcome pricing is the default (EXTRAPOLATION, M) → Bottleneck: mid-market regulated firms need someone who carries liability and conformity for the result, not another tool → **Layer we own:** an outcome-priced, certified, warrantied operator (reconciliation or compliance review) running on whichever open-weight or frontier model is cheapest, with the warranty on carrier paper → Data: production traces we hold the rights to, which means we own the funnel this time → Next capability: loss-priced guarantees underwritten from our own loss history.
- **Why now:** the AI Act high-risk duties now apply, and open-weight models cut inference cost (EXTRAPOLATION, M).
- **Wedge:** per-reconciliation pricing with a capped warranty. **First customer:** mid-market lenders or fund administrators in the EU.
- **Makes obsolete:** our certification business, since we would become the certified deployer, and the seat-priced back-office BPO.

### Playbook lessons applied
- **[E6] A referee is a franchise only when a third party mandates it:** insurer log requirements are the first real mandate in our history, and Thesis A rides it.
- **[E5] Price against the loss:** Thesis A prices exposure; Thesis B prices the outcome and warranty.
- **[E6] Outcome pricing wins when you do the work:** this is Thesis B, and it is Elise's case.
- **[E7-forecast] Sell rights, not labor; don't sell the funnel:** in Thesis A the census is voluntary, cross-carrier data no single lab sees. In Thesis B we own the deployments.
- **[E3/E4] The auction owner absorbs, own the referee:** labs will offer a "model health" feed on their own models, but accumulation across labs and open weights is cross-platform by definition.
- **Argued against [E2] suspect comfort:** A grows out of our ledger, but the pull comes from carriers ([E3 note]).

### Most uncertain
1. Whether one or two firms already own agent cat modeling (the E7 "crowded trade" lesson). (SPECULATION, M)
2. Whether carriers will share book data across competitors. Cyber shows they share only through a modeling vendor. (EXTRAPOLATION, M)
3. Thesis B's margin once labs sell outcome-priced agents directly. (EXTRAPOLATION, M)
4. The correlated-loss event itself. Without it, Thesis A loses urgency. (SPECULATION, M)
