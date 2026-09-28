"""Compare era scores across runs (e.g. repeated seeds or ablations).

    python -m harness.compare runs/run-002 runs/run-003 runs/abl-noplaybook
Prints a per-era table of totals and the mean over training / forecast eras.
"""

import csv
import statistics
import sys
import pathlib


def load(run_dir):
    p = pathlib.Path(run_dir) / "scores.csv"
    with open(p) as f:
        return {r["era"]: r for r in csv.DictReader(f)}


def main(paths):
    runs = {pathlib.Path(p).name: load(p) for p in paths}
    eras = sorted({e for r in runs.values() for e in r}, key=lambda e: int(e[1:]))
    print("era   " + "  ".join(f"{n[:14]:>14}" for n in runs))
    for e in eras:
        print(f"{e:<5} " + "  ".join(f"{runs[n].get(e, {}).get('total', '-'):>14}" for n in runs))
    for mode in ("training", "live", "forecast"):
        cells = []
        for n, r in runs.items():
            vals = [float(v["total"]) for v in r.values() if v.get("mode") == mode and v.get("total") not in (None, "", "?")]
            cells.append(f"{statistics.mean(vals):>14.1f}" if vals else f"{'-':>14}")
        print(f"{mode[:5]:<5} " + "  ".join(cells))


if __name__ == "__main__":
    main(sys.argv[1:] or ["runs/run-001"])
