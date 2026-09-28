# Frontier Research Memo: Era E8 (Jan 2032, forecast)
*Tags: FACT(2026) = public by Sep 2026; EXT = extrapolation; SPEC = speculation. Confidence H/M/L. Question put to the department: in a world of agents that work for weeks, what becomes the scarce, unmeasured, unowned thing?*

## Transcript

**Dr. Yuki Harada, Head of Frontier Research:** The curve didn't stop. It stopped being legible. METR's suite was saturating at ≥16h in 2026 (FACT(2026), H), and looped models were already weakening chain-of-thought monitoring (FACT(2026), H). By 2032 the labs report "autonomous work-weeks" (EXT, M). With reasoning uninspectable, what's left to check is what the agent was *allowed* to do and what *happened* afterwards.

**Samuel Brandt, Technology Historian:** This is the oldest problem in commerce: an agent acting for a principal over time and distance. Every earlier fix was a record of *mandate* plus a *settlement*: power of attorney, the bill of lading, double-entry books, the letter of credit. The money went to whoever cleared what the captain did against what the owner authorized. My worry is [E3]: whoever runs the agent absorbs the record. A lab's console will offer "approvals" for free.

**Ines Varga, Futurist & Scenario Planner:** Three scenarios. *Consolidated (45%)*: three lab-platforms run most enterprise agents, and mandate plus audit ship as bundled features. *Plural (40%)*: enterprises run frontier and open-weight agents side by side, because cost-sensitive work goes to Chinese open weights 6–12 months behind (EXT, M), so someone neutral has to hold cross-agent authority. *Shock (15%)*: a correlated agent-loss event forces sublimits (SPEC, M), and carriers demand a mandate record overnight. Indicators: multi-vendor agent share, insurer log requirements beyond OTel traces, outcome-contract disputes.

**Dr. Kofi Mensah, Research Scientist, Measurement (Head of Environments & Graders):** *Scarce*: accountable human sign-off. A qualified person who can accept three weeks of agent work and be liable for it. That supply shrinks as entry-level hiring collapses (EXT, M), which is exactly where tomorrow's reviewers used to come from. *Unmeasured*: **intent drift and delayed outcomes**. Over 3 weeks the spec changes 20 times in Slack, and the real grade (did the reconciliation survive audit, did the migration hold at 90 days) arrives months after the agent is paid. Traces measure actions, not actions against evolving intent or consequences at t+90. *Unowned*: **the mandate itself**. The lab owns the agent, the platform owns the logs, the insurer owns a questionnaire, and HR owns the human. The chain "who delegated what authority, with what budget, revised when, accepted by whom" belongs to nobody.

**Samuel:** And unowned layers are usually unowned because they're worthless.

**Kofi:** Or because the mandate that makes them valuable hasn't arrived yet. [E6] says a referee needs a third party that requires it. Outcome-priced contracts (EXT, M: the default model) create two parties who need the same number.

## DEPARTMENT RECOMMENDATION

**Thesis 1: The Mandate Ledger (delegated-authority registry)**
Multi-week autonomous agents → enterprises delegate projects with budget, credentials and spend authority → bottleneck: nobody can prove the scope of authority, its revisions, or who accepted the work, across agents from several vendors, and monitoring of reasoning is failing → **we own the neutral, signed record of delegation, revision and acceptance** → data: intent spec × revisions × actions × human acceptances and overrides → next capability: *priced authority*, meaning per-agent credit-limit-style authority ceilings that insurers and auditors accept.
- *Why now:* reasoning is no longer inspectable; AI Act high-risk duties apply and insurers require tamper-evident logs (EXT, M).
- *Wedge:* authority limits plus acceptance sign-off for finance-ops agents running across 2+ model vendors.
- *First customer:* a fund administrator or mid-market controller group whose auditors reject "the agent did it" (Moffatt precedent, FACT(2026), H).
- *Makes obsolete:* point-in-time continual certification (our own 2028 pivot) and trace schemas treated as the product.

**Thesis 2: Outcome Settlement (the delayed-truth clearing house)**
Agents priced per outcome → buyer and vendor dispute what counts as success weeks or months later → bottleneck: delayed ground truth is uncollected and unneutral → **we own settlement: linking each unit of agent work to its consequence at t+30/90/365 and clearing payment against it** → data: work × delayed consequence, a signal labs cannot see from their own products → next capability: loss-priced warranties settled on the same file (Assure, finally with its own data).
- *Why now:* outcome pricing is the default (EXT, M), and multi-week tasks outgrew cheap verification (EXT, M).
- *Wedge:* escrowed settlement for outcome-priced agent contracts in software migrations and reconciliations.
- *First customer:* an agent vendor selling on outcome price to a regulated buyer that won't accept the vendor's own grading.
- *Makes obsolete:* Foundry's simulated environments, because a real settled outcome beats a synthetic one.

**Playbook applied:** [E4] "own the referee" plus [E6] "a referee needs a mandate": in Thesis 2 the mandate is the counterparty contract, not a regulator. [E7-forecast] "sell rights, not labor": consequence data exists only where the buyer's books are, not in a lab's product. [E7-forecast] "don't sell the funnel": settlement *is* the funnel. [E2] "defensible data accrues to voluntary intent": the mandate is recorded intent. **Argued against:** [E3] "the auction owner absorbs." It holds in Ines's Consolidated scenario (45%), which is the case against us. [E2] adjacent-layer alarm is live: both theses sit next to our ledger.

**Most uncertain about:** whether plurality of agent vendors survives (Thesis 1 dies in a three-platform world); attributing delayed outcomes when agents chain (SPEC, L-M); and whether "human acceptance" persists as a legal requirement or gets automated away by agents grading agents. If sign-off disappears, the scarce thing becomes the *liability-bearing entity* (who can be sued), and that points to insurers or new agent-bonding firms, not to us.
