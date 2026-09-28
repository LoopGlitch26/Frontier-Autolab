# Limitations and the v2 experiment

## Why run 001 is not a paper yet

| Problem | Why it matters |
|---|---|
| n = 1 | The patterns (adjacent-layer choice, dissent accuracy) could be noise from one run. |
| One model plays every role | Dissent is simulated diversity, and the judge grades reasoning produced by its own priors. |
| Hindsight is measured, not controlled | The model knows 1990–2026. The anti-hindsight rule is a discipline, not a guarantee. |
| No baselines | Nothing shows that the Playbook, the Red Team or the org structure helped. |
| Outcomes are simulated | Revenues, exits and probabilities are calibrated guesses, and they compound across eras. |
| Forecast eras are circular | The E8 judge wrote the kill case that became the E9 world. |
| Operator intervention | The E6 board decision was written by the operator (see run-001-notes.md). |

## v2 design

**Research questions**

1. Does scoring against history (with a carried-forward Playbook) improve an agent org's strategic calls over the eras, relative to controls?
2. How much of any improvement is hindsight leakage, and can leakage be detected by the judge?
3. Is the "named the frontier, built the adjacent layer" pattern stable across runs and models?

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

**Metrics**

- Per-era total and subscores; the slope across training eras.
- *Layer distance:* whether the chosen layer matches, is adjacent to, or misses the layer the judge identifies as where value pooled.
- *Dissent accuracy:* the share of logged dissents the judge marks as vindicated.
- *Leakage rate:* the judge's leakage subscore, plus the vocabulary probe.

**Expected cost:** roughly 45 calls per run × 4 conditions × 5–10 runs = 900–1,800 calls, plus human rating time.
