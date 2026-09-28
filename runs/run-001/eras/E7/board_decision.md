# Board Decision — Era E7 (28 September 2026, live)
*Present: Mira Castell, Dev Anand Rao, Dr. Lena Okafor, Tomas Weil, Victor Hale. Tags: FACT / EXT (extrapolation) / SPEC (speculation), with confidence H/M/L.*

## 1. Transcript highlights

**Victor (Convergence Audit):** All three departments split between the same two theses: (a) agent-action underwriting evidence and (b) long-horizon environments sold to labs. [E4] unanimity alarm: (b) is the E6 reveal's "road not taken" (Surge), (a) is Jonah's E6 dissent. We are answering the last scorecard.

**Victor on (a), the adjacent-layer test:** Six eras running we chose the layer next to our own asset; (a) is built on the 1996 ledger and our own customers. Three attacks. *Mandate thinness*: ISO exclusions and a handful of specialist carriers (FACT, M) are not a mandate. AIUC already has $40M, Beazley paper and its own standard, AIUC-1 (FACT, M). *Carrier absorption*: Beazley says it is pricing AI risk into its cyber book (FACT, M, one trade report), so agent risk may fold into existing lines with no separate referee. *No loss data*: incidents are rare and correlated (EXT, M). Comfort, with unproven pull.

**Jonah:** The pull is Moffatt, the exclusions and the AI Act logging dates. Every one of them is a third party forcing evidence.

**Victor:** Forcing evidence that AIUC and the carriers' own cyber forms already collect. The [E3 note] test is to judge on pull. Name one carrier that will bind on our file in 2027.

*(Nobody named one.)*

**Victor on (b), the in-sourcing test:** Labs hire RL-environment engineers directly; 40+ vendors plus Mercor and Surge sell environments (FACT, M); Scale lost OpenAI overnight (FACT, H). Concentrated buyers who can build what they buy. The "≥16h" figure rests on one METR point estimate with a CI of 8.5–55h (FACT, H), and "doubling every 3.5–4 months" is an analyst fit (EXT, M). Surge's window was 2020–24; 2026 is not early.

**Lena:** Then sell only what labs *cannot* build: consented enterprise workflows and real deployed-agent failures. Enterprise API terms generally bar labs from training on customer data (EXT, M).

**Tomas:** (b) changes the *buyer*, which [E6] says we failed to do six times. (a) changes only the *pricing*.

**Dev:** The code is shared. Signed recorder → adversarial scenarios → graders. A scenario that breaks an agent is both an RL environment and a certification test.

**Arjun:** The evaluation/observability category is being bought right now (Galileo, Langfuse, Promptfoo: FACT, H). [E4]: sell on the credit calendar.

**Carmen (dissenting):** Selling the dashboard sells the funnel that produces the traces Lena needs.

**Mira:** Carve it so it doesn't. We decide.

## 2. DECISION

**Name:** **Proofworks** (renamed from Clearproof). The evaluation SaaS keeps the Clearproof name inside a sale process.
**Identity:** "We build the hard-to-fake, long-horizon work that frontier agents are trained and certified on, from real enterprise workflows and real agent failures."

**Reinvention thesis:** agent horizons of ~16h+ with fast doubling (FACT H / EXT M) → labs train agents by RL on verifiable tasks, and enterprises deploy them with production authority (FACT, H) → realistic, reward-hack-resistant, multi-day tasks with verified outcomes are scarce, and suites saturate within months (FACT, H) → **we own the environment and grader supply built from consented enterprise workflows and deployed-agent failure traces** → data: agent trajectories × verified outcomes × real incidents → next capability: continual certification of deployed agents, then loss-priced agent warranties once a carrier mandate is real (SPEC, M-L).

**Victor's rulings, adopted:** (a) is comfort → a *gated option*, not the identity. (b) is in-sourcing-exposed → differentiate on *rights-bearing real-world data*, not labor.

**KILL:**
- Seat-priced evaluation dashboards as our identity. Run a sale process for the Clearproof SaaS line by Q2 2027 (floor ~$400M, EXT M).
- Clearsight moderation: harvest, and sell by end-2027.
- Any plan that holds insurance risk on our own balance sheet.

**KEEP (carved out of any sale):**
- The signed action ledger, open-sourced as a trace-evidence schema built on OpenTelemetry GenAI.
- Opt-in pooled evaluation results and the 2013–19 corpus, where the rights allow.
- The evaluation-science team, meaning our reward-hacking expertise.
- Trace-contribution rights, written as perpetual data licenses into the SaaS sale contract.

**Wedge:** *Proofworks Foundry*. 30 enterprise-workflow environments (finance ops, support refunds, deploy pipelines, trust & safety), 16–100h each, hardened against reward hacking, with sandbox-escape containment. Priced per environment ($20k–300k, FACT M from Epoch) plus per verified trajectory. Exclusivity windows earn the premium.

**First customer:** two neolabs or open-weight labs plus one government AI safety institute (6-month pilots), then one frontier lab's agent team.

**3-year plan:**
- 2026 Q4–2027: 30 → 150 environments, ≥4 buyers, trace schema adopted by ≥3 agent frameworks.
- 2028: continual certification suites for deployed agents, sold to agent vendors ahead of the AI Act high-risk dates (Dec 2027 / Aug 2028, FACT H).
- 2029: if the gate passes, *Proofworks Assure*: evidence and pricing for a partner MGA on carrier paper.

**Capital:** ~$110M cash, ~$45M ARR. New-bet burn ~$30M/yr. Sale proceeds, if a deal closes, are held as a buffer against a capex correction (Ines puts that at ~20%, SPEC). No raise.

**Reserved slot (10%, funded, not watch):** physical-world agents (robotics foundation models): environments and graders for embodied tasks. It is a curve outside our data ([E4]; the [E6 note] says watch-only captured nothing).

**Kill criteria:**
1. ≥3 paying environment buyers and ≥$8M contracted by 30 Jun 2027. No buyer above 40% of Foundry revenue by end-2027.
2. **In-sourcing tripwire:** if two of the top-3 labs cut external environment spend, or one ships environment generation that matches our graders on held-out outcomes, pivot Foundry to enterprise certification within 90 days.
3. **Assure gate:** a carrier or MGA binds ≥10 policies priced on our evidence by Q4 2027, or the option closes and the schema stays an open standard.
4. **Horizon tripwire:** if METR's next estimate shows doubling slower than 7 months, shift weight to enterprise certification.
5. If no SaaS bid reaches $400M by Mar 2027, keep the line and cut burn to $20M.

**Org changes:**
- Priya Nair → GM, Foundry.
- Dr. Kofi Mensah → Head of Environments & Graders (reward-hack red team).
- Hana Kowalski → Head of Evidence Infrastructure (ledger and schema; not for sale).
- Leo Mbeki → trace-schema standard.
- Jonah Reyes + Carmen Ortiz → Assure option.
- Arjun Mehta → SaaS sale.
- Dr. Yuki Harada → embodied slot.
- Victor Hale adds an **In-sourcing Watch** (a quarterly read on lab hiring and spend).

**Dissent log:**
- **Jonah:** "Third era I've been deferred. The warranty *is* the mandate."
- **Carmen:** "Selling the SaaS starves the trace supply."
- **Arjun:** "Foundry is a concentrated-buyer business. You made it the identity anyway."
- **Elise:** agrees with the decision, but warns that per-environment prices will fall as 40+ vendors compete (EXT, M).
- **Victor:** "The environments call still looks like the E6 answer key. Score us on whether the rights-bearing data moat is real by mid-2027."

## 3. [Redacted]

*A section giving advice for one specific founder was removed before publication. It is not part of the simulation's decision.*
