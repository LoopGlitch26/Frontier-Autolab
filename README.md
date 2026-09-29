# Frontier Autolab

**A multi-agent startup that reinvents itself across fifty years of technology history.**

Sixteen LLM agents with named roles run one company. It lives through 1990–2020 as *training*: in each era it decides using only what was knowable then. A historian-judge then reveals what actually happened, scores the call, and writes lessons into a Playbook that carries into the next era. From 2026 the trained org forecasts 2032 and 2040, where there is no answer key.

The research question: **can an agent organization learn strategy by being scored against history, and does hindsight leakage make that scoring meaningless?**

> Status: exploratory. `runs/run-001` is a single run. Treat the results as hypotheses for the controlled experiments described in [docs/limitations-and-v2.md](docs/limitations-and-v2.md).

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

Training average 60, forecast average 57. Subscores are in [`results/scores.csv`](results/scores.csv), and an interactive view is in [`results/results_page.html`](results/results_page.html).

**Main observations (from one run: hypotheses, not findings)**

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
harness/            a reproducible Python harness for new runs (Anthropic API)
runs/run-001/       every briefing, memo, board decision and reveal from run 001
  eras/E1..E9/      world_briefing.md, memo_{frontier,product,market}.md, board_decision.md, reveal.md
  playbook.md       the lessons as they accumulated
  company_state.md  identities, capital and outcomes across eras
  roster.md         how the org restructured itself
  final_synthesis.md
results/            scores.csv, results_page.html
docs/               methodology, run notes, limitations and v2 plan
```

## Reproducing and extending

Run 001 was executed by an orchestrating agent that launched sub-agents with file and web tools (the instructions are in `prompts/`). The `harness/` package reproduces the same loop with direct API calls, so runs can be repeated, varied and compared.

```bash
pip install -r requirements.txt
export ANTHROPIC_API_KEY=...

# offline smoke test (no API calls)
python -m harness.run --run-id dry --dry-run

# a full run: separate models for players and judges is recommended
python -m harness.run --run-id run-002 --player-model <model-id> --judge-model <other-model-id> --web-search

# ablations
python -m harness.run --run-id abl-noplaybook --ablation no_playbook   --player-model <id> --judge-model <id>
python -m harness.run --run-id abl-noredteam  --ablation no_redteam    --player-model <id> --judge-model <id>
python -m harness.run --run-id abl-single     --ablation single_prompt --player-model <id> --judge-model <id>

# compare runs
python -m harness.compare runs/run-001 runs/run-002 runs/abl-noplaybook
```

Every prompt and raw response is logged under `runs/<run-id>/logs/`. Runs resume: completed eras are skipped.

## Limitations

- **One run**, one model for all players and judges.
- **Hindsight is measured, not prevented.** The model knows what happened after 1990.
- **Outcomes are simulated.** Revenues, exits and probabilities are the judges' calibrated guesses.
- **Human intervention:** the 2020 board decision was written by the operator during an outage of agent launches. The 2020 judge was told and penalised it.
- **Redactions:** two sections giving advice to one specific founder were removed from the 2026 files and the final synthesis. Nothing else was edited.

See [docs/limitations-and-v2.md](docs/limitations-and-v2.md) for the controlled v2 design.

## License

MIT. See [LICENSE](LICENSE).
