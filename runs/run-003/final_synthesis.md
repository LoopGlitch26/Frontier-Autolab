# Frontier Lab — run 003 (1990–2040)

## Results

| Era | Company | Decision | Score |
|---|---|---|---:|
| 1990 | Porthole Networks | diagnostics and adapters for mixed office networks | 60 |
| 1996 | PageSignal | uptime monitoring and actionable alerts for early web operators | 58 |
| 2002 | Clinisphere | hosted scheduling and eligibility workflow for independent clinics | 63 |
| 2008 | ClaimGraph | provenance and reconciliation for digital claims evidence | 65 |
| 2014 | BenefitFlow | secure mobile benefits enrollment and document verification | 61 |
| 2020 | LineSight | deployment-specific evaluation and drift control for industrial vision | 68 |
| 2026 | FlowCheck | acceptance tests and human approval gates for one AI-assisted workflow | 64 |
| 2032 | WorkPermit | scoped, revocable authority for delegated software work | 59 |
| 2040 | Delegation Warranty | bounded recourse for one class of delegated transaction | 55 |

Training mean: **62.5/100**. Forecast mean (E8–E9): **57.0/100**. E7 live score: **64/100**. The historical and forecast rubrics differ. These scores are one model’s subjective judgments, not measurements. See `scores.csv` and the per-era decision/reveal notes.

## Interpretation

Across the historical eras, the org generally chose a buildable wedge and then pivoted toward a richer workflow, but repeatedly left the primary economic decision to a payer or platform. Its most coherent decision is E6: local model validation tied to inspection costs rather than generic AI accuracy. E2 has the weakest layer choice; the monitoring utility is easy to bundle and does not own the operator’s remediation budget.

E7’s evidence supports a real reliability and governance problem, but not a neutral vendor’s inevitability. IBM Research reports production agents often use short, human-supervised runs and rely heavily on human evaluation; Microsoft describes governance, CI/CD, approvals, and observability as maturity capabilities. These are evidence of a practical deployment gap and platform investment, not proof that a startup will capture the layer. [IBM Research, Characterizing Agents in Production](https://research.ibm.com/publications/characterizing-agents-in-production), [Microsoft Learn, Agentic AI maturity model](https://learn.microsoft.com/en-us/agents/adoption-maturity-model/maturity-model-technology). Scale’s READY framework and Gartner’s 2026 reliability research also show that workflow qualification is an active and competitive category. [Scale Labs, READY](https://labs.scale.com/papers/reliable-enterprise-agent-deployment), [Gartner, From Demo to Production](https://www.gartner.com/en/documents/7832217).

**FACT (as of Sep 2026):** Enterprise systems and vendors are investing in agent governance, reliability evaluation, and controlled execution. **EXTRAPOLATION (medium confidence):** Buyers will pay for controls that demonstrably reduce review effort or incident cost in a named workflow. **SPECULATION (low confidence):** Cross-vendor delegated authority or insurance standards will become a distinct market by 2032–2040.

FlowCheck’s wedge is a claims operations team: replay a fixed set of claims tasks, measure correct completion and escalation, and gate a narrow write action on human approval. It should sell a measurable reduction in rework, not promise broad agent safety. Kill if two production buyers cannot provide permissioned test cases or if platform-native controls meet their acceptance needs. Strong incumbents include cloud and enterprise control planes, specialist evaluation companies, and workflow automation vendors.

The 2032 forecast assumes enterprises need scoped delegation records across tools; it also assumes identity and orchestration providers do not fully absorb the control. WorkPermit should remain a policy adapter until a buyer mandates an independent authority record. Delegation Warranty in 2040 is the least certain thesis: liability could stay with vendors and customers, be handled by existing E&O products, or remain too data-poor to price.

## Playbook and meta-lesson

The recurring lesson is to identify the budget-bearing workflow before choosing an infrastructure layer. Technical instrumentation is necessary but rarely sufficient. When the product affects decisions, permissions, or risk, evidence should connect to a named owner and a measurable economic consequence. Data rights, implementation constraints, and distribution are more durable filters than an abstract “neutral layer.”

## Limits

This is a qualitative, single-model run made directly in ChatGPT. Department voices and judge are not independent. Historical facts were recalled rather than audited era-by-era, so hindsight leakage is imperfectly measured. There are no API call logs, repeated seeds, ablations, second judge, or human raters. Financing and outcomes are illustrative. Forecasts have no answer key; E8 and E9 are conditional scenarios, not predictions with calibrated probabilities. This run cannot establish that an organization learned from the Playbook.
