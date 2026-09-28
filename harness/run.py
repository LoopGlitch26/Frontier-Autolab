"""Run the Frontier Lab simulation end to end.

Examples
    python -m harness.run --run-id dry --dry-run
    python -m harness.run --run-id run-002 --player-model <model-id> --judge-model <other-model-id>
    python -m harness.run --run-id abl-noplaybook --ablation no_playbook --player-model <id> --judge-model <id>
    python -m harness.run --run-id abl-single --ablation single_prompt --player-model <id> --judge-model <id>

Every prompt and raw response is saved under runs/<run-id>/logs/ so a run can be audited.
"""

import argparse
import csv
import json
import pathlib
from concurrent.futures import ThreadPoolExecutor

from . import prompts
from .eras import ERAS, BY_KEY, next_era
from .llm import AnthropicClient, MockClient, extract

ROOT = pathlib.Path(__file__).resolve().parent.parent
ABLATIONS = ("none", "no_playbook", "no_redteam", "single_prompt")

INITIAL_STATE = """# COMPANY STATE
- Era: E0 (founding, Jan 1990)
- Name: (unnamed; the board chooses in E1)
- Team: 16 founding members
- Capital: $1.5M seed
- Assets carried: none yet
- History of identities: []
"""
INITIAL_PLAYBOOK = "# PLAYBOOK: lessons that compound across eras\n"
INITIAL_ROSTER = "# Roster changes log\n- E0: founding roster of 16.\n"


class Run:
    def __init__(self, args, client):
        self.a = args
        self.c = client
        self.dir = ROOT / "runs" / args.run_id
        (self.dir / "logs").mkdir(parents=True, exist_ok=True)
        self.charter = (ROOT / "prompts" / "charter.md").read_text()
        self.state = self._load("company_state.md", INITIAL_STATE)
        self.playbook = self._load("playbook.md", INITIAL_PLAYBOOK)
        self.roster = self._load("roster.md", INITIAL_ROSTER)
        self.use_playbook = args.ablation != "no_playbook"

    # ---- file helpers -------------------------------------------------
    def _load(self, name, default):
        p = self.dir / name
        return p.read_text() if p.exists() else default

    def _save(self, rel, text):
        p = self.dir / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text.strip() + "\n")

    def _era_file(self, era_key, name):
        p = self.dir / "eras" / era_key / name
        return p.read_text() if p.exists() else ""

    def _call(self, label, model, prompt, web=False):
        out = self.c.complete(model, prompt, web_search=web)
        with open(self.dir / "logs" / f"{label}.json", "w") as f:
            json.dump({"label": label, "model": model, "web_search": web,
                       "prompt": prompt, "response": out}, f, indent=1)
        return out

    def _persist_state(self):
        self._save("company_state.md", self.state)
        self._save("playbook.md", self.playbook)
        self._save("roster.md", self.roster)

    # ---- steps ----------------------------------------------------------
    def founding_briefing(self):
        if self._era_file("E1", "world_briefing.md"):
            return
        e1 = BY_KEY["E1"]
        p = (f"You are The Record, an external historian. Write a neutral world briefing (500-800 words) of technology, "
             f"key players, research whispers, capital climate, society and regulation as of {e1.start}. Use ONLY "
             f"knowledge public before that date; do not hint at what comes next.\n\n"
             f"Return it inside <next_briefing>...</next_briefing>.")
        out = self._call("E0_record_briefing", self.a.judge_model, p)
        self._save("eras/E1/world_briefing.md", extract("next_briefing", out, out))

    def era(self, era):
        k = era.key
        if self._era_file(k, "reveal.md"):
            print(f"{k}: already complete, skipping")
            return
        print(f"{k} ({era.start}, {era.mode})")
        briefing = self._era_file(k, "world_briefing.md")
        prev = ERAS[ERAS.index(era) - 1] if ERAS.index(era) > 0 else None
        prev_dec = self._era_file(prev.key, "board_decision.md") if prev else ""
        prev_rev = self._era_file(prev.key, "reveal.md") if prev else ""
        web = self.a.web_search and era.mode == "live"
        pb = self.playbook if self.use_playbook else ""

        if self.a.ablation == "single_prompt":
            memos = {}
            summary = self.state
            dec_out = self._call(f"{k}_single", self.a.player_model,
                                 prompts.single_prompt_baseline(era, briefing, summary), web)
        else:
            def memo(dept):
                p = prompts.department_prompt(era, dept, self.charter, self.state, pb, briefing, prev_dec, prev_rev)
                return dept, extract("memo", self._call(f"{k}_memo_{dept}", self.a.player_model, p, web))
            with ThreadPoolExecutor(max_workers=3) as ex:
                memos = dict(ex.map(memo, prompts.DEPARTMENTS))
            for dept, text in memos.items():
                self._save(f"eras/{k}/memo_{dept}.md", text)
            print(f"  memos done")
            dec_out = self._call(f"{k}_board", self.a.player_model,
                                 prompts.board_prompt(era, self.charter, self.state, pb, self.roster, briefing,
                                                      memos, prev_dec, red_team=self.a.ablation != "no_redteam"),
                                 web)

        decision = extract("decision", dec_out, dec_out)
        self._save(f"eras/{k}/board_decision.md", decision)
        self.state = extract("company_state", dec_out, self.state) or self.state
        rc = extract("roster_change", dec_out, "none")
        if rc and rc.lower() != "none":
            self.roster += f"- {k}: {rc}\n"
        print(f"  board done")

        nxt = next_era(k)
        j_out = self._call(f"{k}_judge", self.a.judge_model,
                           prompts.judge_prompt(era, nxt, self.charter, self.playbook, self.state, briefing,
                                                memos, decision, use_playbook=self.use_playbook),
                           web or (nxt is not None and nxt.mode == "live" and self.a.web_search))
        self._save(f"eras/{k}/reveal.md", extract("reveal", j_out, j_out))
        try:
            scores = json.loads(extract("scores", j_out, "{}"))
        except json.JSONDecodeError:
            scores = {}
        self._save(f"eras/{k}/scores.json", json.dumps(scores, indent=1))
        outcome = extract("outcome", j_out)
        self.state += f"\n- Outcome {k}: {scores.get('total', '?')}/100 - {outcome}\n"
        if self.use_playbook:
            lessons = extract("lessons", j_out)
            if lessons:
                self.playbook += f"\n## [{k}]\n{lessons}\n"
        if nxt:
            self._save(f"eras/{nxt.key}/world_briefing.md", extract("next_briefing", j_out))
        self._persist_state()
        print(f"  judge done: {scores.get('total', '?')}/100")

    def write_scores(self):
        rows = []
        for e in ERAS:
            p = self.dir / "eras" / e.key / "scores.json"
            if p.exists():
                s = json.loads(p.read_text())
                rows.append({"era": e.key, "mode": e.mode, **s})
        if rows:
            keys = sorted({k for r in rows for k in r}, key=lambda x: (x not in ("era", "mode", "total"), x))
            with open(self.dir / "scores.csv", "w", newline="") as f:
                w = csv.DictWriter(f, fieldnames=keys)
                w.writeheader()
                w.writerows(rows)

    def go(self):
        (self.dir / "config.json").write_text(json.dumps(vars(self.a), indent=1))
        self.founding_briefing()
        for e in ERAS:
            if e.key in self.a.eras:
                self.era(e)
        self.write_scores()
        print(f"done: {self.dir}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--run-id", required=True)
    ap.add_argument("--player-model", default="mock-player", help="model id for the 16 company agents")
    ap.add_argument("--judge-model", default="mock-judge", help="model id for The Record / The Auditor")
    ap.add_argument("--ablation", choices=ABLATIONS, default="none")
    ap.add_argument("--eras", default=",".join(e.key for e in ERAS), help="comma list, e.g. E1,E2,E3")
    ap.add_argument("--web-search", action="store_true", help="enable server-side web search in the live era")
    ap.add_argument("--temperature", type=float, default=1.0)
    ap.add_argument("--seed", type=int, default=0, help="mock seed; real runs vary via temperature")
    ap.add_argument("--dry-run", action="store_true", help="offline mock model, no API calls")
    a = ap.parse_args()
    a.eras = [x.strip() for x in a.eras.split(",")]
    client = MockClient(a.seed) if a.dry_run else AnthropicClient(temperature=a.temperature)
    Run(a, client).go()


if __name__ == "__main__":
    main()
