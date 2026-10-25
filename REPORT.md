# What Makes the Best Awesome Lists Great

**A data-driven study of GitHub's most-starred curated lists: stars, structure, history and governance.**
Data as of 25 October 2026. Corpus: 1,609 cloned repositories, 1,291 curated lists analysed, more than 40 lists read in depth.

## Contents

- [Key findings](#key-findings)
- [1. Why awesome lists matter](#1-why-awesome-lists-matter)
- [2. How this study was done](#2-how-this-study-was-done)
- [3. Who the winners are](#3-who-the-winners-are)
- [4. What separates top lists from the rest](#4-what-separates-top-lists-from-the-rest)
- [5. Ten things the best lists do](#5-ten-things-the-best-lists-do)
- [6. Same-topic rivals: a natural experiment](#6-same-topic-rivals-a-natural-experiment)
- [7. Why most lists stay small](#7-why-most-lists-stay-small)
- [8. What stars do and do not measure](#8-what-stars-do-and-do-not-measure)
- [9. 2026: the AI inflection](#9-2026-the-ai-inflection)
- [10. Playbook](#10-playbook)
- [Appendix A: full feature tables](#appendix-a-full-feature-tables)
- [Appendix B: data, code and reproducibility](#appendix-b-data-code-and-reproducibility)
- [Sources](#sources)

---

## Key findings

1. **Curated lists are GitHub's hall of fame.** Five of the ten most-starred repositories on all of GitHub are curated link lists (nine of the top 25, fifteen of the top 100). Almost half of the top 100 (48) are not software at all.
2. **Stars are extremely concentrated.** Across 1,291 curated lists holding 11.1 million stars, the top 10 lists hold 31% of all stars and the top 10% hold 71% (Gini 0.78).
3. **Timing is the single biggest factor.** 35% of lists started in 2014–15 (when the format took off) passed 10,000 stars, against 9% of lists started in 2019–22. 40 of the 100 most-starred lists were created in 2014–15, against 21% of all lists. A second window opened with the AI wave: 19 of the top 100 were created since 2023, and lists born in that period earn about 1.9× the stars their age would predict.
4. **The "quality hygiene" checklist is table stakes, not a differentiator.** Descriptions on every entry, a table of contents, badges, a licence, a CONTRIBUTING file: small lists have them as often as giant ones. The share of described entries has essentially zero correlation with stars (ρ = 0.05 in the census, 0.01 inside the official index).
5. **Scale and breadth do differentiate.** Lists with 50k+ stars have a median of 593 entries in 51 categories; lists under 2k stars have 146 entries in 18 categories. Top lists also have more balanced taxonomies (largest category = 11% of entries vs 21%).
6. **Winners launch full and keep growing for years.** One year after launch, today's 50k+ lists already had a median of 408 entries (vs 97 for <2k lists), and half of them more than doubled after year one (vs a quarter of small lists; 73% vs 17% inside the official index).
7. **The best lists cut.** 23% of 50k+ lists are currently at least 10% smaller than their peak (8% for <2k lists). awesome-python went from 739 entries to 498 under a written "shortlist, not a catalog" policy; free-for-dev cut ~25% in eight cleanup PRs; awesome-react cut 65% in a week; awesome-vue cut 62%.
8. **Governance scales with success.** PR templates (46% vs 14%), issue forms (36% vs 10%), CI (55% vs 37%) and longer contribution guides (≈300 vs 135 words) are far more common at the top. The most effective lists turn their rules into bots and make contributors supply the evidence.
9. **Communities form around winners, but they are still run by one person.** Top lists have a median of 387 commit authors (vs 20) and 6 people who have merged PRs (vs 1), yet nearly every top list we read in depth has a single active gatekeeper today.
10. **Design explains only part of it.** Everything visible in the repository (size, age, structure, process, licence, translations, index listing) explains about 21% of the variance in log-stars in the census sample and 50% inside the official index. Topic demand, timing and distribution do the rest.
11. **Same-topic rivalries confirm it: be there at the topic's birth, then stay alive.** Comparing winners with same-scope rivals in 12 topics, the earliest list won 7 of 12, and the winner out-worked its rival in the first two years in 10 of 12. Six late clones launched bigger or better maintained than the leader and got 1–7% of its stars. Every overtake combined an incumbent that stalled early, a *different* product and an existing audience.
12. **Stars measure the promise, not current quality.** 95 lists whose content had not changed for at least a year gained 202,000 stars in that time (median +20%). Several top-30 lists have been dormant for two to four years.
13. **2026 broke the contribution model.** A flood of AI-generated pull requests led sindresorhus/awesome to close external PRs (no new list added in 2026), awesome-nodejs to pause submissions, and others to add honeypot checkboxes, "prove you're human" emails, account-age gates and issue-form-only intake. One MCP list went the other way and opened a fast lane for agents.

---

## 1. Why awesome lists matter

An "awesome list" is a curated Markdown README of links on one topic, in the format popularised by [sindresorhus/awesome](https://github.com/sindresorhus/awesome) in July 2014. The format predates it: [ziadoz/awesome-php](https://github.com/ziadoz/awesome-php) began as a Gist and has commits from January 2012, and vinta/awesome-python (June 2014) and avelino/awesome-go (July 2014) both credit their predecessor in their first README.

<!-- chart:top100 -->

**Share of GitHub's 100 most-starred repositories, by kind** (EvanLi/Github-Ranking snapshot, 24 Oct 2026; classification ours):

| Kind | Top 10 | Top 25 | Top 100 |
|---|---|---|---|
| Curated link lists | 5 | 9 | 15 |
| Guides, books and courses | 3 | 4 | 16 |
| AI agent skills and configs | 0 | 4 | 9 |
| Artifact collections (prompts, templates, playlists) | 0 | 0 | 7 |
| Other non-software | 0 | 1 | 1 |
| Software | 2 | 7 | 52 |

Within the curated-list world, attention is winner-take-most:

| Sample | Lists | Stars | Top 10 share | Top 10% share | Gini | Median |
|---|---|---|---|---|---|---|
| All lists in the corpus | 1,291 | 11.1M | 31% | 71% | 0.78 | 2,000 |
| Census (top-1,000 `awesome-list` topic) | 861 | 8.1M | 35% | 68% | 0.74 | 2,400 |
| Official index lists with known stars | 558 | 5.4M | 46% | 77% | 0.84 | 1,400 |

The corpus is truncated at the bottom (lists with a few dozen stars are under-represented), so the true concentration is higher still.

---

## 2. How this study was done

The GitHub search API was not available from the research environment, so the corpus was built from three ranked sources plus the official index, and every repository was then cloned and analysed locally.

| Source | What it gave | Size |
|---|---|---|
| GitHub topic page `awesome-list`, sorted by stars (pages 1–50) | Ranked list with star counts | 1,000 repos (down to 970 stars) |
| GitHub topic page `awesome`, sorted by stars (pages 1–25) | Ranked list with star counts | 500 repos (down to 2.4k stars) |
| [trackawesomelist](https://github.com/trackawesomelist/trackawesomelist) README | Tracked lists with star counts and last-update dates | 682 lists |
| [sindresorhus/awesome](https://github.com/sindresorhus/awesome) readme | Official index membership and category | 670 lists |
| [EvanLi/Github-Ranking](https://github.com/EvanLi/Github-Ranking) | Exact stars for GitHub's overall top 100 | 100 repos |
| Partial git clones (all commits and trees; root files checked out) | Full history, file tree, README, CI, templates | 1,609 repos, 2.4 GB |

**Three analysis samples.** The corpus mixes sources, and that creates a selection bias: small lists entered mostly through the official index, big ones through the topic ranking. Comparing them naively makes index membership, the Awesome badge and awesome-lint look harmful. So the statistics are run on two clean samples and the full set is used only for description:

- **Census (n = 861):** every curated list among the 1,000 most-starred repositories tagged `awesome-list`. It is sampled purely by stars, so it is unbiased with respect to every feature.
- **Official index (n = 558):** every list in sindresorhus/awesome with a known star count. All passed the same quality gate.
- **All lists (n = 1,291):** for descriptive statistics only.

After de-duplicating renamed repos and forks by root commit (30 removed), each repo was classified as a link list, an artifact collection (prompt files, rule files, templates) or other (code, books, apps); 225 non-lists were excluded and 50 classifications were set by hand.

**Features.** A custom extractor computed about 90 features per repo:

- *History:* first and last commit, commits, distinct authors, top-author share, merge commits, people who merged PRs, highest issue/PR number referenced, activity by year, bot share.
- *Files:* CONTRIBUTING, code of conduct, PR and issue templates, FUNDING.yml, CI workflows and what they check (link checking, awesome-lint, markdown lint, stale bots), licence type, translations, website configs, data files.
- *README:* entries (format-agnostic: Markdown bullets, HTML anchors, tables, blockquotes, reference links, bare URLs, setext headings), share of entries with a description, words per description, categories, items per category, alphabetical ordering, ToC, back-to-top links, badges, images, emoji, sponsor sections, stated inclusion criteria.

**README history.** For 1,289 lists the README was reconstructed at every quarter since the first commit (about 60,000 historical snapshots), giving entry counts over time: size at launch, peak size, and pruning events.

**Qualitative work.** Five analysts (AI sub-agents working from the local clones and git history, with spot checks of key claims by the lead researcher) each read one archetype in depth against a shared rubric, more than 40 lists in all; one ran a same-topic rivals comparison across 12 topics plus 12 quick-check pairs; one coded a random control sample of 30 low-star lists; one reviewed the literature. Their full notes are in `notes/`.

**Limitations.**

- *Stars are a proxy.* They measure bookmarking and reach as much as quality (Section 8).
- *No star histories.* GitHub's stargazer API and BigQuery were unavailable, so growth is measured in content, not stars.
- *Correlation, not causation.* Community size, governance files and sponsorship are partly consequences of popularity. Features observable at launch (age, size in year one) are more defensible as causes.
- *Rounding.* Topic-page stars are rounded to three significant digits.
- *CI detection is keyword-based* and is a lower bound (awesome-go's custom Go bot does not register as a link checker; awesome-selfhosted keeps its checks in a separate data repo).
- *Survivorship.* Lists with very few stars are under-represented.

---

## 3. Who the winners are

<!-- chart:archetypes -->

**The 30 most-starred curated lists** (stars from GitHub topic pages or EvanLi exact counts; entries from the README parser):

| # | List | Stars | Archetype | Created | Entries | Commit authors | Commits, last 12 mo | Last commit |
|---|---|---|---|---|---|---|---|---|
| 1 | [codecrafters-io/build-your-own-x](https://github.com/codecrafters-io/build-your-own-x) | 556k | Learning & knowledge | 2018 | 363 | 145 | 19 | 3 mo ago |
| 2 | [sindresorhus/awesome](https://github.com/sindresorhus/awesome) | 524k | Meta (list of lists) | 2014 | 683 | 682 | 34 | 52 d ago |
| 3 | [public-apis/public-apis](https://github.com/public-apis/public-apis) | 492k | Practical directory | 2016 | 2,244 | 2,103 | 1,813 | 0 d ago |
| 4 | [EbookFoundation/free-programming-books](https://github.com/EbookFoundation/free-programming-books) | 400k | Learning & knowledge | 2013 | ~13,000 (multi-file) | 3,548 | 306 | 2 d ago |
| 5 | [vinta/awesome-python](https://github.com/vinta/awesome-python) | 330k | Ecosystem catalog | 2014 | 552 | 588 | 1,483 | 2 d ago |
| 6 | [awesome-selfhosted/awesome-selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted) | 330k | Practical directory | 2015 | 1,365 | 1,367 | 254 | 2 d ago |
| 7 | [trimstray/the-book-of-secret-knowledge](https://github.com/trimstray/the-book-of-secret-knowledge) | 253k | Learning & knowledge | 2018 | 912 | 110 | 0 | 23 mo ago |
| 8 | [ossu/computer-science](https://github.com/ossu/computer-science) | 210k | Learning & knowledge | 2014 | 78 courses | 185 | 22 | 3 mo ago |
| 9 | [avelino/awesome-go](https://github.com/avelino/awesome-go) | 190k | Ecosystem catalog | 2014 | 3,178 | 2,637 | 492 | 1 d ago |
| 10 | [521xueweihan/HelloGitHub](https://github.com/521xueweihan/HelloGitHub) | 184k | Practical directory | 2016 | multi-file (monthly issues) | 11 | 15 | 27 d ago |
| 11 | [f/prompts.chat](https://github.com/f/prompts.chat) | 174k | AI-era | 2022 | 2,627 prompts (CSV) | 1,468 | 8,859 | 0 d ago |
| 12 | [ripienaar/free-for-dev](https://github.com/ripienaar/free-for-dev) | 140k | Practical directory | 2015 | 1,363 | 2,337 | 913 | 0 d ago |
| 13 | [Hack-with-Github/Awesome-Hacking](https://github.com/Hack-with-Github/Awesome-Hacking) | 123k | Meta (list of lists) | 2016 | 83 | 38 | 15 | 3 mo ago |
| 14 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | 123k | AI-era | 2026 | 84 files | 4 | 66 | 10 d ago |
| 15 | [jaywcjlove/awesome-mac](https://github.com/jaywcjlove/awesome-mac) | 117k | Practical directory | 2016 | 1,493 | 1,028 | 1,008 | 0 d ago |
| 16 | [papers-we-love/papers-we-love](https://github.com/papers-we-love/papers-we-love) | 111k | Learning & knowledge | 2013 | ~585 papers (multi-file) | 318 | 11 | 25 d ago |
| 17 | [MunGell/awesome-for-beginners](https://github.com/MunGell/awesome-for-beginners) | 91k | Learning & knowledge | 2015 | 253 | 363 | 134 | 23 d ago |
| 18 | [DopplerHQ/awesome-interview-questions](https://github.com/DopplerHQ/awesome-interview-questions) | 85k | Meta (list of lists) | 2015 | 353 | 151 | 0 | 2.2 y ago |
| 19 | [binhnguyennus/awesome-scalability](https://github.com/binhnguyennus/awesome-scalability) | 75k | Learning & knowledge | 2017 | 920 | 31 | 7 | 9 mo ago |
| 20 | [enaqx/awesome-react](https://github.com/enaqx/awesome-react) | 75k | Ecosystem catalog | 2014 | 149 | 672 | 28 | 51 d ago |
| 21 | [josephmisiti/awesome-machine-learning](https://github.com/josephmisiti/awesome-machine-learning) | 75k | Ecosystem catalog | 2014 | 1,254 | 757 | 110 | 2 d ago |
| 22 | [fffaraz/awesome-cpp](https://github.com/fffaraz/awesome-cpp) | 74k | Ecosystem catalog | 2014 | 1,398 | 495 | 97 | 14 d ago |
| 23 | [vuejs/awesome-vue](https://github.com/vuejs/awesome-vue) | 74k | Ecosystem catalog | 2015 | 1,076 | 2,467 | 123 | 28 d ago |
| 24 | [prakhar1989/awesome-courses](https://github.com/prakhar1989/awesome-courses) | 72k | Learning & knowledge | 2014 | 712 | 147 | 0 | 3.9 y ago |
| 25 | [sindresorhus/awesome-nodejs](https://github.com/sindresorhus/awesome-nodejs) | 67k | Ecosystem catalog | 2014 | 593 | 406 | 6 | 52 d ago |
| 26 | [Solido/awesome-flutter](https://github.com/Solido/awesome-flutter) | 62k | Ecosystem catalog | 2017 | 511 | 368 | 14 | 51 d ago |
| 27 | [rust-unofficial/awesome-rust](https://github.com/rust-unofficial/awesome-rust) | 60k | Ecosystem catalog | 2014 | 1,947 | 1,436 | 1,136 | 1 d ago |
| 28 | [wasabeef/awesome-android-ui](https://github.com/wasabeef/awesome-android-ui) | 58k | Ecosystem catalog | 2014 | 293 | 80 | 1 | 4 mo ago |
| 29 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | 56k | AI-era | 2025 | 253 | 18 | 1,973 | 0 d ago |
| 30 | [vsouza/awesome-ios](https://github.com/vsouza/awesome-ios) | 54k | Ecosystem catalog | 2014 | 1,867 | 1,033 | 37 | 58 d ago |

Note that only 18 of these 30 have "awesome" in their name. Commit counts for AI-era lists mostly measure automation (prompts.chat syncs each web edit as a commit; 1,823 of awesome-claude-code's 2,229 commits are bot commits).

### Five archetypes

| Archetype | Examples | The question it answers | Typical value driver |
|---|---|---|---|
| **Ecosystem catalog** | awesome-python, awesome-go, awesome-rust, awesome-vue | "Which library should I use for X in language Y?" | Being the default answer for a big language community |
| **Practical directory** | public-apis, free-for-dev, awesome-selfhosted, awesome-mac | "Which free API / free tier / self-hostable app / Mac app can I use?" | Standardised decision metadata per entry |
| **Learning & knowledge** | build-your-own-x, free-programming-books, the-book-of-secret-knowledge, awesome-scalability | "What should I learn, and from where?" | Aspiration; evergreen content; a strong voice |
| **Meta (list of lists)** | sindresorhus/awesome, Awesome-Hacking, awesome-interview-questions | "Which list is *the* list for topic X?" | A namespace: one canonical slot per topic |
| **AI-era collection** | prompts.chat, awesome-mcp-servers, awesome-claude-code, awesome-design-md | "What can I plug into my AI tool today?" | Speed to a new platform; copy-pasteable artifacts |

### The two windows

<!-- chart:cohorts -->

Lists in the census sample by year of first commit:

| First commit | Lists | Median stars | Share with 10k+ stars |
|---|---|---|---|
| 2014–2015 | 147 | 4,500 | **35%** |
| 2016–2018 | 288 | 2,500 | 13% |
| 2019–2022 | 272 | 1,900 | 9% |
| 2023–2026 | 147 | 2,300 | 14% |

The 2014 cohort alone has a median of 8,200 stars, and 25 of its 59 census lists passed 10,000. Among the 100 most-starred lists overall, 40 were created in 2014–15, while only 21% of all lists were. The awesome-list genre was founded in a burst: all six of the big ecosystem catalogs (Python, Go, Node.js, Java, C++, Rust) were created within 19 days of each other in June–July 2014.

The second window is the AI wave. 19 of the top 100 lists were created since 2023, three of them already above 50k stars. In the census regression, lists created since 2023 earn about 1.9 times the stars their age predicts.

---

## 4. What separates top lists from the rest

<!-- chart:dumbbell -->

Each feature below compares lists with 50k+ stars (n = 22) against lists with under 2k stars (n = 350) in the census sample, with the Spearman correlation against stars across all 861 census lists and the same correlation controlling for age. The official-index sample (Appendix A) shows the same directions, usually stronger.

### 4.1 Table stakes: what does not differentiate

| Feature | 50k+ stars | Under 2k | ρ with stars |
|---|---|---|---|
| Share of entries with a description | 93% | 82% | +0.05 |
| Words per description | 9.9 | 11.2 | −0.02 |
| Table of contents | 91% | 83% | +0.03 |
| Any badge | 82% | 83% | +0.01 |
| Awesome badge | 73% | 73% | +0.01 |
| Creative Commons licence | 36% | 49% | −0.02 |
| No licence file at all | 32% | 26% | −0.00 |
| awesome-lint in CI | 5% | 11% | −0.02 |
| Code of conduct | 41% | 28% | −0.00 |
| Name contains "awesome" | 73% | 88% | −0.06 |

These are the rules the official index enforces, and they are worth following: they make a list usable and they are the price of admission to the index. But almost every list that has been noticed at all already follows them. Inside the official index, the share of described entries has a correlation of 0.01 with stars.

### 4.2 Scale and breadth

| Feature | 50k+ stars | Under 2k | ρ | ρ, age-controlled |
|---|---|---|---|---|
| Entries in the README | 593 | 146 | +0.27 | +0.28 |
| Categories with entries | 51 | 18 | +0.19 | +0.18 |
| Largest category's share of entries | 11% | 21% | −0.14 | −0.14 |
| README words | 7,585 | 2,293 | +0.28 | +0.31 |

<!-- chart:scatter -->

Big lists win, but the relationship is loose (ρ ≈ 0.27) and it is not "more is better" without limit: many of the most respected lists deliberately shrank (Section 4.4). What the top lists share is *coverage of a broad topic with a balanced taxonomy*. Thin lists fake depth with headings: the control group's lists average 3–4 entries per category, and one Ember list spreads 881 entries over 130 categories.

### 4.3 Launch full, then keep growing

| Feature | 50k+ stars | Under 2k | ρ | ρ, age-controlled |
|---|---|---|---|---|
| Entries one year after the first commit | 408 | 97 | +0.20 | +0.24 |
| Peak size at least double the year-one size | 50% | 25% | +0.17 | +0.13 |
| Year-one size as a share of peak | 56% | 71% | −0.15 | −0.08 |

In the official index the contrast is sharper: 73% of 50k+ lists more than doubled after their first year, against 17% of sub-2k lists. A third of the control group were "one-shot" launches, with half or more of all their commits in the first 90 days; none of the top four lists were. Winners arrived substantial (awesome-machine-learning had 160 entries by the end of day one; awesome-cursorrules 140 by day two; awesome-openclaw-skills 565 on day one) and then kept compounding for years.

### 4.4 Pruning

| Feature | 50k+ stars | Under 2k | ρ |
|---|---|---|---|
| Currently ≥10% smaller than its peak | 23% | 8% | +0.11 |
| Ever cut ≥10% of entries in a single quarter | 32% | 15% | +0.07 |

In the index sample the same comparison is 32% vs 8% and 50% vs 13%.

<!-- chart:growth -->

The README histories show that the best-maintained lists remove things, often in large, documented purges:

| List | Pruning | Effect |
|---|---|---|
| vinta/awesome-python | Mar 2019 cleanup; Feb 2024 "remove old projects"; Mar 2026 redesign; Aug 2026 "shortlist" ADR with 39 section sweeps in one day | 739 entries (2019 peak) → 498 → ~550 now |
| ripienaar/free-for-dev | Eight owner PRs `cleanup1`…`cleanup8` (2–3 Jan 2026: "Dead entries / Not free entries / Unclear pricing"); Mar 2026 scope trim deleting whole sections | 1,672 → 1,273 → 1,372 |
| enaqx/awesome-react | Owner purges in 2019 (−42%) and April 2023 (−65%: "Remove Redux section", "Flatten list") | 1,063 → 177 |
| vuejs/awesome-vue | Community prune, Nov 2024 | 3,169 → 1,215 |
| awesome-selfhosted | Nightly bot flags projects with no activity for 186 days (warning) or 365 days (error); 343 removals tagged "unmaintained since <date>" | Held flat at ~1.2–1.36k for three years |
| sindresorhus/awesome | Bulk removal of 25 archived lists in 2026 | First net decline in 12 years |

Lists that never prune only grow: awesome-machine-learning has grown every year since 2014 and about 12% of its entries carry a `[Deprecated]` tag from a single 2019 pass. awesome-cpp still links 39 SourceForge and 4 Google Code projects.

### 4.5 Process and governance

| Feature | 50k+ stars | Under 2k | ρ | ρ, age-controlled |
|---|---|---|---|---|
| PR template | 46% | 14% | +0.20 | +0.20 |
| Issue templates or forms | 36% | 10% | +0.11 | +0.14 |
| Any CI | 55% | 37% | +0.16 | +0.15 |
| Automated link checking (lower bound) | 27% | 18% | +0.14 | +0.11 |
| CONTRIBUTING file | 86% | 66% | +0.12 | +0.09 |
| CONTRIBUTING length | 297 words | 135 words | +0.16 | +0.15 |
| Flags unmaintained or archived entries | 32% | 24% | +0.03 | +0.03 |

Part of this is cause, part consequence: a list that receives 50 PRs a week needs a template. The qualitative work shows *how* these documents differ. At the top they are governance documents, not boilerplate: awesome-python's ADR and overrides register, awesome-go's 2,241-word CONTRIBUTING with measurable bars and a removal protocol, free-for-dev's list of "services we do not accept". At the bottom, CONTRIBUTING files are often copied templates that do not even fit the list (awesome-scalability's tells contributors to use a `[List Name](link)` format).

### 4.6 Community and maintenance

| Feature | 50k+ stars | Under 2k | ρ | ρ, age-controlled |
|---|---|---|---|---|
| Distinct commit authors | 387 | 20 | +0.45 | +0.41 |
| People who merged PRs | 6 | 1 | +0.31 | +0.26 |
| Top author's share of commits | 35% | 59% | −0.22 | −0.17 |
| Highest issue/PR number referenced | 1,574 | 48 | +0.49 | +0.47 |
| Any commit in the last 12 months | 86% | 67% | +0.09 | +0.12 |
| No commit for 2+ years | 9% | 25% | −0.09 | −0.12 |

These are the strongest correlates, and they are mostly *consequences* of popularity: a popular list attracts contributors. Two parts are still informative. First, the top lists turned a one-person launch into a multi-contributor process (the control group's median top-author share is 71%, against 13% for awesome-python, awesome-go, awesome-selfhosted and free-for-dev). Second, maintenance matters more inside the curated index: 95% of the index's 50k+ lists had a commit in the last year, against 48% of its sub-2k lists, and 47% of the latter have been silent for two years or more.

### 4.7 Presentation and money

| Feature | 50k+ stars | Under 2k | ρ | ρ, age-controlled |
|---|---|---|---|---|
| Header image or logo | 77% | 44% | +0.09 | +0.13 |
| Centred HTML header | 59% | 27% | +0.07 | +0.14 |
| Companion website config in repo | 18% | 7% | +0.07 | +0.06 |
| Translated READMEs | 5% (14% for 10k–50k) | 4% | +0.12 | +0.16 |
| Sponsors section or FUNDING.yml | 50% | 10% | +0.15 | +0.18 |

Top lists look more finished: a logo, a centred header, a website. But visual polish alone is not a strategy: goabstract/Awesome-Design-Tools, the most heavily designed list we read (about 2,000 inline SVG labels and a generated website), gained ~40k stars in its launch year and has had no commits since September 2020. Sponsorship is a consequence of reach, and it carries risks for neutrality (Section 5, item 10).

### 4.8 The rules came after the winners

Inside the official index, the conventions the index now requires are *more* common among small lists than big ones:

| Feature (index sample) | 50k+ stars | Under 2k |
|---|---|---|
| Awesome badge | 77% | 99% |
| Any badge | 91% | 99% |
| awesome-lint in CI | 5% | 20% |
| Creative Commons licence | 41% | 62% |
| CONTRIBUTING file | 82% | 91% |

The big early lists were admitted before these rules existed and were grandfathered. awesome-vue is MIT-licensed, which the index's PR template calls "not acceptable"; awesome-machine-learning's LICENSE file reads, in full, "Creative Commons Legal Code / No need"; awesome-react has no licence file. The quality features of the genre (description grammar, `#readme` links, the 30-day rule, review requirements) were all added between 2016 and 2026, after the audience existed.

### 4.9 How much does design explain?

Ordinary least squares on log₁₀(stars), robust standard errors, census sample (n = 853):

| Predictor | Effect on stars | p |
|---|---|---|
| Each additional year of age | ×1.12 | <0.001 |
| Created 2023 or later (AI era) | ×1.90 | <0.001 |
| 10× more entries | ×1.78 | <0.001 |
| PR template | ×1.77 | <0.001 |
| Translated READMEs | ×1.76 | <0.001 |
| Listed in the official index | ×1.29 | 0.004 |
| Share of described entries, ToC, CONTRIBUTING, link-check CI, structured metadata, "awesome" in name | no significant positive effect | – |

These variables explain 21% of the variance in the census sample and 50% in the index sample (adding activity and author concentration: 24% / 58%; adding the number of contributors: 30% / 68%). The rest is topic demand, timing within the topic, distribution and luck, which is why the qualitative work matters.

---

## 5. Ten things the best lists do

These patterns come from the deep dives into more than 40 lists (notes in `notes/deepdive_*.md`), cross-checked against the data above.

### 1. Claim a canonical slot early, and keep earning it

Every one of the big ecosystem catalogs was created in a 19-day window in 2014 and took the generic name and the index's single slot for its topic. Those slots are durable: awesome-machine-learning (four days after the index) and awesome-react (26 days after) still hold the index's ML and React entries twelve years later. vinta/awesome-python kept gaining stars through 2021–23 while its README sat frozen at 715 entries with 48 commits in three years. The AI-era lists show the same race compressed to days: prompts.chat started 5 days after ChatGPT launched, awesome-mcp-servers 4 days after MCP was announced, awesome-agent-skills 12 days after Agent Skills.

But being first is not sufficient. punkpeye/awesome-mcp-servers was the *third* MCP list (wong2's started 1.5 days earlier) and leads 96.8k stars to 4.4k; ComposioHQ's skills list beat VoltAgent's by 11 days and leads 77.8k to 36.3k. And incumbency protects only lists that stay maintained (Sections 6 and 7).

### 2. Answer one recurring question, with sharp scope

The strongest taglines are questions the reader already has: "The definitive list that answers 'I want to do X in Python, which tool should I use?'" (awesome-python); "a list of SaaS, PaaS and IaaS offerings that have free tiers" (free-for-dev); "Master programming by recreating your favorite technologies from scratch" (build-your-own-x). Scope is then defended in writing and delegated outward: awesome-selfhosted sends deployment tools to awesome-sysadmin and checks staticgen and dbdb.io for duplicates; awesome-nodejs bans boilerplates and SaaS SDKs outright ("The world (and this list) doesn't need yet another ORM or framework"); awesome-mcp-servers spins out remote servers and clients to sibling lists.

### 3. Curate by deciding: scarcity and explicit bars

The manifesto says "It's a curation, not a collection", and the leading lists make that operational. Three working definitions of "awesome" emerged:

| Model | Example | How it is enforced |
|---|---|---|
| Editorial shortlist | awesome-python: "up to 3 obvious choices plus up to 2 challengers", hard cap 5 per use case; a full use case admits a newcomer only by **Displacement** ("name the entry your project replaces"); admission judged on PyPI downloads, not stars | Caps, an ADR, an overrides register, a rejected-additions register, removal evidence in every commit body |
| Engineering hygiene | awesome-go: ≥5 months of history, `go.mod`, a SemVer release, pkg.go.dev docs, ≥80% test coverage | A Go bot with 12 blocking checks; submitters must put the evidence links in the PR body |
| Popularity threshold | awesome-rust: 50+ stars or 2,000+ crate downloads; awesome-nodejs: 100+ stars (ratcheted up from 30) | CI in `src/main.rs`, with a commented whitelist |

Directories define their scope operationally instead: free-for-dev requires "a free tier, not just a free trial", lasting at least a year, with TLS on the free tier and "pricing information clearly visible without signup"; free-programming-books asks "How do we know it's really free?" and refuses anything "we'll need to remove in six months"; awesome-selfhosted routes BUSL, SSPL and Elastic-licensed software to a separate non-free page by a licence allowlist in its exporter.

Only scarcity rules make a list *shrink*. Threshold and hygiene lists only grow (awesome-go 2,792 → 3,170; awesome-rust +32% in 2026), and even awesome-python's cap leaks through its taxonomy (use cases grew from 77 to 140 after the prune).

### 4. Encode decision metadata in every entry

The directories that dominate their space standardise the two to five facts a reader needs to decide without clicking:

| List | Per-entry metadata |
|---|---|
| public-apis | `Auth` (apiKey / OAuth / No), `HTTPS` (Yes / No), `CORS` (Yes / No / Unknown) in a table |
| free-for-dev | The free-tier limit itself: 59% of entries contain a number ("2 million requests per month…") |
| awesome-selfhosted | Licence and language tags, a ⚠ flag for dependence on a proprietary service, Demo and Source links |
| awesome-mac | Icons for open source, freeware, App Store, native |
| awesome-courses | Material icons: lecture videos, notes, assignments, readings |
| awesome-java (2026) | Generated ★ count, SPDX licence chip and a green / orange / red activity light |
| awesome-mcp-servers | A whitelist of 15 emoji for language, scope and OS, plus a quality-score badge |

As one analyst put it: topic lists describe; directories classify. Notably, awesome-mac dropped its early subjective icons ("hot", "recommended", "must-install") by 2019 in favour of factual ones, which can be maintained and defended across 1,500 entries.

### 5. Launch full, then grow for years

See Section 4.3. Winners arrived with a substantial first version and then kept compounding; the typical small list was a weekend launch that never got its second wind.

### 6. Prune on purpose, and write down why

See Section 4.4. The distinctive practice is not just removing things but recording the reason in the commit body: "remove X (unmaintained since 2025-09-04)" (awesome-selfhosted), "It's badly maintained" (sindresorhus/awesome removing a list), "remove litellm, it got hacked twice" (awesome-python), each entry's download figure and data source (awesome-python's sweeps). That record lets maintainers answer "but X is listed" arguments, which awesome-python's ADR cites as the reason a retroactive prune was needed. Two designs coexist: *remove staleness* (awesome-python: "git history is the archive"; awesome-go: removal after notice and a 7-day grace period) or *show staleness* (awesome-java's activity lights, awesome-machine-learning's `[Deprecated]` tags). A single vetted answer earns more trust than a traffic light the reader must interpret.

### 7. Turn the README into a pipeline

At scale, the README stops being hand-edited:

- **Data as the source of truth.** awesome-selfhosted keeps 1,358 YAML files (one per entry) in a separate data repo; a tool (`hecat`) generates the README (now labelled "legacy") and the website ("recommended"), and a nightly bot refreshes stars, release dates and activity. awesome-claude-code keeps a CSV; awesome-for-beginners a JSON file; open-source-mac-os-apps a JSON file and a Swift generator; awesome-java a `README_SOURCE.md` and a Java generator.
- **Rules as bots.** awesome-go's Go bot runs 12 blocking checks and, since October 2026, auto-merges add-only PRs after one maintainer approval; additions rose from about 10 to about 40 a month. awesome-rust auto-approves PRs once CI passes, which lets one maintainer merge 388 PRs in 2026. project-based-learning keeps a link-rot state machine that opens removal PRs for entries dead two weeks in a row.
- **Contributors bring the evidence.** awesome-go wants pkg.go.dev and coverage links in the PR body; awesome-python wants a tier claim and a displacement argument; awesome-nodejs says "argue how it's better". Shifting the cost to submitters is what makes 2,600 authors with a 2% top-author share workable.

The cost is contributor friction (YAML schemas, kebab-case file names, a one-week merge delay at awesome-selfhosted) and occasional regressions: awesome-for-beginners' 2022 move to JSON silently dropped the deep links to each project's beginner-issue label (222 of 257 entries had them before, 0 after).

### 8. Build distribution into the list

- **Backlinks.** The "Mentioned in Awesome" badge turns every listed project into a backlink; awesome-claude-code automatically opens a "🎉 Your project has been featured" issue with a badge snippet on every repo it lists.
- **Websites, search and LLMs.** awesome-go.com has a page per project; awesome-python.com is rebuilt daily and ships an `llms.txt`, and its sponsorship pitch cites "referenced by ChatGPT and other LLMs" and first-page Google ranking; free-programming-books has a static site and a search site; awesome-selfhosted.net is now the recommended way to read it. Above roughly 1,000 entries, lists are looked up rather than read.
- **Communities and brands.** Awesome-Hacking (123k stars on 141 commits) is the anchor asset of the "Hack with GitHub" social accounts; papers-we-love is the index of a real meetup community; awesome-cto feeds a Substack.
- **Hacktoberfest.** 68% of free-programming-books' commits since 2023 and 35% of all awesome-for-beginners commits landed in October.
- **The index itself.** Being listed in sindresorhus/awesome is associated with ×1.29 stars in the census regression.

### 9. Ship original content or artifacts, not only links

The lists that are hardest to replace contain something of their own: the-book-of-secret-knowledge's 264 shell one-liners (about 60% of its README lines); papers-we-love's 203 hosted PDFs, which cannot rot; build-your-own-x's project briefs. Pure link lists are fungible and get captured by SEO content: about 38% of awesome-interview-questions' entries now point to content-marketing or hiring sites. In the AI era the most-starred "awesome" repos are artifact collections you use directly: prompts.chat (174k), awesome-llm-apps (143k), awesome-design-md (123k with only 66 commits), against 36–97k for the pure link lists of the same era. The adjacent mega-repos make the same point: coding-interview-university (363k) and system-design-primer (375k) are study plans with checkboxes, Anki decks and solutions, not catalogs.

### 10. Keep a voice, and keep neutrality

The high-trust knowledge lists are single-author voices: awesome-scalability is ~94% one author, awesome-cto 90%, the-book-of-secret-knowledge 84%. "Opinionated" shows through what is left out and through credential tags ("Werner Vogels *(Amazon CTO)*"), not through commentary. awesome-claude-code's descriptions read like reviews.

Money is tolerated where it stays out of the entries. sindresorhus/awesome rotates sponsor logos in its header only (45 "Meta tweaks" commits since 2020); awesome-python sells $99–$500/month placements under an explicit "does not influence which projects are listed" clause; awesome-go: "no monthly fee, but we have employees". Where commercial owners reach into the entries, quality measurably erodes:

- **public-apis:** in March 2022 the APILayer account replaced the logo, pushed an entry straight to master and, after a long-time maintainer reverted it, re-applied the change and deleted the "Currently Active Maintainers" block; the community maintainers stopped committing. After four near-silent years, 869 of 874 merges since April 2026 came from one agency email; the README now opens with APILayer ads, about 18 APILayer-family entries sit inside the "neutral" tables, and alphabetical-order errors went from 0 to 55.
- **Awesome-Design-Tools:** its acquirer's banners sit inside five categories and the acquisition announcement is still the first heading, six years after the last commit.
- **awesome-mac, awesome-ionic, VoltAgent's lists:** sponsor and owner products listed as ordinary entries without disclosure; in awesome-ionic about 39% of entries now point to the maintaining vendor's repos.

Non-profit stewardship (free-programming-books under the Free Ebook Foundation) and donation models limited to hosting costs (awesome-selfhosted's Liberapay) avoid this.

---

## 6. Same-topic rivals: a natural experiment

Many topics have several lists with the same scope, yet one has 2× to 70× the stars of the others. Comparing a winner with its same-topic rivals holds topic demand constant. The rivals study (`notes/rivals.md`) did this for 12 topics in depth, plus 12 quick-check pairs, measuring each list's entries at +7, +30, +90 and +365 days and reading early README versions.

| Topic | Winner | Best same-scope rival | Star ratio | Did the earliest list win? |
|---|---|---|---|---|
| Python | vinta/awesome-python | best-of-python | 72× | yes |
| macOS apps | jaywcjlove/awesome-mac | serhii-londar/open-source-mac-os-apps | 2.3× | **no** (iCHAIT was first) |
| React | enaqx/awesome-react | brillout/awesome-react-components | 1.5× | yes |
| Machine learning | josephmisiti/awesome-machine-learning | awesome-deep-learning | 2.6× | yes |
| MCP servers | punkpeye/awesome-mcp-servers | appcypher/awesome-mcp-servers | 17× | **no** (third of three, 1.7 days late) |
| Claude Code | hesreallyhim/awesome-claude-code | awesome-claude-code-plugins | 57× | yes |
| Claude Skills | ComposioHQ/awesome-claude-skills | VoltAgent/awesome-agent-skills | 2.1× | **no** (12 hours late) |
| iOS / Swift | vsouza/awesome-ios; matteocrippa/awesome-swift | ivanvorobei/awesome-ios; Wolg/awesome-swift | 32×; 4.5× | yes; yes |
| Hacking | Hack-with-Github/Awesome-Hacking | enaqx/awesome-pentest | 4.5× | **no** |
| Design tools | goabstract/Awesome-Design-Tools | gztchan/awesome-design | 2.4× | **no** |
| Self-hosted | awesome-selfhosted | mikeroyal/Self-Hosting-Guide | 14× | yes |
| Public APIs | public-apis/public-apis | public-api-lists | 30× | yes |

**The earliest list won 7 of 12 topics (58%), 7 of 10 if two near-simultaneous launches are excluded, and 18 of 24 including the quick checks.** Survivorship inflates these numbers. When rivals launched within hours of each other (MCP, Skills, Swift, React Hooks), the literal first mover won only 2 of 4. The timing variable that matters is "be there when the topic is born", not "beat the rival by a day": winners launched within days or weeks of WWDC 2014, the MCP announcement, the Skills launch, React Hooks day or the mid-2014 awesome wave.

**What separated winners from rivals, ranked by how often it applied:**

| Rank | Factor | Topics where it separated winner from rival | Caveat |
|---|---|---|---|
| 1 | Activity in the first 1–2 years | 10 of 12 | Highly active *late* rivals do not overtake a live incumbent |
| 2 | Present at the topic's birth | 9 of 12 | The three later winners all overtook an incumbent that stalled within 18 months |
| 3 | Distribution, brand or an existing audience | ~6 of 12, and all 5 overtakes | Never rescued a same-scope clone against a maintained incumbent |
| 4 | Scope clarity or differentiation | ~6 of 12 | Differentiation mostly produces coexistence, not victory |
| 5 | Index slot | 5 of 12 | Follows timing (granted 2–53 days after launch); 5 winners never held one |
| 6 | Launch completeness | 5 of 12 | Big late launches lost every time against a live incumbent |
| 7 | Description quality | ~4 of 12 | Matters only against weak rivals; many losers describe 99–100% of entries |
| 8 | Repo name | 0 of 12 | 7 of 12 topics had identical repo names |

**Every overtake followed the same recipe:**

1. *The incumbent stalled early.* iCHAIT/awesome-macOS had 4 entries for its first month and later lost its index slot as "badly maintained"; carpedm20/awesome-hacking sat at 65 entries for 18 months; gztchan/awesome-design froze in its second year; one MCP rival stopped accepting PRs. No list in the sample was overtaken after two years of sustained activity.
2. *The challenger offered a different product, not a better copy:* Chinese-first for developers and designers (awesome-mac), a list of lists one level up (Awesome-Hacking), "tools" with every entry described (Awesome-Design-Tools), UI-only with GIF previews (awesome-android-ui), installable skill files instead of links (ComposioHQ), a merge-everything community flywheel (awesome-mcp-servers).
3. *The challenger brought an audience:* a viral WeChat article (awesome-mac), a Discord and a directory business (awesome-mcp-servers), a company channel (ComposioHQ), social accounts (Hack with GitHub), a startup team (Awesome-Design-Tools).

**Head-on clones never beat a live incumbent.** Six late entrants launched bigger, fresher or better maintained than the leader and each got 1–7% of its stars: uhub/awesome-python launched with 869 entries against vinta's 632; public-api-lists imported public-apis' open PRs and launched larger; marcelscruz's fork of public-apis now has 1,416 commits a year and 2,027 authors; mikeroyal/Self-Hosting-Guide launched with 957 entries; Lissy93/awesome-privacy launched with more entries, a website and an API; best-of-python offers weekly quality rankings. **Differentiated neighbours coexist** at 40–65% of the winner's stars (brillout's React components, awesome-deep-learning, open-source-mac-os-apps, VoltAgent's agent skills, dkhamsing's open-source iOS apps).

Other regularities: in 6 of the 12 topics a rival has *more* entries than the winner; copying wording and formats is common and unpunished (punkpeye's launch intro is appcypher's, word for word); leads survive radical pruning, dormancy, freezes and commercialisation; and fake signals fail (one MCP list back-dated 3,489 commits to fake a 1,400-day history and has 1.1k stars).

**Bottom line:** a same-topic winner is best predicted by being there when the topic is born and staying visibly alive for the first 18–24 months. A later list wins only by finding an incumbent that stalled early and attacking it with a different product backed by an existing audience.

---

## 7. Why most lists stay small

A random, reproducible sample of 30 low-star lists (20 official-index lists under 1k stars, 10 lists with 1–3k) was read and coded by hand (`notes/control_group.md`).

| Reason the list stayed small | Any | Primary |
|---|---|---|
| Small or off-GitHub audience (Minecraft, fonts, academic niches) | 63% | **57%** |
| A dominant rival already owns the topic | 17% | 17% |
| Late arrival | 20% | 10% |
| Low effort (fewer than 60 entries or mostly undescribed) | 30% | 7% |
| Abandoned (no commit in the last year) | 53% | 3% |
| Poor discoverability (opaque name, not indexed) | 23% | 0% |
| The topic itself declined after launch | 27% | 3% |

- **Audience is a ceiling, not a failure.** `awesome-jmeter` (806 stars) and `awesome-gatling` (80) share a maintainer, template, CI and website; their stars track the tools' user bases. Framework lists track framework size: React 75k ≫ Angular 10k ≫ Svelte 2.2k > Ember 191.
- **Hygiene does not separate them.** The index sample's small lists describe 94% of their entries and have a ToC and CONTRIBUTING file almost universally.
- **Scale and continuity do.** Control-group medians: 126 entries, 12 authors, top author 71% of commits, 0 commits last year. Top four lists: 1,335 entries, 1,852 authors, top author 13%, about 700 commits last year.
- **Effort does not rescue a declining topic.** An ActionScript 3 list with 388 entries, 99.7% described, has 188 stars.
- **Incumbency only protects a maintained list.** `awesome-games-of-coding` (2017) overtook the abandoned `awesome-educational-games` (2016); a 2026 AI-security list is passing a stale 2016 one.

---

## 8. What stars do and do not measure

<!-- chart:dormant -->

**Dormant lists keep gaining stars.** trackawesomelist freezes each list's star count at its last content update. Comparing that snapshot with today's count gives the stars gained while the content was unchanged; the ratio rises steadily with time since the last update, which confirms the freeze:

| Time since last content update | Lists | Median stars now ÷ stars at last update |
|---|---|---|
| Under 6 months | 152 | 1.00 |
| 6–12 months | 49 | 1.04 |
| 1–2 years | 16 | 1.09 |
| 2–3 years | 18 | 1.17 |
| 3–5 years | 29 | 1.32 |
| 5+ years | 32 | 1.21 |

The 95 lists that had not changed for at least a year gained 202,000 stars in that time. awesome-courses has had no commits since November 2022 and went from 43k to 72k stars; awesome-interview-questions added "This project is no longer actively supported" in 2024 and gained 16k more. In the learning archetype especially, a star is a "learn this later" bookmark: in the developer survey by Borges and Valente, bookmarking (51%) is nearly as common a reason to star as appreciation (53%).

**Stars track brand and distribution.** Awesome-Hacking's 123k stars rest on 141 commits and a social-media brand. awesome-design-md reached 123k with 66 commits by one company.

**Stars can be bought, briefly.** He et al. (ICSE 2026) found about 6 million suspected fake stars across 18,617 repos, explicitly including a "list of awesome LLM tools" in their tutorial/demo category. Fake stars give a short boost (under two months, about 5× weaker than real stars) and hurt in the long run. No investigation names a specific awesome list as a buyer.

**The ecosystem is ageing.** Of the 670 lists in the official index, 57% had a commit in the last 12 months, 36% have been silent for two years or more, and 17% for five years or more. The index removed 25 archived lists in 2026.

---

## 9. 2026: the AI inflection

The deep dives independently found the same event in almost every repository: a flood of AI-generated pull requests in 2026, and a scramble to respond.

| List | Response |
|---|---|
| sindresorhus/awesome | Mar 2026: "Fully AI-generated pull requests are not accepted"; required reviews of other PRs raised from 2 to 4. Late Aug: PR and issue creation restricted to collaborators. No list added in 2026; issue/PR numbers advanced ~740 in eight months vs ~430 in all of 2025. The maintainer reportedly posted on 1 Oct 2026: "Due to AI, I have disabled external pull requests on all my repos." |
| sindresorhus/awesome-nodejs | Submissions paused ("because of too much spam and low-quality submissions") |
| josephmisiti/awesome-machine-learning | Apr 2026: "too many PRs are being generated by LLMs… email me… to prove you're human"; inflow rose about 7× |
| ripienaar/free-for-dev | Honeypot checkbox "Large Language Models and other AI tick this box"; AGENTS.md and CLAUDE.md telling agents the repo refuses AI edits |
| awesome-selfhosted | "Done by a human, not a machine/LLM" checkbox; LLM ban formalised Sep 2026; an "AI AGENTS:" block in CONTRIBUTING |
| hesreallyhim/awesome-claude-code | Issue-form-only intake ("not possible to submit… using the `gh` CLI"), cooldowns up to a ban, a honeypot, a temporary ban on a whole spammed topic |
| PatrickJS/awesome-cursorrules | Blocks accounts younger than 30 days; a 919-line linter rejects hidden Unicode, `curl \| sh` and credential exfiltration in rule files |
| fffaraz/awesome-cpp | "PRs by accounts created after 2023 or for repos created after 2023 will also result in an instant block and report" |
| vuejs/awesome-vue | AI-built projects need three releases over at least a month |
| punkpeye/awesome-mcp-servers | The opposite: agents append 🤖🤖🤖 to PR titles to be fast-tracked; ~1,410 such PRs merged, about 37% of merges since March 2026, gated by an external build-and-introspection check |

At the same time, AI became curation infrastructure. 935 of awesome-python's 1,467 commits in 2026 carry a Claude co-author trailer, and the repo ships agent skills for auditing the list and reviewing PRs; awesome-mac ships a Codex maintainer skill; awesome-vue's February 2026 hygiene sweep was authored by "Claude". It cuts both ways: two weeks later an agent-made PR left a tool-output artifact (`Resource from plugin:github:github at repo://…`) on the first line of awesome-vue's README, where it has stayed for seven months.

Three structural shifts follow:

1. **Review capacity, not demand, is now the binding constraint.** The lists that hit the wall first are single-merger lists with large inflow.
2. **Maturity replaces taste as the first filter.** When a plausible-looking repo costs nothing to generate, lists ask for time and adoption instead: 14 days of activity or 100 stars (awesome-claude-code), "brand new skills… are not accepted" (awesome-agent-skills), account age (cursorrules, awesome-cpp), a passing build (awesome-mcp-servers).
3. **Security becomes a curation axis.** Skills, hooks and rule files are instructions an agent will execute. Lists now publish malicious-exclusion counts (awesome-openclaw-skills: 373 malicious, 4,065 probable spam), lint for prompt injection, and add "curated, not audited" disclaimers.

---

## 10. Playbook

### If you are starting a list

1. **Pick a topic with a large, GitHub-native audience**, or the broadest framing of one. This is the biggest single lever, and the one no amount of polish can replace.
2. **Arrive early or arrive better.** The first credible list for a new platform has an edge measured in days. If an incumbent exists, only start a rival if you can out-maintain it; otherwise contribute to it.
3. **Write the question your list answers in the first line**, and a scope statement that says what you will refuse.
4. **Launch with a substantial first version**, with a balanced taxonomy (no category over ~15% of entries, no categories with two items).
5. **Meet the table stakes:** a one-line description for every entry, a ToC, consistent formatting, a CC0 licence, a CONTRIBUTING file, the badge, the `awesome-list` topic. They will not make you popular, but you cannot get into the index or keep readers' trust without them.
6. **Standardise decision metadata** if your list is a directory: the two to five facts a reader needs before clicking.

### If your list is growing

7. **Publish measurable inclusion criteria** and make submitters supply the evidence in the PR.
8. **Automate the rules:** link checking, format and duplicate checks, an activity check, ideally a data file as the source of truth and a generated README.
9. **Prune on a schedule** and write the reason in each removal commit. Decide whether you remove staleness or display it.
10. **Recruit a second merger** before you need one; every list that paused in 2026 had one.
11. **Build reading surfaces** beyond the README once you pass ~1,000 entries: a website, per-entry pages, search, an `llms.txt`.

### If your list is big

12. **Fence money off from entries**, with a written independence clause and disclosure for anything sponsored or owned.
13. **Defend the intake:** issue forms or templates, a human attestation, maturity gates, and bots that do the first pass. Decide your stance on agent-made submissions explicitly; both refusal and a gated fast lane can work.

### Anti-patterns

- A weekend launch that never gets a second wave of work.
- A taxonomy of many tiny categories that fakes depth.
- Copied CONTRIBUTING boilerplate that does not fit the list.
- Accretion without removal, or `[Deprecated]` tags that are never cleaned up.
- A sole maintainer with no automation and growing inflow.
- Sponsor entries mixed into the list without disclosure.
- A list on a topic that is already declining.

---

## Appendix A: full feature tables

Medians for numeric features, percentages for yes/no features. ρ is the Spearman correlation with stars; the age-controlled ρ is a partial rank correlation holding the first-commit date constant.

### Census sample (n = 861: 22 lists with 50k+ stars, 113 with 10k–50k, 376 with 2k–10k, 350 under 2k)

| Feature | Group | ρ (stars) | ρ age-controlled | ≥50k | 10k–50k | 2k–10k | <2k |
|---|---|---|---|---|---|---|---|
| Year of first commit | Timing & positioning | -0.20 | -0.00 | 2015 | 2017 | 2018 | 2019 |
| Name contains "awesome" | Timing & positioning | -0.06 | -0.07 | 73% | 83% | 85% | 88% |
| Listed in sindresorhus/awesome | Timing & positioning | +0.15 | +0.08 | 68% | 41% | 30% | 24% |
| README mostly Chinese/Japanese/Korean | Timing & positioning | -0.07 | -0.03 | 0% | 3% | 7% | 6% |
| Entries (links) in README | Content | +0.27 | +0.28 | 593 | 352 | 214 | 146 |
| Share of entries with a description | Content | +0.05 | +0.04 | 93% | 87% | 88% | 82% |
| Words per description | Content | -0.02 | +0.01 | 9.9 | 10.6 | 10.6 | 11.2 |
| Categories with entries | Content | +0.19 | +0.18 | 51 | 28 | 21 | 18 |
| Median entries per category | Content | +0.07 | +0.09 | 7 | 6 | 6 | 5 |
| Largest category share of entries | Content | -0.14 | -0.14 | 11% | 17% | 18% | 20% |
| Structured per-entry metadata (tags/stars/table) | Content | +0.04 | +0.08 | 14% | 18% | 18% | 15% |
| Entries alphabetized (>=90% sorted pairs) | Content | +0.07 | +0.06 | 28% | 29% | 17% | 18% |
| Share of links pointing to GitHub repos | Content | +0.01 | -0.01 | 39% | 37% | 40% | 40% |
| README words | Content | +0.28 | +0.31 | 7,584 | 5,542 | 3,245 | 2,292 |
| Words before first section | Presentation | +0.07 | +0.08 | 108 | 63 | 52 | 52 |
| Table of contents | Presentation | +0.03 | +0.01 | 91% | 80% | 83% | 83% |
| Back-to-top links | Presentation | +0.10 | +0.10 | 18% | 12% | 9% | 6% |
| Any badges | Presentation | +0.01 | +0.02 | 82% | 82% | 83% | 83% |
| Awesome badge | Presentation | +0.01 | -0.01 | 73% | 75% | 70% | 73% |
| Header image/logo | Presentation | +0.09 | +0.13 | 77% | 59% | 49% | 44% |
| Centered HTML header | Presentation | +0.07 | +0.14 | 59% | 34% | 29% | 27% |
| Emoji per entry | Presentation | +0.05 | +0.10 | 0.021 | 0.006 | 0.005 | 0.003 |
| Collapsible <details> sections | Presentation | -0.01 | +0.04 | 14% | 10% | 8% | 10% |
| Translated READMEs | Presentation | +0.12 | +0.16 | 4% | 14% | 8% | 4% |
| Companion website config in repo | Presentation | +0.07 | +0.06 | 18% | 10% | 10% | 7% |
| CONTRIBUTING file | Process & governance | +0.12 | +0.09 | 86% | 78% | 69% | 66% |
| CONTRIBUTING length (words) | Process & governance | +0.15 | +0.15 | 296 | 225 | 139 | 134 |
| PR template | Process & governance | +0.20 | +0.20 | 46% | 42% | 19% | 14% |
| Issue template/forms | Process & governance | +0.11 | +0.14 | 36% | 22% | 12% | 10% |
| Code of conduct | Process & governance | -0.00 | -0.00 | 41% | 20% | 28% | 28% |
| README states inclusion criteria | Process & governance | +0.04 | +0.06 | 23% | 28% | 16% | 21% |
| Any CI (Actions/Travis) | Process & governance | +0.15 | +0.15 | 54% | 61% | 44% | 37% |
| Automated link checking | Process & governance | +0.14 | +0.11 | 27% | 37% | 22% | 18% |
| awesome-lint in CI | Process & governance | -0.01 | -0.01 | 4% | 10% | 11% | 11% |
| Creative Commons license | Process & governance | -0.02 | -0.01 | 36% | 49% | 46% | 49% |
| No license file | Process & governance | -0.00 | -0.05 | 32% | 26% | 27% | 26% |
| Sponsors section or FUNDING.yml | Process & governance | +0.15 | +0.18 | 50% | 24% | 13% | 10% |
| Flags unmaintained/archived entries | Process & governance | +0.03 | +0.03 | 32% | 27% | 27% | 24% |
| Commits (all time) | Activity & community | +0.43 | +0.41 | 1,510 | 587 | 221 | 135 |
| Distinct commit authors | Activity & community | +0.45 | +0.41 | 387 | 129 | 39 | 20 |
| Top author share of commits | Activity & community | -0.22 | -0.17 | 35% | 36% | 49% | 59% |
| People who merged PRs | Activity & community | +0.31 | +0.26 | 6 | 3 | 2 | 1 |
| Highest issue/PR number referenced | Activity & community | +0.49 | +0.47 | 1,574 | 349 | 94 | 47.5 |
| Commit in last 12 months | Activity & community | +0.09 | +0.12 | 86% | 78% | 67% | 67% |
| Human commit in last 12 months | Activity & community | +0.09 | +0.12 | 82% | 78% | 66% | 66% |
| No commit for 2+ years | Activity & community | -0.09 | -0.12 | 9% | 17% | 23% | 25% |
| Calendar years with commits | Activity & community | +0.23 | +0.12 | 10.5 | 8 | 7 | 6 |
| Entries one year after launch | History | +0.20 | +0.24 | 408 | 176 | 117 | 97 |
| Share of peak size reached by year 1 | History | -0.15 | -0.08 | 56% | 60% | 67% | 71% |
| Ever cut >=10% of entries in a quarter | History | +0.07 | +0.05 | 32% | 24% | 14% | 15% |
| Currently >=10% smaller than its peak | History | +0.11 | +0.10 | 23% | 20% | 10% | 8% |
| More than doubled in size after year 1 | History | +0.17 | +0.12 | 50% | 43% | 34% | 25% |

### Official-index sample (n = 558: 22 / 67 / 145 / 324)

| Feature | Group | ρ (stars) | ρ age-controlled | ≥50k | 10k–50k | 2k–10k | <2k |
|---|---|---|---|---|---|---|---|
| Year of first commit | Timing & positioning | -0.37 | +0.07 | 2014 | 2015 | 2016 | 2017 |
| Name contains "awesome" | Timing & positioning | -0.14 | -0.05 | 77% | 87% | 94% | 94% |
| Listed in sindresorhus/awesome | Timing & positioning | – | +0.00 | 100% | 100% | 100% | 100% |
| README mostly Chinese/Japanese/Korean | Timing & positioning | – | +0.00 | 0% | 0% | 0% | 0% |
| Entries (links) in README | Content | +0.57 | +0.56 | 712 | 369 | 166 | 94 |
| Share of entries with a description | Content | +0.05 | +0.12 | 95% | 91% | 92% | 90% |
| Words per description | Content | +0.09 | +0.17 | 10.8 | 10.8 | 10.8 | 10.1 |
| Categories with entries | Content | +0.36 | +0.34 | 65 | 28 | 22 | 15 |
| Median entries per category | Content | +0.30 | +0.30 | 9 | 6 | 5 | 4 |
| Largest category share of entries | Content | -0.26 | -0.24 | 11% | 14% | 16% | 21% |
| Structured per-entry metadata (tags/stars/table) | Content | +0.02 | +0.04 | 18% | 6% | 6% | 6% |
| Entries alphabetized (>=90% sorted pairs) | Content | +0.11 | +0.10 | 37% | 30% | 19% | 18% |
| Share of links pointing to GitHub repos | Content | +0.16 | +0.11 | 58% | 46% | 47% | 35% |
| README words | Content | +0.53 | +0.56 | 14,427 | 5,216 | 2,631 | 1,409 |
| Words before first section | Presentation | +0.10 | +0.10 | 83.5 | 61 | 56 | 53 |
| Table of contents | Presentation | +0.01 | +0.15 | 91% | 90% | 90% | 89% |
| Back-to-top links | Presentation | +0.10 | +0.10 | 23% | 8% | 6% | 3% |
| Any badges | Presentation | -0.15 | -0.08 | 91% | 92% | 96% | 99% |
| Awesome badge | Presentation | -0.17 | -0.11 | 77% | 92% | 96% | 99% |
| Header image/logo | Presentation | -0.03 | +0.10 | 64% | 46% | 50% | 50% |
| Centered HTML header | Presentation | +0.07 | +0.18 | 50% | 21% | 23% | 17% |
| Emoji per entry | Presentation | +0.23 | +0.26 | 0.016 | 0.003 | 0 | 0 |
| Collapsible <details> sections | Presentation | +0.04 | +0.09 | 9% | 3% | 2% | 2% |
| Translated READMEs | Presentation | +0.09 | +0.09 | 4% | 8% | 2% | 2% |
| Companion website config in repo | Presentation | +0.10 | +0.11 | 23% | 10% | 7% | 6% |
| CONTRIBUTING file | Process & governance | -0.08 | +0.08 | 82% | 87% | 88% | 91% |
| CONTRIBUTING length (words) | Process & governance | +0.15 | +0.27 | 340 | 214 | 169 | 162 |
| PR template | Process & governance | +0.32 | +0.36 | 64% | 48% | 21% | 10% |
| Issue template/forms | Process & governance | +0.18 | +0.20 | 27% | 18% | 11% | 5% |
| Code of conduct | Process & governance | -0.09 | +0.05 | 50% | 22% | 32% | 38% |
| README states inclusion criteria | Process & governance | +0.09 | +0.11 | 23% | 21% | 10% | 11% |
| Any CI (Actions/Travis) | Process & governance | +0.15 | +0.20 | 64% | 69% | 59% | 47% |
| Automated link checking | Process & governance | +0.17 | +0.13 | 32% | 52% | 34% | 27% |
| awesome-lint in CI | Process & governance | -0.09 | +0.08 | 4% | 9% | 19% | 20% |
| Creative Commons license | Process & governance | -0.12 | +0.11 | 41% | 49% | 57% | 62% |
| No license file | Process & governance | +0.02 | -0.14 | 27% | 33% | 28% | 28% |
| Sponsors section or FUNDING.yml | Process & governance | +0.16 | +0.20 | 46% | 18% | 14% | 8% |
| Flags unmaintained/archived entries | Process & governance | +0.15 | +0.14 | 41% | 24% | 26% | 14% |
| Commits (all time) | Activity & community | +0.68 | +0.66 | 2,112 | 599 | 221 | 99 |
| Distinct commit authors | Activity & community | +0.78 | +0.73 | 630 | 182 | 51 | 14 |
| Top author share of commits | Activity & community | -0.50 | -0.43 | 24% | 28% | 41% | 64% |
| People who merged PRs | Activity & community | +0.46 | +0.38 | 8.5 | 3 | 2 | 1 |
| Highest issue/PR number referenced | Activity & community | +0.76 | +0.74 | 2,550 | 399 | 116 | 26 |
| Commit in last 12 months | Activity & community | +0.31 | +0.38 | 96% | 69% | 70% | 48% |
| Human commit in last 12 months | Activity & community | +0.30 | +0.37 | 91% | 67% | 68% | 47% |
| No commit for 2+ years | Activity & community | -0.32 | -0.39 | 4% | 27% | 21% | 47% |
| Calendar years with commits | Activity & community | +0.61 | +0.52 | 13 | 11 | 9 | 6 |
| Entries one year after launch | History | +0.41 | +0.41 | 422 | 208 | 96 | 66.5 |
| Share of peak size reached by year 1 | History | -0.45 | -0.41 | 34% | 49% | 56% | 78% |
| Ever cut >=10% of entries in a quarter | History | +0.20 | +0.18 | 50% | 25% | 22% | 13% |
| Currently >=10% smaller than its peak | History | +0.17 | +0.13 | 32% | 18% | 14% | 8% |
| More than doubled in size after year 1 | History | +0.36 | +0.32 | 73% | 51% | 42% | 17% |


## Appendix B: data, code and reproducibility

Everything is in the [depuschm/awesome-lists-research](https://github.com/depuschm/awesome-lists-research) repository:

| Path | Contents |
|---|---|
| `REPORT.md` | This report |
| `notes/` | Literature review, six archetype deep dives, rivals study, control group, analyst rubric |
| `data/master_stars.tsv` | 1,598 repos with stars from every source, index membership and category |
| `data/corpus.csv` | 1,568 repos × ~110 columns (features, stars, classification) |
| `data/analysis/lists_enriched.csv` | 1,291 analysed lists with the main features and README-history metrics |
| `data/analysis/feature_tiers_{census,index,all}.csv` | Tier comparisons and correlations |
| `data/analysis/summary_*.json`, `cohorts_*.csv` | Concentration, cohorts and regression results |
| `data/readme_history_final.jsonl` | Quarterly README size and entry counts for 1,609 repos |
| `data/analysis/dormant_star_growth.csv` | Star growth while content was unchanged |
| `data/github_top100_classified.tsv` | GitHub's overall top 100 by kind |
| `data/manual_kind.csv`, `data/archetypes_top.csv` | Manual classifications |
| `scripts/` | `clone_one.sh`, `extract.py`, `readme_history.py`, `build_corpus.py`, `analyze.py`, `export_viz.py` and the parsers |

To reproduce: run `scripts/clone_one.sh` over `data/master_stars.tsv`, then `extract.py` and `readme_history.py` over `clones/`, then `build_corpus.py`, `analyze.py`, `export_viz.py` and `build_page.py` (Python 3.13; see `requirements.txt` and the README for exact commands).

## Sources

**Data**

- [GitHub topic: awesome-list](https://github.com/topics/awesome-list) - 17,872 repositories; top 1,000 by stars collected.
- [GitHub topic: awesome](https://github.com/topics/awesome) - 12,754 repositories; top 500 by stars collected.
- [sindresorhus/awesome](https://github.com/sindresorhus/awesome) - The official index; its manifesto, PR template and contributing rules.
- [sindresorhus/awesome-lint](https://github.com/sindresorhus/awesome-lint) - The linter that gates the index.
- [trackawesomelist](https://github.com/trackawesomelist/trackawesomelist) - Star snapshots and last-update dates for 682 lists.
- [EvanLi/Github-Ranking](https://github.com/EvanLi/Github-Ranking) - GitHub's overall top 100 by stars.

**Research**

- [Wu, Kropczynski, Prates & Carroll, The Rise of Curation on GitHub (HCOMP 2015)](https://ojs.aaai.org/index.php/HCOMP/article/view/13244) - First description of curation repositories as a popular category.
- [Wu, Wang, Kropczynski & Carroll, The appropriation of GitHub for curation (PeerJ CS, 2017)](https://peerj.com/articles/cs-134/) - Interviews with 16 curators on motivations and limits.
- [Wu, Kropczynski, Prates & Carroll, Understanding How GitHub Supports Curation Repositories (Future Internet, 2018)](https://www.mdpi.com/1999-5903/10/3/29) - Curation repos are more popular than software repos and mostly run by individuals.
- [Kalliamvakou et al., The Promises and Perils of Mining GitHub (MSR 2014)](https://kblincoe.github.io/publications/2014_MSR_Promises_Perils.pdf) - A large share of repositories are not software.
- [Borges, Hora & Valente, Understanding the Factors that Impact the Popularity of GitHub Repositories (ICSME 2016)](https://arxiv.org/abs/1606.04984) - Domain effects and growth patterns.
- [Borges & Valente, What's in a GitHub Star? (JSS 2018)](https://arxiv.org/abs/1811.07643) - Why developers star; viral growth follows social-media promotion.
- [Borges & Valente, How do Developers Promote Open Source Projects? (IEEE Computer 2019)](https://arxiv.org/abs/1908.04219) - Promotion channels and the Hacker News effect.
- [Fan et al., What makes a popular academic AI repository? (EMSE 2021)](https://arxiv.org/abs/2010.02472) - README links, images and licences separate popular repos.
- [He et al., Six Million (Suspected) Fake Stars on GitHub (ICSE 2026)](https://arxiv.org/abs/2412.13459) - Fake-star campaigns and their short-lived effect.

**Practitioner sources**

- [vinta/awesome-python: shortlist ADR](https://github.com/vinta/awesome-python/blob/master/docs/adr/0001-shortlist-not-catalog.md) - The 2026 "shortlist, not a catalog" decision.
- [avelino/awesome-go: CONTRIBUTING](https://github.com/avelino/awesome-go/blob/main/CONTRIBUTING.md) - Measurable quality standards and the removal protocol.
- [awesome-selfhosted-data](https://github.com/awesome-selfhosted/awesome-selfhosted-data) - Data-driven list architecture and freshness checks.
- [ripienaar/free-for-dev: CONTRIBUTING](https://github.com/ripienaar/free-for-dev/blob/master/CONTRIBUTING.md) - Eligibility rules and the services the list refuses.
- [hesreallyhim/awesome-claude-code: CONTRIBUTING](https://github.com/hesreallyhim/awesome-claude-code/blob/main/CONTRIBUTING.md) - Issue-form intake and maturity gates.
- [punkpeye/awesome-mcp-servers: CONTRIBUTING](https://github.com/punkpeye/awesome-mcp-servers/blob/main/CONTRIBUTING.md) - The agent fast lane.
- [HackerNoon, Awesome-Lists, Everywhere](https://hackernoon.com/the-history-of-github-awesome-lists) - Early history of the format.
- [GitHub changelog, 13 Feb 2026](https://github.blog/changelog/2026-02-13-new-repository-settings-for-configuring-pull-request-access/) - New settings to restrict pull requests.
- [Sindre Sorhus on X, 1 Oct 2026](https://x.com/sindresorhus/status/2105693826690298314) - "Due to AI, I have disabled external pull requests on all my repos" (as reported in search results; not fetched directly).

The full source list, with about 90 links, is in `notes/literature.md`.
