# Run 004

Run 004 is a qualitative, multi-context simulation conducted 2026-09-29 using the Frontier Lab's nine-era sequence and scoring rubric. It preserves the Run 001–003 records and is a new trajectory.

## Orchestration and limits

For each era, three department memos were produced in separate assistant sub-agent contexts: Frontier Research (four named roles), Product & Engineering (four roles), and Market & Capital (three roles). A separate Red Team context critiqued the proposals. The root context wrote the dated briefing, convened the simulated executive board, and acted as Record/Auditor for the reveal and scoring. The sixteen charter roles are represented, but this was not sixteen separately instantiated agents: role voices inside each department memo share that department context, and board/judging share the root context. No private chain-of-thought is collected or represented as evidence. This is therefore a multi-context role simulation, not a controlled experiment, independent multi-agent replication, or proof that the Playbook improves strategy.

Historical briefings are bounded to each era's start date as a discipline; model pretraining makes complete hindsight control impossible. Scores are subjective judge assessments. E7 uses current cited sources; E8–E9 are conditional forecasts without an answer key. Consult each era folder for the briefing, three memos, independent critique, decision, reveal, and scorecard. `scores.csv` is the run-level score export; the main repository README summarizes the trajectory.

## Results

See [`final_synthesis.md`](final_synthesis.md), [`company_state.md`](company_state.md), [`playbook.md`](playbook.md), and [`scores.csv`](scores.csv).

## Review note (29 Sep 2026)

- **Probable exposure to Run 001.** The company begins as "Switchyard Systems", Run 001's E1 name. The run was probably generated with the repository's Run 001 records visible; treat it as conditioned on Run 001, not as an independent replication.
- **Judge independence.** The root context that wrote the briefings and board decisions also acted as Record/Auditor, so the judge scored its own decisions.
- **Rubric effect.** Hindsight discipline counts toward the total (sum × 2). The company never built a product across the nine eras (every decision is a gated manual pilot) yet has the highest training mean of the four runs. The rubric has no measure of whether the company reached where value pooled.
- **Briefing selection.** Dated briefings contain only pre-era facts, but choosing which signals to foreground (for example the 1989 CERN proposal in E1) can itself reflect hindsight.
