# Paper: Scored Against History

LaTeX source for *Scored Against History: A Pilot Study of Hindsight Leakage and Strategic Learning in an LLM-Simulated Organization*.

- `main.tex`, `refs.bib`: manuscript and references
- `figures/`: data figures (PDF); regenerate with `python make_figures.py` (reads `../results/all_runs_scores.csv`)
- `main.pdf`: compiled paper

Build: `latexmk -pdf main.tex`. For arXiv, upload `main.tex`, `main.bbl`, `refs.bib` and `figures/`.
