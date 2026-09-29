# Limitations and the v2 experiment

| Problem | Why it matters |
|---|---|
| No controlled replication | There are three qualitative trajectories, but no condition has repeated runs under a controlled harness; patterns may be noise or prompt effects. |
| One model plays every role | Dissent is simulated diversity, and the judge grades reasoning produced by its own priors. |
| Hindsight is measured, not controlled | The model knows 1990–2026. The anti-hindsight rule is a discipline, not a guarantee, and the leakage subscore is self-graded. |
| Learning and leakage are confounded | Training scores rose in E4–E5, the same eras in which the leakage subscore worsened. Run 001 cannot tell improvement from leakage. |
| No baselines | Nothing shows that the Playbook, the Red Team or the org structure helped. |
| Outcomes are simulated | Revenues, exits and probabilities are calibrated guesses, and they compound across eras. |
| Forecast eras are circular | The E8 judge wrote the kill case that became the E9 world. |
| Operator intervention | The E6 board decision, including its GPT-3-like tripwire, was written by the operator (see [run-001-notes.md](run-001-notes.md)). |
| Qualitative claims are judge-labelled | "Named the frontier", "adjacent layer" and "dissent was right" are the judge's words, not counted metrics. |

## Provenance of the existing runs

| Run | Execution method | Interpretation |
|---|---|---|
| 001 | Original file-based sub-agent orchestration; one human-authored board decision in E6 | Role calls used separate agent launches, but shared a model family and hindsight exposure. |
| 002–003 | Separate, manually orchestrated harness following the same era prompts; one model generated all role perspectives and judging per run | Useful as qualitative alternate trajectories, not independent-agent replications or controlled samples. |
| Python `harness/` | API-based runner with ablations and logging; not used to produce Runs 001–003 | Its ability to reproduce the published trajectories has not been evaluated. |

## Status of each run-001 observation

| Observation (README) | Evidence in run 001 | What would weaken it | v2 test |
|---|---|---|---|
| Named the frontier, built the adjacent layer | Judge reveals for E1, E2, E4, E5; final synthesis §3. E3 is a counterexample. | Same pattern absent in replicates, or present equally in the single-prompt baseline | Layer distance per era, across runs and conditions |
| Dissent often right when the decision was not | Final synthesis §3 lists vindicated dissents in E1–E8 | Wrong dissents are as common as right ones | Dissent accuracy: share of all logged dissents vindicated |
| Scores rose as leakage rose | `results/scores.csv`: totals vs `hindsight_leakage` (r ≈ −0.58, n = 6) | Gains persist on fictional or post-cutoff eras | Leakage controls below |
| Correct idea adopted late | E5–E9 board decisions and reveals | Not a repeated pattern | Qualitative only; report if recurrent |
| Forecasts are circular | E8 reveal → E9 world briefing | — | Independent briefing author for forecast eras |

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

**Replication:** 5–10 runs per condition at temperature 1.0, with at least two different models as players and a different model family as judge.

**Leakage controls**

- *Fictional era:* insert a synthetic era with an invented technology history (consistent, plausible, and unknown to the model). Any "leakage" there is a false positive, which calibrates the judge.
- *Post-cutoff era:* evaluate one training era that falls after the player model's training cutoff, where true foresight and leakage can be separated.
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
| Vocabulary probe, layer distance, dissent accuracy | Not yet (need structured judge output) |
| Human rating sheets | Not yet |

**Expected cost:** roughly 5 calls per era, about 46 per run with the founding briefing, × 4 conditions × 5–10 runs ≈ 900–1,850 calls, plus human rating time.
