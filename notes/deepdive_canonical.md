# Deep dive: the canonical index + classic topic lists

Analyst notes for the archetype "canonical index + classic topic lists". Sources: local clones under `clones/<owner>__<repo>` (HEAD as of Oct 2026, full git history), plus GitHub pages read through WebFetch for live counts (stars, open PRs) and the current PR-restriction state. Entry counts come from lines matching `^\s*[-*] \[` (tables counted by row). They are approximate and include ToC lines unless noted.

| List | First commit | Commits | Distinct authors | Entries: peak, then now | Effective mergers | Status (Oct 2026) |
|---|---|---|---|---|---|---|
| sindresorhus/awesome | 2014-07-11 | 1,209 | 681 | 728 (Jan 2026), now 703 | 1 (Sindre Sorhus) | PR and issue creation limited to collaborators |
| josephmisiti/awesome-machine-learning | 2014-07-15 | 2,169 | 763 | 1,387 (still rising) | 1 (Joseph Misiti) | Active. "Email me to prove you're human" |
| enaqx/awesome-react | 2014-08-06 | 2,055 | 667 | 1,063 (Apr 2019), now 177 | 2 (Nick Raienko, Haroen Viaene) | Active, small |
| vuejs/awesome-vue | 2015-10-19 | 5,372 | 2,473 | 3,169 (Nov 2024), now 1,209 | 1 at a time; 5 maintainer eras | Active |
| Hack-with-Github/Awesome-Hacking | 2016-03-30 | 141 | small | 84 (Apr 2026), now 81 | 1 (Chandrapal Badshah) | Active again since Apr 2026 |
| goabstract/Awesome-Design-Tools | 2019-02-12 | 1,649 | n/a | ~1,990 across 4 files | company team | Frozen since 2020-09-28 |

---

## 1. sindresorhus/awesome (~524k stars), the index of lists

**Value proposition and scope.** In 2014 the whole README was `# Awesome` / `> A curated list of awesome lists`, with 59 bare links in 7 sections. It answers one question: "which list is *the* list for topic X?" The unit is a list, never a tool. Each topic gets one slot (create-list.md: "Search this list before making a new one… If it is, try and contribute to the best one instead of making your own."). Scope is everything, including non-tech topics. Issue #732, opened by Sindre in 2016, is titled "More non-{tech,science} awesome lists please!"; Health and Social Science, Veganism and Transgender lists are included. Blockchain lists have been banned since the June 2023 guideline update.

**README as a product.** The page is built like a landing page more than a document:
- A centered SVG logo, a sponsor block, and a navigation row: What is an awesome list? / Contribution guide / Creating a list / Twitter / Subscribe (RSS). The RSS link was added Jun 2026 (#4279).
- A vanity short URL, "Just type `awesome.re` to go here" (added Jun 2016).
- A `## Contents` of 27 H2 categories, the entries, and then a `## Related` section that points outward to search and discovery tools (awesomelists.top, trackawesomelist.com, StumbleUponAwesome, Awesome CLI). The index thus hands off "search" to third parties instead of building it.
- The badge assets in `media/` (badge.svg, mentioned-badge) turn every compliant list into a backlink to the index. The PR template says the badge "Should link back to this list."

**Curation policy.** The rules live in the PR template (9 KB, ~45 checkboxes, ending "**Go to the top and read it again.**") and in awesome.md and awesome-lint, which another analyst covers. Index-specific mechanics:
- Description rule: an entry describes the *topic*, not the list ("❌ Resources and tools for iOS development"), in title case, and URLs end in `#readme`. The `#readme` suffix was applied to all links in Jul 2018 (#1343).
- New lists must be at least 30 days old (since Nov 2016) and must not be AI-generated (since 9 Mar 2026).
- Pruning is real but episodic. 43 commit subjects mention removal. Reasons are stated bluntly in commit bodies:
  - TypeScript (2017): "The author is not willing to participate… This will let someone create a better TypeScript list."
  - webpack (2021): "It's no longer an Awesome list."
  - macOS (2022): "It's badly maintained."
  - Zig (Nov 2025).
- Bulk archived-list sweeps came from community PRs: #4278 (Jun 2026) removed 17 lists and #4390 (Aug 2026) removed 8, including big names such as Unity, Qt, Xamarin, Google Cloud, C and Amazon Alexa.
- When a parent list dies, its children keep their place under a plain-text heading (`- Linux`, `- macOS`). Sub-lists survive the parent.
- Entry count rose every year, 59 → 266 (2016) → 551 (2020) → 728 (Jan 2026). It then fell to 703, the first net decline in 12 years.

**Entry format.** `- [Topic](https://github.com/owner/awesome-x#readme) - Objective description of the topic.` There are 80 tab-nested sub-entries; one nesting level is allowed. New entries go "at the bottom of the appropriate category", so order within a category is chronological, a record of seniority. Legacy debt: about 212 of ~671 list entries (32%) still have no description. Examples are Machine Learning, Hacking, and most of Programming Languages (37 of 77). Miscellaneous is the largest category with 132 entries, about 20% of the index.

**Contribution workflow and governance.**
- **PR flow:** 2014–2016 used merge commits (155, of which 143 are Sindre's). From 2017 PRs are squash-merged through the GitHub UI (545 squash commits). From 2020 every landed PR has committer "GitHub". There is no evidence of a second merger after 2017; Craig Davison landed 29 commits in 2016–17.
- **Merge rate:** about 700 merged PRs against about 2,490 opened (89 open and 2,398 closed on GitHub), roughly 28%.
- **Cadence is batchy:**
  - 10 lists were added on 2025-05-15 and 9 on 2025-10-27/28.
  - The repo had 160 active commit days in 2015 and 19 in 2025.
  - Latency can be years: #2607, opened around mid-2023, was merged in Nov 2025.
- **New lists added per year:** 93 (2019), 51, 36, 35, 28, 22, 27 (2025), and **0 in 2026**. The only 2026 "Add" commit is "Add RSS link".
- **Self-sustaining review tax:** since Jul 2018 a submitter must review other open PRs. The requirement was 2 PRs, raised to **4** on 4 Mar 2026. It is meant to "help make the Awesome project self-sustaining". Draft lists go to pinned issue #2242, "Incubate" (303 comments).
- **CI:** `repo_linter.sh` takes the newly added `…#readme` URL from the PR diff, clones that repo and runs `npx awesome-lint`. The CI lints the submitted list, not the index itself (issue #1619 "Lint Awesome itself" has been open since 2019).
- **Monetization and neutrality:** sponsor logos sit only in the header block and are rotated through 45 "Meta tweaks" commits since 2020. Examples: Circleback was added Apr 2026 and removed Sep 2026; Nitric and Wispr Flow were removed May 2026. The header also promotes the owner's macOS app ("Supercharge"). Sponsors never appear inside the list body. The sponsor history goes CodeSponsor (2017) → Patreon (2018) → GitHub Sponsors (2019) → direct logos.

**Current "PRs disabled" state.**
- The live repo shows "Only collaborators can create PRs" and "Only collaborators can create issues".
- The last PR (#4396, "Add AI Agent Tools") was opened 22 Aug 2026, and the last commit was 2 Sep 2026 (a sponsor removal). The restriction was therefore switched on between 22 Aug and 30 Sep 2026; on 30 Sep the first Incubate comment says the author "couldn't open a PR".
- **No explanation exists anywhere in the repo.** contributing.md still says "Please ensure your pull request adheres…". The pinned Incubate issue is now the only intake channel, and its latest comments mix real list announcements (awesome-mbse, awesome-python-math-packages, awesome-maki) with spam ("@copilot", a bag-manufacturer ad).
- The context points to an AI-generated submission flood on a one-person review queue:
  - Issue and PR numbers advanced about 430 in all of 2025 but about 740 in Jan–Aug 2026.
  - The "not AI-generated" rules arrived in Mar 2026, and the review tax doubled the same week.
  - Issue #4094 (Apr 2026) contests a rejection labelled "AI generated lists are not accepted". A third party wrote there that maintainers "have to wade through dozens of AI slop PRs in their free time."
  - This motive is my inference; it is not stated by the maintainer.

**Maintenance over time.** Commits per year: 91, 310 (2015 peak), 195, 124, 52, 113, 72, 60, 56, 45, 35, 36, and 20 in 2026. Authors per year: 142 in 2015, 30 in 2025, 13 in 2026.

**Secret sauce.**
1. One slot per topic plus a strict description grammar. The index is a namespace registry, so being listed means being canonical.
2. The badge and backlink network, with a manifesto that downstream lists must obey. The index exports its standards to roughly 700 lists.
3. The contribution tax (review 4 PRs, the `unicorn` comment to prove the rules were read) shifts review labor to submitters.
4. Pruning is explicit and justified in commit bodies, and done in bulk when it matters (25 archived lists in 2026).
5. Product polish: a short URL, RSS, logo assets, and pointers out to search tools.

**Weaknesses.**
- A single gatekeeper with multi-year latency, and now a closed front door with no written notice.
- 32% of entries have no description, and Miscellaneous is a catch-all.
- Grandfathering: classic members break today's rules. awesome-machine-learning uses "Table of Contents" and has no contributing.md and a placeholder license; awesome-vue is MIT, which the template calls "not acceptable"; awesome-react has no license file.
- Huge lists such as Awesome-Hacking (123k stars) and Awesome-Design-Tools (42k) are not in the index at all.

**Quotes.**
- "Awesome lists are curations of the best, not everything."
- "**Don't waste my time.** Do a good job, adhere to all the guidelines, and be responsive."
- "Please read it multiple times. I spent a lot of time on these guidelines and most people miss a lot."

---

## 2. Hack-with-Github/Awesome-Hacking (~124k stars), a security list of lists

**Value proposition and scope.** "**A collection of awesome lists for hackers, pentesters & security researchers.**" The audience is offensive-security practitioners and learners. Its scope is wider than "awesome lists": the second table, "Other Useful Repositories" (34 rows), holds practitioner corpora that could never pass the index's rules, such as SecLists, PayloadsAllTheThings, Vulhub, GTFOBins, OWASP CheatSheetSeries, trickest/cve, CyberChef, and even Free Programming Books.

**Curation policy.**
- contributing.md is 898 bytes. Its only rules are "make sure that the edited list is in alphabetical order" and, for removals, "If you have any issues accessing any of the resources listed here, please let us know."
- There is no quality bar. The real curation happened in one maintainer sweep (PR #206, 18–20 Apr 2026, "cleanup/2026-refresh"):
  - Removed 4 archived or deprecated lists (e.g. sundowndev/hacker-roadmap).
  - Removed 10 stale lists, with the last-commit year in the commit message ("FuzzySecurity/Resource-List (2016)", "0x90/wifi-arsenal (2020)").
  - Replaced 5 with active alternatives ("meitar/awesome-lockpicking → DavidProbinsky/RedTeam-Physical-Tools", "andrewjkerr/security-cheatsheets → OWASP/CheatSheetSeries").
  - Added about 10 lists and updated redirected URLs.
- Before that, almost nothing happened: 1 commit in 2023 and 3 in 2025.

**Entry format.** Two Markdown tables (`Repository | Description`), alphabetical, with no categories inside them. Descriptions are inconsistent, and 50 of 81 (62%) describe the list ("List of…", "Collection of…"), which the index forbids. History of the format:
- **Apr 2016:** each list had its own `####` heading, a backticked description, a ToC and the Awesome badge.
- **27 Oct 2016:** "Removed badge".
- **22–23 Nov 2016:** "Put everything in a table".

**Navigation.** No ToC is needed because the README is 12 KB and 81 rows long; it is the most scannable page in this set. It has a banner image (PNG → WebP in Jul 2026, redesigned May 2026 via community PR #211) and a Tweet share button.

**Contribution workflow and governance.**
- 141 commits in 10 years. Chandrapal Badshah lands essentially all merges (27 merge commits plus direct commits).
- No CI for content. The only workflow, `lock-threads.yml` (added Aug 2024), runs hourly and locks issues and PRs inactive for 7 days. That is anti-noise, not quality control.
- GitHub shows no open-issue count (the tab appears disabled) and 24 open PRs.
- Brand funnel: "## Need More ? Follow **Hack with GitHub** on your favorite social media to get daily updates…" (Twitter/Facebook). The list is the anchor asset of a social-media brand, which explains 124k stars on 141 commits.

**Maintenance over time.** Commits per year: 51 (2016), 37, 4, 15, 5, 2, 3, 1, 5, 3, and 15 (2026). Entry count: 22 (May 2016) → 68 (2018) → 78 (2023) → 81 now. The list was essentially dormant for 2018–2025.

**Lists of lists: what it adds beyond aggregation.**
- 25 of its 80 repo URLs also appear in sindresorhus/awesome.
- All of the April 2026 additions (CI/CD Attacks, Detection Engineering, Malware Persistence, Password Cracking, Prompt Injection, Executable Packing, Suricata, Annual Security Reports, Tor) already sit in the index's Security section. The refresh largely mirrored the canonical index.
- Its distinct value is the other 55: a domain lens that admits non-list "arsenal" repos (payloads, wordlists, vulnerable labs) and a single 30-second scannable table.

**Secret sauce.**
1. Extreme brevity: one table, alphabetical, scannable on one screen.
2. A "collect the collections" positioning in a field where practitioners already know the tool repos.
3. A strong external brand and social distribution.
4. A permissive scope that mixes awesome lists and arsenal repos.

**Weaknesses.**
- Long dormancy and no stated quality bar.
- Descriptions that describe lists, and a fuzzy line between the two tables ("AI Security" and "Annual Security Reports" are awesome lists but sit in "Other Useful Repositories").
- Thread-locking hides problems instead of fixing them.

**Quotes.**
- "A collection of awesome lists for hackers, pentesters & security researchers."
- "Your contributions are always welcome !"

---

## 3. enaqx/awesome-react (~75k stars)

**Value proposition and scope.**
- 2014 tagline: "A collection of awesome React tools, resources, videos and shiny things."
- Now: "A collection of awesome things regarding the React ecosystem."
- The closing note frames the current philosophy: "When it was initiated, React was still in beta… Today, React has become boring mainstream." It covers React plus a small React Native section.

**Curation policy.** The rules live in a single README paragraph: "Kindly refrain from using this list as an advertisement board… We focus on sharing entirely free resources here… I would prefer GitHub links." 137 of 177 links go to GitHub. Its defining trait is **two owner-led great purges**:
- **May–Jul 2019:** about 50 commits by Nick Raienko took the list from 1,063 to 614 entries (−42%). Typical subjects: "Remove non-free books…", "Remove non-free video courses", "Remove SSR section as mostly outdated", "Remove Flow section", "Merge Boilerplates with React Development Tools".
- **18–22 Apr 2023:** 519 → 181 entries (−65%). Typical subjects: "Remove Redux section", "Remove GraphQL and Relay since they are the things on their own nowadays", "Remove Demo React Apps section. These examples outdated", "Flatten list".
- **Sep 2025:** a mini-prune removed create-react-app, wouter, million and react-styleguidist.

The README went from 113 KB (2019) to 18.8 KB today. This is the clearest case in the set of an owner deliberately trading size for currency.

**Entry format.** `- [repo-slug](github-url) - Short description` with no trailing period. Names follow the GitHub repo slug in lowercase (`next`, `shadcn-ui`, `react-bits`). Order is by importance, not alphabet; shadcn-ui, ant-design and material-ui lead Component Libraries. There are about 148 real entries in 26 `####` subsections averaging 5–6 picks each, so a "short-list of defaults" design.

**Navigation.** A two-level ToC (React / React Native) with no badges beyond Awesome and no images. Earlier versions had 109 headings (2018); today there are 30.

**Contribution workflow and governance.**
- No CONTRIBUTING, PR template, CI or license file. The footer badge's alt text says "CC0" but links to CC BY 4.0.
- Merges are rebased so authorship is kept and the committer is the merger. Merge commits: Nick Raienko 313, Jason Brown 136, Haroen Viaene 91.
- Maintainer relay: Nick (2014–15), Jason Brown (2016: 148 commits landed), Paul Melnikow (2017), Haroen Viaene (2018–2022: 135 landed in 2018), Nick again (2023+).
- A sponsor banner (Fern) was added Sep 2024 and removed Dec 2024 ("Remove sponsor link").
- 29 open PRs and 1 open issue.

**Maintenance over time.** Commits per year: 386, 595 (2015), 324, 209, 148, 138, 67, 61, **10 (2022)**, 43 (2023 purge), 20, 34, and 20. Contributors still land additions monthly in 2026 (e.g. Formisch, Markstream, xprem).

**Secret sauce.**
1. Ruthless, owner-executed pruning: two purges that removed over 80% of the peak.
2. A free-only rule.
3. A "pick the defaults" ordering by importance.
4. A short single page that is now easier to read than most competitors.

**Weaknesses.**
- No written process or automation, so it depends on one person's taste and time. 2022 had only 10 commits.
- Inconsistent descriptions, and a license ambiguity.
- The purges removed history that some readers valued; there is no archive file.

**Quotes.**
- "This list began as a personal compilation of interesting things related to React."
- "Kindly refrain from using this list as an advertisement board or a space to promote your experiments."
- "We focus on sharing entirely free resources here."

---

## 4. vuejs/awesome-vue (~74k stars), backed by the official org

**Value proposition and scope.** "> A curated list of awesome things related to Vue.js". It was created by Vue's author Evan You on 19 Oct 2015. It is the Vue ecosystem directory: official resources, community, *who uses Vue* (Companies, Projects: Open Source, Commercial Products, Apps/Websites, Interactive Experiences, Enterprise Usage, A11y), and a deep Components & Libraries taxonomy. The skeleton of the first README (logo, Official Resources first, External Resources, Community, Projects Using Vue.js with the same subsections) has survived 11 years almost unchanged.

**Curation policy.** contributing.md is the most specific of the classic lists:
- "Always add your items to the end of a list. To be fair, the order is first-come-first-serve."
- "Just useful is not enough, especially if its for niche use cases" (added Feb 2026).
- A **"Truly awesome projects"** tier ("exceptionally high quality, have a proven trackrecord, and are virtually indispensable"). It currently holds Vue DevTools, unplugin-icons and vue-i18n, and overlapping libraries face "an even higher" bar.
- Open-source entries need a README with demo or screenshots plus a CONTRIBUTING section, English docs, active maintenance, acceptance of contributions, and no commercial nature.
- Apps must be detectable with vue-devtools; a screenshot is accepted for non-public pages.
- Commercial products must be checkable, otherwise "the entry will be seen as an advertisement… If you're interested in advertisement open an issue first."
- AI rule (30 Apr 2026): AI-built projects need "at least 3 updates published with a minimum of a month between first and last release."

**Pruning.**
- **Nov 2024:** community member Coops0 submitted seven prune commits ("remove unmaintained/abandoned open source", "remove non existent professional products", "remove many old components", "remove all empty categories"), merged by Jogai in Dec 2024. Entries fell from 3,169 to 1,215 (−62%) and the README from 412 KB to 155 KB.
- **18 Feb 2026:** a maintenance sweep whose commits are **authored by "Claude"** (an AI agent):
  - removed defunct platforms and dead URLs, plus goo.gl/bit.ly links;
  - upgraded http links to https;
  - pinned GitHub Actions to commit SHAs;
  - fixed ToC anchors.

  The next days followed with "Remove archived and inactive entries" and "Remove Vue 2 only entries from Components & Libraries".

**Entry format.** `- [name](url) - description`, with inconsistent punctuation and length. Some entries run past 300 characters (vuetify-drilldown-table); the JARVIS entry is a tech-stack advert. There are 134 headings nested up to 5 levels (`##### Progress Bar`), plus italic sub-labels (`_Tables / data grids_`).

**Navigation.** A centered Vue logo, the Awesome and Track Awesome List badges, and a doctoc-style ToC regenerated by CI (`toc.yml`, technote-space/toc-generator on push).

**Contribution workflow and governance.**
- PR template with Fix/Feature type and per-category checklists.
- CI `readme-lint-double-link.yml` blocks duplicate links on PRs.
- 2,473 distinct authors, the broadest contributor base in the set.
- Maintainer eras, all with commit rights from the org:
  - Evan You (Oct 2015–May 2016);
  - kazuya kawaguchi / kazupon, core team (2016–2019: 382, 886 and 716 commits landed in 2016–18);
  - Thorsten Lünborg, core team (2016–2020);
  - Ivan Demidov (2017–Jan 2023, 870 merge commits);
  - **Jogai** (2023–now, sole committer: 86, 96, 60 and 115 commits landed per year).
- FUNDING.yml points donations to Evan You, posva, the vuejs Open Collective and Tidelift, i.e. to the framework rather than the list's curators.
- 64 open PRs and 40 open issues.

**Official vs individual trust signals.** The vuejs namespace, official logo and "Official Resources" block make it the default answer. Owner churn never forked or broke the list because the org kept the keys, and rights moved from core team to community volunteers. Org backing does not guarantee review quality, though:
- **The first line of README.md at HEAD reads `Resource from plugin:github:github at repo://vuejs/awesome-vue/sha/14fa265…/contents/README.md] <p align="center">`.**
- It is a tool-output artifact injected by a 4 Mar 2026 PR, "Add JARVIS - Self-hosted AI assistant platform". The sha it names is Jogai's 20 Feb ToC commit, which suggests an agent read the file through a GitHub MCP plugin and wrote it back with the header.
- It survived about 7 months and dozens of later merges. It shows that a busy single reviewer sees the added line, not the whole diff.

**Maintenance over time.** Commits per year: 83, 763, 949, 734, 456, **1,204 (2020)**, 508, 283, 110, 96, 69, and 117 (2026). Entries: 154 (Jan 2016) → 1,070 (2017) → 2,326 (2019) → 3,169 (2024) → 1,209 now.

**Secret sauce.**
1. Official namespace and day-one founder authorship.
2. Showcase sections ("Projects/Companies Using Vue") that double as adoption marketing for the framework.
3. First-come-first-serve ordering, stated as fairness.
4. A "Truly awesome" tier that creates a canon above the long tail.
5. Written, testable inclusion criteria (the vue-devtools detection test).

**Weaknesses.**
- Bloat until 2024 (3k+ entries, 400 KB), with deep nesting.
- The artifact line in the header, and description inconsistency.
- An MIT license on a content list.
- Bus factor of 1 since 2023.

**Quotes.**
- "Always add your items to the end of a list. To be fair, the order is first-come-first-serve."
- "Just useful is not enough, especially if its for niche use cases."
- "These projects are exceptionally high quality, have a proven trackrecord, and are virtually indispensable."

---

## 5. josephmisiti/awesome-machine-learning (~75k stars)

**Value proposition and scope.** "A curated list of awesome machine learning frameworks, libraries and software (by language). Inspired by `awesome-php`." It is the only list here whose primary axis is **programming language**: 37 language H2s from APL to TensorFlow, then tasks (`#### Computer Vision`, NLP, General-Purpose ML, Data Analysis / Data Visualization). Books, courses, blogs, events, meetups and an ML curriculum are moved to six companion .md files.

**Early-mover seeding.** It was created four days after the index. The third commit on day one (15:18, 15 Jul 2014) is literally "cut and pasted". The list had 160 entries by the end of day one and 409 by day three. The `## Credits` section still admits "Some of the python libraries were cut-and-pasted from [vinta](…awesome-python)".

**Curation policy.**
- No inclusion criteria at all.
- The only policy is deprecation: "a listed repository should be deprecated if… owner explicitly says… not maintained [or] Not committed for a long time (2~3 years)."
- Deprecated items are **flagged in place** with `**[Deprecated]**`, not removed. A single contributor pass on 22 Jan 2019 ("Fix links, find all deprecated projects") tagged 162 entries. The count has been 165 since 2020, so there has been no sweep in six years, and about 12% of entries carry the tag.
- The list has **never shrunk**: 507 (Aug 2014) → 797 (2017) → 1,036 (2020) → 1,313 (Jan 2026) → 1,387 (Oct 2026), now 222 KB.

**Entry format.** `* [Name](url) - description`, with a median line of 140 characters. Order within sections is insertion order (0 of 19 sections with 5+ entries is alphabetical). The ToC is a manual MarkdownTOC at depth 4. A star-history chart and a Track Awesome List badge sit at the top.

**Contribution workflow and governance.**
- Joseph Misiti authored about 965 of about 980 merge commits: a pure single-merger model for 12 years.
- No CONTRIBUTING, PR template or CI. LICENSE is 38 bytes: "Creative Commons Legal Code / No need".
- On 21 Apr 2026 (#1298) the contribution line was replaced by "**IMPORTANT NOTE ON PRs:** As of April 2026, too many PRs are being generated by LLMs, this is no longer fun or manageable. If you want to contribute… email me… to prove you're human".
- Inflow evidence: issue and PR numbers advanced about 54 in all of 2025 (1016 → 1070) versus about 376 in 2026 so far (→ #1446), roughly 7x.
- The email gate did not reduce merges: 34 PRs were merged in 2026 before the note and 34 after. Recent ones look like low-bar self-promotion ("Add qwen3.8-27b-in-c", "Add HypercubeESN, HypercubeWTF, HypercubeCascade, and HypercubeHopfield links").

**Maintenance over time.** Commits per year: 284, 226, 237, 242, 192, 161, 189, 156, 130, 88, 76, 95, and 93. This is the steadiest cadence in the set, all of it accretion.

**Secret sauce.**
1. Being first: day-one seeding, and the index slot "Machine Learning" (still without a description) since 2014.
2. The language-first taxonomy fits how engineers search ("ML in Go?").
3. Low friction: almost everything gets merged.
4. Companion files keep the main README about software.

**Weaknesses.**
- No pruning, so 12% of entries are visibly deprecated and the rest are unaudited.
- Accretive bloat, with ML-in-2026 (LLMs, agents) buried under language headers.
- Single merger, now behind an email gate.
- Placeholder license and an outdated "awesome-php" framing.

**Quotes.**
- "Inspired by `awesome-php`."
- "too many PRs are being generated by LLMs, this is no longer fun or manageable."

---

## 6. goabstract/Awesome-Design-Tools (~42k stars), the visually designed list

**Value proposition and scope.** "The best design tools and plugins for everything 👉" (About). It is a directory for designers: 637 tools in 36 categories in the README, plus Awesome-Design-Plugins.md (1,112 entries: Sketch, Figma, XD and InVision Studio plugins), UI Kits (224) and Conferences (14), about 1,990 items in total. Each category opens with a prose intro written partly for search ("Here you will find web accessibility tools, accessibility testing tools, and accessibility apps…").

**Visual design.**
- Cover image, Awesome and PRs-Welcome badges.
- **445 inline SVG label icons** in the README (free 308, open-source 72, Mac-only 62), 1,083 platform icons in the Plugins file and 442 in UI Kits.
- Yellow `banner` divs that cross-reference other categories ("Drama, Principle, Framer, Invision Studio, Flinto are also among UI & UX animation apps").
- The README is wrapped in `<article>`, `<main>` and `<div class="hidden-in-page">` markup because it was the source for a generated website. `index.js` uses markdown-it and jsdom, adds a hamburger menu and `addAllPromoBanners`, and builds flawlessapp.io/designtools.
- **That domain no longer resolves (DNS ENOTFOUND).** The web scaffolding now shows up on GitHub as clutter, and 397 links still point at the old `LisaDziuba/Awesome-Design-Tools` path.

**Curation policy.** Contribution_Guidelines.md (4.8 KB):
- Alphabetical order, "All tools are great, so we want to treat them equally".
- One tool per category, with mentions elsewhere as cross-reference sentences.
- Strict label semantics: "Free means entirely free tools, not freemium".
- New categories need 2+ tools.

Pruning was almost nil (45 "remove/dead" subjects, mostly about banners and code). The last content commit, 2020-09-28, is "Removing microcopyinspirations.com - website down".

**Contribution workflow and governance.**
- A startup team did the merging: Lisa Dziuba 155, Valia Havruliyk 152, Vladimir Berezovsky 47; then Tom Moor of Abstract in 2020.
- No CI. The guidelines refer to a PR template that does not exist in the repo.
- 1,508 commits in 2019, 141 in 2020, **zero since Sep 2020**. 200 open PRs and 32 open issues are frozen.

**Monetization.**
- Sponsorship.md (2019) sold "6 banners slots" plus social promotion, citing "15K ⭐" and "#5 product in the Design Category on Product Hunt".
- Oct–Nov 2019: "remove all banners except abstract".
- Feb 2020: the first H2 of the README became "Awesome Design Tools as a part of Flawless App family joins Abstract!", and it still is.
- 5 Abstract banners sit inside category sections, and Abstract is also a list entry. Neutrality was traded away openly.

**Secret sauce.**
1. Rich, scannable metadata (free, open-source, Mac-only, platform) that answers designers' real filters.
2. Narrative category intros and cross-references.
3. A companion website and Product Hunt launch that drove a burst of about 40k stars in two years.
4. Four themed files instead of one 500 KB page.

**Weaknesses.**
- Frozen for 6 years, so it is a time capsule of the Sketch/InVision era (40 Sketch or InVision Studio mentions). It still lists defunct products such as Daqri, a company that shut down in 2019.
- Sponsor and acquisition messaging occupies the top of the page.
- Dead website scaffolding, and not part of the index.

**Quotes.**
- "All tools are great, so we want to treat them equally."
- "Your contribution might be rejected if the tool… didn't pass our curation. Of course, this is very subjective."
- "Please, consider that we have a full-time job in our startup :)"

---

## Cross-list patterns for this archetype

1. **Being early buys a durable slot, not quality.** awesome-ML (4 days after the index) and awesome-react (26 days after) took the generic slugs and the index's one-per-topic slot in 2014. awesome-vue was created by Vue's author a week before Vue 1.0 shipped. All three remain the canonical entries in sindresorhus/awesome 12 years later, even though:
   - awesome-ML still has no index description and 12% `[Deprecated]` entries;
   - awesome-react shrank by 83%.

   Once a list holds the canonical spot, the stars keep accumulating whether or not it improves.
2. **First-year READMEs were bigger and cruder than today's, not smaller.**
   - awesome-ML: 160 entries on day one by cut-and-paste.
   - awesome-react: 602 entries by Jan 2015, organised by medium (Videos/Books/Demos).
   - Awesome-Hacking: one `####` heading per list.
   - The index: plain links with no descriptions.

   The "quality" features (description grammar, `#readme`, the 30-day rule, the review tax, free-only rules, truly-awesome tiers) were all added in 2016–2026, after the audience existed.
3. **The best-maintained classics shrink on purpose. Unpruned ones only grow.** Pruning events:

   | List | Pruning event | Size change |
   |---|---|---|
   | awesome-react | 2019 purge | −42% |
   | awesome-react | 2023 purge | −65% |
   | awesome-vue | Nov 2024 community prune | −62% |
   | sindresorhus/awesome | 2026 archived-list sweeps (25 lists) | first ever net decline |
   | Awesome-Hacking | Apr 2026 stale-repo sweep | 15 removed or replaced |
   | awesome-ML | never pruned (2014 → 2026) | grew from 507 to 1,387 entries |
   | Awesome-Design-Tools | never pruned (2019 → 2026) | frozen since 2020 |

   Pruning is episodic and bulk (a few days of focused commits), not continuous. Commit bodies that state the reason are a distinctive, reusable practice: "It's badly maintained", "(2016)", "since they are the things on their own nowadays".
4. **The 2026 AI-PR flood is the archetype's defining current event, and each governance style answered it differently.**

   | List | 2026 response |
   |---|---|
   | sindresorhus/awesome | AI rules (Mar), 4-PR review tax (Mar), then PR and issue creation closed to collaborators (late Aug), with no announcement |
   | awesome-ML | "Email me to prove you're human" (Apr), while inflow rose about 7x |
   | awesome-vue | Release-history rule for AI-built projects (Apr) |
   | awesome-react | No policy change |
   | Awesome-Hacking | No policy change; locks threads after 7 days |

   Single-merger lists with large inflow hit the wall first. The index added zero lists in 2026.
5. **AI cuts both ways inside the same repo.** awesome-vue's 18 Feb 2026 hygiene sweep (dead links, SHA-pinned actions, https) was authored by "Claude". Two weeks later an agent-made PR injected a `Resource from plugin:github:github…` artifact into the first line of the README, and it is still there 7 months later. Agents make bulk maintenance cheap, and single-reviewer merge flows fail to catch agent artifacts.
6. **Official backing buys continuity and trust, not editorial quality.**
   - vuejs/awesome-vue passed through five maintainer eras (Evan You → kazupon → LinusBorg → Demidov → Jogai) without a fork, rename or link break, because the org held the keys. Individually owned lists depend on one person: awesome-react's 2022 had 10 commits, and Awesome-Hacking had 1 commit in 2023.
   - awesome-vue's trust signals are institutional: namespace, official logo, "Official Resources" first, funding routed to the framework.
   - Its review quality is no better than individual lists: an artifact in the header, MIT license, inconsistent descriptions, 3k entries before the community prune.
   - Its edge is written, testable criteria (the vue-devtools detection test, the open-source checklist, "Truly awesome" tier) and the broadest contributor base (2,473 authors versus about 670–760 for the others).
7. **Ordering rules encode a governance stance.**

   | Rule | Lists | Stance |
   |---|---|---|
   | Alphabetical | Awesome-Hacking; Awesome-Design-Tools ("treat them equally") | neutral |
   | First-come-first-serve | awesome-vue | fairness among submitters |
   | Append at bottom (chronological) | the index | seniority |
   | By importance | awesome-react (shadcn-ui first) | opinionated, editorial |

   Only importance ordering helps readers choose; awesome-vue makes up for its order with a separate canon tier.
8. **Visual polish drove launch velocity but not longevity.**
   - Awesome-Design-Tools has the heaviest presentation in the set (about 2,000 inline SVG labels, category prose, cross-reference banners, a generated website). It got about 40k stars from 1,508 commits in a single launch year, then froze.
   - The plain-text classics (awesome-ML, awesome-react) kept compounding for 12 years.
   - The index is visually polished only at the page frame (logo, nav row, short URL, badge kit); entries stay plain text.
   - The polish that lasts is metadata readers can filter on (free / open-source / Mac labels, `[Deprecated]` tags), not decoration.
   - Presentation tied to an external site becomes debt when the site dies: the flawlessapp.io DNS is gone, but the `<div class="hidden-in-page">` markup remains.
9. **Lists of lists add a namespace, a standard and a pruning service, not just links.**
   - The index adds four things: one canonical slot per topic, an enforced format exported to downstream lists (badge, awesome-lint run in CI on each submission, `#readme`), a seniority-ordered registry, and periodic removal of archived lists.
   - Awesome-Hacking adds a domain lens and admits "arsenal" repos the index would reject (SecLists, PayloadsAllTheThings, Vulhub, GTFOBins). 55 of its 80 links are absent from the index.
   - Both under-describe: 32% of index entries and 62% of Awesome-Hacking descriptions break the index's own description rule.
   - The specialised list can drift into mirroring the general one: all of Awesome-Hacking's Apr 2026 additions were already in the index's Security section.
10. **Stars here reflect distribution and brand more than activity.** Awesome-Hacking has 124k stars on 141 commits, driven by the "Hack with GitHub" social account ("Need More? Follow… to get daily updates"). Awesome-Design-Tools reached 42k through a Product Hunt launch and a startup's marketing, and has 0 commits since 2020. The index has 524k stars from 20 commits in 2026 and closed PRs. Commit volume and star count are close to uncorrelated across these six lists.
11. **Monetization is tolerated where it stays out of the entries.**
    - The index rotates sponsor logos in the header only (45 "Meta tweaks" commits) and never in categories.
    - awesome-react tried a top banner (Fern) for 3 months and removed it.
    - Awesome-Design-Tools sold banner slots, then put its acquirer's banners inside 5 categories and its acquisition announcement as the first H2. It is the one list here whose neutrality is visibly compromised.
    - awesome-vue routes funding to the framework and treats paid placement as an explicit, separate negotiation ("open an issue first").
12. **Process artifacts are thin outside the index.**
    - Of the five topic lists, only awesome-vue has CI that checks content (duplicate-link lint) and a PR template.
    - awesome-react and awesome-ML have no CONTRIBUTING file and no license text worth the name.
    - Awesome-Hacking's only workflow locks threads.
    - These lists predate the norms the index now enforces, and the index grandfathers them; none would pass today's PR template.

    Process rigor is not what made the classics; slot ownership plus a few decisive editors is.
13. **Bus factor of one is the norm, and handoffs happen only within a network.** Every list has one active merger today: Sindre, Joseph Misiti, Nick Raienko (with Haroen Viaene), Jogai, Chandrapal Badshah, or nobody (ADT). Successful handoffs went to trusted contributors: awesome-react to Jason Brown and Haroen Viaene; awesome-vue within the org. The only list owned by a company (ADT) died with the company's change of focus after its acquisition.
14. **Scope hygiene through satellite files.** awesome-ML (books, courses, blogs, events, meetups, curriculum) and Awesome-Design-Tools (plugins, UI kits, conferences) moved non-core media out of the README. awesome-react instead deleted non-free media outright (2019). Both approaches keep the main page about the primary artifact.
