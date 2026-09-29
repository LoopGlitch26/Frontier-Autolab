# Paper outline (draft)

A working outline for an arXiv write-up. It assumes the v2 experiment has been run; run 001 appears as the pilot.

## Working titles

- *Scored Against History: Can an LLM Agent Organization Learn Strategy, or Only Remember It?*
- *Frontier Lab: Hindsight Leakage in Historically Scored Multi-Agent Strategy*

## Abstract (draft, pilot-only version)

We simulate a startup staffed by sixteen LLM personas that must reinvent itself across nine technology eras, 1990–2040. In six training eras it decides using only information public at the time; an LLM historian-judge then reveals what happened, scores the decision and writes lessons that carry forward. In the three later eras the organization faces the live market and then forecasts, without ground truth. In a single pilot run, training-era scores rose from 52–58 to 66–68 while the judge's hindsight-leakage subscore worsened, so apparent learning could not be separated from recall. The organization's memos repeatedly named the capability shift that the judge later identified, while the board chose an adjacent layer its assets could reach. We describe a controlled design, with ablations of the Playbook, Red Team and org structure, cross-family judges, fictional and post-cutoff eras, and human raters, to test whether historical scoring teaches strategy or only rewards leakage.

## Contributions

1. A reproducible protocol for scoring agent-organization strategy against dated history, with an offline harness and full logs.
2. A pilot run with every artifact published, including the one operator intervention and the redactions.
3. An analysis of hindsight leakage as a confound for any "learn from history" agent benchmark, with proposed controls.
4. (v2) Ablation results and judge-validity measurements.

## Sections

1. **Introduction.** Why strategy is hard to evaluate; why history is an attractive answer key; why a model that already knows history makes it a leaky one.
2. **Related work.** LLM agent societies and role-play simulations; LLM-as-judge reliability and self-preference; forecasting benchmarks and knowledge-cutoff contamination; organizational learning.
3. **Frontier Lab.** Eras, personas, the per-era loop, rules, rubrics (from `docs/methodology.md`).
4. **Pilot: run 001.** Score trajectory; the five observations with their caveats; the E6 intervention; the circular forecast eras.
5. **v2 design.** Hypotheses H1–H4, conditions, replication, leakage controls, metrics (from `docs/limitations-and-v2.md`).
6. **Results (v2).** Slope by condition; leakage on fictional vs real eras; judge agreement across model families and with humans; layer distance and dissent accuracy.
7. **Discussion.** What the org "learned"; whether Playbook lessons generalise or only restate the last reveal; limits of simulated outcomes.
8. **Threats to validity.** Self-grading; simulated outcomes; era granularity; prompt sensitivity; persona collapse within one call.
9. **Ethics and disclosure.** Operator intervention and redactions; no personal advice in the published artifacts.

## Figures and tables

- Fig. 1: loop diagram.
- Fig. 2: training-era total and leakage subscore by era, per condition, with run-to-run spread.
- Fig. 3: layer distance (match / adjacent / miss) by era and condition.
- Table 1: eras and windows. Table 2: rubrics. Table 3: run 001 trajectory. Table 4: ablation results.

## Must be true before submission

- [ ] At least 5 runs per condition, with players and judge from different model families.
- [ ] Hypotheses fixed in the repository before the v2 runs start.
- [ ] Human ratings on a stratified sample, with agreement statistics.
- [ ] Every quantitative claim in the paper traceable to a file in `runs/` or `results/`.
- [ ] Pilot observations restated as hypotheses, and each one either supported or dropped.

> Superseded by the full manuscript in [`../paper/`](../paper).
