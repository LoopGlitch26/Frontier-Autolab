# Market & Capital Memo: Era E7 (28 September 2026, live)
*Carmen Ortiz (Head of GTM), Arjun Mehta (CFO), Dr. Elise Laurent (Chief Economist). Live era. Every claim is tagged **FACT** (public reporting, with confidence), **EXTRAPOLATION** (a trend carried forward) or **SPECULATION**.*

## Meeting transcript

**Dr. Elise Laurent, Chief Economist:** Apply [E5] literally. The scarcest inputs are compute and power ($89B quarterly Nvidia data-center revenue; $650–730B capex; FACT, high), and we can't touch them. Two we can reach: verified long-horizon tasks (METR: only 5 of 228 tasks exceed 16 hours; FACT, high) and loss data on what agents break. Intelligence gets cheaper (100× price spread); liability doesn't. Margins move to whoever prices the loss.

**Carmen Ortiz, Head of GTM:** Who pays first? Insurers. ISO/Verisk generative-AI exclusions entered liability renewals on 1 January (FACT, medium-high). About six specialist carriers launched agent covers this year; AIUC reportedly has Beazley paper and AIUC-1 audits run through the CSA registry (FACT, medium; trade sources). None holds years of signed agent actions tied to outcomes. We do. That is the mandate [E6] said the referee lacked: the insurer requires the audit before it binds cover.

**Arjun Mehta, CFO:** We have ~$110M cash, ~$45M ARR and ~$10M/yr burn. Our category is being bought now: Galileo→Cisco, Langfuse→ClickHouse, Promptfoo→OpenAI (FACT, high). H1 venture was $510B and an Anthropic roadshow is reported for October (FACT, medium). [E4] says sell on the credit calendar, which is open today and may not be in 2028 (EXTRAPOLATION). Carmen, I won't bear risk on our cash. We act as MGA or data partner on someone else's paper, or not at all.

**Carmen:** Agreed. The carrier holds the risk. We own pricing and the evidence.

**Elise:** I disagree on priority. [E6] says to ask who pays most for an input. Labs pay billions for judgment: Mercor passed $2B ARR and Surge made $1.2B in 2024 (FACT, high). Our evaluation scientists can build verified environments longer than 16 hours. Insurance is the franchise we'd hold in 2032. Selling tasks to labs is the cash business for 2027.

**Arjun:** Selling to labs is a concentrated-buyer business. Scale lost OpenAI overnight (FACT). I'd fund it as a cash engine and not make it the identity.

## DEPARTMENT RECOMMENDATION

### Thesis A (lead): Price the agent's loss. Underwriting evidence and an MGA for autonomous agents
**Capability** agents reliably run tasks of 16 hours or more, with horizons doubling every ~4 months (FACT/EXTRAPOLATION, medium) → **adoption** enterprises let agents act: code, payments, support refunds, procurement → **bottleneck** nobody can price the tail. Policies exclude AI, boards won't sign off without cover, and the AI Act's high-risk duties land in Dec 2027 and Aug 2028 → **layer we own** the loss-pricing layer. Signed agent-action ledgers plus audits in the AIUC-1 style feed an MGA pricing model, which runs on carrier paper → **data** agent configuration × action trace × incident × claim, pooled across insureds (a claims triangle for agents) → **next capability** capital-light warranties per agent, and priced autonomy limits: an insurer-set "how much can this agent do unsupervised" that gets written into contracts.
- **Why now:** the exclusions (Jan 2026) created the gap, and carriers are entering without loss history. The window to become their data layer is about 2–3 years (EXTRAPOLATION, medium).
- **Wedge:** "Clearproof Assure." It turns an existing customer's traces into an underwriting file and a quote with a partner carrier. It is priced as a share of premium and a per-agent audit fee, not per seat ([E5] price against the loss).
- **First customer:** 10–20 mid-market customers running agents for support refunds or code deployment, sold together with one specialist carrier or MGA.
- **Makes obsolete:** our own seat-priced evaluation dashboard, which becomes a free intake funnel.

### Thesis B (cash engine): Verified long-horizon environments sold to labs
**Capability** horizons exceed what suites can measure → **adoption** labs need multi-day tasks for RL and safety sign-off → **bottleneck** verified tasks, graders, experts → **layer** environment and grader supplier (the Surge path missed in E6) → **data** how agents fail → **next capability** failure-mode priors for Thesis A's pricing.
- **Why now:** suites are saturating, and sandbox escapes make hardened environments worth a premium (FACT: GPT-5.6 Sol incident, per OpenAI).
- **Wedge:** 50 trust, fraud and compliance environments of 16–100 hours, built from our 2013–19 corpus with the required rights.
- **First customer:** one frontier lab plus a government AI safety institute.
- **Makes obsolete:** the Clearsight moderation book (harvest it or sell it).

### Where value pools, 2026–2032
- **Compute, power, labs:** largest pool, closed to us (high).
- **Agent-commerce auction owners** (Visa/Mastercard agent tokens, assistant checkout, x402 >169M payments): they bundle single-rail fraud scoring ([E3]) (EXTRAPOLATION, medium-high). Stablecoin rails have no chargeback, so a cross-rail dispute referee is an option (SPECULATION).
- **Loss pricers:** small today; a standing cost of every agent deployment by 2032, as cyber insurance became (SPECULATION, medium-low).

### Playbook applied
[E5] price against the loss. [E6] referee needs a mandate (insurers and AI Act supply it). [E6] sell scarce judgment upstream (Thesis B). [E4] credit calendar: open an optional sale process for the evaluation/observability line now (floor ~$400M) and keep the ledger. [E5] don't clock the referee: the ledger is not included in any sale. **Argued against:** [E6] "outcome pricing wins when you do the work." Taking the tail risk counts as doing the work.

### Most uncertain about
1. **Absorption risk.** Labs or hyperscalers may warrant their own agents, the way Stripe Radar bundled fraud scoring. That would repeat [E3]. Tripwire: a top-3 lab offers indemnity for agent actions. If that happens, we become their loss-data vendor.
2. **Loss frequency.** Serious agent incidents may be too rare or too correlated to insure before 2028.
3. **Our own convergence.** The memo leans on our own ledger asset. [E2] suspect comfort applies.

Sources: [Zylos, agent liability stack](https://zylos.ai/research/2026-07-10-ai-agent-liability-insurance-underwriting/); [The Insurer, AIUC/Beazley](https://www.theinsurer.com/ti/news/exclusive-ai-insurance-mga-aiuc-secures-beazley-paper-for-liability-product-2026-05-15/); [Fenwick, "silent AI"](https://www.fenwick.com/insights/publications/end-silent-ai-emerging-ai-exclusions-coverage-fragmentation-and-practical-implications); [Forbes, agent payments](https://www.forbes.com/sites/digital-assets/2026/06/07/visa-mastercard-and-coinbase-are-fighting-over-how-ai-agents-pay/).
