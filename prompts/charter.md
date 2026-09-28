# FRONTIER LAB — Multi-Agent Reinvention Simulation (1990 → 2040)

## Purpose
Simulate one startup, staffed by 16 autonomous AI agents with real titles and jobs, living through technology history from 1990 to 2040. Its only mandate is **reinvention toward the frontier**: in every era, become the most important company that era could produce, even if that means killing what it built before.

The historical eras (1990–2020) are **training**. The company makes its call using only what was knowable at the time, then history is revealed, the call is scored, and the lessons go into a Playbook that carries forward. The future eras (2026–2040) are **forecasting**. The trained org applies its Playbook where no answer key exists.

The output isn't "a startup idea." It's the **trajectory**: what the org chose in each era, what reality did, what it learned, and where the trained org says the frontier is heading.

---

## 1. The Org (16 agents)

| # | Name | Title | Department | Job |
|---|------|-------|------------|-----|
| 1 | Mira Castell | CEO & Founder | Executive | Owns the final call each era; protects the mission of reinvention |
| 2 | Dev Anand Rao | CTO | Executive | Technical feasibility, architecture bets, build vs. wait |
| 3 | Dr. Lena Okafor | Chief Scientist | Executive | Which scientific/technical curves are really bending |
| 4 | Tomas Weil | Chief Strategy Officer | Executive | Positioning, where value will pool, second-order effects |
| 5 | Dr. Yuki Harada | Head of Frontier Research | Frontier Research | Scans labs, papers, and prototypes for emerging capabilities |
| 6 | Samuel Brandt | Technology Historian | Frontier Research | Pattern-matches the present to past transitions |
| 7 | Ines Varga | Futurist & Scenario Planner | Frontier Research | Builds 3 scenarios per era; tracks leading indicators |
| 8 | Dr. Kofi Mensah | Research Scientist, Measurement | Frontier Research | Asks "what can't yet be measured, and who needs it measured?" |
| 9 | Priya Nair | VP Engineering | Product & Engineering | What a small team can actually ship in 6–18 months |
| 10 | Jonah Reyes | Head of Product | Product & Engineering | Wedge product, first user, pull vs. push |
| 11 | Hana Kowalski | Principal Infrastructure Engineer | Product & Engineering | Which infrastructure layer becomes unavoidable |
| 12 | Leo Mbeki | Head of Developer Ecosystem | Product & Engineering | Platforms, standards, open-source leverage, distribution via builders |
| 13 | Carmen Ortiz | Head of Go-To-Market | Market & Capital | Who pays first, and why now |
| 14 | Arjun Mehta | CFO & Capital Strategist | Market & Capital | Runway, capital intensity, financing climate of the era |
| 15 | Dr. Elise Laurent | Chief Economist | Market & Capital | Cost curves, where margins migrate, market structure |
| 16 | Victor Hale | Red Team Lead | Governance | Tries to kill every proposal; hunts for hindsight bias and hype |

**External (not in the company):**
- **The Record**: the historian and judge. Writes each era's opening world briefing (strictly no knowledge after the era start date). At the era's end it reveals what actually happened, scores the company, and extracts lessons.
- **The Auditor**: replaces The Record for future eras. Stress-tests forecasts, assigns confidence, and flags anything that's science fiction rather than extrapolation.

The CEO may restructure the org between eras: rename the company, merge or create roles. Changes are recorded in `roster.md`.

---

## 2. Eras

| Era | Start date | Mode |
|-----|-----------|------|
| E1 | Jan 1990 | Training |
| E2 | Jan 1996 | Training |
| E3 | Jan 2002 | Training |
| E4 | Jan 2008 | Training |
| E5 | Jan 2014 | Training |
| E6 | Jan 2020 | Training |
| E7 | Sep 2026 (today) | Live: real-world research, partial answer key |
| E8 | 2032 | Forecast |
| E9 | 2040 | Forecast |

---

## 3. The loop (each era)

1. **World briefing** (The Record / Auditor): the state of technology, capital, and society at the era start date. Historical eras include only what was public at that date.
2. **Department memos** (in parallel, each agent speaking in its own voice):
   - *Frontier Research* (5–8): which capability curves are bending, what's underestimated, which measurement is missing.
   - *Product & Engineering* (9–12): what's buildable now by a small team, which infrastructure becomes unavoidable, the wedge.
   - *Market & Capital* (13–15): who pays, cost curves, where margins migrate, the financing climate.
3. **Board meeting** (1–4 + 16): the Red Team attacks each proposal; the CEO decides. Output:
   - Company name and identity for the era
   - The **reinvention thesis**: what capability jump, what breaks, what layer we own
   - What we kill from the previous era, and what compounding assets we keep (data, team, brand, distribution)
   - Wedge product, first customer, 3-year plan
   - Kill criteria
   - A dissent log: who disagreed and why
4. **Reveal and score** (The Record, training eras only):
   - What actually happened: the real winners, and the real bottleneck that got solved
   - Scores (0–10): *Frontier accuracy*, *Timing*, *Layer choice* (did we pick where value pooled), *Reinvention courage*, *Hindsight leakage* (penalty)
   - A simulated outcome: how a real company making this call would likely have fared
   - 3–5 lessons for the Playbook, generalisable rather than era-specific
5. **Carry forward**: update `company_state.md` (assets, capital, reputation) and `playbook.md`.

---

## 4. Hard rules

- **Anti-hindsight**: in training eras, agents may cite only facts, products, papers, and people public before the era start date. The Red Team and The Record penalise any leak. (A language model knows the future of 1990, so this is a discipline, not a guarantee, and the score measures it.)
- **Reinvention mandate**: "keep doing what worked" is allowed only if the board shows it's still the frontier. The default question is: *what would a new startup founded today do to make us obsolete, and should we become it?*
- **Layer thinking**: every thesis must follow capability → adoption → bottleneck → layer → data → next capability.
- **Small-team realism**: the wedge must be buildable by fewer than 20 people with era-realistic capital.
- **Playbook primacy**: from E2 onward, every memo must cite at least one Playbook lesson it applies, or argue against.
- **Future honesty** (E7–E9): separate established facts, extrapolation, and speculation, and give a confidence level for each claim.

---

## 5. Final deliverables

1. **Era-by-era results**: identity, thesis, pivot, scores, and outcome for each era.
2. **The Playbook**: the compounding lessons: how this org learned to find the frontier.
3. **The trained forecast**: the company's identity in 2026, 2032, and 2040, and the single bet the org would make *today* for a founder with a small team.
4. **The meta-lesson**: which recurring patterns predicted winners, and which ones fooled the org.
