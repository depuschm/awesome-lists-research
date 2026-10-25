# Research handoff: a data-driven study of a GitHub phenomenon

You are the research lead for a multi-hour, data-driven study that ends as a polished public GitHub repository with a website. Work autonomously and thoroughly: this is hours of work and I want it done properly, not summarised.

A finished example of everything below is https://github.com/depuschm/awesome-lists-research (website: https://depuschm.github.io/awesome-lists-research). Clone it early. Reuse its pipeline, page, README and publishing scripts as templates, and adapt them to the new topic rather than starting from scratch.

**My research topic:** [write the topic here, or write "suggest topics"]
**My GitHub username:** depuschm

---

## Step 1: Agree on the topic before any heavy work

**If I gave a topic,** assess it and reply before starting. Give a verdict (good as is / narrow it / expand it / reframe it) with a short reason, checked against these criteria:

1. **A sharp question with a measurable outcome.** For example "what makes the most-starred X so popular" or "why do some X die". Name the outcome variable: stars, downloads, forks, survival, adoption.
2. **A population of hundreds to a few thousand comparable items**, findable through public sources, with a natural ranking.
3. **Data reachable from a cloud sandbox:** git clones of public repos, raw.githubusercontent.com, GitHub topic pages through web fetch, public datasets. Check feasibility before promising anything.
4. **Observable features:** content and structure, git history, governance files, timing.
5. **Room for a natural experiment** (same-topic rivals) and a control group (a random sample of low performers).
6. **Novelty:** not already answered well by existing research.
7. **No personal data about private individuals,** and respect for terms of service.

Then offer two or three improved framings (narrower, wider or reframed), say which you recommend, and estimate the corpus size and effort. Wait for my go-ahead.

**If I wrote "suggest topics",** propose six to eight candidates around GitHub and open source. For each, give the question, the population and how to find it, the outcome variable, the data sources, the feasibility risks and what might be surprising. Recommend one, then wait for my choice.

---

## Step 2: Check the environment (first ten minutes)

Test what is reachable before designing the method, and adapt to what you find:
- the GitHub REST API (`gh api rate_limit`), the search API and GraphQL. In the last session search and GraphQL were blocked, and only repo-scoped endpoints for attached repos worked;
- `git clone` of a public repo (worked) and raw.githubusercontent.com (worked);
- web fetch of github.com topic pages (worked: 20 repos per page, pages 1–50) and web search (worked; many other sites were blocked);
- BigQuery and other data services (unauthenticated last time).

Report in a few lines what works, and adapt the plan.

---

## Step 3: Build an unbiased corpus

- **Combine ranked sources:** topic pages, curated indexes, trackers or datasets hosted on GitHub, overall rankings such as EvanLi/Github-Ranking. Save every raw snapshot in `raw/` and every parsed ranking in `data/`.
- **Clone everything** as partial, sparse clones (`git clone --filter=blob:none --sparse`, then `git sparse-checkout add .github`). That gives full commit history with only root files checked out. Run clones 8 in parallel in the background.
- **De-duplicate** by root commit *and* by case-insensitive name. Renamed repos and forks share a root commit, and the same repo can get cloned twice under different capitalisations.
- **Classify each item** (in scope or not) with a heuristic, then review the top tier by hand and keep the manual overrides in a CSV.
- **Avoid selection bias.** Last time, small items entered mostly through one source and big ones through another, which made a harmless feature look harmful. Run statistics only on clean samples (a census taken from a single ranking, and a population defined by one gate), and use the union of sources only for description.
- **Keep a manifest:** every item, its status (analysed / excluded and why / duplicate / failed) and the exact commit SHA analysed.

---

## Step 4: Extract features

- **History:** first and last commit, commits, distinct authors, top-author share, people who merged PRs, highest issue/PR number referenced, activity by year, bot share, activity in the last 12 months.
- **Files:** CONTRIBUTING, code of conduct, PR and issue templates, CI workflows and what they check, licence type, translations, website configs, funding files.
- **Content:** a parser for the item's main artifact (for lists, entries, descriptions, categories, ordering, ToC and badges).
- **History snapshots:** reconstruct content quarter by quarter from git. Batch-fetch the old blobs with `git fetch --filter=blob:none --stdin` in one call per repo, then compute growth, peak and pruning.

Rules:
- Test the parser on ten very different real examples before running it at scale. Real formats include HTML anchors, tables without leading pipes, blockquote entries, reference-style links, bare URLs, setext headings and headings that contain links.
- Measure every time-based feature against a fixed reference date, so the results are reproducible.
- Watch for quadratic code: one repo had 225,000 commits.
- Never use `pkill -f` with a pattern that also matches your own command line.

---

## Step 5: Qualitative work, in parallel

Launch background sub-agents while you build the pipeline. Give each a precise brief, its own output file, and a shared rubric (`notes/RUBRIC.md`):
- **Ranking scrapers:** one per page range, each with its own output file and helper script. Last time, two agents sharing a helper script wrote into each other's files.
- **Literature review:** origins, official rules, academic papers, practitioner advice, recent developments. Every claim cites a URL, and anything taken only from search snippets is marked as secondary.
- **Archetype deep dives:** group the top items into four to six archetypes and give each to one analyst, who reads the actual files and git history.
- **Same-topic rivals:** for ten to twelve topics, compare the winner with its same-scope rivals (timing, launch completeness, maintenance, distribution) and count how often each factor separates them.
- **Control group:** a seeded random sample of about 30 low performers, coded for why they stayed small.

Read every note in full yourself, and spot-check the surprising claims against the data before using them.

---

## Step 6: Statistics

- **Tiers:** compare the top tier with the bottom, and report medians or percentages per tier.
- **Correlations:** Spearman correlation with the outcome, plus a partial correlation controlling for age.
- **Two sorts of feature:** separate "table stakes" (equally common at every tier) from differentiators.
- **Cohorts:** results by creation year, to find the windows when items could win.
- **Concentration:** top-10 share, top-10% share and the Gini coefficient.
- **Regression:** OLS on log(outcome) with robust standard errors, in two or three nested models (design-only, then adding activity, then community). Report R² honestly.
- **Causes vs consequences:** say which features are probably consequences of popularity (contributors, templates, sponsors) and which can be measured at launch.
- **What the outcome measures:** test what it does and doesn't capture (last time, stars kept growing while content sat still).

---

## Step 7: Write and fact-check the report

Write `REPORT.md` with these parts:
- the title and a Contents list;
- Key findings, numbered, each with a number;
- why the topic matters;
- method (sources table, samples, features, limitations);
- who the winners are (top-30 table, archetypes, cohorts);
- what separates the top from the rest (table stakes, then differentiators, then regression);
- "N things the best ones do";
- same-topic rivals;
- why most stay small;
- what the outcome does and doesn't measure;
- current shifts;
- a playbook;
- appendices (full feature tables; data and reproducibility);
- sources, in a fitting format.

Before anything goes public, check every number you typed by hand against the data files. Last time this caught a wrong count (45 that should have been 40), a sentence mixing two samples, and a wrong chart caption. Also look for overreaching wording.

---

## Step 8: Publish

Everything goes into my repository. Only these steps need me:
1. **Create an empty public repo** (no README, licence or .gitignore). Make sure the Claude GitHub App can access it, then tell you the name.
2. **Paste the About description and topics** you draft. The description must be 350 characters or fewer. Leave out topics that would put the repo into the very population it studies.
3. **Turn on GitHub Pages:** Settings → Pages → Deploy from a branch → `main`, folder `/docs`. You are not allowed to switch on a public site yourself.
4. **Upload the social preview:** Settings → General → Social preview → upload `assets/social-preview.png`.

**Repository layout:**
- `README.md`
- `REPORT.md`
- an item manifest (for example `REPOSITORIES.md`), plus `data/repositories.tsv` with pinned commit SHAs and links to each snapshot
- `docs/index.html`, `docs/social-preview.png`, `docs/.nojekyll`
- `page/` (the fragment for the private Claude page)
- `assets/readme/*-light.png` and `*-dark.png`, `assets/social-preview.png`
- `notes/`, `data/` and `data/analysis/`, `raw/`, `scripts/`
- `requirements.txt` with pinned versions
- `.gitignore` covering the clones and the virtual environment
- `LICENSE`: CC BY 4.0 for content, using the official text from github/choosealicense.com
- `scripts/LICENSE`: MIT, "Copyright (c) [year] depuschm"
- A README licence section saying third-party snapshots and quoted material keep their owners' terms.

**Scripts:**
- paths relative to the repo;
- one build script that writes both the website (`docs/index.html`) and the private Claude page from `REPORT.md` and the chart data, and copies the social card into `docs/`;
- a manifest script;
- a `clone_one.sh owner/repo [sha]` that can re-create a pinned snapshot;
- an image script (Playwright) that screenshots the website into README images in light and dark, plus the 1280×640 social card. Drop "hover" cues from static images.

Before pushing, re-run the whole pipeline from another directory and compare checksums of the key outputs. Do not commit the clones; the manifest makes them reproducible.

**Website:**
- one standalone HTML file with a description, Open Graph and Twitter tags (large image, `og:image` pointing at the social card) and a canonical URL;
- light and dark themes, with hand-built SVG charts and hover tooltips;
- charts used last time: a unit chart, cohort columns, a dumbbell chart (top tier vs bottom), a log-log scatter, small-multiple growth curves, and dormancy columns;
- validate the chart palette (load the dataviz skill) and check desktop and phone widths in both themes for overflow and errors;
- give each study its own visual identity that fits its subject (fonts, palette, one subject-specific detail), rather than copying the last one's look;
- also publish the page as a private Claude artifact for quick viewing.

**README:**
- a centred banner that switches with the reader's theme (`<picture>` with a `prefers-color-scheme` source);
- three badges (read the report, items analysed, data date) and a link row;
- a two-column "separates the winners / barely matters" table with numbers;
- three key charts as light and dark images;
- "N things the best ones do", one line each, linking to report sections;
- a Mermaid diagram of the pipeline;
- limitations in a `> [!NOTE]` box;
- a "which items were studied" section;
- collapsible `<details>` blocks for the repository layout and the reproduce steps;
- licence and credits.

**Commits:** clear messages with the attribution trailers your instructions require. After each push, confirm the remote matches with `git ls-remote`, and check the Pages deployment through the repo's Actions runs.

---

## How to work with me

- Keep me posted with short progress notes, and share striking findings as they emerge.
- Ask me only about decisions that are mine: the topic, the repo name, anything that goes public.
- Be honest about limitations and anything you could not verify, and correct mistakes openly.
- Write plainly. Keep final summaries short, with links.
- The cloud environment is temporary, so make sure everything worth keeping ends up pushed.
