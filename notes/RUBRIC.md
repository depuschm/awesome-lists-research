# Deep-dive rubric (shared by all qualitative analysts)

Context: research project "what makes the most-starred GitHub awesome lists so good". Quantitative
features (stars, commits, entries, CI flags...) are computed separately by script, so focus on what a
script cannot see: judgment about design, curation, writing, governance and positioning.

Local data: every list is a partial git clone at clones/<owner>__<repo>
- Root files and .github/ are checked out (README, CONTRIBUTING, PR template, workflows, LICENSE...).
- Other files: `git -C <dir> show HEAD:<path>` (fetches lazily); list all files: `git -C <dir> ls-tree -r --name-only HEAD`.
- Full commit history is available offline: `git -C <dir> log --format='%ad %an %s' --date=short` etc.
  Useful: commits per year, grep commit subjects for remove/delete/dead/unmaintained/archived/revert/spam/sort.
- To read an old README version: `git -C <dir> log --format=%H --before=2016-01-01 -1 HEAD` then `git -C <dir> show <sha>:README.md`.
- If you need a repo that isn't cloned, run: scripts/clone_one.sh owner/repo
- READMEs can be huge (300KB+). Do NOT cat whole files; use head/sed -n ranges/grep/wc.
- Network: raw.githubusercontent.com works; api.github.com and github.com HTML do not (except via WebFetch, which may work for github.com pages).

For EACH list, cover:
1. Value proposition & scope: the question it answers, audience, scope boundaries; quote the tagline/intro.
2. Curation policy: explicit inclusion/exclusion criteria (quote key rules), quality bars (stars, activity,
   license, maturity), how dead/unmaintained entries are handled; evidence of pruning in git history.
3. Entry format: the item template (name - description, metadata such as license/language/stars/icons/tags),
   description quality & consistency, ordering rule (alphabetical? by importance?), nesting.
4. Navigation & structure: ToC, number/granularity of categories, back-to-top, collapsibles, legend,
   companion website/HTML version/search, translations.
5. Contribution workflow & governance: CONTRIBUTING length and key rules, PR template checklist, CI checks
   (link checking, linting, formatting, duplicate detection), number of active maintainers/mergers
   (from merge commits), bus factor, anti-spam/self-promotion rules, sponsorship/monetization and how
   neutrality is preserved.
6. Maintenance over time: commit activity by year, current status (active/paused/archived), freshness.
7. Secret sauce: 3-5 SPECIFIC design decisions that make it stand out versus a generic awesome list.
8. Weaknesses visible: staleness, link rot, bloat, inconsistency, spam, scope creep.
9. Up to 3 short verbatim quotes (<=25 words each) that capture its philosophy.

Be concrete and evidence-based (cite file names, numbers, commit counts, dates). No generic filler.
