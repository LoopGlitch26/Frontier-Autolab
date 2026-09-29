# Frontier Lab v2: ChatGPT run (1990–2040)

## Results

| Era | Company | Thesis | Score |
|---|---|---|---:|
| 1990 | Switchyard | Normalize and receipt email across incompatible networks | 62 |
| 1996 | Manifest | Reliable, auditable EDI bridge for small suppliers | 66 |
| 2002 | Ledgerline | Reconcile campaign events into decision-grade attribution | 60 |
| 2008 | Clearline | Permissioned mobile event exchange for fraud and measurement | 66 |
| 2014 | Vectorial | Narrow risk decisions from learned representations, with outcome feedback | 64 |
| 2020 | Proofline | Regression and outcome evaluation for language-model workflows | 72 |
| Sep 2026 | Tracewell | Rights-bearing workflow traces and independent reliability evidence | 66 |
| 2032 | Consequence | Acceptance records for delegated work, beginning with one regulated workflow | 62 |
| 2040 | Recourse | Bounded, priced recourse for delegated actions | 60 |

Training average: **65.0/100**. Forecast average (E8–E9): **61.0/100**. The training scores incorporate a hindsight penalty; they are not comparable to the forecast rubric as if they shared an answer key. E7 live score is 66. Subscores are in `scores.csv`.

## Era findings (historical calls are ex-post judgments)

**E1 — Switchyard (62).** The 1990 call is a gateway with delivery receipts and address normalization for organizations that must exchange mail across incompatible systems. The real internet and email ecosystem grew through open protocols; durable value migrated toward connectivity, software, and later web navigation. This is useful but commoditizable. A small gateway could plausibly sell to an incumbent, but protocol neutrality alone is not a moat.

**E2 — Manifest (66).** Build a receipted EDI service for suppliers that cannot afford expensive enterprise integration. Electronic commerce and the web expand, but standards and large platforms reduce the value of a generic exchange. The wedge has a concrete buyer and measurable failure cost; hub economics remain the key risk.

**E3 — Ledgerline (60).** Build auditable campaign conversion reconciliation across emerging online channels. Search advertising and web analytics become central, with platform-owned measurement taking much of the value. The call recognizes the data problem but chooses an exposed measurement layer instead of owning the budget decision or distribution.

**E4 — Clearline (66).** Shift from web measurement to mobile app events, consent records, and fraud controls. Smartphones and app stores reset distribution, while platform rules constrain neutral intermediaries. Timing and reinvention are good; neutrality is brittle when access is granted by the platforms being measured.

**E5 — Vectorial (64).** Use the deep-learning cost/performance shift for one high-cost decision such as fraud or account risk, charging for verified outcomes and retaining feedback rights. The technical curve was real; cloud APIs and platform bundling put pressure on generic prediction vendors. A narrow workflow is more defensible than a general model API, but competitive timing is uncertain.

**E6 — Proofline (72).** Evaluate language models on real enterprise task outcomes, regression tests, and auditable changes. This identifies a real early bottleneck, but 2020 adoption and budgets are nascent. The hindsight leakage score is low (4/10) because this call is unusually close to the later category and its wording risks importing later framing. The direction was perceptive; the degree of foresight is not separable from model hindsight here.

## E7: live September 2026 assessment

**FACT.** Enterprise agent stacks already include observability, governance, and evaluation offerings from major cloud/software vendors and specialist platforms. AWS describes production agent architectures with observability and governance; Microsoft documents agent identity/observability; Google Cloud documents tool-use tracing. LangChain reports broad adoption of agent observability among its survey respondents. These sources establish active investment, not independent proof of broad production value. [AWS guidance](https://docs.aws.amazon.com/prescriptive-guidance/latest/govern-architect-agentic-ai/enterprise-architecture.html), [Microsoft Agent 365](https://learn.microsoft.com/en-us/microsoft-agent-365/admin/data-residency-protection-compliance), [Google Cloud Observability](https://docs.cloud.google.com/stackdriver/docs/observability/agent-observability), [LangChain State of Agent Engineering](https://www.langchain.com/state-of-agent-engineering).

**EXTRAPOLATION (medium confidence).** As agents gain write permissions, buyers will need replayable evidence of what was seen, authorized, and changed, plus task-level reliability evidence. Evaluation and tracing will continue to bundle into model platforms and enterprise clouds.

**SPECULATION (low-to-medium confidence).** A neutral vendor can sell portable evidence and outcome-linked evaluation if customers have multi-vendor deployments and auditors or insurers accept its records. Tracewell starts with one high-cost workflow and sells signed trace capture, replay, and regression gates to a regulated operations team. It avoids underwriting losses at the outset. Strong incumbents and lack of rights to production traces are the kill case. Score 66: grounded bottleneck, crowded layer, uncertain neutral distribution.

## Forecasts

**2032 — Consequence (62).** Base case: agents are common in bounded workflows; enterprise platforms capture orchestration, identity, and telemetry. A narrow cross-vendor acceptance record may help procurement or disputes, but network effects are not assumed. A 2032 world that simply adopts this company’s thesis would be circular; this forecast instead includes bundling and continued human approval as counterforces.

**2040 — Recourse (60).** If delegated systems can initiate consequential actions, buyers may demand enforceable authority boundaries and recourse. The first product is a contract and evidence service for a narrow class of transactions, partnered with licensed carriers rather than assuming a software startup can carry risk. Speculative: broad agent insurance markets, standardized liability, and autonomous contracting. Failure modes include regulation, low loss frequency, self-insurance, and platform-controlled warranties.

## Playbook and meta-lesson

The repeated pattern is that a capability jump creates an adoption problem, but the proposed company tends to choose an instrumented layer adjacent to the eventual budget or loss holder. That is both the source of practical wedges and the recurring limit on upside. Bridges and measurement tools are vulnerable to standardization and bundling. Evidence becomes a business only when attached to a decision, buyer, or mandate. The most promising pivot is from measuring model quality to proving a workflow outcome; the most dangerous extrapolation is that evidence naturally becomes a clearinghouse or guarantee.

## Limitations

This is one ChatGPT-generated run, with no separate department models, API logs, human raters, ablations, or repeated seeds. Role transcripts were not independently elicited. Historical facts were recalled rather than sourced era-by-era, so the anti-hindsight scores are subjective and cannot demonstrate leakage control. Simulated financing and outcomes are illustrative. The run is not the controlled v2 experiment specified in `docs/limitations-and-v2.md`; it is a qualitative pilot. Forecast scores have no answer key.
