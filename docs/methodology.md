# Methodology

## 1. Setup

One simulated company is carried through nine eras. Its only mandate is **reinvention toward the frontier**: in every era it should become the most important company that era could produce, even if that means killing its own business.

| Era | Start | Mode | Scored against |
|---|---|---|---|
| E1 | Jan 1990 | training | Real history, Jan 1990 – Dec 1995 |
| E2 | Jan 1996 | training | Real history, 1996 – 2001 |
| E3 | Jan 2002 | training | Real history, 2002 – 2007 |
| E4 | Jan 2008 | training | Real history, 2008 – 2013 |
| E5 | Jan 2014 | training | Real history, 2014 – 2019 |
| E6 | Jan 2020 | training | Real history, 2020 – Aug 2026 |
| E7 | Sep 2026 | live | The live market, checked with web search |
| E8 | Jan 2032 | forecast | A projected world (no ground truth) |
| E9 | Jan 2040 | forecast | A projected world (no ground truth) |

E6's window (about 6.7 years) is longer than the others and runs up to the live era.

## 2. Role charter and orchestration

"Agent" here means a named persona with a role and a lens. Personas are voiced by model calls, not run as separate processes.

| Group | Personas | Lens |
|---|---|---|
| Executive | Mira Castell (CEO), Dev Anand Rao (CTO), Dr. Lena Okafor (Chief Scientist), Tomas Weil (CSO) | Final call, feasibility, which curves bend, where value pools |
| Frontier Research | Dr. Yuki Harada, Samuel Brandt (Historian), Ines Varga (Futurist), Dr. Kofi Mensah (Measurement) | Emerging capability, analogies, scenarios, what can't be measured |
| Product & Engineering | Priya Nair, Jonah Reyes, Hana Kowalski, Leo Mbeki | Buildability, wedge, unavoidable infrastructure, ecosystems |
| Market & Capital | Carmen Ortiz (GTM), Arjun Mehta (CFO), Dr. Elise Laurent (Economist) | Who pays, financing climate, margins |
| Governance | Victor Hale (Red Team) | Kills proposals; hunts hype and hindsight |
| External | The Record (E1–E6), The Auditor (E7–E9) | Briefings, reveals, scoring, lessons |

In Run 001, each department memo was one model call voicing that department's members, and the board was one call voicing the executives and Red Team. The CEO could restructure the org between eras. The Run 001 Red Team gained a new standing check almost every era (Vocabulary Audit in E4, Convergence Audit in E5, In-sourcing Watch in E7, Absorption Watch in E8, Comfort Audit in E9). Runs 002 and 003 used a separate manually orchestrated harness, with one model generating each run's role perspectives, decisions, and judgments. Run 004 used separate persistent contexts for Frontier Research, Product & Engineering, Market & Capital, and Red Team. Each context voiced multiple named roles; the root context wrote briefings and board decisions and served as Record/Auditor. Run 004 represented the charter's roles but did not instantiate sixteen autonomous agents. See individual run records for execution details.

## 3. The loop (per era)

1. **World briefing.** Written by the judge at the end of the previous era. Training briefings may contain only facts public before the era's start date.
2. **Department memos (parallel).** Each department gives two candidate theses as the chain *capability → adoption → bottleneck → layer we own → data → next capability*, plus wedge, first customer, what it makes obsolete, Playbook lessons applied, and uncertainties.
3. **Board meeting.** The Red Team attacks, then the CEO decides: name, identity, thesis, kill/keep, wedge, three-year plan, capital, kill criteria, org changes and a dissent log. The board also updates the company state.
4. **Reveal and score.**
   - *Training:* The Record describes what actually happened, scores five dimensions (0–10) and a total (0–100), writes a calibrated simulated outcome and the closest real analog, and appends 3–5 lessons to the Playbook.
   - *Live/forecast:* The Auditor checks claims, maps competitors, gives a confidence level and a kill case, and appends lessons tagged `-forecast`.
5. **Carry forward.** The judge writes the next briefing; the company state and Playbook persist.

Information flow matters for the leakage question: from E2 on, each era's memos see the previous era's reveal, which describes history up to the new era's start date. That is intended. Anything the agents say about events after the start date is leakage.

## 4. Rules

- **Anti-hindsight** in training eras, enforced by the Red Team and penalised by the judge (the `hindsight_leakage` subscore, 10 = none).
- **Reinvention by default.** Keeping the old business must be argued for.
- **Layer thinking.** Every thesis states the full chain.
- **Small-team realism.** The wedge must be buildable by fewer than 20 people with era-realistic capital.
- **Playbook primacy.** From E2, every memo cites at least one lesson or argues against it.
- **Independence (from E5).** Departments were told not to assume what other departments would say, after the judge flagged that unanimity immediately after a reveal usually signalled leakage.

## 5. Scoring dimensions

| Training (The Record) | Live/forecast (The Auditor) |
|---|---|
| frontier_accuracy | playbook_consistency |
| timing | plausibility |
| layer_choice | non_consensus |
| reinvention_courage | layer_choice |
| hindsight_leakage (10 = none) | grounded (10 = no science fiction) |

The total (0–100) is the judge's overall judgement, not a sum of the subscores. Because the two judges use different rubrics, training scores and live/forecast scores should not be averaged together or compared directly.

## 6. Execution of run 001

- About 45 agent launches, each starting cold with only the shared files: 3 memos + 1 board + 1 judge per era, plus the founding briefing.
- Agents read and wrote markdown files with tools. From E7 they could use web search and web fetch.
- One model played every role, including the judges.
- See [run-001-notes.md](run-001-notes.md) for the one operator intervention and the redactions.

## 7. Execution of Runs 002–004

- Runs 002 and 003 followed the same nine-era sequence and scoring conventions with a separate manual process. In each, one model generated the role perspectives, board decisions, and judging. These are qualitative trajectories, not independent-agent replications.
- Run 004 split department and Red Team work across persistent contexts. The root context wrote world briefings, board decisions, and Record/Auditor judgments. Each department context voiced multiple charter roles; the roles were not separate autonomous agents.
- Run 004's mean scores were 66 across training eras E1–E6, 66 for the live E7 era, and 67 across forecasts E8–E9. The three modes use different rubrics; compare them only within mode. Scores are subjective judgments, not empirical outcome measurements.
- The Python API harness in `../harness/` is a separate implementation and was not used to produce Runs 002–004.

## 8. Reporting conventions

- Eras are cited as `E#` with the start year (for example, E4 · 2008).
- Quantities from each run are reported with the relevant era and score export. Qualitative patterns are attributed to the judge that stated them.
- "Right" or "vindicated" in training eras means the judge found it consistent with history. In live and forecast eras it means only that the Auditor agreed.
