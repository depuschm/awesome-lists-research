# Deep dive: PRACTICAL DIRECTORIES archetype

Lists that answer a concrete, recurring need ("which free API / free tier / self-hostable app / Mac app / free book can I use for X?").
Data: local partial clones as of 2026-10-24/25 (plus `awesome-selfhosted/awesome-selfhosted-data`, cloned for this note). Counts are mine (grep on HEAD or on historical blobs), so they may differ slightly from script-computed numbers.

---

## 1. public-apis/public-apis (~491k stars)

**Value proposition & scope.** The 2022 tagline: *"A collective list of free APIs for use in software and web development."* The current heading is *"Try Public APIs for free"*. Scope test (CONTRIBUTING): the API needs "full, free access or at least a free tier" and must not depend "on the purchase of a device/service". The audience is hobby and early-stage developers who need a data source fast.

**Curation policy.** The rules are mostly about format. Exclusions: marketing PRs, paid-only APIs, and "update/new version" duplicates. Dead entries were handled by sweeps, not by policy: 128 removal commits in 2021 and 62 in 2022 ("Remove X, it's broken", Matheus Felipe), then 1 in 2024 and 17 in 2026. A nightly `validate_links.yml` exists, but there is no visible follow-up on its results.

**Entry format.** A table `API | Description | Auth | HTTPS | CORS` with closed vocabularies: Auth is one of `apiKey`/`OAuth`/`X-Mashape-Key`/`User-Agent`/`No`; HTTPS is Yes/No; CORS is Yes/No/Unknown. Descriptions are capped at 100 characters with no trailing punctuation, names may not end in "API", and sections are alphabetical. Across the 2,190 body rows:

| Field | Distribution |
|---|---|
| Auth | No 1,050 / apiKey 980 / OAuth 150 |
| HTTPS | Yes 2,101 / No 88 |
| CORS | Unknown 1,038 / Yes 892 / No 259 |

Why it matters, in CONTRIBUTING's words: *"Without proper CORS configuration an API will only be usable server side."* The three columns answer a front-end developer's first questions (do I need a key, can I call it from the browser, will mixed content break?) without a click. That is why a table beats bullets here. The new MCP Servers table (2026-09-21) replaces HTTPS/CORS with `Transport` (stdio/HTTP/SSE) and `Install` (marketplace links), extending the schema per resource type.

**Navigation.** 51 flat categories, an Index, and a "⬆ Back to Index" link after each table. The 2022 live count badges and the links to 5 unofficial alternative sites are gone. No translations.

**Workflow & governance.**
- CI runs a Python validator (alphabetical order, padding, vocabularies, description length, at least 3 entries per category) and link-checks only the lines a PR adds. 9-item PR checklist; "Add one link per Pull Request".
- *Takeover:* before March 2022 the README listed "Currently Active Maintainers" (matheusfelipeog, pawelborkar, marekdano, yannbertrand) and an M3O sponsor logo.
  - 2022-03-11: the `APILayer` account swapped in its own logo and pushed a "Code Detection API" row straight to master. Yann Bertrand, a maintainer since 2016, reverted all four commits that day.
  - 2022-03-16: APILayer re-applied the change and deleted the maintainers block. Yann's and Matheus's last commits date from 2022-03-11/16.
- *Dormancy:* 2, 6 and 2 commits in 2023, 2024 and 2025 (APILayer "Update README.md" plus a 2024 Postman redesign).
- *2026 flood:* 1,812 commits. 869 of 874 merges since April 2026 come from one email (`…@studio1hq.com`) under three display names (Arindam, Astro_mike, commit10). The same identity added Filestack, which also appears in the sponsor table. 103 commits in 2026 carry Claude or Cursor co-author traces.
- *Commercialization:* the README opens with an "APILayer Unified Suite" ad, a 9-product list (Mediastack twice), an 11-row "APILayer APIs" table with Postman buttons, and a banner, all `utm_campaign=Public-apis-repo` tagged.
- *Neutrality:* inside the "neutral" tables I count about 18 APILayer-family entries, 16 utm-tagged links, IPstack listed twice in Geocoding, and the APILayer "IPstack MCP" pinned first in the MCP table, out of alphabetical order. CONTRIBUTING still says *"This API list is not a marketing tool."*

**Maintenance & drift.** Feb 2022 had 0 alphabetical inversions (my own check). Now there are 55 inversions in 29 of 51 sections, 105 rows with a stray extra column, and 14 descriptions over 100 characters, so the format CI no longer gates merges. Entries: 1,419 (2022-02), 1,436 (2026-04), 2,190 (2026-10).

**Secret sauce.**
1. Closed-vocabulary technical columns that make a link list a filterable spec sheet.
2. A machine-checkable format that let strangers safely edit a 1,400-row table (in its good years).
3. A crisp "free tier, no hardware purchase" test.
4. A per-type schema extension (the MCP table).

**Weaknesses.** Sponsor capture with no in-table disclosure. Bus factor 1. CORS unknown for 47% of rows. A 4-year review gap. CONTRIBUTING documents a "Call this API" column that the body tables lack.

**Quotes.**
- "This API list is not a marketing tool, but a tool to help the community build applications and use free, public APIs" (CONTRIBUTING)
- "Without proper CORS configuration an API will only be usable server side." (CONTRIBUTING)
- "Only link to listings that exist. A link to a marketplace page that 404s will get the pull request closed." (CONTRIBUTING, MCP)

---

## 2. ripienaar/free-for-dev (~140k stars)

**Value proposition & scope.** *"This is a list of software (SaaS, PaaS, IaaS, etc.) and other offerings with free developer tiers."* It is deliberately narrowed to what *"infrastructure developers (System Administrators, DevOps Practitioners, etc.) are likely to find useful… this is opinionated."* Hard rules:
- as-a-Service only;
- a free tier, not a trial;
- a time-bucketed tier must last at least a year;
- *"I will not accept services that restrict TLS to paid-only tiers"*.

The trial and one-year rules were present by 2019 and the TLS rule by 2021.

**Curation policy.** CONTRIBUTING's "Services we do not accept": cPanel-style PHP hosting, DNS frontends to Cloudflare, verbatim copies, disposable email ("we have enough of those"), and generic browser "toolbox" sites. The PR template (new submissions only) requires: SaaS not self-hosted; free tier not trial; *"Pricing information is clearly visible without signup or phone calls"*; the entry states what is free; contact details and a privacy policy; and (2026-09-20) *"This is not a generic browser based developer toolbox, I agree to be banned from this list if it is"*.

**Pruning events (the 2025 to 2026 drop).** My counts of `* [` lines:

| Date | Entries |
|---|---|
| 2025-01 | 1,611 |
| 2026-01-01 | 1,672 |
| 2026-02-01 | 1,396 |
| 2026-03-01 | 1,409 |
| 2026-04-01 | 1,273 |
| 2026-10-01 | 1,372 |

- **2026-01-02/03.** R.I.Pienaar merged eight self-authored PRs `cleanup1`…`cleanup8` (#3957-#3965). Each is a "Remove entries" commit with the same body, *"Dead entries / Not free entries / Unclear pricing"*, removing about 325 lines in total. A whole-list "Sort entries" pass (374+/372-) followed. The same batch added the LLM canary checkbox to the PR template.
- **2026-03-29/30, a scope trim.**
  - "Trim the design and ui section down to services and not icons sets etc" (-104).
  - "Remove some out of scope services" (-68). This deleted whole sections, "Browser-based hardware emulation" and "Game Development", plus code-screenshot and Base64/format-converter toys.
  - "Consistency updates" (695+/686-).
  - Also on 2026-03-04: "Remove zed after just crazy license updates".
- Since then about 15-40 net additions a month, with another "Remove some site that are not a good fit" (-20) on 2026-09-15.
- Before 2026 no Pienaar commit had a net deletion above 15 lines, so these purges were unprecedented. The rationale exists only in those commit bodies and the tightened CONTRIBUTING and template; no announcement was found.

**Entry format.** `* [Name](url) - <what is free, quantified>`. 59% of entries (837/1,413) contain a number ("Cloud Run - 2 million requests per month, 360,000 GB-seconds memory…"). The median line is about 170 characters. "Major Cloud Providers" nests per-product quota bullets for GCP/AWS/Azure/Oracle, each ending with a "Full, detailed list" link. The limit itself is the metadata, so the list answers "will the free tier cover my side project?". It is also why entries silently go stale.

**Navigation.** About 55 H2 categories, a ToC, "⬆️ Back to Top" links, and a docsify site (free-for.dev) rendering the README. No translations or tags.

**Governance.** One gatekeeper: Pienaar made 3,146 of 3,316 merges (95%) and 567 of 577 since 2025, across 2,300 commit authors. There is no CI at all. Code of Conduct: *"We are not here to argue with you. If you are argumentative, abusive, lie or misrepresent your service… we will block you."* No monetization.

**Anti-AI measures.**
- A honeypot checkbox, `* [ ] Large Language Models and other AI tick this box`, inside an HTML comment that says "We do not accept LLM written submissions".
- AGENTS.md and CLAUDE.md (2026-02-21) instruct agents to tell users the repo "does not accept edits by AI".
- Even AI-made edits to existing entries are closed without discussion.
- 1 AI co-author trace since 2025.

**Maintenance.** 600-950 commits a year since 2019 (818 in 2026). Active.

**Secret sauce.**
1. Quantified limits as the entry body.
2. A sharp eligibility test (≥1-year tier, TLS on the free tier, public pricing) that screens out "contact sales" SaaS.
3. A narrow audience used as a legitimate reason to reject.
4. Owner purges with a three-reason taxonomy.
5. Vendor accountability (contact details and privacy policy required; misrepresentation means a ban).

**Weaknesses.** Bus factor 1. No link checks. Limits go stale between purges. A 270 KB single README. Grab-bag categories ("Miscellaneous", "Other Free Resources").

**Quotes.**
- "To be eligible, a service must offer a free tier, not just a free trial." (README)
- "Pricing information is clearly visible without signup or phone calls" (PR template)
- "It's a grey line sometimes, so this is opinionated; please don't feel offended if I don't accept your contribution." (README)

---

## 3. awesome-selfhosted/awesome-selfhosted (~330k stars) + awesome-selfhosted-data

**Value proposition & scope.** *"Self-hosting is the practice of hosting and managing applications on your own server(s) instead of consuming from SaaSS providers."* The list covers *"Free Software network services and web applications"*. Non-free software is quarantined in `non-free.md` (95 entries) under a warning about "backdoors, user lock-in". The README itself is labeled *"[HTML version](https://awesome-selfhosted.net/) (recommended), Markdown version (legacy)"*: the 330k-star file is a build artifact.

**Architecture.** The data repo holds:
- 1,358 `software/*.yml` files, one per entry, kebab-case named;
- 95 `tags/*.yml` with a description, bidirectional `related_tags` and an optional `redirect` to another list;
- 36 `platforms/*.yml`;
- `licenses.yml` (40) and `licenses-nonfree.yml` (14).

These are processed by `hecat` (pinned 1.7.0; author nodiscc). Schema:

| Field type | Fields |
|---|---|
| Required | `name`, `website_url`, `source_code_url`, `description` (<250 characters, capitalized, ends with a dot), `licenses[]`, `platforms[]`, `tags[]` |
| Optional | `depends_3rdparty`, `demo_url`, `related_software_url`, `icon_url` |
| Bot-written | `stargazers_count`, `updated_at`, `archived`, `current_release`, 12-month `commit_history` |

**CI and checks.**
- PR: lint plus a markdown export dry-run.
- Push to master: lint, then regenerate the README and the Sphinx/Furo site and force-push both to their repos via deploy keys.
- Nightly 22:22 UTC:
  - Metadata refresh: bot commits "[bot] update projects metadata" (927 bot commits since 2024).
  - URL check, with about 75 annotated exclusions ("DDoS protection page, always returns 403").
  - `awesome_lint_strict`: warn after 186 days without an update, error after 365, error if archived.
- A `last_updated_skip` whitelist spares 14 "simple/no maintenance required" projects, each with a comment.
- Nightly results feed rolling issue #1 and two README badges.
- Lint also enforces at least 3 items per tag, bidirectional related tags, known licenses and platforms, filename equal to the kebab-cased name, and no dangling icons.

**Curation policy.**
- "Software with no development activity for 6-12 months may be removed"; serious security issues mean removal.
- Admission requires a first release more than 4 months old, active maintenance, working install docs, and absence from awesome-sysadmin, staticgen, staticsitegenerators and dbdb.io.
- "What does not qualify": cloud-locked software, libraries/SDKs, PaaS/serverless, generic deployment tools, and mere "Dockerization".
- Canned replies explain the 4-month rule politely.

Pruning evidence: removal commits ran 206 (Jun-Dec 2023), 110 (2024), 135 (2025), 104 (2026). Of the parenthesized reasons, "unmaintained" appears 343 times, "archived" 44, dead 4; the convention is `remove X (unmaintained since 2025-09-04)`. The size is held flat: about 1,294 (2023-06), 1,233 (2023-12, after the strict check landed in July 2023), about 1,360 (2026-10).

**Entry format.** `- [Name](url) `⚠` - Description. ([Demo](..), [Source Code](..)) `GPL-3.0` `PHP/Docker``. A license legend sits at the bottom. The single "anti-feature" flag ⚠ means "Depends on a proprietary service outside the user's control" (70 entries). Category headers carry a Wikipedia-linked definition and a "_Related:_" line. Style rules: no "open-source/free/self-hosted" in descriptions; standard suffixes "(alternative to X)", "(fork of X)", "(documentation in LANG)".

Each tag answers one question: license ("may I run, modify and keep using it?"), platform ("does it fit my stack?"), ⚠ ("is it really self-hosted?"), Demo ("can I try it first?"). Together they make the list a pre-filtered shortlist.

**Navigation.** 95 categories, with hierarchy expressed through names like "Communication - Email - …". The HTML site adds per-tag, per-platform and per-license pages with stars and last-update dates. Alternative frontends are linked. In the Markdown, a multi-tag entry appears only under its first tag ("choose wisely").

**Governance.** Founded in 2015 by Kickball; nodiscc has 2,677 commits. Recent humans: Rabenherz112 (360 since 2024), nodiscc (195), Kieran (110), kokomo123 (64). Squash merges. *"Any maintainer with merge permissions can merge… Consensus is preferable but not required"*, with a deliberate "merged at least ~1 week after approval" delay. Funding is Liberapay, explicitly for domain costs; no sponsors. AI: an LLM ban formalized 2026-09-15 (#3084), a "done by a human, not a machine/LLM" checkbox, and an "AI AGENTS:" comment block forbidding agents from opening PRs/issues or writing entries while allowing them to explain rules. 0 AI traces since 2025.

**Secret sauce.**
1. YAML source of truth with a generated README and site.
2. Automated freshness that turns pruning into a routine stream of "remove X (unmaintained since …)" PRs.
3. Free-software purity enforced by the exporter's license allowlist (BUSL, SSPL, Elastic, Commons-Clause go to non-free.md).
4. Objective, checkable admission gates.
5. Scope delegated to sister lists.

**Weaknesses.** High contributor friction (YAML, kebab-case, one-week wait). Dependence on one tool author. Activity-based pruning punishes "finished" software unless it is whitelisted. The long URL-exclusion list shows how bot protection limits link checking.

**Quotes.**
- "Software with no development activity for 6-12 months may be removed from the list" (CONTRIBUTING)
- "Please avoid redundant terms in project descriptions, such as open-source, free, self-hosted… as their presence on awesome-selfhosted already implies this." (CONTRIBUTING)
- "The line is between helping a person understand the rules, which is welcome, and producing the submission, which is not." (CONTRIBUTING, AI block)

---

## 4. jaywcjlove/awesome-mac (~117k stars)

**Value proposition & scope.** *"This project is dedicated to collecting high-quality macOS software and organizing them systematically by different categories."* It is a consumer-plus-developer app guide. It started Chinese-first (2016-07, "for developers and designers", thanking GitHubDaily for promotion). English became README.md by mid-2017, with zh/ja/ko as siblings.

**Curation policy.** Loose: "Make sure each list item is useful", alphabetical, one item per PR. There are no license, activity or maturity bars. Removals are ad hoc, 6-43 a year ("Remove Arc browser", "Remove NotchNook"). A distinctive section, *"Pirated software download site blocklist"*, lists struck-through piracy sites ("Refuse piracy from me."), with a pinned issue for reporting cracks, next to "Genuine Sites".

**Entry format.** `* [Name](site) - One sentence. [OSS](repo) [Freeware] [App Store] [Native] [Awesome-list]`, with the legend at the top. Out of about 1,434 entries: OSS 682, Freeware 948, App Store 193, Native 64 (the Native icon is new in 2025-26). The icons answer the Mac buyer's questions: free? auditable? on the App Store? native or Electron? The OSS icon doubles as a second link to the repo.

Notably, the 2016-2018 README used *subjective* icons: "hot" (71 uses in 2017), "recommended", "must-install", and red stars for "strongly recommended". All were gone by early 2019. The list moved from editorial ratings to factual attributes, presumably because ratings could not be maintained or defended across 1,000+ entries.

**Navigation & distribution.**
- 28 H2 / 42 H3 categories.
- Separate command-line and editor-plugin pages.
- An idoc website and per-language RSS feeds regenerated in CI (355 bot commits).
- An npm package exporting JSON in 4 languages, and a Docker image.
- Translation drift: EN 1,434, JA 1,433, ZH 1,308, KO 913.

**Governance & monetization.**
- One maintainer: jaywcjlove and 小弟调调 are the same person, with about 1,311 commits.
- Above the title: 4 sponsor banners (Enconvo, getapps.cafe, ScreenSage Pro, and the reseller LIZHI.SHOP), then about 32 icons of the maintainer's own apps ("Using my app is also a way to support me").
- Neutrality leaks: sponsors appear as ordinary body entries (Enconvo, ScreenSage Pro, 3 getapps.cafe apps), as do about 6 of the maintainer's apps, without disclosure. 2026 has "Add Enconvo donation" next to "Add Enconvo".
- CI only builds and deploys. No link or format checks.
- AI is embraced: *"AI-assisted contributions are welcome"*. The repo ships a Codex skill (`.codex/skills/awesome-mac-maintainer`, 2026-04-11) encoding the rules: choose the category from comparable entries, one sentence, "Avoid marketing phrasing", sync all 4 language files. 67 AI traces since 2025.

**Maintenance.** 964 commits in 2026 (355 by bots), versus 91-195 a year in 2019-25.

**Secret sauce.**
1. A factual icon legend, and the shift away from subjective ratings.
2. Multilingual parity, now delegated to an AI maintainer skill.
3. Multi-channel distribution (site, RSS, npm JSON, Docker).
4. An anti-piracy stance that builds vendor trust.

**Weaknesses.** Ad-first README with undisclosed sponsor and self listings. Bus factor 1. No freshness checks. Translation drift. Inconsistent icon usage (e.g. an OSS icon with no repo link on the maintainer's DevHub).

**Quotes.**
- "Refuse piracy from me. Software vendors can go to these places rights." (README)
- "We love apps, but only authentic ones. :)" (README)
- "AI-assisted contributions are welcome, but they should follow the same repository rules as manual edits." (docs/CONTRIBUTING.md)

---

## 5. serhii-londar/open-source-mac-os-apps (~51k stars)

**Value proposition & scope.** *"A curated list of open source applications for macOS"*, with a contributor angle: *"The main goal of this repository is to find free open source apps and start contributing."* Open source is the ticket in, so the differentiating metadata is the implementation language rather than price.

**Curation policy.** "Projects are ineligible if: Lack recent commit; README is not clear or not written in English". The PR checklist requires "a commit from less than 2 years ago". Deletion reasons include "Doesn't build in the current Xcode" and "Lacks license". Enforcement is manual and rare: 28 removals in 2018, then 0-7 a year. There is no automated activity check.

**Entry format / architecture.** `applications.json` is the source of truth (931 apps), with fields `title`, `short_description`, `categories[]`, `repo_url`, `icon_url`, `screenshots[]`, `official_site`, `languages[]`. A 609-line Swift generator rebuilds the README on each push:
- a stats table ("Swift: 476 • Objective-C: 142…") and a "Last Updated" badge;
- a language-icon legend;
- per-entry language icons and a collapsible `<details>` Screenshots block.

Many fields go unfilled: 331 entries have no screenshots and 508 no official site. The taxonomy leaks: one-off categories "Editors" vs "editors", "Android", "csv". The README is 739 KB.

**Navigation.** An 11-link quick bar, full Contents, headers like "🎵 Audio (62)", and a Telegram channel announcing new apps.

**Governance.**
- Solo: Serhii Londar (3 name variants) made about 748 commits and 265 merges.
- PR CI runs `awesome_bot` on the JSON and a Dangerfile (fails on an empty PR body, warns on "Update README.md" titles).
- Bursty history: 584 commits in 2018; 45/28/2/28 in 2022-25; 482 in 2026. That includes 173 in Feb 2026 (15 by the GitHub Copilot coding agent clearing old issues, e.g. "Remove discontinued Atom editor") and 259 in Oct 2026. Apps went from 617 to 931 during 2026.
- Review-quality signal: PR #940 ("Add mxMarkEdit", 2026-02-20) overwrote `PULL_REQUEST_TEMPLATE.md` with the contributor's filled-in submission and was merged. Every new PR now starts pre-filled with mxMarkEdit.
- Monetization: Patreon only.

**Secret sauce.**
1. Implementation language as the primary metadata, aimed at would-be contributors.
2. JSON plus a generator: automatic stats and collapsible screenshots.
3. Open-source-only scope, which removes the commercial spam vector.

**Weaknesses.** The 2-year activity rule is unenforced. Batch merges with minimal review. README bloat. The broken PR template.

**Quotes.**
- "The main goal of this repository is to find free open source apps and start contributing." (README)
- "Typical reasons for deleting a project: Doesn't build in the current Xcode" (CONTRIBUTING)

---

## 6. EbookFoundation/free-programming-books (~400k stars)

**Value proposition & scope.** *"List of Free Learning Resources In Many Languages."* It began as a StackOverflow list, was moved to GitHub by Victor Felder, and was transferred to the Free Ebook Foundation on 2017-05-30: *"a not-for-profit organization… Donations… are tax-deductible in the US."* Scope is defined by genre (books, courses, interactive tutorials, playgrounds, podcasts/screencasts, problem sets, cheat sheets) and by "really free".

**Curation policy.** This is the most rigorous definition of "free" in the archetype.
- *"'A link to easily download a book' is not always a link to a free book."*
- No Google Drive, Dropbox, Mega or Scribd links.
- The most authoritative source wins.
- *"We don't list things that we'll need to remove in six months"*: no time-limited courses or trials.
- Excluded genres: blogs, articles, short videos, chapters, teasers, Slack/Telegram channels.
- Book-ness heuristics (ISBN, ToC, editions, self-contained).

The PR template asks *"How do we know it's really free?"* and *"For book lists, is it a book?"*. Link rot is repaired, not only deleted: an `archived` notation substitutes a Wayback URL (85 in the language-books file), and `in process` marks unfinished books.

**Entry format.** `* [Title (year)](url) - Author, `trl.:` Translator (PDF, EPUB) (CC BY-SA) *( :card_file_box: archived)*`. Library-grade rules:
- MARC relator codes for translators;
- no creator links, no honorifics, no ALLCAPS, no emojis, no invented titles;
- tracking codes stripped;
- access notes such as `(email address *requested*, not required)` or `(Leanpub account or valid email requested)`;
- versionless license tags (CC BY, CC BY-SA…, GFDL).

These rules answer the learner's questions: offline readable? which format? may I share it?

**Multi-file / multilingual organization.** Eric Hellman reorganized about 121 list files on 2020-12-03 into `books/`, `courses/`, `casts/` and `more/`, with locale suffixes (`-zh`, `-pt_BR`, `-fa_IR`). The README is only an index of these files.
- English books are split by language (1,875 entries) and by subject (893; split off in 2021 because "Language Agnostic… got so big"). 43 other languages have their own book files.
- Courses cover about 40 languages (EN 1,502, HI 579, VI 456, AR 403). Casts cover 21.
- About 13,000 entries in total, long-tailed (e.g. `books/…-hy.md` has 0 entries).
- Contributor docs are translated too: 35 HOWTO, 23 CONTRIBUTING, 32 Code of Conduct.
- A custom RTL/LTR linter covers Arabic, Hebrew, Farsi and Urdu files.
- Discovery runs through a Jekyll static site and a separate search site, with the search box embedded in the README.

**Governance & scale.**
- 3,525 commit authors. Squash merges hide mergers; Eric Hellman (Foundation) is a visible committer.
- CI: `fpb-lint` (alphabetical order and spacing across all lists), `check-urls` (awesome_bot on changed files only), conflicting-PR detection, an issue pinner, and a stale bot (PRs stale at 60 days, closed 30 days later; issues exempt).
- **Hacktoberfest is the engine:** a README badge advertises it, and 1,327 of about 1,955 commits since 2023 (68%) landed in October.
- No explicit self-promotion or AI rules (20 AI traces since 2025).

**Maintenance.** Peaks in 2013-14 and 2020-22. 370 commits in 2024, 536 in 2025, 198 in 2026 so far (pre-October). Active, but seasonal.

**Secret sauce.**
1. An operational definition of "free" and of each genre.
2. Library-grade metadata conventions.
3. Language as a first-class axis.
4. Non-profit ownership with no sponsor placements.
5. Search and static sites, so nobody scrolls a 13k-item Markdown list.

**Weaknesses.** Near-empty language files. No scheduled full link check. A one-month contribution peak. Heavy English skew.

**Quotes.**
- "'A link to easily download a book' is not always a link to a free book. Please only contribute free content." (CONTRIBUTING)
- "We don't list things that we'll need to remove in six months." (CONTRIBUTING)
- "If you can print it out and retain its essence, it's not an Interactive Tutorial." (CONTRIBUTING)

---

## Cross-list patterns for this archetype

1. **Decision metadata is the product.** Each list standardizes the 2-5 facts a user needs to decide without clicking:
   - public-apis: Auth/HTTPS/CORS;
   - free-for-dev: numeric free-tier limits (59% of entries);
   - awesome-selfhosted: license, platform, ⚠ third-party dependency, Demo;
   - awesome-mac: OSS/Freeware/App Store/Native icons;
   - open-source-mac-os-apps: implementation language;
   - free-programming-books: format, license, access notes.

   Topic lists describe; directories classify.
2. **"Free" is defined operationally, with edge cases spelled out.** Free tier not trial, ≥1 year, TLS included (free-for-dev). No device purchase (public-apis). Email "requested, not required" (free-programming-books). A license allowlist that routes BUSL/SSPL/Elastic to non-free.md (awesome-selfhosted). Disputes with vendors become checkbox failures.
3. **Objective admission gates replace taste.** First release older than 4 months, working install docs, recent commits (awesome-selfhosted, open-source-mac-os-apps). Pricing visible without signup, contact details, privacy policy (free-for-dev). Canned replies make rejection cheap and polite.
4. **Two pruning styles keep size flat.** Continuous automation: awesome-selfhosted's nightly strict lint yields about 555 removal commits since mid-2023, 343 tagged "unmaintained since <date>". Owner purges: free-for-dev's eight `cleanup` PRs on 2026-01-02/03 ("Dead entries / Not free entries / Unclear pricing") and the March 2026 scope trim that deleted whole sections. awesome-selfhosted stayed at about 1.2-1.36k for 3 years; free-for-dev went 1,672, 1,273, 1,372. Lists without pruning only grow.
5. **Data-as-source plus a generated README is the mature architecture.** awesome-selfhosted (YAML + hecat; README "legacy", site "recommended") and open-source-mac-os-apps (JSON + Swift) separate data from presentation. That enables stats badges, per-facet pages, bot-refreshed stars and update dates, and multiple outputs (awesome-mac also exports npm JSON and RSS). The price is contributor friction.
6. **Anti-self-promotion is written as quotable, enforceable rules:** "not a marketing tool" (public-apis); "Services we do not accept… we have too many already" plus a ban-acknowledging checkbox (free-for-dev); one item per PR and "human, not LLM" (awesome-selfhosted). Open-source-only scope (awesome-selfhosted, open-source-mac-os-apps) blocks most SaaS spam by construction.
7. **2026 split the lists over AI submissions.** free-for-dev (honeypot checkbox, AGENTS.md/CLAUDE.md) and awesome-selfhosted (LLM ban, an "AI AGENTS" comment block) refuse machine-written PRs: 1 and 0 AI traces since 2025. awesome-mac ships a Codex maintainer skill (67 traces). public-apis absorbed 100+ AI-assisted commits. Both camps now embed agent-directed instructions in the repo itself.
8. **Commercial ownership erodes neutrality, and it is measurable.** At public-apis, APILayer removed the maintainers block and overrode a founder-era maintainer's reverts (March 2022). Four near-silent years followed, then a 2026 flood merged by a single agency identity (869/874 merges). The body now holds about 18 sponsor-family rows, utm links, and a sponsor MCP pinned out of order, and alphabetical inversions went from 0 to 55. awesome-mac repeats the pattern at smaller scale (banners above the title, undisclosed sponsor and self-authored apps). Non-profit stewardship (free-programming-books) and domain-cost-only donations (awesome-selfhosted) avoid it.
9. **Bus factor is usually 1, and owner judgment is the quality bar.** free-for-dev (95% of merges by Pienaar), awesome-mac, open-source-mac-os-apps and public-apis-2026 are each single-gatekeeper. The resilient exceptions, awesome-selfhosted (several mergers, "consensus preferable") and free-programming-books (foundation), get their resilience from automation and institutions rather than from more reviewers.
10. **Dormancy-then-flood cycles degrade consistency.** public-apis (2/6/2 commits in 2023-25, then 1,812), open-source-mac-os-apps (2 in 2024, then 482 in 2026, including Copilot-agent backlog clearing) and free-programming-books (68% of commits in October) all merge in bursts. Burst merges leave stray columns, overlong descriptions, and even a contributor's text merged as the PR template.
11. **Narrow scope is kept by delegating outward.** awesome-selfhosted sends deployment tools to awesome-sysadmin and checks staticgen/dbdb.io for duplicates. free-for-dev excludes self-hosted software and toolboxes and links each cloud's official free-tier page. free-programming-books excludes blogs, articles and channels. Narrow scope is what keeps 1-2k-entry directories usable.
12. **Multilingual reach is a structural choice with a maintenance tax.** free-programming-books makes language a top-level axis (40+ languages per genre, translated docs, an RTL linter) but has near-empty files. awesome-mac keeps 4 parallel READMEs and drifts (KO 913 vs EN 1,434). The English-only lists skip the tax.
13. **Off-GitHub reading surfaces become essential above about 1,000 entries.** free-for.dev (docsify), awesome-selfhosted.net, the free-programming-books static and search sites, and awesome-mac's idoc site and RSS. public-apis dropped its alternative-site links and live badges after 2022. Directories are looked up, not read.
14. **Link-rot handling: repair beats deletion, and checks need triage.** free-programming-books uses Wayback `archived` links and http fallbacks. awesome-selfhosted documents about 75 false-positive exclusions instead of disabling checks, and triages through rolling issue #1. public-apis runs a nightly checker with no visible follow-up, and free-for-dev has none at all; both rely on periodic manual sweeps.
