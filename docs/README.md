# Frontier Lab

**An LLM-simulated startup reinvents itself across fifty years of technology history, is scored against what actually happened, and then forecasts.**

One simulated company, staffed by sixteen named agent personas, lives through six *training* eras (1990–2020). In each era it decides using only what was public at the time. A historian-judge then reveals what really happened, scores the call, and writes lessons into a Playbook that carries into the next era. From 2026 the trained org faces the live market and then forecasts 2032 and 2040, where there is no answer key.

**Research question:** can an agent organization learn strategy by being scored against history, and does hindsight leakage make that scoring meaningless?

> **Status: exploratory, n = 1.** `runs/run-001` is a single run in which one model played every role, including the judges, and a human operator wrote one board decision (E6). Everything below is a hypothesis for the controlled design in [docs/limitations-and-v2.md](docs/limitations-and-v2.md), not a finding.

## Run 001 at a glance

| Era | Mode | Company | The call | Score |
|---|---|---|---|---|
| E1 · 1990 | training | Switchyard Systems | Mail and address gateway between incompatible networks | 55 |
| E2 · 1996 | training | Manifest Networks | Receipted Web-EDI exchange | 52 |
| E3 · 2002 | training | Ledgerline | Neutral cross-channel conversion ledger | 58 |
| E4 · 2008 | training | Clearline | Exchange for verified in-app actions | 66 |
| E5 · 2014 | training | Clearsight | GPU-trained moderation and account-risk API | 68 |
| E6 · 2020 | training | Clearproof | Outcome-graded evaluation of language models | 61 † |
| E7 · 2026 | live | Proofworks | Long-horizon RL environments from real enterprise work | 56 |
| E8 · 2032 | forecast | Clearwork | Clearing house for delegated agent work | 57 |
| E9 · 2040 | forecast | Clearbond | Bonding house for agents acting without a human signature | 58 |

† E6's board decision was written by the operator, not the agents ([run notes](docs/run-001-notes.md)).

Training mean 60 (E1–E6). Live 56 (E7). Forecast mean 57.5 (E8–E9). Training, live and forecast scores use different rubrics and different judges, so they are not directly comparable. Scores are 0–100 overall judgements by the judge, not sums of subscores. Subscores are in [`results/scores.csv`](results/scores.csv); an interactive view is in [`results/results_page.html`](results/results_page.html).

## Observations from run 001

These are patterns in a single run, graded by the same model that produced them. Each is paired with the reason it may not hold.

1. **The org named the frontier, then built the adjacent layer.** In most training eras a department memo named the capability jump that the judge later identified (E1 hypertext and the index, E2 relevance, E4 neural networks, E5 deep learning), and the board chose the layer its existing assets could reach. E3 is a counterexample: the judge found that no memo named the era's biggest shifts (social, cloud, mobile).
   *Caveat:* "named" and "adjacent" are the judge's labels, applied with hindsight. v2 measures this as *layer distance* across runs.
2. **Dissent was often right when the decision was not.** The final synthesis lists vindicated dissents in E1–E8, especially those about who holds the money or the loss.
   *Caveat:* nobody counted the dissents that were wrong, so this is not yet a rate. In E7–E8 "right" means the Auditor agreed, not that history did.
3. **Scores rose in the same eras that leakage rose.** Training scores climbed from 52–58 (E1–E3) to 66–68 (E4–E5), while the hindsight-leakage subscore (10 = none) fell from 7 to 5–6, then 4 in E6. Across the six training eras the two move against each other (r ≈ −0.58, n = 6). This run cannot separate learning from leakage, and that is the central problem v2 is built to address.
   *Caveat:* E6's low leakage score is partly the operator's doing. Its tripwire ("a public model ≥10× Megatron that works from prompts alone"), which GPT-3 matched in May 2020, was written by the operator, so E6 timing is contaminated.
4. **One correct idea surfaced early and was adopted late.** Guaranteeing the outcome (carrying the loss, not just scoring the risk) appeared in E5 as a phase-3 step, when, per the judge, real companies such as Forter and Riskified won with exactly that. It was deferred or gated in E6–E8 and adopted in E9, applied to autonomous agents, into what the Auditor judged a crowded market.
5. **The forecasts became circular.** The E8 Auditor's kill case became the E9 world briefing, which the E9 board then adopted. Forecast-era scores therefore partly grade the judge's own scenario.

## How it works

```
             ┌──────────────────────── next era ◄─────────────────────────┐
             ▼                                                            │
  World briefing ──► 3 department memos ──► Board meeting ──► Reveal & score ──► Playbook +
  (written by the     Frontier Research     Red Team attacks,   The Record (≤2020)   company state
   judge, dated)      Product & Eng.        CEO decides         The Auditor (≥2026)
                      Market & Capital
                      (in parallel)
```

- **Personas and calls.** 16 named personas (CEO, CTO, Chief Scientist, CSO; 4 in Frontier Research, 4 in Product & Engineering, 3 in Market & Capital; a Red Team lead) plus two external judges. Each department memo is one model call that voices all of its members, and the board is one call, so an era is five calls: three memos, one board, one judge. Charter: [`prompts/charter.md`](prompts/charter.md).
- **Eras.** 1990, 1996, 2002, 2008, 2014, 2020 (training) · Sep 2026 (live, with web search) · 2032, 2040 (forecast).
- **Scoring.** Training eras: frontier accuracy, timing, layer choice, reinvention courage, hindsight leakage. Live and forecast eras: playbook consistency, plausibility, non-consensus, layer choice, groundedness.
- **Memory.** Agents share state only through files: company state, the Playbook, the roster and per-era folders.

Full protocol: [docs/methodology.md](docs/methodology.md).

## Repository layout

```
prompts/            charter.md and the exact instructions given to agents in run 001
harness/            Python harness for new runs (Anthropic API), with ablations and an offline dry run
runs/run-001/       every briefing, memo, board decision and reveal from run 001
  eras/E1..E9/      world_briefing.md, memo_{frontier,product,market}.md, board_decision.md, reveal.md
  playbook.md       the lessons as they accumulated
  company_state.md  identities, capital and outcomes across eras
  roster.md         how the org restructured itself
  final_synthesis.md
results/            scores.csv, results_page.html
docs/               methodology, run notes, limitations and v2 design, paper outline
```

## Reproducing and extending

Run 001 was executed by an orchestrating agent that launched sub-agents with file and web tools (their instructions are in `prompts/`). The `harness/` package runs the same loop with direct API calls, inlining the documents each agent would have read, so runs can be repeated, varied and compared. No harness run has been published yet, and the harness has not been checked to reproduce run 001's score distribution.

```bash
pip install -r requirements.txt
export ANTHROPIC_API_KEY=...

# offline smoke test (no API calls)
python -m harness.run --run-id dry --dry-run

# a full run (use a different model for the judges than for the players)
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

- **n = 1, one model.** The same model played all 16 personas and both judges, so dissent is simulated diversity and the judge grades reasoning produced by its own priors.
- **Hindsight is measured, not prevented.** The model knows what happened after 1990. The anti-hindsight rule is a discipline, and the leakage subscore is the same model grading itself.
- **Outcomes are simulated.** Revenues, exits and probabilities are the judges' guesses, and they compound across eras.
- **Forecast eras have no ground truth** and are partly circular (observation 5).
- **Operator intervention.** The E6 board decision, including its tripwire, was written by the operator during an outage of agent launches. The E6 judge was told and penalised it.
- **Redactions.** Passages applying the simulation to one founder's personal situation were removed from three files (listed in the [run notes](docs/run-001-notes.md)). Nothing else was edited.

The controlled v2 design (replicates, ablations, cross-family judges, leakage controls, human raters) is in [docs/limitations-and-v2.md](docs/limitations-and-v2.md). A draft paper outline is in [docs/paper-outline.md](docs/paper-outline.md).

## Citing

If you use this work, please cite it using [`CITATION.cff`](CITATION.cff).

## License

MIT. See [LICENSE](LICENSE).
