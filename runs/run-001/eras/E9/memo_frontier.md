# Frontier Research Memo: Era E9 (Jan 2040, forecast)
*Tags: FACT(2026) / EXT / SPEC, confidence H/M/L. Start: E8 Auditor base case (EXT, M), with Clearwork as a consequence-data and acceptance-standards company at ~$200–260M revenue. Question: once human sign-off is gone, what is scarce, and who holds the loss?*

## Transcript

**Dr. Yuki Harada, Head of Frontier Research:** In the base branch (~55%) power and *real-world verification* bind progress, not algorithms (EXT, M). Agents run quarter-long projects and propose materials and drug candidates faster than anyone can check them. The frontier question is now "who confirms it happened, and who pays if it didn't."

**Samuel Brandt, Technology Historian:** When the human signatory goes, liability doesn't vanish. It moves to a bonded party. Ship masters gave way to hull insurers and classification societies, and clerks gave way to fidelity bonds. My warning: we have been the recorder beside the risk-holder for eight eras, and in this era the recorder's share is the smallest it has ever been.

**Ines Varga, Futurist & Scenario Planner:** Each branch needs its own thesis. *Base (55%)*: safe harbors, deployer liability and verification scarcity. *Slowdown (25%)*: cheap open-weight agents deployed by millions of small firms with no risk function, so bonding demand *rises* and verification demand falls. *Acceleration (20%)*: 2–3 lab-state compacts, where the only neutral work left is verifying what they claim (SPEC, L). Indicators: finance safe harbors, premium-pool concentration, open-weight lag, and whether a correlated-loss event has happened.

**Dr. Kofi Mensah, Head of Consequence Science:** *Scarce*: a party that can be sued for an agent's action, and capacity to confirm physical claims. *Unmeasured*: the **authority-weighted loss rate per agent configuration**, meaning losses per dollar of delegated authority by model version, permissions and deployer. Carriers still price per deployer. *Unowned*: the per-agent limit. Our t+30/90/365 history is the only priced record that could size one.

**Samuel:** Then we'd have to hold the variance, the thing we refused in E5, E7 and E8.

**Kofi:** Hold it the way managing general agents do: we write the terms, and carriers supply the capacity. [E8]: whoever holds the variance sets the evidence standard.

## DEPARTMENT RECOMMENDATION

**Thesis 1: Agent Surety (the bonding house for agents that act without sign-off)**
Quarter-long autonomous agents → safe harbors remove per-task human acceptance and put liability on deployers (EXT, M) → bottleneck: deployers can't size or transfer the loss per agent, and "bonded agent" regimes need an issuer (SPEC, L-M) → **we own per-agent bonding and authority limits as an MGA, with capacity from 2–3 carriers who co-own the vehicle** → data: bond × authority used × claims × consequence → next capability: dynamic authority pricing, a live credit line for each agent that tightens after model updates or drift.
- *Why now:* the sign-off requirement has fallen away (EXT, M), and the premium pool is large and concentrated (EXT, M; size L).
- *Wedge:* bonds for open-weight agents run by mid-market deployers in lending ops and procurement.
- *First customer:* a regional lender using a safe harbor, whose incumbent carrier will quote only a blanket sublimit.
- *Makes obsolete:* our acceptance-protocol standard (nobody has to sign) and our consequence-data licences to carriers (we underwrite with that data instead of selling it).
- *Branches:* base: strong. Slowdown: strongest, because cheap agents, many deployers and thin risk teams mean more bond demand. Acceleration: weak, since the compacts self-insure.
- *Premise count ([E8] stacked):* safe harbors (0.6) × carriers grant capacity rather than build it themselves (0.5) × per-agent pricing beats per-deployer pricing (0.6) ≈ **18%**. Bonded personhood isn't required, so it is upside only.

**Thesis 2: Ground-Truth Exchange (verification capacity for agent-generated claims)**
Discovery agents produce candidates faster than labs can verify them (EXT, M) → bottleneck: physical verification and replication are what bind the base branch → **we own brokered, independently attested verification**: routing claims to contracted autonomous labs and test facilities, and issuing signed replication certificates that regulators, licensors and carriers accept → data: claim × replication outcome → next capability: replication-probability models that let us price a claim before it is tested.
- *Why now:* verification, not generation, bounds progress, and margins pool in proprietary real-world data (EXT, M).
- *Wedge:* replication certificates for agent-discovered materials claims that enter licensing deals.
- *First customer:* a materials licensor or a mid-size pharma that is buying claims from discovery-agent vendors.
- *Makes obsolete:* software-agent certification, which is our legacy, along with Foundry-style synthetic graders.
- *Branches:* base: strong. Slowdown: modest. Acceleration: the **only thesis that survives**, because automated research makes independent verification (and, as a variant, verifying compliance with compute and access controls) the neutral scarce input (SPEC, L).
- *Premise count:* verification remains the bottleneck (0.55) × labs don't vertically integrate the facilities (0.4) × certificates are accepted by counterparties (0.6) ≈ **13%**.

**Playbook applied:** [E8] "whoever holds the variance" drives Thesis 1: we finally take the loss, with carriers as co-owners ([E8] "flow-holders co-own"), which also applies [E5] "price against the loss." [E4] reserved slot and [E5] "scarce inputs" drive Thesis 2, since verification capacity is this era's scarce input and it sits outside our own data. [E8] early liquidity gate: Thesis 1 needs ≥$50M in bonded authority and ≥2 capacity carriers by month 12. **Argued against:** [E2] hub-and-spoke says carriers will own the graph. We accept that and give them equity. Our no-balance-sheet rule is relaxed only in the MGA form, with no float held.

**Most uncertain about:** which pace branch we are in. The two theses are a hedge: Thesis 1 covers base plus slowdown, and Thesis 2 covers base plus acceleration. We are also unsure whether per-agent losses stay stable enough to price across monthly model updates, and whether carriers will treat us as a partner or as a feed. At these odds, the board should fund the fallback (consequence-data licensing) as the base case.
