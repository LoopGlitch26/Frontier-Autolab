# E7 Memo: Product & Engineering (28 September 2026, live era)
*Tags: **[F]** = fact (public reporting; "1 src" = single or secondary source), **[X]** = extrapolation, **[S]** = speculation. Confidence is H/M/L.*

## Transcript

**Priya Nair, VP Engineering:** Here is what we have: ~140 people, ~$110M in cash, an evaluation-science team, the signed action ledger, and an open-source SDK. We are not a lab and we never will be. What we can ship in 6–18 months is anything that turns *agent traces* into something a third party will pay for. [F, H] Task suites are saturating: METR puts Mythos Preview at ≥16h with only 5 of 228 tasks above that. [F, M, 1 src] Epoch reports that labs pay $200–2,000 per RL task, ~$20k–300k per environment and six to seven figures per quarter per contract, and that the hard part is preventing reward hacking. Our evaluation scientists have been doing exactly that work since 2020.

**Jonah Reyes, Head of Product:** I've dissented about guarantees for two eras. Now the market has created the mandate for me. [F, M, 1 src] ISO generative-AI exclusions for general liability took effect from January 2026. AIUC-1 pairs an audit with Lloyd's-backed cover. HSB, Testudo and Klaimee sell AI liability. [F, H] Moffatt v. Air Canada says "the AI did it" is not a defence. So every company that deploys an agent now holds an uninsured tail risk, and underwriters have no loss data. [E6] says a referee is a franchise only when a third party mandates it. Here the insurer is that third party.

**Hana Kowalski, GM Clearproof (infra lens):** The layer that becomes unavoidable is the *tamper-evident action record*: what the agent saw, what it called, what authority it had and what happened next. Observability tools store traces for debugging. Nobody stores them as *evidence* that a claims adjuster, a regulator (AI Act logging, OSA) or a court will accept. The ledger we built in 1996 is finally the product. [X, M] Once underwriters price per trace, which one secondary source already reports, the logging format becomes a de facto standard.

**Leo Mbeki, Head of Open Source & Developers:** I'm with Priya. [E6] was explicit: sell the scarce judgment to whoever trains. Jonah's plan needs insurers who move at insurer speed. Environments sell *now*. The danger is that 40+ startups, plus Mercor and Surge, are already selling them, and labs are bringing the work in-house. My compromise is to open-source the trace schema (built on OpenTelemetry GenAI conventions) so every agent framework emits our format. Real failure traces from insured deployments would then become the one environment supply that nobody else can fabricate.

**Priya:** Then that's the loop. Jonah's underwriting business produces the traces, and my environment business sells them.

## DEPARTMENT RECOMMENDATION

### Thesis A (lead: Jonah, Hana): "Agent Warranty": the underwriting referee for agent actions
- **Chain:** agents act for ≥hours with real authority [F, H] → enterprises deploy coding, support and ops agents with production privileges [F, H] → the risk can't be insured: carriers exclude AI, have no loss data, and deployers can't prove what their agent did [F, M] → **we own the signed trace-evidence and risk-scoring layer that carriers and MGAs underwrite against**. We take a premium share per certified agent and do not carry the risk in years 1–2 [X, M] → pooled incident and near-miss traces tied to claims outcomes [X, M] → trace-priced cover, then real-time authority limits that tighten when risk rises [S, L].
- **Why now:** the exclusions (Jan 2026), a Lloyd's-backed standard, and the first specialist carriers all arrived within 9 months. **Wedge:** "Warranty Pack" for vendors selling agents into enterprises: signed recorder, a 200-scenario adversarial pre-deployment suite, and an evidence file an MGA accepts. **First customer:** 10 of our existing evaluation customers who ship agents, plus one MGA partner. **Makes obsolete:** our own seat-priced evaluation dashboards, which Braintrust, Arize and the model owners already commoditize ([E6]: owners absorb evaluation).

### Thesis B (lead: Priya, Leo): "Failure Foundry": reward-hack-resistant environments from real deployments
- **Chain:** RL on verifiable tasks drives capability [F, H] → labs and neolabs buy environments at scale [F, M] → realistic long-horizon enterprise tasks with rewards that can't be hacked are the scarce input [F, M] → **we own environments built from consented, anonymised real agent failures** → graded trajectories and calibration of how hard each task is → "horizon extension" suites past 16h [X, M].
- **Why now:** suites are saturating and exclusive tasks earn 4–5× [F, M, 1 src]. **Wedge:** 50 enterprise-workflow environments (CRM, finance ops, deploy pipelines) sold to 2 neolabs. **Makes obsolete:** static evaluation benchmarks, including our published ones.

**Playbook applied:** [E6] mandate: insurers are the mandating third party. [E5] price against the loss: price against premium, not seats. [E6] sell upstream: B. [E4] own the referee: Hana. [E3] date against the incumbent: model owners will ship agent logs, but carriers won't accept a model owner grading its own model [X, M]. **Argued against:** [E3] reserved-slot warning. Both theses lean on last era's lessons, and Victor should audit that. We reserve 10% for a curve outside our data: cyber-restricted models and autonomous vulnerability markets (Glasswing).

**Most uncertain:** (1) Will carriers actually price on vendor evidence, or build it themselves (Munich Re/HSB) [S, L–M]? (2) Correlated agent failures (a single model regression) could make the risk uninsurable at any price [S, M]. (3) The consent terms needed to reuse customer traces for B [X, M].

*[A founder-specific sub-section was removed before publication.]*
