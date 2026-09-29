# Limitations and the v2 experiment

## Known problems with the published runs

| Problem | Why it matters |
|---|---|
| No controlled replication | There are four qualitative trajectories, but no condition has repeated runs under a controlled harness; patterns may be noise or prompt effects. |
| Possible cross-run contamination | Runs 002–004 were generated in an environment where the repository (including Run 001's records, README findings and Playbook) was likely visible. Run 002 reuses Run 001's company names and theses for E1–E4 (Switchyard, Manifest, Ledgerline, Clearline) and restates its headline finding; Run 004 also begins as "Switchyard Systems". Agreement between runs is therefore not independent confirmation. |
| Inconsistent score aggregation | Run 001 totals are holistic judge judgements. Run 004 totals are the subscore sum × 2 (documented). Run 002 matches sum × 2 except E6 (72 vs 68). Run 003 matches sum × 2 only for E1–E2. `results/all_runs_scores.csv` reports both the published total and the recomputed sum × 2 for every era. Compare runs on the recomputed column. |
| One model plays every role | Dissent is simulated diversity, and the judge grades reasoning produced by its own priors. In Run 004 the same root context wrote the briefings and board decisions and then judged them. |
| Hindsight is measured, not controlled | The model knows 1990–2026. The anti-hindsight rule is a discipline, not a guarantee, and the leakage subscore is self-graded. |
| Briefing selection is a leakage channel | Choosing which "frontier signals" appear in a dated briefing is itself informed by hindsight (for example, Run 004's 1990 briefing foregrounds the 1989 CERN proposal). Facts can be pre-date while their selection is not. |
| Learning and leakage are confounded | In all four runs, training-era totals rise across eras while the hindsight subscore falls in the same eras (per-run r between total and hindsight subscore: −0.58, −0.58, −0.92, −0.38). |
| The rubric can reward caution over frontier capture | Hindsight discipline counts toward the Run 004 total, and Run 004 scored highest while never building a product in fifty simulated years (every era is a gated manual pilot). A company that names nothing about the future scores well on hindsight; the rubric has no measure of whether the company reached where value pooled. |
| Unequal protocol depth | Run 002 has no per-era records; Run 003's era files are short decision/reveal summaries without briefings, memos or Red Team output. Runs 001 and 004 have full per-era records. |
| No baselines | Nothing shows that the Playbook, the Red Team or the org structure helped. |
| Outcomes are simulated | Revenues, exits and probabilities are calibrated guesses, and they compound across eras. |
| Forecast eras are circular | In Run 001 the E8 judge wrote the kill case that became the E9 world. |
| Operator intervention | The Run 001 E6 board decision, including its GPT-3-like tripwire, was written by the operator (see [run-001-notes.md](run-001-notes.md)). |
| Qualitative claims are judge-labelled | "Named the frontier", "adjacent layer" and "dissent was right" are the judge's words, not counted metrics. |
| Era window mismatch | Run 003's E6 reveal covers 2020–2025, while the protocol defines E6 as Jan 2020 – Aug 2026. |

## Corrections applied (29 Sep 2026)

- `results/run-002-scores.csv`, `results/run-003-scores.csv`, `runs/run-002/scores.csv`, `runs/run-003/scores.csv`: live and forecast rows had their five Auditor subscores shifted one column to the left (starting in the unused `hindsight_leakage` column). Values are now placed in `playbook_consistency, plausibility, non_consensus, layer_choice, grounded`, the order used in the Run 003 reveals. Run 002 has no per-era reveals, so the same mapping is assumed for it. Totals are unchanged.
- `results/all_runs_scores.csv` added: every era of every run in one long table, with the published total, the recomputed subscore sum × 2, their difference, and each run's aggregation rule.

## Provenance of the existing runs

| Run | Execution method | Interpretation |
|---|---|---|
| 001 | Original file-based sub-agent orchestration (about 45 separate agent launches); one human-authored board decision in E6 | Role calls used separate agent launches, but shared a model family and hindsight exposure. |
| 002–003 | Separate, manually orchestrated harness following the same era prompts; one model generated all role perspectives and judging per run | Qualitative alternate trajectories with thinner records; not independent-agent replications or controlled samples; possibly exposed to Run 001. |
| 004 | Separate persistent contexts for three departments and the Red Team; the root context wrote briefings, board decisions and judgments | Multi-context role simulation with full per-era records; possibly exposed to Run 001; the judge is not independent of the decision-maker. |
| Python `harness/` | API-based runner with ablations and logging; not used to produce Runs 001–004 | Its ability to reproduce the published trajectories has not been evaluated. |

## Status of each run-001 observation

| Observation (README) | Evidence | What would weaken it | v2 test |
|---|---|---|---|
| Named the frontier, built the adjacent layer | Run 001 judge reveals for E1, E2, E4, E5; final synthesis §3. E3 is a counterexample. Layer choice is the lowest mean training subscore in all four runs (4.7–5.8 of 10). | Same pattern absent in clean replicates, or present equally in the single-prompt baseline | Layer distance per era, across runs and conditions |
| Dissent often right when the decision was not | Run 001 final synthesis §3 lists vindicated dissents in E1–E8 | Wrong dissents are as common as right ones | Dissent accuracy: share of all logged dissents vindicated |
| Scores rose as leakage rose | All four runs: positive training slope (+1.4 to +2.6 points per era) and negative total–hindsight correlation | Gains persist on fictional or post-cutoff eras | Leakage controls below |
| Correct idea adopted late | Run 001 E5–E9 board decisions and reveals | Not a repeated pattern | Qualitative only; report if recurrent |
| Forecasts are circular | Run 001 E8 reveal → E9 world briefing | — | Independent briefing author for forecast eras |

## v2 design

**Research questions**

1. Does scoring against history (with a carried-forward Playbook) improve an agent org's strategic calls over the eras, relative to controls?
2. How much of any improvement is hindsight leakage, and can leakage be detected by the judge?
3. Is the "named the frontier, built the adjacent layer" pattern stable across runs and models?

**Pre-registered hypotheses** (to be fixed before running)

- H1: The training-era slope of the total score is higher in `full` than in `no_playbook`.
- H2: `full` beats `single_prompt` on mean training score.
- H3: On a fictional era, the judge's leakage subscore does not differ between conditions (a check that the leakage measure is calibrated).
- H4: Layer distance is "adjacent" more often than "match" in all conditions.

**Conditions** (all supported by `harness/run.py --ablation`)

| Condition | What changes |
|---|---|
| full | The loop as in run 001 |
| no_playbook | No lessons carried between eras |
| no_redteam | Board without the Red Team |
| single_prompt | One founder call per era; no departments, no board |

**Replication:** 5–10 runs per condition at temperature 1.0, with at least two different models as players and a different model family as judge. Every run starts in a clean working directory that contains only `prompts/` and `harness/`, never `runs/`, `results/` or the READMEs.

**Scoring rule:** the total is always the subscore sum × 2, computed by the harness, never typed by the judge. Hindsight is reported as a separate measure and excluded from the total. Add a `frontier_capture` subscore: did the chosen layer match, neighbour or miss the layer where value pooled?

**Leakage controls**

- *Fictional era:* insert a synthetic era with an invented technology history (consistent, plausible, and unknown to the model). Any "leakage" there is a false positive, which calibrates the judge.
- *Post-cutoff era:* evaluate one training era that falls after the player model's training cutoff, where true foresight and leakage can be separated.
- *Blind briefings:* generate training-era briefings from sources dated before each era, selected by a procedure that does not see later history.
- *Vocabulary probe:* automatically flag memo terms whose first recorded usage postdates the era's start date.

**Judge validity**

- Two to three human raters (technology historians or experienced investors) score a stratified sample of eras on the same rubric. Report agreement with the model judges.
- Swap judges across model families and report how the scores shift.
- Blind the judge to the condition label.

**Metrics**

- Per-era total and subscores; the slope across training eras.
- *Layer distance:* whether the chosen layer matches, is adjacent to, or misses the layer the judge identifies as where value pooled.
- *Dissent accuracy:* the share of logged dissents the judge marks as vindicated.
- *Leakage rate:* the judge's leakage subscore, plus the vocabulary probe.

**Implementation status in `harness/`**

| Component | Status |
|---|---|
| Four ablation conditions, separate player and judge models, full logging, resume | Implemented |
| Run comparison (per-era totals, per-mode means) | Implemented (`harness.compare`) |
| Replicate orchestration, custom or fictional era schedules | Not yet |
| Harness-computed totals, frontier-capture subscore | Not yet |
| Vocabulary probe, layer distance, dissent accuracy | Not yet (need structured judge output) |
| Human rating sheets | Not yet |

**Expected cost:** roughly 5 calls per era, about 46 per run with the founding briefing, × 4 conditions × 5–10 runs ≈ 900–1,850 calls, plus human rating time.
