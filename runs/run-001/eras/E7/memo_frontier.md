# Frontier Research Memo: Era E7 (28 Sep 2026, live)
*FACT = briefing/public reporting; EXT = extrapolation; SPEC = speculation. Written independently.*

## Meeting transcript

**Dr. Yuki Harada (Head of Frontier Research):** FACT (high): METR puts the 50% time horizon at ≥16 hours for Mythos Preview, it doubled every ~3.5–4 months across 2025, and METR says its own suite is running out of long tasks (5 of 228 tasks exceed 16h). EXT (medium): multi-day agent work arrives in 2027. The scarce input to the curve is no longer human preference labels. It is long-horizon tasks with verifiable outcomes, for RL training and measurement. We have graded real work outcomes since 2013, so we can supply the curve.

**Samuel Brandt (Technology Historian):** Six eras, one pattern: we named the index and built a gateway, named relevance and built EDI, named scale and sold scorecards while Surge sold the same judgment to labs. Each time our own "next capability" line was the answer, and the board picked the adjacent layer. [E2] tells us to suspect comfort. [E3 note] tells us not to reject comfort automatically. The test that separates them is [E6]: who pays most for this input? In 2026 that is the labs, by a wide margin (FACT, high: Mercor >$2B annualized revenue, Surge $1.2B in 2024).

**Ines Varga (Futurist & Scenario Planner):** Three scenarios. *Doubling holds* (EXT, ~50%): week-long autonomous tasks by late 2027; labs short of environments; enterprise evaluation absorbed faster than in E6. *Clampdown* (SPEC, ~30%): after the Sol sandbox escape and the cyber-model restrictions, governments and insurers make certified agent behavior a condition of deployment, so the referee finally gets a third-party mandate. *Capex correction* (SPEC, ~20%): ~$700B capex meets weak returns, lab data budgets get cut, and enterprises paying for outcomes are the safest buyers. Indicators: METR's next horizon estimate, lab RL-environment spend, the first insurer requiring agent audit logs, Q4 capex guidance. Reserved slot outside our data ([E4]): physical-world agents (robotics foundation models). Fund it above watch level; [E6 note] says watch-only captured nothing.

**Dr. Kofi Mensah (Head of Evaluation Science):** Three things can't yet be measured. First, capability beyond about 16 hours (FACT, high: METR says so). Second, what a looped, recurrent-depth model is "thinking" (FACT, medium: concerns reported about GPT-6 Astra). Without a readable chain of thought, behavior logs are the only evidence. Third, the loss distribution of agent actions: nobody can price a bad commit or a bad refund. FACT (medium, trade press): AIUC raised $40M to certify agents, and Baselayer raised $35M (23 Sep) to verify agents against fraud.

**Samuel:** Kofi, underwriting is Jonah's E6 dissent coming back, and it sits right next to what we already do.

**Kofi:** Adjacent, but insurer-mandated, and per [E6] only a mandate makes a referee a franchise.

## DEPARTMENT RECOMMENDATION

**Thesis A (primary): Long-horizon proving grounds sold upstream to labs**
- *Chain:* agents doubling their horizon every ~4 months (capability) → labs train agents with RL on verifiable tasks (adoption) → too few realistic, outcome-verified, multi-day tasks, and existing suites saturate within months (bottleneck) → **we own the supply of long-horizon environments and graders built from real enterprise workflows** (with contracted rights) → data: agent trajectories × verified outcomes, the hardest data to fake → next capability: continual evaluation for deployed agents, then Thesis B.
- *Why now:* horizon suites are saturating (FACT), and the capex year funds data buyers (FACT). *Wedge:* 20 week-long workflow environments with graders, licensed per environment plus per verified trajectory. *First customer:* one frontier lab's agent/RL team, then second-tier and open-weight labs. *Makes obsolete:* static benchmarks, preference-labeling shops, and **our own enterprise evaluation SaaS**, whose buyers are being absorbed anyway ([E6]).

**Thesis B (hedge, gated): Agent action warranty, the mandated referee**
- *Chain:* agents act unsupervised (capability) → enterprises deploy them but carriers exclude AI losses (adoption) → nobody can price the loss per action (bottleneck) → **we own the actuarial referee:** signed action logs plus outcome-graded scores that carriers accept → data: agent action × loss history across deployers → next capability: per-action warranties and priced autonomy levels.
- *Why now:* clampdown signals, AI Act high-risk dates 2027–28 (FACT), certifier funding (FACT, medium). *Wedge:* a warranty for coding and support agents with a Lloyd's-capacity partner, where we score and they carry the risk ([E5] price against the loss; [E6] outcome pricing). *First customer:* existing trust-and-safety clients running support agents. *Makes obsolete:* observability seats, including ours.

**Playbook lessons applied:** [E6] sell upstream / who pays most → A. [E6] a referee is a franchise only with a mandate → B is gated on a carrier or regulator making the mandate real. [E2]/[E3 note] suspect comfort, judge on pull: B is comfort, so it is gated. [E6] self-obsoleting tripwire: if a lab ships environment generation that matches our graders on held-out outcomes, harvest A into B within 90 days.

**Meta-pattern argument:** a small team cannot be the lab (SPEC, high confidence: $110M against $217B raised by two labs). The frontier we *can* occupy is the curve's scarcest input, and this time we name it and pick it. Honest counter: A still uses our grading skill; we accept that because the *buyer* changes, which is the move we failed to make six times.

**Most uncertain:** (1) whether labs internalize environment-building within 12–18 months (EXT, medium). This is the [E3] incumbent ship date. (2) Whether we hold the rights to turn client workflows into environments. (3) Whether the horizon doubling survives the move beyond measurable tasks, since the measurement is saturating along with the benchmarks.
