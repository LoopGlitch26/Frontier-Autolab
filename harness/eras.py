"""Era schedule for the Frontier Lab simulation."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Era:
    key: str          # "E1"
    start: str        # human-readable start date
    window_end: str   # end of the window the judge reveals
    mode: str         # "training" | "live" | "forecast"


ERAS = [
    Era("E1", "January 1, 1990", "December 1995", "training"),
    Era("E2", "January 1, 1996", "December 2001", "training"),
    Era("E3", "January 1, 2002", "December 2007", "training"),
    Era("E4", "January 1, 2008", "December 2013", "training"),
    Era("E5", "January 1, 2014", "December 2019", "training"),
    Era("E6", "January 1, 2020", "the day before the live era", "training"),
    Era("E7", "the live date (today)", "n/a (no answer key)", "live"),
    Era("E8", "January 2032", "n/a (projected)", "forecast"),
    Era("E9", "January 2040", "n/a (projected)", "forecast"),
]

BY_KEY = {e.key: e for e in ERAS}


def next_era(key: str):
    keys = [e.key for e in ERAS]
    i = keys.index(key)
    return ERAS[i + 1] if i + 1 < len(ERAS) else None
