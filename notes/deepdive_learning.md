# Deep dive: LEARNING & KNOWLEDGE lists (self-improvement / career)

Analyst notes, Oct 2026. Sources: clones in `clones/`, `data/features_1.jsonl`, star/fork snapshots in `raw/EvanLi_*` and `data/tal_lists.tsv`. "Top author" means the top identity after merging name aliases that share one e-mail, so it can differ from the script's per-e-mail `top1_author_share`.

| List | Stars | Commits | Last human commit | Top author | Entries | Shape |
|---|---|---|---|---|---|---|
| trimstray/the-book-of-secret-knowledge | 253k | 1,069 | 2024-11-19 (last entry Feb 2022) | 84% (5 names, 1 e-mail) | ~906 links + 264 one-liners | personal toolkit + original recipes |
| practical-tutorials/project-based-learning | 288k | 609 | 2026-07-04 (weekly bot since) | 42% | 326 items / 456 URLs | catalog by language |
| MunGell/awesome-for-beginners | 90.7k | 1,032 | 2026-10-01 | 29% (new steward since 2024) | 224 repos | data-driven catalog |
| DopplerHQ/awesome-interview-questions | 85.2k | 451 | 2024-07-29 ("no longer actively supported") | ~35% | 351 | list of lists |
| binhnguyennus/awesome-scalability | 75.1k | 1,216 | 2026-01-04 | ~94% | 919 | concept → case-study reading list |
| prakhar1989/awesome-courses | 72.2k | 554 | 2022-11-12 | ~51% (90% of merges) | 228 courses | catalog + material legend |
| papers-we-love/papers-we-love | 111k | 891 | 2026-09-29 | 14.5% | ~585 papers, 203 hosted PDFs | community directory |
| kuchin/awesome-cto | 35.6k | 201 | 2026-03-02 | 90% | 242 | personal reading list |
| *jwasham/coding-interview-university* | 363k | 2,511 | 2024-12-06 | 39% | 463 checkboxes | study plan (contrast) |
| *donnemartin/system-design-primer* | 375k | 343 | 2026-03-20 | 51% | prose + 86 solution files | textbook (contrast) |

---

## 1. trimstray/the-book-of-secret-knowledge (~253k)

**Value proposition & scope.** The README opens with a mystique line: "*Knowledge is powerful, be careful how you use it!*", then "A collection of inspiring lists, manuals, cheatsheets, blogs, hacks, one-liners, cli/web tools, and more." It is framed as one practitioner's toolkit ("materials and tools that I use every day in my work"), aimed at sysadmins, DevOps, pentesters and security researchers. The scope is whatever the author found useful. The title promises insider status.

**Curation.** The only stated bar is a highlighted `diff` line: "not meant to contain everything but only good quality stuff". There are no criteria. Dead links get a `*` marker convention ("Please don't delete it without confirming that it has permanently expired"), but only about 6 are marked. 43 commit subjects match remove/dead/broken/dup. Link checking is a bash loop pasted into CONTRIBUTING, with no CI.

**Entry format.** Entries are HTML, not Markdown: `<a href><b>Name</b></a> - is a ...<br>`. 900 of 906 have a description, and 200 begin with "is" (a sentence-completion house style). Order is by judgment; the ToDo still says "- [ ] Sort order in lists". The differentiator is original content: **264 shell one-liner recipes**, grouped by tool (terminal, mount, lsof, find...), take up about 2,685 of the README's 4,442 lines. There are also hand-written mini-guides such as "Build your own Certificate Authority".

**Navigation.** A 15-chapter ToC, `[TOC]` back-links on every chapter, a separate one-liner ToC, and 123 emoji markers. It is one 211 KB file with no site or search.

**Governance.** CONTRIBUTING (319 words) requires a **signed-off-by line on every commit**, which is rare for a list. Five author names share `trimstray@gmail.com`: 896/1,069 commits (84%). Merges came in batches; 20 PRs were merged on 2022-02-23, the last content burst. Funding goes through GitHub Sponsors and Open Collective, with no sponsor placements.

**Maintenance.** Commits by year: 2018 338, 2019 521, 2020 123, 2021 59, 2022 25, 2023 0, 2024 3, 2025–26 0. The three 2024 commits are cosmetic (one swapped the bullet icon on 908 lines).

**Secret sauce.** (1) Original, copy-pasteable recipes make it a reference *book*, not just a link hub. (2) A mystique title plus a personal voice make starring feel like collecting a grimoire. (3) It merges sysadmin, security and DevOps tools the way those jobs actually overlap. (4) Every link has a uniform one-liner.

**Weaknesses.** No entries for about 4.5 years. HTML entries raise the barrier to contributing. No CI, 71 `http://` links, aging "Best Personal Twitter Accounts" sections, unsorted lists, bus factor 1.

**Quotes.** "This repository is not meant to contain everything but only good quality stuff." / "materials and tools that I use every day in my work" / "Knowledge is powerful, be careful how you use it!"

---

## 2. practical-tutorials/project-based-learning (~288k)

**Value proposition & scope.** "A list of programming tutorials in which aspiring software developers learn how to build an application from scratch." The word "aspiring" replaced "learners" between 2020 and 2023. The promise is an outcome you can show: you will *build* a shell, a Lisp, a database, a NES game.

**Curation.** For six years the rules were format-only, and they even allowed "Google URL Shortener" for long URLs. The **2026-07-03/04 revival** added real criteria: "free and open -- no paywall, login wall, or required newsletter signup", "project-based -- ...builds a complete, working artifact", and **affiliation disclosure**. A weekly `link-rot.yml` keeps state in `.github/link-rot-state.json` (456 URLs: 369 OK, 75 BLOCKED, 10 HARD_DEAD, 2 SUSPECT). Entries dead for 2+ consecutive weeks get a bot-opened removal PR. Anything ambiguous is "left in the report for a human to judge".

**Entry format.** `- [Title](url)` with no description. Multi-part series are nested. Titles are imperative briefs ("Write a Shell in C", "Build Your Own Lisp"), so the title *is* the description. Order is insertion order.

**Navigation.** 22 language sections with framework subsections (JavaScript → React/Vue/Node; Python → Bots/ML/OpenCV). A flat ToC and no site.

**Governance.** A PR template with 8 checkboxes (one tutorial per PR, free, project-based, searched for duplicates, ran the linter, relationship disclosure), YAML issue forms with a section dropdown, and a 1,178-line "README-as-data validator" (`scripts/check_readme.py`) that treats README and diffs as "untrusted input". `stale-prs.yml` stales PRs only; its comment says the old probot issue-staling "buried legitimate broken-link reports for years". The founder has 42% of commits, and a bulk adder made 114 commits, all in 2018.

**Maintenance.** Commits by year: 2017 156, 2018 257, 2019 39, 2020 33, 2021 74, 2022 8, 2023 3, **2024 0, 2025 0**, 2026 39 (17 of them bot). It went more than 3 years without a commit (2023-03-21 → 2026-07-03) while it was a top-15 GitHub repo. The revival merged about 20 queued PRs in two days, then the bot took over the weekly cadence.

**Secret sauce.** (1) The "build X from scratch" promise matches what self-learners want: a portfolio artifact. (2) A strict but one-line-explainable bar: free + project-based + complete. (3) Titles work as project briefs. (4) Now the most sophisticated link-rot pipeline in the archetype: a state machine, auto-fix PRs, and a domain policy marking Medium, Reddit and Udemy as unverifiable.

**Weaknesses.** No difficulty or level signal for a beginner audience. "Additional Resources" still lists Udemy.com, which contradicts the free-only rule. 14 URLs have failed 2+ weeks and await a human merge. 153 open issues.

**Quotes.** "following it, the reader builds a complete, working artifact (not just a concept explainer)" / "free and open -- no paywall, login wall, or required newsletter signup" / "aspiring software developers learn how to build an application from scratch"

---

## 3. MunGell/awesome-for-beginners (~90.7k)

**Value proposition & scope.** The H1 is "Awesome First Pull Request Opportunities". It is a two-sided list: newcomers find projects with beginner labels, and maintainers are told to "add the label `first-timers-only` (or similar) to your project and list it here". It points adjacent audiences to sibling lists.

**Curation.** It has real requirements: "Reasonably Developed", "Active Maintenance", "Appropriate Labels... must exist", "Supportive Community", no "small personal projects". There is also "No tracking links... This list is not for advertising purposes." Pruning is explicit: **32 "remove ... for inactivity" commits in 2024–26**. Lychee runs weekly and on PRs.

**Entry format.** `[Name](repo) _(label: good first issue)_ <br> description`, rendered by Jinja2 (`.github/scripts/render-readme.py`) from `data.json`. Every entry has a description (16 words on average). The label is the functional metadata (159/224 use "good first issue"). Entries and sections are sorted alphabetically by the generator.

**Navigation.** An A–Z table ToC over 30 technology sections. Repos with several technologies repeat across sections (11% duplicate links).

**Governance.** JSON authoring arrived on 2022-08-29. `invalid.yml` **auto-comments on, labels and closes any PR that edits README.md**. A new steward (Sammy Hori) has made 300 commits and 184 of the 245 merges since 2024. 166 of the founder's 264 commits are the build bot's "Update README.md". **35% of all commits (362/1,032) land in October**, the Hacktoberfest effect, and the issue/PR counter is at #2137.

**Maintenance.** Commits by year: 2015 29, 2016 87, 2017 76, 2018 45, 2019 89, 2020 85, 2021 19, 2022 44, 2023 12, 2024 275, 2025 170, 2026 101. It is active after the 2024 handover.

**Secret sauce.** (1) The only list here where *freshness is the product*: an opportunity rots when the project dies, so it prunes for inactivity. (2) Data-file authoring plus auto-closing README PRs absorbs heavy beginner traffic. (3) Two-sided framing gives maintainers a reason to submit and to keep labels alive.

**Weaknesses.** It has a **regression from the JSON migration**. Before Aug 2022, 222 of 257 entries deep-linked to the label page (`.../labels/first-timers-only`), one click from beginner issues. After it, 0 do (1/224 today). Beginners now land on repo roots. There is no per-entry issue count or freshness metadata, even though an unused `cghi.py` script that counts open labelled issues exists.

**Quotes.** "This list is not for advertising purposes." / "small personal projects not be added in the hope of receiving contributions" / "add the label `first-timers-only` (or similar) to your project and list it here"

---

## 4. DopplerHQ/awesome-interview-questions (~85.2k)

**Value proposition & scope.** "A curated list of lists of technical interview questions." It is a meta-list (originally MaximAbramchuck/awesome-interviews) with 60 H3 sections, mostly language/framework. Since 2024-07-29 its second line reads "**This project is no longer actively supported.**"

**Curation.** It ships an `awesome.md` manifesto ("it's a curation, not a collection"; "Comment on why something is awesome"), but entries are title-only despite the CONTRIBUTING rule that "every item has a good succinct description". The rule "added to the bottom of the relevant category" makes order follow arrival time. About 38% of entries (~135/351) come from content-marketing or hiring sites: guru99 31, Toptal 24, InterviewBit 16, techbeamers 10, careerride 9, javatpoint 8, adevait 7... Pruning happened in 2019 community PRs and a 2021 staff sweep.

**Entry format.** `* [Long descriptive title](url)`; the title stands in for the description. No metadata.

**Navigation.** A nested ToC only.

**Governance.** The creator has ~35% of commits, there were 11 mergers, and 82% of authors made one commit. In March 2021 the repo moved to DopplerHQ, a **UTM-tagged Doppler banner** appeared above the title ("All your environment variables, in one place"), and staff added a markdown-link-check Action. Its ignore-list exempts 11 URLs, **7 of them adevait.com**, a hiring marketplace whose pages are entries. The 2024 deprecation commit added "no longer supported" **but kept the banner**.

**Maintenance.** Commits by year: 2015 104, 2016 48, 2017 51, 2018 43, 2019 90, 2020 28, 2021 85, 2022–23 0, 2024 2. It has been dead since the 8-PR batch on 2021-11-16. A tracker snapshot that refreshes only on change froze it at 69k stars on 21/11/11. It now has 85.2k, about +16k while unmaintained.

**Secret sauce.** (1) It meets high-intent search demand ("X interview questions") with one bookmarkable page per stack. (2) Meta-list breadth at low curation cost.

**Weaknesses.** The clearest case of an aspirational audience attracting SEO content: "Top 25..."-style listicles, 149 `http://` links, dead stacks (AngularJS, Backbone, Knockout, MS Access), and sponsorship that outlived maintenance.

**Quotes.** "This project is no longer actively supported." / "it's a curation, not a collection." / "A curated list of lists of technical interview questions."

---

## 5. binhnguyennus/awesome-scalability (~75.1k)

**Value proposition & scope.** "An updated and organized reading list for illustrating the patterns of scalable, reliable, and performant large-scale systems." Its intro gives **situational entry points**: "If your system goes slow", "...goes down", "If you are having a system design interview", "If you are building your dream team". Each routes the reader to sections, making it the closest any catalog here gets to a learning path.

**Curation.** There are no written criteria. CONTRIBUTING is generic awesome boilerplate (it even says "Use the following format: `[List Name](link)`"). The real policy is visible in the content: primary sources by engineers at named companies. Pruning comes in owner sweeps ("Remove the book section" 2023; "Correct some obsolete links" 2025; "Fix dead links and remove obsolete resources (2026 cleanup)" ×4). 62 subjects match remove/dead/fix-link.

**Entry format.** A **concept → case study** hierarchy. The parent is a concept link (`[Distributed Caching](...)`) and the children follow `[<Thing> at <Company>]` ("Kubernetes at Tinder", "Sharding Postgres at Figma"), or "Talk - Speaker, Role at Company". The company name works as both metadata and authority. No descriptions. Commit subjects are the entry titles (772 one-entry commits in 2018).

**Navigation.** An 11-item ToC, a companion site (awesome-scalability.com, Jekyll), a logo. Sections are huge (median 58 items; Scalability ~417).

**Governance.** About 1,144 of 1,216 commits (~94%) come from five name variants of the owner. There have been only 38 PR merges and 3 mergers, and the issue/PR counter is at #108. Monetisation: "Roses are red. Violets are blue. Binh likes sweet. Treat Binh a tiramisu?" (PayPal).

**Maintenance.** Commits by year: 2017 5, 2018 772, 2019 210, 2020 82, 2021 43, 2022 35, 2023 28, 2024 21, 2025 14, 2026 6. The steadiest gardening in the set: 95 of ~98 months active, with a maximum gap of 63 days.

**Secret sauce.** (1) "X at Company" case studies make patterns concrete and double as interview prep. (2) Situational entry points. (3) One curator adding about one high-signal article a month for eight years. (4) It covers organisational scaling too (hiring, culture).

**Weaknesses.** The ToC has linked `[Book](#book)` to a section deleted three years ago. Link-rot risk is concentrated in 204 medium.com and 33 eng.uber.com links plus legacy blog domains. Rules are boilerplate; bus factor 1.

**Quotes.** "Case studies are taken from battle-tested systems that serve millions to billions of users." / "Knowledge is power, knowledge shared is power multiplied." / "Treat Binh a tiramisu?"

---

## 6. prakhar1989/awesome-courses (~72.2k)

**Value proposition & scope.** "There are a lot of ~~hidden~~ treasures lying within university pages scattered across the internet." The scope is university CS courses with free materials.

**Curation.** It has an explicit **anti-mainstream rule**: "not keen on adding popular courses (such as MOOCs / MIT OCW)... ideally for courses which are relatively unknown". Alphabetisation is required. Pruning is minimal (17 remove/dead commits).

**Entry format.** The richest template in the set: `[CS 61C](url) **Great Ideas in Computer Architecture** *UC Berkeley*`, then **material-type icons** (Lecture Videos / Notes / Assignments / Readings, explained in a Legend with hover tooltips), then a nested description and per-material sub-links. Institutions skew to Cornell (45 courses, against Stanford 22 and Berkeley 18), a contributor artefact going back to the 2015 "cornell-adds" merge.

**Navigation.** 11 topic sections and a ToC in a single 237 KB README.

**Governance.** The owner made 284/554 commits and 166 of ~185 merges; 8 mergers in total. No CI.

**Maintenance.** Commits by year: 2014 113, 2015 204, 2016 123, 2017 57, 2018 23, 2019 17, 2020 6, 2022 11, then nothing since 2022-11-12. The tracker snapshot froze it at **43K stars on 22/11/13**. It now has 72.2k: **+29k (+68%) with zero commits.**

**Secret sauce.** (1) The legend icons answer the learner's real question: is there video? Are there assignments I can do? (2) The anti-MOOC rule gives it an identity. (3) Course codes plus institution names feel like a credential ("CS 61C, Berkeley").

**Weaknesses.** Links are semester-pinned (348 tokens like `sp15` or `spring14`), so content drifts as course sites roll over. 541 `http://` links and no link CI. Icons are hot-linked from the legacy `assets-cdn.github.com` (not verifiable from this sandbox), a single point of failure for the legend. Dormant.

**Quotes.** "There are a lot of ~~hidden~~ treasures lying within university pages scattered across the internet." / "I'm not keen on adding popular courses (such as MOOCs / MIT OCW)" / "ideally for courses which are relatively unknown"

---

## 7. papers-we-love/papers-we-love (~111k)

**Value proposition & scope.** "a community built around reading, discussing and learning more about academic computer science papers. This repository serves as a directory". The repo is a by-product of a real community (meetup chapters, Discord, YouTube). The README spends more words on chapters, "How To Read a Paper" and other paper sources than on papers.

**Curation.** The strictest *type* rule in the set: "Books, blogposts, and/or reference pdfs don't go through the same review process... we won't add them". There is a copyright rule (PDFs are hosted only if redistribution is allowed) and a justification requirement ("why you love this paper"). Merging needs "**Two-Thumbs-Up minimum from PWL organizers/collaborators**". Recent activity is mostly link repair (78 such commits), often to web.archive.org.

**Entry format.** 88 topic READMEs across 78 directories. An entry is `* [Title](url)` plus optional "by Author". `:scroll:` marks a hosted copy: 215 of ~585 entries, backed by 203 PDFs in the repo. A rough parse finds that only ~18% of entries give a year (requested since issue #290) and ~6% carry justification text. **The "why" lives in PR bodies** (the template asks for "Reasons for including paper"), not in the index readers see.

**Navigation.** A directory-per-topic filesystem taxonomy and `scripts/download.sh` for bulk download. No ToC.

**Governance.** The most community-like profile: 318 authors, top author 14.5%, 12 mergers (6 with 5+ merges), a CoC that also governs meetups, and trademark terms for chapters. Monthly Lychee CI opens an issue. **`AGENTS.md` (2026-08-31)** gives AI agents editing rules ("Add an academic paper, not a book, blog post, or general reference"), the first such file in this set. A 1 MB `nautilus.db` from a 2017–18 bot still sits at the root.

**Maintenance.** Commits by year: 2013 35, 2014 363, 2015 162, 2016 81, 2017 77, 2018 31, 2019 44, 2020 25, 2021 11, 2022 22, 2023 16, 2024 8, 2025 5, 2026 11. Low volume but still merging (Mamba and ReAct papers in 2026).

**Secret sauce.** (1) Hosted PDFs make about a third of the collection immune to link rot. (2) An offline community gives the list a social purpose beyond starring. (3) A hard "papers only" boundary. (4) Review by two organisers.

**Weaknesses.** Justifications are required but invisible. 88 inconsistent index files. Wrong-target links that link checkers cannot catch: "A Note on Distributed Computing" points to a ResearchGate PDF titled "Why do users like video". Committed cruft.

**Quotes.** "every pull request we receive must have Two-Thumbs-Up minimum from PWL organizers/collaborators to be merged." / "Books, blogposts, and/or reference pdfs don't go through the same review process" / "a short justification of why you love this paper"

---

## 8. kuchin/awesome-cto (~35.6k)

**Value proposition & scope.** It opens with an AA-meeting joke, "— Hello, my name is Dima and I'm a CTO / — (chorus) Welcome, Dima", then "A curated and **opinionated** list of resources for Chief Technology Officers and VP R&D, with the emphasis on startups and hyper-growth companies." The scope follows the *job*, not a technology: Hiring, People management, Due Diligence, Money/Finance (equity, fundraising, procurement), Product, Marketing.

**Curation.** No CONTRIBUTING file. "Opinionated" means owner taste: there is no rubric and only about 15% of entries are annotated. Opinion shows through **selection plus authority attribution**: "- Werner Vogels *(Amazon CTO)*", "- Greg Brockman *(Stripe CTO)*". Light pruning ("Broken link fix, web.archive.org to the rescue"; 8 archive.org links).

**Entry format.** `* [Title](url) - Author *(Org/role)*`. 60 entries carry *(Quora)*/*(GitHub)*-style tags and 34 name an author. Light nesting (Startups vs Big companies).

**Navigation.** An 18-topic ToC, a GitHub Pages mirror, sibling lists (Awesome CEO, Awesome TPM), and a **Substack** ("📢 Subscribe to get updates"), so the list doubles as an audience channel.

**Governance.** The owner has 180/201 commits (90%) and there are 2 mergers. Only 46 issues and PRs in ten years: this audience reads rather than submits. Neutrality slip: a 2025 PR added a "CTO Insights Podcast" hosted on `ctoinsights.adevait.com`, the same hiring marketplace that is over-represented in the interview list.

**Maintenance.** Commits by year: 2016 9, 2017 28, 2018 22, 2019 15, 2020 33, 2021 30, 2022 42, 2023 7, 2024 2, 2025 12, 2026 1. Intermittent, at the owner's pace.

**Secret sauce.** (1) Job-shaped scope covers what technical lists do not (due diligence, equity, procurement). (2) Credential tags let executives skim by authority. (3) A self-deprecating peer voice in place of a vendor catalog.

**Weaknesses.** It calls itself "opinionated" but states almost no opinions. Quora links age badly. Bus factor 1 and no contribution rules.

**Quotes.** "Hello, my name is Dima and I'm a CTO" / "A curated and **opinionated** list of resources for Chief Technology Officers and VP R&D" / "with the emphasis on startups and hyper-growth companies"

---

## Contrast: study plans vs link lists

- **coding-interview-university (363k)** is a first-person *path*. It opens with an outcome story ("After going through this study plan, I got hired as a Software Development Engineer at Amazon!"), lists prerequisites ("Patience", "Time"), and limits scope ("only knowing about 75% is good enough for an interview"). It gives an order ("tackle the items in order from top to bottom") and **463 checkboxes**, and it tells readers to **fork and tick boxes**. Fork ratio: 85k/363k = **23%**, against 7–11% for sindresorhus/awesome, public-apis and awesome-python, 5.8% for book-of-secret-knowledge and 12.7% for project-based-learning. It covers motivation too ("Don't feel you aren't smart enough", "Don't Make My Mistakes", "The Daily Plan") and has 31 translation files. Money: sponsor logos (OSS Capital, Gitpod) in 2022, "Become a sponsor" removed 2024-12-06, and `utm_source=ciu` links to paid prep services (AlgoMonster, Meetapro, Hello Interview, Codemia) still in the content.
- **system-design-primer (375k)** is a *textbook with practice assets*: original summaries ("Everything is a trade-off"), 36 diagrams with credited sources, 86 solution files, 3 **Anki decks**, an EPUB build, a study guide by **interview timeline (short/medium/long)**, and TRANSLATIONS.md with named maintainers and a "Stalled" status. Its author wrote 51% of commits, mostly in 2017. It has had about 26 commits since 2021, nearly all link fixes.
- **What they do differently.** They sequence instead of grouping, write content instead of pointing to it, give a time budget and an exit condition, and provide practice tools. Both are "finished" artifacts that need little upkeep, so dormancy barely hurts them. The awesome lists that come closest borrow pieces of this: awesome-scalability's interview router, book-of-secret-knowledge's original one-liners, and awesome-courses' material legend.

---

## Cross-list patterns for this archetype

1. **Stars measure the promise, not current quality, and they keep growing during dormancy.** awesome-courses: 0 commits since 2022-11-12, yet 43K (tracker snapshot frozen at that update) became 72.2k. awesome-interview-questions: 69k (frozen 21/11/11) became 85.2k after declaring itself unsupported. book-of-secret-knowledge: no entries since Feb 2022, 253k stars. project-based-learning: 3.3 years with zero commits while in GitHub's top ~15. Here a star is a "learn this later" bookmark, an act of aspiration.
2. **Evergreen content makes dormancy survivable, unlike ecosystem catalogs.** The value is in classics (Turing 1936; Jeff Dean and Brewer; Spolsky; shell one-liners) that don't break when a library dies. Decay concentrates in time-bound formats: semester-pinned course URLs (348 tokens in awesome-courses), SEO listicles, and Twitter/Medium links.
3. **The biggest winners are paths, not catalogs.** system-design-primer and coding-interview-university outrank every awesome list here by sequencing, budgeting time ("8–12 hours a day, for several months"; short/medium/long) and adding practice tools (checkboxes, Anki, solutions). The awesome lists default to a **language/stack taxonomy** (22, 30 and 44 sections in project-based-learning, awesome-for-beginners and the interview list): an index of what you already know, not where you are going. None marks difficulty, despite beginner audiences.
4. **Framing sells transformation or insider status.** Through titles ("Secret Knowledge", "University", "Primer", "from scratch", "First Pull Request"), through intros ("I got hired... at Amazon"; "If you are having a system design interview... Good luck!"; "aspiring software developers", added between 2020 and 2023), and through identity ("Hello, my name is Dima and I'm a CTO").
5. **A single author's voice dominates the high-trust knowledge lists.** awesome-scalability ~94%, awesome-cto 90%, book-of-secret-knowledge 84%, awesome-courses ~90% of merges, against papers-we-love 14.5% and the interview list ~35%. First-person framing ("tools that I use every day") borrows the trust of a practitioner's bookshelf. The cost is bus factor 1: book-of-secret-knowledge and awesome-courses stopped when their authors moved on.
6. **"Opinionated" shows through omission and attribution, not commentary.** awesome-cto annotates about 15% of entries and signals taste through credential tags. awesome-scalability uses "X at Company". awesome-courses states opinion as an exclusion (no MOOCs/OCW). papers-we-love excludes whole content types. Even where justification is *required* (papers-we-love), only ~6% of index entries show it, because the reasons sit in PR bodies.
7. **Original content is the moat; pure link lists are fungible and get captured by SEO.** About 38% of the interview list comes from content-marketing or hiring sites. The defensible lists add their own material: 264 one-liners (book-of-secret-knowledge), 203 hosted PDFs (papers-we-love, immune to link rot), diagrams and solutions (system-design-primer), a study plan (coding-interview-university).
8. **Career audiences invite monetisation and neutrality leaks.** A Doppler UTM banner sits above "no longer actively supported". The interview list's link checker whitelists 7 adevait.com URLs, and an adevait-hosted podcast entered awesome-cto in 2025. coding-interview-university carries `utm_source=ciu` links to paid prep services. Healthy counter-rules: awesome-for-beginners' "not for advertising purposes" and project-based-learning's 2026 affiliation-disclosure checkbox.
9. **Beginner lists become contribution sandboxes and need defensive automation.** awesome-for-beginners: 35% of commits in October, an issue/PR counter at #2137 for 224 entries, and auto-closing of README edits. project-based-learning: ~#898. Both moved to README-as-data (JSON + Jinja; a 1,178-line validator), because the audience they serve is the one flooding them.
10. **Making a list data-driven can silently remove learner affordances.** awesome-for-beginners' 2022 JSON migration dropped beginner-label deep links from 222/257 entries to 0, so newcomers land on repo roots instead of filtered issues. Neither link checkers nor star counts notice.
11. **How much freshness matters depends on what kind of value the list offers.** Opportunity lists must prune for liveness (32 removals "for inactivity" in 2024–26; "Active Maintenance" required). Knowledge lists treat age as a feature, so their upkeep is link repair, often via web.archive.org.
12. **Maintenance comes in sweeps, often from a revival or a new steward rather than the founder.** Examples: 20 PRs merged on 2022-02-23 (book-of-secret-knowledge, then silence); 8 on 2021-11-16 (interview list, then death); about 20 on 2026-07-03/04 plus a bot (project-based-learning); a 2026-10-01 batch by awesome-for-beginners' 2024 steward; awesome-scalability's "2026 cleanup". Only awesome-scalability gardens continuously (95/98 months).
13. **A social layer outside GitHub gives a list a reason to exist beyond stars.** papers-we-love has meetups, Discord, YouTube and two-organiser review. awesome-cto has a Substack. coding-interview-university turns forks into workbooks (23% fork/star, the highest observed). Lists without such a layer (awesome-courses, the interview list) survive purely as bookmarks.
14. **Written rules are often boilerplate; the real policy shows in the data, and good rules arrive late.** awesome-scalability's and the interview list's CONTRIBUTING files share generic "`[List Name](link)`" text that fits neither. The interview list demands descriptions it never had. book-of-secret-knowledge requires DCO sign-offs but has no link CI. The meaningful rules in this set were written during revivals: project-based-learning's 2026 free/project-based/disclosure criteria and papers-we-love's 2026 AGENTS.md.
