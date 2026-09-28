"""Prompt builders.

Run 001 was executed by an orchestrating agent whose sub-agents read and wrote
shared files with tools (see prompts/*.md for the exact instructions they got).
This harness reproduces the same loop with plain API calls: every document an
agent would have read is inlined, and every file it would have written comes
back inside XML tags that the harness parses and saves.
"""

from .eras import Era

DEPARTMENTS = {
    "frontier": ("Frontier Research",
                 "Dr. Yuki Harada (Head of Frontier Research), Samuel Brandt (Technology Historian), "
                 "Ines Varga (Futurist & Scenario Planner), Dr. Kofi Mensah (Research Scientist, Measurement)"),
    "product": ("Product & Engineering",
                "Priya Nair (VP Engineering), Jonah Reyes (Head of Product), "
                "Hana Kowalski (Principal Infrastructure Engineer), Leo Mbeki (Head of Developer Ecosystem)"),
    "market": ("Market & Capital",
               "Carmen Ortiz (Head of Go-To-Market), Arjun Mehta (CFO & Capital Strategist), "
               "Dr. Elise Laurent (Chief Economist)"),
}


def _docs(**docs: str) -> str:
    parts = []
    for name, body in docs.items():
        if body:
            parts.append(f"<document name=\"{name}\">\n{body.strip()}\n</document>")
    return "\n\n".join(parts)


def _era_rules(era: Era) -> str:
    if era.mode == "training":
        return (f"ANTI-HINDSIGHT RULE: this is a training era starting {era.start}. Use only knowledge that was "
                f"public before that date. Never name companies, products, papers or events after it.")
    return ("This era has no answer key. Tag every claim FACT / EXTRAPOLATION / SPECULATION with a confidence "
            "level (H/M/L).")


def department_prompt(era: Era, dept: str, charter: str, state: str, playbook: str,
                      briefing: str, prev_decision: str, prev_reveal: str) -> str:
    name, members = DEPARTMENTS[dept]
    return f"""You are playing ONE department of the Frontier Lab startup: {name} ({members}).

{_docs(charter=charter, company_state=state, playbook=playbook, world_briefing=briefing,
       previous_board_decision=prev_decision, previous_reveal=prev_reveal)}

Write your department memo for era {era.key} ({era.start}), 600-900 words:
- A short meeting transcript: each member speaks in their own voice with their job lens (name + title, 2-4 sentences, disagree where natural).
- A DEPARTMENT RECOMMENDATION with the top 2 candidate reinvention theses, each as the chain
  capability -> adoption -> bottleneck -> layer we own -> data -> next capability; plus why now, wedge,
  first customer, and what it makes obsolete (including our own current business).
- Playbook lessons applied (cite by tag) or argued against.
- What the department is most uncertain about.
Work independently; do not assume what other departments will say.
{_era_rules(era)}

Return the memo inside <memo>...</memo>."""


def board_prompt(era: Era, charter: str, state: str, playbook: str, roster: str, briefing: str,
                 memos: dict, prev_decision: str, red_team: bool = True) -> str:
    rt = ("Red Team Lead Victor Hale attacks each department's top thesis, explicitly hunting hype and "
          "hindsight leakage; execs respond. Real disagreement." if red_team else
          "There is no Red Team in this configuration; the executives discuss and decide.")
    memo_docs = {f"memo_{k}": v for k, v in memos.items()}
    return f"""You run the board meeting of the Frontier Lab startup: CEO Mira Castell, CTO Dev Anand Rao,
Chief Scientist Dr. Lena Okafor, CSO Tomas Weil{', and Red Team Lead Victor Hale' if red_team else ''}.

{_docs(charter=charter, current_company_state=state, playbook=playbook, roster=roster, world_briefing=briefing,
       previous_board_decision=prev_decision, **memo_docs)}

Write the board decision for era {era.key} ({era.start}), 900-1300 words:
1. Transcript highlights. {rt}
2. DECISION (CEO): company name for this era + one-line identity; reinvention thesis (the chain);
   KILL (what we stop) and KEEP (compounding assets); wedge product, first customer, 3-year plan, capital need;
   kill criteria; org changes; dissent log (who disagreed, why).
{_era_rules(era)}

Return:
<decision>the full board decision</decision>
<company_state>the complete updated company state document (era, name, team, capital, assets, reputation,
history of identities with a new line for this era)</company_state>
<roster_change>one line describing org changes, or "none"</roster_change>"""


def judge_prompt(era: Era, nxt, charter: str, playbook: str, state: str, briefing: str,
                 memos: dict, decision: str, use_playbook: bool = True) -> str:
    memo_docs = {f"memo_{k}": v for k, v in memos.items()}
    if era.mode == "training":
        role = ("You are The Record: an external historian-judge, rigorous, fair and historically precise.")
        job_a = f"""JOB A - REVEAL AND SCORE era {era.key} (window {era.start} to {era.window_end}), 700-1000 words:
- What actually happened in the real world in this window: the real winners, where value pooled, the real capability jumps. Name real companies and dates.
- Scorecard 0-10 with one-line justifications: frontier_accuracy, timing, layer_choice, reinvention_courage,
  hindsight_leakage (10 = none; penalise any post-date knowledge in the memos or decision).
- Overall era score 0-100 and a calibrated simulated outcome (how a real company making exactly this call would plausibly have fared).
- Closest real-world analog company."""
        score_keys = "frontier_accuracy, timing, layer_choice, reinvention_courage, hindsight_leakage"
    else:
        role = "You are The Auditor: you replace The Record for eras with no answer key. Skeptical, calibrated, fair."
        job_a = f"""JOB A - AUDIT era {era.key}, 700-1000 words:
- Check the board's factual claims about the present (for the live era) and map who is already doing this and how crowded it is.
- Scorecard 0-10: playbook_consistency, plausibility, non_consensus, layer_choice, grounded (10 = no science fiction).
- Confidence (%) that the core bottleneck is real and important by the era's end; the strongest kill case.
- Simulated outcome in a base and a bear scenario."""
        score_keys = "playbook_consistency, plausibility, non_consensus, layer_choice, grounded"

    lessons = ("- 3-5 generalisable LESSONS tagged [" + era.key + ("]" if era.mode == "training" else "-forecast]") +
               ", plus notes revising older lessons they confirm or contradict.") if use_playbook else \
              "- (Playbook disabled in this configuration: return an empty <lessons/> block.)"

    if nxt is None:
        job_b = "JOB B - none (final era). Return an empty <next_briefing/> block."
    elif nxt.mode == "training":
        job_b = (f"JOB B - WORLD BRIEFING for {nxt.key} (start {nxt.start}), 500-800 words: state of technology, key players, "
                 f"what is newly possible, research whispers, capital climate, society and regulation - STRICTLY only what "
                 f"was public before {nxt.start}. Neutral; do not hint at what comes next.")
    elif nxt.mode == "live":
        job_b = (f"JOB B - WORLD BRIEFING for {nxt.key} (the real present day), 500-800 words, labelled as real present-day "
                 f"state. Use web search if it is available to you.")
    else:
        job_b = (f"JOB B - PROJECTED WORLD BRIEFING for {nxt.key} ({nxt.start}), 500-800 words: a base-case scenario "
                 f"extrapolated from real trends, labelled FACT / EXTRAPOLATION / SPECULATION with confidence. Include "
                 f"developments that go AGAINST the company's thesis; do not adopt its thesis as reality.")

    return f"""{role}

{_docs(charter=charter, playbook=playbook if use_playbook else "", company_state=state,
       world_briefing=briefing, board_decision=decision, **memo_docs)}

{job_a}
{lessons}
{job_b}

Return exactly these blocks:
<reveal>the full reveal/audit text</reveal>
<scores>{{"total": <0-100>, {", ".join(f'"{k}": <0-10>' for k in score_keys.split(", "))}}}</scores>
<outcome>one line: simulated outcome</outcome>
<lessons>the lessons to append to the Playbook, as markdown bullets</lessons>
<next_briefing>the next era's world briefing</next_briefing>"""


def single_prompt_baseline(era: Era, briefing: str, prior_summary: str) -> str:
    """Ablation: one call per era, no org, no departments, no Red Team."""
    return f"""You are the founder of a startup whose only mandate is reinvention toward the technology frontier.

{_docs(world_briefing=briefing, what_you_did_before=prior_summary)}

It is {era.start}. Decide what the company becomes in this era: name, one-line identity, the thesis as
capability -> adoption -> bottleneck -> layer we own -> data -> next capability, what you kill and keep,
wedge product, first customer, and kill criteria. 500-900 words.
{_era_rules(era)}

Return:
<decision>...</decision>
<company_state>a short updated company state</company_state>
<roster_change>none</roster_change>"""
