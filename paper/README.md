# Paper: Frontier Autolab

LaTeX source for *Frontier Autolab: Organizational Memory, Adversarial Dissent and Temporal Leakage in Multi-Agent LLM Firms Across Fifty Years of Technological Change*.

- `main.tex`, `refs.bib`: manuscript and references
- `figures/`: data figures (PDF); regenerate with `python make_figures.py` (reads `../results/all_runs_scores.csv`)
- `main.pdf`: compiled paper

Build: `latexmk -pdf main.tex`. For arXiv, upload `main.tex`, `main.bbl`, `refs.bib` and `figures/`.
