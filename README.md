# Frontier Autolab

**A multi-agent startup that reinvents itself across fifty years of technology history.**

Sixteen named roles are represented in the simulation for one company. It lives through 1990–2020 as *training*: in each era it decides using only what was knowable then. A historian-judge then reveals what actually happened, scores the call, and writes lessons into a Playbook that carries into the next era. From 2026 the org forecasts 2032 and 2040, where there is no answer key. Orchestration differs by run; consult each run's methodology before treating role voices as independent agents.

The research question: **can an agent organization learn strategy by being scored against history, and does hindsight leakage make that scoring meaningless?**

> Status: exploratory. Run 001 used the original sub-agent orchestration. Runs 002 and 003 used a separate, manually orchestrated harness that follows the same era prompts, with one model generating each run's department perspectives, board decisions, and judging. None is a controlled replication. See [the run limitations and experiment plan](docs/limitations-and-v2.md).

> **Review corrections (29 Sep 2026).** Score aggregation differs by run (Run 001 holistic; Run 004 subscore sum × 2; Runs 002–003 mixed), so compare runs with the recomputed column in [`results/all_runs_scores.csv`](results/all_runs_scores.csv). The live/forecast subscores of Runs 002 and 003 were exported one column off and are now corrected. Runs 002–004 were probably generated with Run 001's records visible (Run 002 reuses Run 001's company names for E1–E4), so they are not independent replications. A paper describing the pilot study is in [`paper/`](paper).

## Run 001 at a glance

| Era | Mode | Company | The call | Score |
|---|---|---|---|---|
| 1990 | training | Switchyard Systems | Mail and address gateway between incompatible networks | 55 |
| 1996 | training | Manifest Networks | Receipted Web-EDI exchange | 52 |
| 2002 | training | Ledgerline | Neutral cross-channel conversion ledger | 58 |
| 2008 | training | Clearline | Exchange for verified in-app actions | 66 |
| 2014 | training | Clearsight | GPU-trained moderation and account-risk API | 68 |
| 2020 | training | Clearproof | Outcome-graded evaluation of language models | 61 |
| 2026 | live | Proofworks | Long-horizon RL environments from real enterprise work | 56 |
| 2032 | forecast | Clearwork | Clearing house for delegated agent work | 57 |
| 2040 | forecast | Clearbond | Bonding house for agents acting without a human signature | 58 |

Training average 60; forecast average 57.5. Subscores are in [`results/scores.csv`](results/scores.csv), and an interactive view is in [`results/results_page.html`](results/results_page.html).

## Run 002 at a glance

| Era | Mode | Company | The call | Score |
|---|---|---|---|---:|
| 1990 | training | Switchyard | Mail and address gateway between incompatible networks | 62 |
| 1996 | training | Manifest | Receipted Web-EDI exchange | 66 |
| 2002 | training | Ledgerline | Neutral cross-channel conversion ledger | 60 |
| 2008 | training | Clearline | Exchange for verified in-app actions | 66 |
| 2014 | training | Vectorial | Narrow deep-learning risk decision with outcome feedback | 64 |
| 2020 | training | Proofline | Outcome evaluation for language-model workflows | 72 |
| 2026 | live | Tracewell | Rights-bearing workflow traces and reliability evidence | 66 |
| 2032 | forecast | Consequence | Acceptance records for delegated work | 62 |
| 2040 | forecast | Recourse | Bounded recourse for delegated actions | 60 |

Training average 65; forecast average 61. Details are in [`runs/run-002`](runs/run-002), and scores are in [`results/run-002-scores.csv`](results/run-002-scores.csv).

## Run 003 at a glance

| Era | Mode | Company | The call | Score |
|---|---|---|---|---:|
| 1990 | training | Porthole Networks | Mixed-network diagnostics | 60 |
| 1996 | training | PageSignal | Web uptime monitoring | 58 |
| 2002 | training | Clinisphere | Hosted clinic workflow | 63 |
| 2008 | training | ClaimGraph | Verified digital claims evidence | 65 |
| 2014 | training | BenefitFlow | Mobile benefits enrollment | 61 |
| 2020 | training | LineSight | Industrial vision validation | 68 |
| 2026 | live | FlowCheck | Acceptance tests for an AI claims workflow | 64 |
| 2032 | forecast | WorkPermit | Scoped authority for delegated tasks | 59 |
| 2040 | forecast | Delegation Warranty | Capped recourse for a narrow delegated transaction | 55 |

Training average 62.5; forecast average 57. Details are in [`runs/run-003`](runs/run-003), and scores are in [`results/run-003-scores.csv`](results/run-003-scores.csv).

Runs 002 and 003 used the same separate, manually orchestrated harness. This is role simulation by one model, not an independent-agent run, controlled ablation, or evidence that the Playbook improves performance. The Python API harness in `harness/` was not used for either run.

## Run 004 at a glance

| Era | Mode | Company | The call | Score |
|---|---|---|---|---:|
| 1990 | training | Switchyard Systems | Permissioned LAN-support casebook for one environment | 60 |
| 1996 | training | Switchyard Systems | Guided troubleshooting with buyer and accuracy gates | 62 |
| 2002 | training | Switchyard Commerce Operations | Manual online-order exception triage | 62 |
| 2008 | training | Switchyard Commerce Operations | Permissioned merchant exception workflow, no connectors | 70 |
| 2014 | training | Switchyard Evidence Operations | Human-reviewed packet for one payment-dispute type | 70 |
| 2020 | training | Switchyard Evidence Operations | Rules-based packet completeness check | 72 |
| 2026 | live | Caseground | Independent qualification for one dispute workflow | 66 |
| 2032 | forecast | Caseground | Conditional paid manual acceptance test | 68 |
| 2040 | forecast | Caseground | Conditional decision-linked evaluation | 66 |

Training mean 66; forecast mean 67; live E7 score 66. Training and forecast rubrics differ, so compare within modes only. Scores are subjective judge assessments, not measurements of company performance. Full records, score details, and limitations are in [`runs/run-004`](runs/run-004), [`runs/run-004/final_synthesis.md`](runs/run-004/final_synthesis.md), and [`results/run-004-scores.csv`](results/run-004-scores.csv).

Run 004 used separate department contexts for Frontier Research, Product & Engineering, and Market & Capital, plus a separate Red Team context. Roles within each department memo shared that context. The root context wrote briefings, board decisions, and Record/Auditor judgments. It represented the charter's 16 roles but did **not** instantiate 16 separately autonomous agents. Run 004 is a multi-context role simulation, not a controlled replication or proof that the Playbook improves strategy. E1–E6 use dated briefs but cannot eliminate model hindsight; E8–E9 are projections without an answer key. The E7 folder links current sources and competitor documentation.

**Run 001 observations (hypotheses, not findings)**

1. **Named the frontier, built the adjacent layer.** In every era the department memos identified the real capability jump. The board then chose the layer its existing assets could reach, one step away from where value pooled.
2. **Dissent beat decisions.** Logged dissents about *who holds the money or the loss* were right far more often than the board's call.
3. **Hindsight leakage rose as the org learned.** The leakage subscore fell from 7 in the early eras to 5 (2008) and 4 (2020). The 2020 board set a tripwire ("a public model ≥10× Megatron that works from prompts alone") that GPT-3 matched five months later.
4. **The best idea was deferred four times.** Pricing against the loss was correct in 2014 (per the judge), deferred in 2020, 2026 and 2032, and adopted in 2040 into a crowded market.
5. **The forecasts became circular.** The 2032 judge's kill case became the 2040 world briefing, which the 2040 board then adopted.

## How it works

```
World briefing ──► 3 department memos (parallel) ──► Board meeting ──► Reveal & score ──► Playbook + company state
 (judge, dated)     Frontier Research                 Red Team attacks   history (≤2020)       │
      ▲             Product & Engineering             CEO decides        or Auditor (≥2026)    │
      └──────────────────────────────── next era ◄──────────────────────────────────────────────┘
```

- **The org:** 16 agents (CEO, CTO, Chief Scientist, CSO; 4 in Frontier Research, 4 in Product & Engineering, 3 in Market & Capital; a Red Team lead). Two external judges: *The Record* (training eras) and *The Auditor* (live and forecast eras). Full charter: [`prompts/charter.md`](prompts/charter.md).
- **Eras:** 1990, 1996, 2002, 2008, 2014, 2020 (training) · Sep 2026 (live, with web research) · 2032, 2040 (forecast).
- **Scoring:** training eras are scored on frontier accuracy, timing, layer choice, reinvention courage and hindsight leakage. Forecast eras are scored on playbook consistency, plausibility, non-consensus, layer choice and groundedness.
- **Memory:** agents share state only through files: company state, the Playbook, the roster, and per-era folders.

Details: [docs/methodology.md](docs/methodology.md).

## Repository layout

```
prompts/            charter.md + the exact instructions given to agents in run 001
harness/            Python API harness for new runs (Anthropic API)
runs/run-001/       every briefing, memo, board decision and reveal from run 001
  eras/E1..E9/      world_briefing.md, memo_{frontier,product,market}.md, board_decision.md, reveal.md
  playbook.md       the lessons as they accumulated
  company_state.md  identities, capital and outcomes across eras
  roster.md         how the org restructured itself
  final_synthesis.md
runs/run-002/       qualitative run records, company state, Playbook, synthesis
runs/run-003/       qualitative run records, company state, Playbook, synthesis
runs/run-004/       multi-context role simulation; era briefs, department memos, critiques, decisions, audits
results/            score exports for runs 001–004, results_page.html
paper/              LaTeX source and PDF of the pilot-study paper
docs/               methodology, run notes, limitations and v2 plan
```

## License

MIT. See [LICENSE](LICENSE).
