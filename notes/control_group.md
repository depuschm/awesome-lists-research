# Control group: ordinary awesome lists and why they stayed small

Analyst note, 2026-10-25. Data: `data/master_stars.tsv`, local clones, `scripts/extract.py`, plus a manual read of 10 random entries per list. Star counts are the `stars` column (Sample A: track-awesome-list snapshot, exact; Sample B: mostly GitHub topic pages, rounded to 0.1k).

## TL;DR

- **Audience size is the main ceiling.** It is the primary cause for 17 of 30 lists (57%) and a factor for 19 (63%): the topic's GitHub audience is small, or it curates elsewhere. Same maintainer, template and CI: `awesome-jmeter` has 806 stars, `awesome-gatling` 80.
- **Inside the index, hygiene doesn't separate low-star lists from top lists.** Sample A medians: desc_ratio 0.94, ToC 100%, CONTRIBUTING 95%. Top four: 0.97, 100%, 75%. Across 585 in-index lists, desc_ratio vs stars has Spearman ρ = 0.01.
- **Scale and continuity do.** Control medians: 126 entries, 12 authors, top author 71% of commits, 0 commits last year. Top four (awesome-python, awesome-go, awesome-selfhosted, free-for-dev): 1,335 entries, 1,852 authors, top author 13%, ~700 commits last year.
- **Abandonment is common but rarely the root cause.** 53% had no commit in the last year; 33% were one-shot launches (≥50% of commits in the first 90 days), against 0 of the top four. Usually the audience never came, and then the maintainer stopped.
- **Rivals (17% any) and late arrival (20%) are secondary.** Topic decline after launch, not in the original taxonomy, touches 27%: Framer Classic, Ember, Seed, Browserify, ActionScript 3, Ionic, pre-LLM question answering, crypto OpSec.
- **Incumbency only protects a maintained list.** A later, maintained rival (games-of-coding, 2.2k) overtook an early, abandoned one (educational-games, 667). A 2026 newcomer (ai-security-tools, 1.7k in under a year) is passing a stale 2016 incumbent.

---

## 1. Sampling (reproducible)

Pools, drawn from `master_stars.tsv` and excluding rows with missing stars:

- **Pool A:** `in_index == 1` and `stars < 1000`. That is 233 repos, which is **40% of the 585 in-index lists that have star data** (the index median is 1,400 stars). The pool median is 333 stars and our sample median is 344, so the sample is representative.
- **Pool B:** `1000 <= stars <= 3000`, any index status. That is 646 repos, 164 of them in the index.

```python
import csv, random
rows = list(csv.DictReader(open('data/master_stars.tsv'), delimiter='\t'))
st = lambda r: int(float(r['stars'])) if r['stars'] else None
A = sorted([r for r in rows if st(r) is not None and st(r) < 1000 and r['in_index'] == '1'], key=lambda r: r['repo'].lower())
B = sorted([r for r in rows if st(r) is not None and 1000 <= st(r) <= 3000], key=lambda r: r['repo'].lower())
rng = random.Random(42)
orderA = rng.sample(A, len(A))   # draw A first...
orderB = rng.sample(B, len(B))   # ...then B, from the same generator
# take the first 20 valid of orderA and the first 10 valid of orderB; skipped items are replaced by the next in order
```

**Skips:**
- Sample A: none. Positions 0–19 were all valid curated lists with clones present.
- Sample B: two skips.
  - Position 2, `uhub/awesome-python` (1,200 stars). It is an auto-generated dump ranked by stars: monthly "uhub update" commits since April 2018, and the entries are the GitHub repo descriptions. It is not human-curated.
  - Position 10, `brycewang-stanford/Awesome-Journal-Skills` (1,300 stars). It is a content/code project (4,166 agent skill packs and 11,153 code files), not a list of external resources.
  - Positions 0, 1, 3–9 and 11 were used. All 30 clones existed.

**Manual entry read:** in each README I took the markdown bullet lines that contain a non-anchor link and drew 10 of them with `random.Random(42).sample`. An entry counts as "described" only if it has explanatory text outside the link name. Two caveats on the extractor:
- It undercounts descriptions in `awesome-vapor`, where a version-badge image comes before each link: the script gives 0.08, the manual read gives 8/10.
- Paper lists (`awesome-qa`, `awesome-imbalanced-learning`) carry citation metadata instead of descriptions. Both the script and the manual read score them low, correctly.

---

## 2. Per-list record

### 2a. Metrics (from `extract.py`; manual = described entries out of 10 random entries)

| # | Repo | Stars | 1st yr | Entries | desc_ratio / manual | ToC · sections w/ items | CONTRIB | Authors | Commits/yr (life) | Commits last 365d | Last commit (days) | 1st-90d share |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| A0 | podo/awesome-framer | 622 | 2015 | 151 | 0.97 / 10 | ✓ · 12 | ✓ | 9 | 7.4 | 4 | 19 | 0.16 |
| A1 | caufieldjh/awesome-bioie | 437 | 2019 | 119 | 0.93 / 9 | ✓ · 24 | ✓ | 4 | 22.4 | 5 | 151 | 0.76 |
| A2 | aliesbelik/awesome-gatling | 80 | 2019 | 73 | 0.80 / 9 | ✓ · 18 | ✓ | 4 | 14.8 | 18 | 19 | 0.09 |
| A3 | seriousran/awesome-qa | 706 | 2018 | 133 | 0.09 / 0 | ✓ · 23 | ✓ | 5 | 16.9 | 0 | 1,746 | 0.74 |
| A4 | folkswhocode/awesome-diversity | 572 | 2017 | 206 | 0.96 / 10 | ✓ · 11 | ✓ | 37 | 24.8 | 0 | 1,951 | 0.37 |
| A5 | ember-community-russia/awesome-ember | 191 | 2018 | 881 | 0.51 / 7 | ✓ · 130 | ✓ | 18 | 76.8 | 0 | 817 | 0.36 |
| A6 | dylanrees/citizen-science | 308 | 2016 | 143 | 0.94 / 10 | ✓ · 24 | ✓ | 12 | 17.9 | 8 | 179 | 0.67 |
| A7 | ConstructCommunity/awesome-construct | 83 | 2016 | 80 | 0.89 / 9 | ✓ · 20 | ✓ | 11 | 8.8 | 0 | 494 | 0.18 |
| A8 | seed-rs/awesome-seed-rs | 218 | 2019 | 33 | 0.91 / 9 | ✓ · 7 | ✓ | 23 | 5.9 | 0 | 652 | 0.23 |
| A9 | candelibas/awesome-ionic | 843 | 2016 | 386 | 0.55 / 6 | ✓ · 38 | ✓ | 28 | 12.4 | 35 | 12 | 0.14 |
| A10 | robinrodricks/awesome-actionscript3 | 188 | 2017 | 388 | 1.00 / 10 | ✓ · 83 | ✓ | 7 | 9.3 | 0 | 1,442 | 0.82 |
| A11 | yrgo/awesome-educational-games | 667 | 2016 | 56 | 0.95 / 10 | ✓ · 9 | ✗ | 11 | 7.3 | 0 | 1,840 | 0.58 |
| A12 | mourarthur/awesome-credit-modeling | 104 | 2020 | 40 | 0.95 / 10 | ✓ · 8 | ✓ | 1 | 11.6 | 0 | 996 | 0.75 |
| A13 | browserify/awesome-browserify | 82 | 2016 | 43 | 0.54 / 2 | ✓ · 14 | ✓ | 3 | 1.6 | 0 | 3,580 | 0.94 |
| A14 | pajaydev/awesome-web-performance-budget | 131 | 2019 | 66 | 0.96 / 10 | ✓ · 12 | ✓ | 4 | 6.3 | 2 | 61 | 0.15 |
| A15 | johnjago/awesome-uncopyright | 379 | 2016 | 97 | 0.95 / 10 | ✓ · 15 | ✓ | 12 | 10.0 | 0 | 1,600 | 0.26 |
| A16 | altamiracorp/awesome-xai | 54 | 2021 | 103 | 0.98 / 10 | ✓ · 11 | ✓ | 2 | 11.3 | 0 | 1,999 | 1.00 |
| A17 | aliesbelik/awesome-jmeter | 806 | 2015 | 233 | 0.77 / 6 | ✓ · 42 | ✓ | 20 | 30.2 | 19 | 17 | 0.05 |
| A18 | bs-community/awesome-minecraft | 559 | 2018 | 136 | 0.99 / 10 | ✓ · 29 | ✓ | 25 | 6.7 | 0 | 427 | 0.14 |
| A19 | dspinellis/awesome-msr | 480 | 2016 | 73 | 0.78 / 9 | ✓ · 6 | ✓ | 28 | 11.9 | 4 | 145 | 0.19 |
| B0 | TheComputerM/awesome-svelte | 2,200 | 2020 | 202 | 0.93 / 9 | ✓ · 44 | ✓ | 125 | 50.4 | 42 | 47 | 0.16 |
| B1 | currenjin/site-for-developers | 1,200 | 2022 | 389 | 1.00 / 10 | ✓ (collapsible) | ✗ | 55 | 63.6 | 68 | 1 | 0.05 |
| B3 | vapor-community/awesome-vapor | 1,300 | 2018 | 72 | 0.08* / 8 | ✓ · 10 | ✓ | 17 | 10.1 | 0 | 1,711 | 0.55 |
| B4 | scadastrangelove/awesome-ai-security-tools | 1,700 | 2026 | 650 | 0.65 / 7 of 7† | ✓ · 29 | ✓ | 102 | 280 in <1 yr | 280 | 2 | 0.37 |
| B5 | humanloop/awesome-chatgpt | 1,500 | 2022 | 54 | 0.06 / 0 | ✗ · 13 | ✗ | 32 | 24.9 | 0 | 374 | 0.85 |
| B6 | ZhiningLiu1998/awesome-imbalanced-learning | 1,500 | 2020 | 134 | 0.07 / 2 | ✓ · 33 | ✗ | 9 | 8.3 | 2 | 137 | 0.15 |
| B7 | OffcierCia/Crypto-OpSec-SelfGuard-RoadMap | 1,900 | 2021 | 486 | 0.02 / 0 | ✗ · 33 | ✗ | 8 | 50.2 | 2 | 69 | 0.01 |
| B8 | feross/awesome-mad-science | 1,200 | 2014 | 56 | 0.98 / 10 | ✗ · 15 | ✗ | 18 | 5.7 | 0 | 3,517 | 0.12 |
| B9 | brabadu/awesome-fonts | 2,100 | 2015 | 161 | 0.73 / 9 | ✓ · 13 | ✓ | 47 | 14.9 | 34 | 4 | 0.07 |
| B11 | pFarb/awesome-crypto-papers | 2,100 | 2017 | 102 | 0.88 / 9 | ✓ · 16 | ✓ | 10 | 7.0 | 0 | 737 | 0.16 |

\* Parser miss, explained in section 1. † Three of the 10 drawn lines were "Related:"/"Sources:" sub-bullets rather than entries; all 7 real entries have rich descriptions plus star, last-update and licence markers.

### 2b. Judgment: audience, timing, rivals, diagnosis

Audience scale used: tiny < small < medium < large < huge. "Rival" means a list in `master_stars.tsv` on the same or a parent topic.

| # | Topic: audience | Launch timing | Bigger rival in master_stars | One-line diagnosis |
|---|---|---|---|---|
| A0 | Framer prototyping tool: small, mostly designers | Early (2015, Framer Classic era). The product then pivoted twice (Framer X in 2018, site builder in 2022) | None; sibling `diessica/awesome-sketch` has 730 | A good list (10/10 described) for a small audience, documenting a product version that no longer exists. Dormant 2019–2025. |
| A1 | Biomedical information extraction: tiny, academic | On time (2019, first such list) | Parents: `keon/awesome-nlp` 19.1k, `Awesome-Bioinformatics` 4.3k | Excellent single-author research list (98% of commits, 22-word annotations), capped by its audience. Opaque acronym in the name. |
| A2 | Gatling load testing: small | First list, but 7 years after the tool (2019) | Overlap: `awesome-http-benchmark` 3.8k, `awesome-testing` 2.4k | Well run (link-check and awesome-lint CI, website, active in 2026). A pure audience ceiling. |
| A3 | Question answering (NLP): medium then, since absorbed by LLMs | Timely (2018 SQuAD/BERT wave) | `keon/awesome-nlp` 19.1k (parent) | A citation dump with 0/10 described. 81% of commits came in 2018 and it froze before LLMs redefined the field. "QA" usually means quality assurance on GitHub. |
| A4 | Diversity in tech: medium, but advocacy reading people rarely star | 2017, after `awesome4girls` (2015) | None bigger (`awesome4girls` 481; `awesome-a11y` 2.0k is adjacent) | Genuinely community-built (37 authors, 52 PR merges), but it serves no recurring developer task. Stopped in 2021. |
| A5 | Ember.js: small and shrinking | Late (2018, past Ember's peak) | None in data. Framework peers: React 75k, Vue 74k, Angular 10.1k | The biggest effort in Sample A (881 entries, 657 commits). Half the entries are undescribed, they are split into 130 tiny sections (median 3 items), and there are only 12 commits after 2020. A lot of effort on a fading framework. |
| A6 | Citizen science: small, mostly not on GitHub | 2016, first list | None | The audience lives on Zooniverse and SciStarter. One author made 91% of commits and 75% of commits came in 2016. The name lacks "awesome". |
| A7 | Construct 2/3 no-code game engine: small, non-programmers | 2016 (Construct 2 era) | `magictools` 17.6k (general game dev) | A competent list for users who rarely use GitHub. Trickle maintenance. |
| A8 | Seed (Rust/Wasm frontend): tiny | 2019, alongside the framework | `awesome-yew` 1.6k (the winning rival framework); `awesome-rust` 60.1k | Only 33 entries. Seed's own README now says "It's not maintained at the moment", so the list died with its subject. |
| A9 | Ionic hybrid apps: medium, then shrinking | 2016, near Ionic's peak | `awesome-angular` 10.1k (parent) | Its audience drifted to Flutter and React Native. No commits in 2018 or 2021–23. Since Aug 2024 it has been run by Martin Donadieu, who adds and merges PRs from the Cap-go org (a Capacitor plugin vendor). 151 of 386 entry lines now point to Cap-go repos, so a vendor has taken the list over. |
| A10 | ActionScript 3 / AIR: dying | Very late (2017, the year Flash's end-of-life was announced) | None | A superb catalogue (388 entries, 99.7% described) built in one burst (82% of commits in 90 days) for a platform with no future users. |
| A11 | Educational games for coders and designers: medium | Early (2016) | `michelpereira/awesome-games-of-coding` 2.2k (2017, later) | Thin (56 entries) and broad. It links a CONTRIBUTING.md that doesn't exist and has had no commits since 2021. A later rival with a sharper name and active maintenance has 3.3× the stars. |
| A12 | Credit-risk modelling: tiny, quant and academic | 2020 | `awesome-quant` 30.3k (parent) | A personal reading list: one author, 40 papers with roughly 50-word abstracts, 96% of commits in 2020. |
| A13 | Browserify: shrinking | Late (2016, as webpack took over) | `awesome-webpack` 4.7k (successor tool) | A skeleton under the official org: 16 commits, 43 entries, 2/10 described, untouched since 2017. |
| A14 | Performance budgets: a slice of web performance | Late (2019, five years after the rival) | `davidsonfellipe/awesome-wpo` 9.1k | A clean list of 66 entries, but on a sub-topic an incumbent already owns. Single maintainer (93% of commits). |
| A15 | Public-domain ("uncopyright") culture: small, ideological | 2016 | `awesome-stock-resources` 14.6k owns the practical "free media" need | Eclectic picks (personal blogs carrying uncopyright notices, vegan recipes) with little reusable value. Coined-word name. Silent since 2022. |
| A16 | Explainable AI: medium | Late (2021, three years after the rival) | `jphall663/awesome-machine-learning-interpretability` 4.1k | A one-shot effort by a company: all 64 commits came in the first 90 days. |
| A17 | Apache JMeter: small to medium | 2015, the first list | None | A best-practice niche list (233 entries, 12 active years, CI, website). 806 stars is roughly the ceiling for a single-tool audience. |
| A18 | Minecraft: huge, but not on GitHub | 2018 | None in data (the real competitors are CurseForge, Modrinth and wikis) | 136 entries for a domain with tens of thousands of mods. Players curate on platform-native indexes. Dormant since mid-2025. |
| A19 | Empirical SE / MSR datasets: tiny, academic | 2016 | None | A useful research tool (28 authors, a 427-word guide) capped by the size of the MSR community. The repo name ("msr") doesn't match the title ("Empirical Software Engineering"). |
| B0 | Svelte: medium | 2020 (after the Svelte 3 boom of 2019) | `awesome-sveltekit` 1.3k (smaller) | Healthy (125 authors, 87 PR merges) but capped by Svelte's market share. Framework lists track framework size: React 75k ≫ Angular 10.1k ≫ Svelte 2.2k > Preact 1.0k > Ember 191. |
| B1 | General developer bookmarks in Korean: limited by language | Late to the genre (2022) | `frontend-dev-bookmarks` 47.7k; Korean `awesome-devblog` 3.6k | Not stuck: still growing (93 commits in 2024 and in 2025). Korean-only and not in the index. |
| B3 | Vapor (server-side Swift): small | On time (2018, Vapor 3) | `awesome-swift` 26.3k (parent) | Small niche, and the list was abandoned in early 2022. |
| B4 | AI security tooling: large and hot | A late entrant (2026) into a crowded space | `awesome-ml-for-cybersecurity` 9.5k (stale since 2024); `h4cker` 29.9k | Not stuck: 1.7k stars in under a year, 102 authors and rich metadata. A fresh list can overtake a stale incumbent. |
| B5 | ChatGPT tools: huge | Very early (first commit 2022-12-04, one day before `f/awesome-chatgpt-prompts`) | `f/awesome-chatgpt-prompts` 172k; `awesome-chatgpt-zh` 11.8k | A company marketing list: 54 bare links, no ToC, 85% of commits in 90 days, abandoned in 2023 in that period's most crowded topic. |
| B6 | Class-imbalance ML: small to medium, academic | 2020 | None | A paper list by an author of the `imbalanced-ensemble` library, which it also promotes. It gives citation counts but describes only 2/10 entries. A niche ceiling. |
| B7 | Crypto/DeFi OpSec: medium, follows the hype cycle | 2021 (bull market) | `personal-security-checklist` 22.6k; `pluja/awesome-privacy` 20.1k | A guide rather than a list: 25 "Problem N" sections, no ToC, bare "Read More" links, many self-links, 97% of commits by one author, peak in 2023. The same author's DeFi roadmap has 10.9k, so the problem is the format and the topic, not the author's reach. |
| B8 | Clever npm packages: a novelty slice of Node | Early (2014) | `awesome-nodejs` 67.2k (parent) | Deliberately tiny (56 entries, 6-word descriptions) novelty list by a famous author. Untouched since 2017. |
| B9 | Fonts: large, but curated outside GitHub | Early (2015) | `chrissimpkins/codeface` 6.5k (programming fonts) | Active, but shallow and mixed in scope (161 entries spanning fonts, emoji, icon fonts and JS libraries). People find fonts on Google Fonts and similar sites. |
| B11 | Cryptography papers: small to medium | 2017, one year after the rival | `sobolevn/awesome-cryptography` 7.2k (2016, 270 entries) | Good curation (9/10 described), but second to a broader incumbent. No commits since late 2024. |

---

## 3. Synthesis: why they stayed small

Each list gets every factor that applies ("any") and one **primary** factor.

Coding rules:
- **(a)** The topic's audience on GitHub is small. This includes audiences who do their curating elsewhere (Minecraft, Construct, fonts) or are limited by language.
- **(b)** A direct rival in `master_stars` has at least 3× the stars and covers essentially the same scope. Parent lists alone don't count.
- **(c)** Launched after the topic's peak, or at least 2 years after an incumbent list.
- **(d)** Fewer than 60 entries, or at most 5 of 10 entries described.
- **(e)** No commit in the last 365 days.
- **(f)** Ambiguous or opaque name, a non-"awesome" name with no index listing, or a non-English-only audience.
- **(g)** Topic decline after launch. This is not in the brief's taxonomy, but it kept coming up.

| Factor | Sample A (n=20) any | Sample B (n=10) any | All 30, any | All 30, primary |
|---|---|---|---|---|
| (a) Small or off-GitHub audience | 14 (70%) | 5 (50%) | **19 (63%)** | **17 (57%)** |
| (b) Dominant rival owns the topic | 3 (15%) | 2 (20%) | 5 (17%) | 5 (17%) |
| (c) Late arrival | 5 (25%) | 1 (10%) | 6 (20%) | 3 (10%) |
| (d) Low effort or quality | 5 (25%) | 4 (40%) | 9 (30%) | 2 (7%) |
| (e) Abandoned (0 commits in last 365d) | 12 (60%) | 4 (40%) | **16 (53%)** | 1 (3%) |
| (f) Poor discoverability | 5 (25%) | 2 (20%) | 7 (23%) | 0 |
| (g) Topic declined after launch | 7 (35%) | 1 (10%) | 8 (27%) | 1 (3%) |
| None (still growing) | 0 | 1 (B4) | — | 1 (3%) |

Primary factor counts, Sample A: a = 12, b = 3, c = 3, e = 1, g = 1. Sample B: a = 5, b = 2, d = 2, still growing = 1.

What each factor looks like in practice:

- **(a) dominates, and it is a ceiling, not a failure.** `awesome-jmeter` and `awesome-gatling` share maintainer, template, CI and website; their stars differ 10× (806 vs 80), in line with the tools' user bases. Academic lists (`bioie`, `msr`, `credit-modeling`, `imbalanced-learning`) plateau at 100–1,500 stars whatever their quality. A distinct subtype is the audience that curates elsewhere: Minecraft (CurseForge, Modrinth), Construct (non-programmers), citizen science (Zooniverse), fonts (Google Fonts).
- **(e) is nearly universal but mostly a symptom.** 16/30 were silent last year; 9/20 in Sample A for over 2 years. Only `awesome-qa` reads as "would have grown if maintained": it froze just before its field exploded. One-shot launches are 33% of the sample and 0/4 of the top lists. Median top-author share is 0.71, against 0.13 for the top four.
- **(g) is underrated.** Eight lists bet on a technology that faded or was absorbed. It often coincides with (c): ActionScript 3 (2017), Browserify (2016) and Ember (2018) were late to already-declining tools. Effort doesn't rescue them: the AS3 (388 entries, 99.7% described) and Ember (881 entries) lists are among Sample A's best-resourced.
- **(b) is real but conditional.** Clear cases: performance budgets vs `awesome-wpo`, XAI vs ML-interpretability, crypto papers vs `awesome-cryptography`, ChatGPT tools vs `awesome-chatgpt-prompts`. The rival was earlier in three of the four. The exception: Humanloop's list (2022-12-04) beat `f/awesome-chatgpt-prompts` by one day, but a 54-link list that stopped in 2023 gained nothing from it. Incumbency also fails once maintenance stops: `awesome-games-of-coding` (2017) overtook `awesome-educational-games` (2016), and `awesome-ai-security-tools` (2026) is passing `awesome-ml-for-cybersecurity` (2016, stale).
- **(d) explains little in the index cohort.** The index's quality gate works: only 5/20 Sample A lists are thin by our rule, against 4/10 in Sample B. B lists reach 1–2k stars on audience alone despite bare links (`awesome-chatgpt`, the OpSec roadmap) or no ToC.
- **(f) is minor.** All of Sample A is indexed and still small; half of Sample B is unindexed and reached 1–3k. Ambiguous names ("qa", "msr", "bioie", "uncopyright") can't be shown to cap stars on their own.
- **Other patterns:** vendor capture (about 39% of `awesome-ionic` entry lines link to the maintaining vendor's repos); author self-promotion (OpSec roadmap, imbalanced-learning); company lists abandoned after a launch spike (Humanloop, Altamira).

---

## 4. Control group vs the top lists

Medians. The "In-index <1k" and "In-index >30k" columns are corpus-wide and come from `features.jsonl` joined with `master_stars.tsv`.

| Feature | Sample A (in-index, <1k) | Sample B (1–3k) | All 30 | In-index <1k (n=233) | In-index >30k (n=33) | Top 4 (python, go, selfhosted, free-for-dev) |
|---|---|---|---|---|---|---|
| Stars | 344 | 1,600 | 597 | 333 | — | 100k+ |
| First year | 2017 | 2020 | 2018 | 2017 | 2014 | 2014.5 |
| Entries (README) | 111 | 148 | 126 | 78 | 552 | 1,335 (552–3,170) |
| desc_ratio | 0.94 | 0.69 | 0.90 | 0.91 | 0.95 | 0.97 |
| Manual described (of 10) | 9.5 | 9 | 9 | — | — | — |
| Has ToC | 100% | 70% | 90% | 88% | 91% | 100% |
| Has CONTRIBUTING | 95% | 50% | 80% | 91% | 88% | 75% |
| CONTRIBUTING words | 192 | 49 | 182 | — | — | 855 |
| Link-check CI | 20% | 30% | 23% | 24% | 42% | 0% (per extractor) |
| Human authors | 11 | 25 | 12 | 11 | 499 | 1,852 |
| Top author's share of commits | 0.81 | 0.58 | 0.71 | — | — | 0.13 |
| Total commits | 94 | 137 | 98 | 81 | 1,905 | 6,409 |
| Commits per year of life | 11.5 | 19.9 | 11.7 | — | — | 544 |
| Commits in last 365 days | 0 | 2 | 0 | 0 | 77 | 703 |
| Active in last year | 40% | 60% | 47% | 40% | 88% | 100% |
| Days since last commit | 573 | 103 | 401 | 917 | 27 | 1.8 |
| PR merge commits | 6 | 12 | 6.5 | — | — | 1,152 |
| One-shot (≥50% of commits in first 90 days) | 40% | 20% | 33% | — | — | 0% |
| Sections with items / items per section | 16.5 / 3 | 15.5 / 4.5 | 15.5 / 4 | — | — | 82 / 14 |

Spearman correlations with stars across all 585 in-index lists:

| Feature | ρ |
|---|---|
| desc_ratio | **0.01** |
| CONTRIBUTING length | 0.14 |
| Entries | 0.41 |
| Commits in last 365 days | 0.40 |
| First year | **−0.38** |
| Top author share | −0.48 |
| Commits | 0.68 |
| Authors | 0.77 |

Authors and commits are partly a *consequence* of stars, so read those two as "communities form around popular lists", not as levers.

How this compares with the brief's profile of a top list (thousands of entries, ~95%+ described, ToC, contributing guide, active maintenance):

- **The "hygiene" half is table stakes, not a differentiator.** Index lists under 1k stars already have about 91–94% of entries described, a ToC (88–100%) and a CONTRIBUTING file (91–95%).
- **The differentiating half is scale and continuity.** Top lists have 10–20× more entries, 100–200× more authors, about 50× the lifetime commit rate, and a spread maintenance load (top author share 0.13 vs 0.71). Their guides are about 4× longer (855 vs 192 words): governance documents, not templates.
- **Section granularity differs.** Low-star lists fragment early: median 3–4 items per section, and Ember has 130 sections. Top lists have 14 items per section across 82 sections. Thin lists fake depth with headings.
- **Timing is a structural advantage.** Top lists date from 2014–2015, the start of the awesome-list wave. The median control list arrived in 2017 (A) or 2020 (B), when generic topics already had incumbents. The control lists that *were* early (mad-science 2014, Framer 2015, fonts 2015, educational games 2016) were early on small or novelty topics.

---

## 5. Implications for the "what makes top lists good" study

1. **Control for audience size before crediting design.** Any comparison of a top list's design with an average list is confounded by topic demand. A fair contrast pairs lists within the same audience tier. Examples: JMeter vs Gatling, Svelte vs Vue, `awesome-cryptography` vs `awesome-crypto-papers`.
2. **The levers that seem to matter, in rough order:**
   1. Pick a topic with a large, GitHub-native audience, or the broadest framing of one.
   2. Arrive before an incumbent, or outlast it.
   3. Turn a one-author launch into a multi-maintainer process. Every top list did this; 33% of the control group never got past the launch burst.
   4. Keep pace with the topic, pruning dead tech and adding successors, rather than freezing at launch.
3. **Descriptions, ToC and CONTRIBUTING are necessary but not sufficient.** They are what the index already enforces, and they show no correlation with stars inside the index.
4. **Watch for failure modes that look like success:**
   - Vendor-maintained revivals (Ionic/Capgo).
   - Author self-promotion (OpSec roadmap, imbalanced-learning).
   - Corporate one-shots (Humanloop, Altamira).
   They look active or well-resourced without building a neutral community.

## 6. Caveats

- **Factor coding is my judgment**, made against the explicit rules in section 3. Primary-cause attribution is single-coded and could reasonably shift by ±2–3 lists per factor.
- **Audience sizes are qualitative.** No download or user counts were collected.
- **Different star sources.** Sample A stars are a track-awesome-list snapshot; Sample B stars are rounded topic-page counts. Neither affects the band membership of any sampled list.
- **The B band mixes "stuck" and "young" lists.** B1 (2022, growing) and B4 (2026) are "not yet big" rather than "stayed small". B4 is coded as having no limiting factor.
- **Survivorship.** `master_stars.tsv` only contains lists that surfaced via topic pages, track-awesome-list or the index, so truly obscure lists (<50 stars, unindexed) are under-represented. The real control population is probably even more niche-heavy and more abandoned than shown here.
- **CI flags are lower bounds.** The extractor's link-check flag is keyword-based and reads 0% for the top four, yet awesome-go runs custom checks (`run-check.yaml`, `pr-quality-check.yaml`), and awesome-selfhosted keeps its data, checks and contributing guide in a separate repository.
