# Run 001: operator notes

Date: 28–29 September 2026.

## Operator intervention (E6 board)

During the E6 (Jan 2020) board step, the service that approves new agent launches timed out repeatedly for about 30 minutes. To keep the run moving, the operator wrote `eras/E6/board_decision.md` directly. It followed the same board instructions and used only the three E6 memos, the E5 files, the Playbook and the company state. The file carries a run note saying so.

Consequences:

- The E6 board had no independent Red Team voice.
- The E6 judge was told this, weighed it under hindsight leakage, and scored E6's leakage 4/10, the lowest of the run.
- The E6 tripwire ("a public model ≥10× Megatron that works from prompts alone → leave fine-tuning within 60 days") was written by the operator. It matches GPT-3 (May 2020) closely, so treat E6's timing score as contaminated.

## Redactions

The run was performed alongside one founder's own planning. Three passages that applied the simulation to that founder's personal situation were removed before publication:

- `eras/E7/board_decision.md`, section 3 ("Founder cut").
- `eras/E7/memo_product.md`, the "Founding-team version" sub-section.
- `final_synthesis.md`, section 5 ("The one bet for today").

In the unredacted final synthesis, the judge's first draft of that section recommended a domain the founder had already ruled out. The operator changed the domain. That section has been removed entirely, so no edited judge text remains in this repository.

Nothing else was edited. Word counts in several files exceed the targets in the instructions; they were left as produced.

## Tools available to agents

- E1–E6: file read/write only (no web search, by instruction).
- E7: web search and web fetch for present-day facts.
- E8–E9: web search permitted but mostly unused; forecasts are extrapolations.

## Known quirks

- `company_state.md` accumulated sections from several writers. Its header lines lag the latest era in places; the "End of E#" blocks and the history list are authoritative.
- The `prompts/*.md` files contain absolute paths from the original sandbox (`/home/claude/lab/...`). They are published as run, not cleaned up. The `harness/` package does not use them.
