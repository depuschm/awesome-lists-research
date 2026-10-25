# Awesome lists research

What makes GitHub's most-starred "awesome" lists so good? This repository holds a data-driven study of 1,291 curated lists: their stars, structure, history and governance, measured from 1,609 cloned repositories and about 60,000 historical README snapshots, plus in-depth reviews of more than 40 lists. Data as of 25 October 2026.

**Read the report:** [as a web page with interactive charts](https://depuschm.github.io/awesome-lists-research) or [as Markdown](REPORT.md).

## Key findings

- Five of the ten most-starred repositories on all of GitHub are curated link lists.
- Timing is the biggest factor: 35% of lists started in 2014–15 passed 10,000 stars, against 9% of lists started in 2019–22. A second window opened with the AI wave.
- The usual quality checklist (descriptions, table of contents, badges, licence, contributing guide) is table stakes. Describing every entry has essentially zero correlation with stars.
- Scale and breadth matter: lists with 50k+ stars have a median of 593 entries in 51 categories, against 146 in 18 for lists under 2k stars.
- The best-maintained lists prune, and record why. awesome-python, free-for-dev, awesome-react and awesome-vue all cut 25–85% of their entries at some point.
- In same-topic rivalries, late clones that launched bigger or better maintained got 1–7% of the leader's stars. Every overtake combined a stalled incumbent, a different product and an existing audience.
- Dormant lists keep gaining stars: 95 lists unchanged for a year or more gained 202,000 stars in that time.
- In 2026, AI-generated pull requests forced several top lists to close or restrict outside submissions.

## Which repositories were studied

All 1,609 repositories are listed in [REPOSITORIES.md](REPOSITORIES.md), each linked to the exact commit that was analysed: 1,291 curated lists in the statistics, plus the repos that were cloned and then excluded (not lists, duplicates, no star data) and the few used only for qualitative comparison. The same list is in [`data/repositories.tsv`](data/repositories.tsv) for scripts. The repositories themselves are not included, as copies or as submodules, to keep this repo small; `scripts/clone_one.sh owner/repo <sha>` re-creates any snapshot.

## Repository layout

| Path | Contents |
|---|---|
| `REPORT.md` | The full report |
| `REPOSITORIES.md` | Every repository studied, with its status and a link to the exact commit analysed |
| `docs/index.html` | The report as a web page with interactive charts, served by GitHub Pages |
| `page/awesome-lists-study.html` | The same page as an HTML fragment (for embedding viewers that supply their own document skeleton) |
| `notes/` | Literature review, five archetype deep dives, same-topic rivals study, low-star control group, analyst rubric |
| `data/repositories.tsv` | The same list, machine-readable: status, stars, census/index membership, pinned commit SHA and date |
| `data/master_stars.tsv` | 1,598 repositories with stars from every source, index membership and category |
| `data/corpus.csv` | 1,568 repositories × ~110 features, with classification |
| `data/features.jsonl` | Raw extracted features, one JSON object per repository |
| `data/readme_history_final.jsonl` | Quarterly README size and entry counts for 1,609 repositories |
| `data/analysis/` | Tier comparisons, correlations, cohorts, regressions, dormant-star growth, chart data |
| `data/topic_*.tsv`, `data/tal_lists.tsv`, `data/awesome_index.tsv` | Raw rankings and index parses |
| `data/manual_kind.csv`, `data/archetypes_top.csv` | Manual classifications |
| `raw/` | Source snapshots (trackawesomelist README, EvanLi/Github-Ranking top 100) |
| `scripts/` | The full pipeline |

## Reproducing the analysis

Requires Python 3.13 and git.

```sh
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt

# 1. Clone every repository at the exact commit analysed (partial, sparse clones; ~2.6 GB)
tail -n +2 data/repositories.tsv | awk -F'\t' '$11 != "" {print $1, $11}' | xargs -P 8 -n 2 scripts/clone_one.sh

# 2. Extract features and reconstruct README histories
ls -d clones/*/ | xargs -P 4 -n 25 python3 -I scripts/extract.py > data/features.jsonl
ls -d clones/*/ | xargs -P 4 -n 10 python3 -I scripts/readme_history.py > data/readme_history_final.jsonl

# 3. Build the corpus, run the statistics, rebuild the page
.venv/bin/python scripts/build_corpus.py
.venv/bin/python scripts/analyze.py
.venv/bin/python scripts/export_viz.py
.venv/bin/python scripts/build_page.py   # writes docs/index.html and page/awesome-lists-study.html
.venv/bin/python scripts/make_manifest.py # rewrites REPOSITORIES.md and data/repositories.tsv from clones/
```

Cloning at the pinned commits reproduces the analysed snapshots; time-based features are measured against a fixed date (25 October 2026), and star counts are fixed snapshots in `data/`. If a list's owner has rewritten its history, the pinned commit may be gone and `clone_one.sh` warns and falls back to the current version. The rankings in `data/topic_*.tsv` were collected from GitHub topic pages, whose star counts are rounded.

## Method notes and limitations

- Statistics are run on two unbiased samples: a **census** of every curated list among the 1,000 most-starred repositories tagged `awesome-list` (n = 861), and **every list in the official [sindresorhus/awesome](https://github.com/sindresorhus/awesome) index** with a known star count (n = 558).
- `data/topic_awesome-list_p3-26.tsv` also contains 60 rows from pages 28–30, written there by a parallel scraper; `scripts/merge_rankings.py` keeps only rows whose page falls in each file's range.
- Stars are a proxy for reach and bookmarking as much as quality. Star histories were not available, so growth is measured in README content.
- Results are correlations. Contributor counts and governance files are partly consequences of popularity.
- The qualitative notes were written by AI sub-agents working from the cloned repositories and their git history; the most surprising claims were spot-checked against the repositories.

## License

- **Report, notes, data and web page:** [Creative Commons Attribution 4.0 International (CC BY 4.0)](LICENSE). You may share and adapt them for any purpose, including commercially, as long as you give credit and link back to this repository.
- **Code in `scripts/`:** [MIT](scripts/LICENSE).
- **Third-party material keeps its own terms.** `raw/` holds snapshots of files from [trackawesomelist](https://github.com/trackawesomelist/trackawesomelist) and [EvanLi/Github-Ranking](https://github.com/EvanLi/Github-Ranking). Repository names, descriptions and quotations from the studied lists belong to their authors and are reproduced for research and commentary.

## Credits

Research and analysis by Claude (Anthropic), commissioned by depuschm.
