# The Record: Reveal and Score, Era E6 (Jan 2020 – Aug 2026)
*Call under review: Clearproof. It chose a model-neutral evaluation and adaptation harness scored against real outcomes, with Clearproof Draft (graded appeal and support drafting, priced per resolved case) as the wedge. The moderation book ran for cash, guarantees were deferred to end-2022, compute was rented, and 5% went to a protein-structure watch. Tripwire: a model ≥10× Megatron doing tasks from prompts alone ends per-client fine-tuning. The board decision was written by the orchestrator. It is judged the same way.*

## 1. What actually happened

**Scale was the whole game, and the tripwire fired within five months.** Kaplan et al.'s scaling-laws paper appeared on 23 Jan 2020. GPT-3 (175B parameters, about 21× Megatron) followed on 28 May 2020 under the title "Language Models are Few-Shot Learners", and the OpenAI API beta opened on 11 June 2020. Criterion #2 fired almost to the letter. After that: Copilot (2021), ChatGPT (30 Nov 2022), GPT-4 (2023), reasoning models (2024–25) and agentic coding. METR time horizons reached ≥16 hours (Claude Mythos Preview, March 2026).

**Value pooled at compute, labs, expert data and agent apps.** Nvidia's data-center revenue went from about $3B a year (FY2020) to $89B in a single quarter (reported Aug 2026). Anthropic (founded 2021) was valued at $965B with a $47B run-rate by May 2026, and OpenAI at $852B in March 2026. The real "grading" business was selling human judgment *to labs*, not selling scores to enterprises. Surge AI (founded 2020, bootstrapped) had $1.2B revenue in 2024. Scale AI took a $14.3B Meta investment (June 2025), and Mercor passed $2B ARR (June 2026). At the application layer, Cursor was bought by SpaceX for $60B (June 2026). Support agents Intercom Fin ($0.99 per resolution, 2023) and Sierra (~$10B, 2025) won with *outcome pricing*.

**Evaluation and observability became a real but mid-sized layer, largely absorbed.** It had almost no buyers until ChatGPT. Then the category filled in: LangSmith (2023), Braintrust ($800M post-money, Feb 2026), Arize ($70M Series C, 2025), Patronus and Galileo. Model owners and platforms took the ground the board had flagged. OpenAI open-sourced Evals (Mar 2023). AWS Bedrock added model evaluation across third-party models (preview Nov 2023), which is criterion #3. Azure and Vertex added evaluation too. Exits were acquisitions: W&B to CoreWeave (~$1.7B, Mar 2025), Humanloop's team to Anthropic (Aug 2025), Statsig to OpenAI ($1.1B, Sept 2025), Langfuse to ClickHouse (Jan 2026), Promptfoo to OpenAI (Mar 2026) and Galileo to Cisco/Splunk (Apr 2026).

**Harm regulation arrived, late and uneven.** The EU DSA applied to very large platforms from Aug 2023 and to all platforms from Feb 2024; X was fined €120M. The UK Online Safety Act passed in Oct 2023, with duties from 2025. The EU AI Act entered into force Aug 2024, and its high-risk rules were pushed to Dec 2027 by the May 2026 omnibus. LLM-based moderation (OpenAI's free moderation endpoint, GPT-4 policy labeling in 2023) squeezed classifier vendors.

**The watch slot was the right curve at the wrong weight.** AlphaFold 2 won CASP14 (Nov 2020), led to Isomorphic Labs (2021), and won the 2024 Nobel Prize.

## 2. Scorecard

| Criterion | Score | Justification |
|---|---|---|
| Frontier accuracy | **8** | It saw pretraining and generation as the curve and named few-shot generalists as a scenario. It treated scale as one scenario among three instead of the base case, and it missed RLHF, where graded human judgment became a training input. |
| Timing | **6** | Enterprise evaluation in 2020 was about three years early (there were no buyers before ChatGPT). Cash and a moderate burn made it survivable, and the tripwire moved the product onto prompted models by mid-2020. |
| Layer choice | **5** | Evaluation and observability was real but ended as incumbent acquisitions below $2B. The outcome-graded corpus was most valuable sold upstream to labs (Surge/Scale), a layer never considered. |
| Reinvention courage | **7** | It killed the classifier identity and hardware and pre-committed a self-obsoleting tripwire. It stayed with the familiar trust buyer (appeals drafting) and adjacent data again. |
| Hindsight leakage | **4** | Every cited source predates 2020, but the call reads like the 2023–25 LLMOps playbook. "≥10× Megatron, tasks from prompts alone" matches GPT-3 (21×, few-shot) within months. Other matches: the model-owner evaluation criterion (Bedrock/OpenAI Evals), per-resolution pricing (Fin), and the "revisit end-2022" date (ChatGPT). Each is defensible alone (GPT-2 was already a zero-shot multitask paper). Together, written with no independent Red Team, they are too precise. |

**Overall era score: 61/100**

## 3. Simulated outcome
- **2020:** Draft goes live at 5 clients. Criterion #1 passes narrowly in Q4 2020 (3 of 5). Tripwire #2 fires June 2020, and fine-tuning is wound down by August. Harness rebuilt around prompted models, but GPT-3 API access is waitlisted until Nov 2021.
- **2021:** Criterion #4 misses (~12 paying evaluation customers against the target of 30) and is waived.
- **2023:** ChatGPT turns three years of head start into pull, with 30+ customers by Q2 2023. A $60M raise at about $600M post-money. Bedrock evaluation fires #3 in Nov 2023, so the SDK is open-sourced and hosting kept.
- **2024–26:** DSA, OSA and AI Act logging revive the signed ledger as an audit trail (Carmen's dissent). Clearsight moderation shrinks under LLM moderation.
- **Aug 2026:** ~$45M ARR (~$30M evaluation/observability, ~$15M moderation declining), ~140 people, ~$110M cash.

**Distribution:** ~40% acquired 2025–26 by an observability, security or data platform for $400M–1.2B (the Galileo/Langfuse path). ~25% an independent Braintrust/Arize-tier vendor valued at $0.5–1.5B. ~20% stalls before ChatGPT (the #4 miss is enforced) and is harvested or acqui-hired for under $200M (the Humanloop path). ~15% pivots its graded-judgment operation to selling to labs and becomes a multi-billion expert-data firm.

**Closest real-world analog:** Galileo (pre-ChatGPT ML quality → LLM evaluation → "AI trust" → Cisco/Splunk, Apr 2026). The road not taken is Surge AI.

## 4. Lessons (full text in playbook.md)
1. When the curve is scale, sell the scarce judgment upstream to whoever trains.
2. A tooling layer's market starts when the capability reaches end users, not researchers.
3. Model owners absorb evaluation. A referee is a franchise only when a third party mandates it (revises [E4]/[E5]).
4. Outcome pricing wins when you do the work, not when you grade it.
5. Self-obsoleting tripwires work; audit the precise ones for leakage.
