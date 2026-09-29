# E7 live audit — September 2026

## Source-checked facts

IBM Research's CAP reports 20 case studies and a survey of 306 practitioners across 26 domains; its reported percentages describe that study's sample, not the whole market. Scale READY provides workflow-specific reliability qualification that accounts for human oversight and cost; its cited clinical-audit study is not a payment-dispute validation. Microsoft's maturity model emphasizes governed data/integrations, approvals, CI/CD, monitoring, and evaluation; this is guidance rather than evidence of buyer demand. [IBM CAP](https://research.ibm.com/publications/characterizing-agents-in-production) · [Scale READY](https://labs.scale.com/papers/reliable-enterprise-agent-deployment) · [Microsoft maturity model](https://learn.microsoft.com/en-us/agents/adoption-maturity-model/maturity-model-technology)

Competition is direct in the packet product: Stripe advertises Smart Disputes that can compile and submit eligible evidence; Chargeflow documents ingesting disputes, assembling evidence, and submitting responses. These are vendor claims/docs, not independent efficacy evidence. [Stripe dispute management](https://stripe.com/payments/dispute-management) · [Chargeflow automation](https://docs.chargeflow.io/docs/merchants/automation)

## Assessment

**FACT:** Reliability and human-oversight measurement are active areas; established vendors already perform dispute evidence automation. **EXTRAPOLATION (medium):** Workflow qualification could help a buyer compare reliability, human effort, and operating cost in a concrete dispute workflow. **SPECULATION (low):** An independent startup can win budget against internal QA, READY-style frameworks, and vendor-native tooling.

Caseground's pivot is directionally better than building a redundant packet tool, but it remains unvalidated and potentially services-heavy. The most important test is whether a named buyer will pay for the evaluation and use it to make a deployment or procurement decision. Its comparative advantage must be measured, not assumed.

## Scorecard (0–10; judge assessment)

| Dimension | Score | Rationale |
|---|---:|---|
| Playbook consistency | 8 | Retains human authority, explicit metrics, permissions, and buyer validation. |
| Plausibility | 6 | A manual evaluation is feasible; budget path is uncertain. |
| Non-consensus-ness | 5 | Workflow qualification is visible in current research and market offerings. |
| Layer choice | 6 | Measures workflow economics, but incumbents can bundle it. |
| Groundedness | 8 | Scope is narrow and forecasts are separated from sourced facts. |

**Total:** 66/100 (subscores × 2), subjective. Confidence the need for workflow-specific reliability/oversight evidence remains important: **70%**; confidence this independent startup captures the value: **25%**. Base case is a niche evaluation service that may productize. Bear case is consulting with sensitive-data burden and no recurring budget.

## Playbook update

1. A strong technical signal can strengthen a problem hypothesis without proving a buyer.
2. Test against incumbent substitution early; a useful feature may already be bundled.
3. Evaluate the whole human/tool workflow at buyer-defined error and cost targets.
4. A manual evaluation service does not prove repeatable software economics.
