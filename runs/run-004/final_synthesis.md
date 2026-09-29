# Frontier Lab — Run 004 synthesis

## Results

| Era | Company | Decision | Score |
|---|---|---|---:|
| 1990 | Switchyard Systems | Permissioned LAN-support casebook for one environment | 60 |
| 1996 | Switchyard Systems | Guided troubleshooting, with buyer and accuracy gates | 62 |
| 2002 | Switchyard Commerce Operations | Manual online-order exception triage | 62 |
| 2008 | Switchyard Commerce Operations | Permissioned merchant exception workflow, no connectors | 70 |
| 2014 | Switchyard Evidence Operations | Human-reviewed evidence packets for one dispute type | 70 |
| 2020 | Switchyard Evidence Operations | Rules-based packet completeness checking | 72 |
| 2026 | Caseground | Independent, workflow-specific qualification | 66 |
| 2032 | Caseground | Conditional paid manual acceptance testing | 68 |
| 2040 | Caseground | Conditional decision-linked evaluation | 66 |

Training mean: **66/100**. Forecast mean: **67/100**. E7 live score: **66/100**. Training and forecast rubrics differ; averages should be compared only within mode. All scores are subjective judge assessments, not measurements of company performance.

## What changed across the run

The company repeatedly narrowed its scope after the Red Team identified gaps between a technical feature and a paying workflow. It moved from local network support to merchant exception work, then to dispute evidence quality. In 2026, documented product competition changed the decision: Stripe and Chargeflow already offer dispute evidence preparation/submission. Caseground therefore pivots to testing whether a specific human-agent workflow meets a buyer's reliability, oversight, and cost targets. That independent evaluation opportunity is itself speculative, especially against internal QA and platform-native features.

The strongest recurring decision rule is to separate evidence quality from authority to decide. Later decisions measure completeness separately from material error, include human review/security/integration in cost, and require a second paying buyer before calling a workflow repeatable. Future boards add another test: whether the buyer uses the evaluation to change a real decision.

## Method and limits

Run 004 used separate persistent assistant contexts for Frontier Research, Product & Engineering, Market & Capital, and Red Team. Each department context voiced the named roles assigned to that department; it was not one independent context per named role. The root context wrote world briefings, board decisions, and Record/Auditor judgments. Thus all charter roles were represented, but Run 004 did **not** instantiate sixteen separately autonomous agents and does not expose or reproduce private chain-of-thought. This is a multi-context role simulation, not a controlled replication or evidence that the Playbook improves strategy.

For E1–E6, briefings were written with era cutoffs, but a model's historical knowledge cannot be erased; hindsight leakage scores are subjective. E7 sources are linked in its briefing and reveal; those sources describe studies/frameworks and current product documentation, not proof of Caseground demand. E8–E9 are conditional forecasts with no answer key, and E8 is not treated as observed history by E9. Funding and outcomes are illustrative. The opening capital constraint is a simulated $1.5M.

See [`README.md`](README.md), [`company_state.md`](company_state.md), [`playbook.md`](playbook.md), and the full per-era records under [`eras/`](eras/).
