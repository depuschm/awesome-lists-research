# Same-topic rivalries: a natural experiment

**Question.** Many topics have several awesome lists with the same scope, yet one of them has 2x to 70x the stars of the others. Comparing a winner with its same-topic rivals holds topic popularity constant. That isolates the other factors: timing, the index slot, launch completeness, scope, name, entry quality, maintenance, and distribution.

**Method.**
- **Stars** come from `data/master_stars.tsv`. Four repos are missing there, so their stars were read from GitHub pages via WebFetch (rounded): punkpeye/awesome-mcp-servers 96.8k, wong2/awesome-mcp-servers 4.4k, ComposioHQ/awesome-claude-skills 77.8k, jqueryscript/awesome-claude-code 534.
- **Repo metrics** come from `scripts/extract.py` on the local clones:
  - first commit, current entry count, `desc_ratio`, authors, commits in the last 365 days, days since the last commit.
- **Launch quality** was measured by counting entries in the README at +7, +30, +90 and +365 days after the first commit, and on the date each rival launched.
  - The helper script for this is in my scratchpad; it reuses `extract.scan_entries`.
  - I also read early README versions with `git show`.
- **Index history** comes from `git log -S` on the `sindresorhus__awesome` clone.
- "Days after earliest" is measured from the earliest first commit among the rivals shown.

**Caveats.**
- Stars are a snapshot from Oct 2026. There is no star time series, so "overtook" means "is ahead now".
- The sample is survivor-biased. Rivals that died with almost no stars, or were deleted, are invisible. Because of this, first-mover win rates are probably overstated.
- Entry counts are script-based. They undercount heading-style and table-style READMEs (early Hack-with-Github, early hesreallyhim, early public-apis), so I recounted those by hand where noted.

---

## Overview

| Topic | Winner | Best same-scope rival | Winner/rival stars | Earliest list won? | Lead of earliest (days) |
|---|---|---|---|---|---|
| Python | vinta/awesome-python | lukasmasuch/best-of-python | 72x | yes | 410 (vs uhub) |
| macOS apps | jaywcjlove/awesome-mac | serhii-londar/open-source-mac-os-apps | 2.3x | **no** (iCHAIT first) | 419 |
| React | enaqx/awesome-react | brillout/awesome-react-components | 1.5x | yes | 638 |
| ML / DL | josephmisiti/awesome-machine-learning | ChristosChristofidis/awesome-deep-learning | 2.6x | yes | 171 |
| MCP servers | punkpeye/awesome-mcp-servers | appcypher/awesome-mcp-servers | 17x | **no** (3rd of 3) | 1.7 |
| Claude Code | hesreallyhim/awesome-claude-code | ccplugins/awesome-claude-code-plugins | 57x | yes | 85 |
| Claude Skills | ComposioHQ/awesome-claude-skills | VoltAgent/awesome-agent-skills | 2.1x | **no** (travisvn first) | 0.5 |
| iOS + Swift | vsouza/awesome-ios; matteocrippa/awesome-swift | ivanvorobei/awesome-ios; Wolg/awesome-swift | 32x; 4.5x | yes; yes | 1,787; 2 |
| Hacking / pentest | Hack-with-Github/Awesome-Hacking | enaqx/awesome-pentest | 4.5x | **no** | 605 |
| Design tools | goabstract/Awesome-Design-Tools | gztchan/awesome-design | 2.4x | **no** | 888 |
| Self-hosted | awesome-selfhosted/awesome-selfhosted | mikeroyal/Self-Hosting-Guide | 14x | yes | 1,540 |
| Public APIs | public-apis/public-apis | public-api-lists/public-api-lists | 30x | yes | 299 |

The ratio splits cleanly by rival type:
- **Head-on clones** with the same scope get 1–7% of the winner's stars: Python, Claude Code, iOS, APIs, MCP, Self-hosted.
- **Differentiated neighbours** get 40–65%: React components, deep learning, open-source macOS apps, agent skills.

---

## 1. Python

| Repo | Stars | First commit | Days after earliest | Entries now | desc_ratio | Authors | Commits 365d | Days since last | In index |
|---|---|---|---|---|---|---|---|---|---|
| vinta/awesome-python | 329,772 | 2014-06-27 | 0 | 552 | 0.96 | 588 | 1,483 | 2 | yes (day 14) |
| lukasmasuch/best-of-python | 4,600 | 2021-01-11 | 2,390 | 808 | 0.22* | 18 | 85 | 2 | no |
| DjangoEx/awesome-python-resources | 1,500 | 2022-05-06 | 2,870 | 334 | 0.00 | 62 | 3 | 8 | no |
| uhub/awesome-python | 1,200 | 2015-08-12 | 410 | 1,843 | 0.96 | 3 | 15 | 28 | no |

\* best-of entries keep their descriptions inside `<details>`, so the script undercounts them.

- **The earliest, and complete from week one.** vinta had 370 entries 7 days after its first commit and 484 at +30 days.
  - It is one of the 8 lists in the first commit of sindresorhus/awesome (2014-07-11), so it predates the index.
  - matteocrippa/awesome-swift's launch line reads "inspired by awesome-python". vinta was the template others copied.
- **The bigger rival lost.** uhub launched 410 days later with 869 entries, more than vinta's 632 on that date, and grew to 1,634 within a year.
  - Its entries are `owner/repo` plus the GitHub description copied verbatim.
  - 120 of its 152 commits are a monthly "update" by the account `uhub`, and it has 3 authors in total. It is a scraper with no community, and it has 1,200 stars.
- **The better product arrived too late.** best-of-python is genuinely novel: projects ranked by a quality score and refreshed weekly, with 577 entries at launch. It arrived 6.5 years late and has 1.4% of the stars.
- **DjangoEx** removed its descriptions on day 1 ("remove additional descriptions"), giving desc_ratio 0.00. Its scope is "Python resources for each field of CS", which blurs what the list is for.
- **The winner kept investing.** It added an MkDocs website in 2015, now at awesome-python.com, and made 1,483 commits in the last year. It now sells sponsor slots ("The #10 most-starred repo on GitHub").

## 2. macOS apps (overtaking case)

| Repo | Stars | First commit | Days after earliest | Entries now | desc_ratio | Authors | Commits 365d | Days since last | In index |
|---|---|---|---|---|---|---|---|---|---|
| jaywcjlove/awesome-mac | 117,000 | 2016-07-17 | 419 | 1,493 | 0.96 | 1,028 | 1,008 | 0 | yes (sub-entry, 2018) |
| serhii-londar/open-source-mac-os-apps | 51,000 | 2017-11-03 | 892 | 1,317 | 1.00 | 586 | 492 | 3 | yes (sub-entry, 2018) |
| iCHAIT/awesome-macOS | 19,400 | 2015-05-25 | 0 | 330 | 0.89 | 200 | 74 | 4 | **held the macOS slot 2015-09 → removed 2022-03** |

- **The pioneer launched empty and then stalled.**
  - iCHAIT had 4 entries for its first 30 days and 34 at +90 days.
  - After a 2015 burst (428 commits), activity fell to 35, 32 and 42 commits a year in 2017–19.
  - Entries sat between 237 and 294 from mid-2016 to 2025.
  - The index removed it on 2022-03-07 with the message "Remove macOS list. It's badly maintained."
- **The challenger launched complete, in another language, off an existing audience.**
  - jaywcjlove had 330 entries in its first week, against iCHAIT's 252 on the same date.
  - The first README was Chinese. Its intro says the list exists because "I recently published a fairly viral WeChat article ('The tool-armed front-end engineer')", and the repo is its continuously updated companion.
  - English followed within 4 days (2016-07-21/22). The stated audience is "developers and designers".
- **Format was copied, so it was not a moat.** jaywcjlove reused iCHAIT's legend convention: the `[OSS Icon]` / `[Freeware Icon]` reference labels, with its own SVGs.
- **Sustained maintenance.** jaywcjlove made 91–501 commits in every year since 2016, and 964 so far in 2026.
  - Entries grew from 429 (2016) to 1,382, with ja/ko/zh READMEs and split-out files for CLI apps and editor plugins.
- **The pioneer lost twice.** serhii-londar arrived 892 days later with a narrower scope (open source only) and a JSON-backed README (`applications.json` generates it). It still has 2.6x the stars of the pioneer.

## 3. React

| Repo | Stars | First commit | Days after earliest | Entries now | desc_ratio | Authors | Commits 365d | Days since last | In index |
|---|---|---|---|---|---|---|---|---|---|
| enaqx/awesome-react | 75,000 | 2014-08-06 | 0 | 149 | 0.88 | 672 | 28 | 51 | yes (day 26) |
| brillout/awesome-react-components | 48,700 | 2016-05-05 | 638 | 564 | 0.99 | 291 | 31 | 271 | no |
| lukasmasuch/best-of-react | 1,100 | 2021-02-21 | 2,391 | 713 | 0.23* | 10 | 0 | 423 | no |

- **First, fast, and in the index.** enaqx went from 74 to 357 entries in the first month and entered the index on 2014-09-01, 26 days after launch.
- **The strong rival is a complement, not a clone.** brillout covers components only and is explicitly opinionated: "it's NOT a comprehensive list… not super popular and well-known… no point in listing those." A different question earns 65% of the winner's stars rather than 2%.
- **The lead survived radical pruning.** enaqx went from 960 entries (2019-04) to 542 (2019-10) to 144 (2023-10), and has 149 now. Stars did not follow the entry count.
- **The late automated product failed again.** best-of-react (ranked, auto-updated) arrived 6.5 years late; it got 1.1k stars and has had no commits since 2025.

## 4. Machine learning / deep learning

| Repo | Stars | First commit | Days after earliest | Entries now | desc_ratio | Authors | Commits 365d | Days since last | In index |
|---|---|---|---|---|---|---|---|---|---|
| josephmisiti/awesome-machine-learning | 75,000 | 2014-07-15 | 0 | 1,254 | 0.95 | 757 | 110 | 2 | yes (day 124) |
| ChristosChristofidis/awesome-deep-learning | 29,100 | 2015-01-02 | 171 | 607 | 0.32 | 147 | 0 | 516 | yes (2015-06) |
| ujjwalkarn/Machine-Learning-Tutorials | 18,300 | 2015-09-12 | 424 | 485 | 0.05 | 37 | 0 | 1,847 | yes (nested) |

- **Launch completeness at matched age.** At +30 days josephmisiti had 453 entries; Christos had 103 and ujjwalkarn 53.
- **A crisp organizing rule.** The tagline promises "frameworks, libraries and software (by language)" and the first section was Python → NLP. Christos mixes numbered books, courses, videos and papers with desc_ratio 0.32. ujjwalkarn is mostly bare tutorial links (0.05).
- **Maintenance gap.** josephmisiti has made at least 76 commits in every year for 12 years. Christos has made 2 commits since 2022, and ujjwalkarn none since 2021.
- **The index did not decide this one.** All three hold index slots. The 2.6x gap is the "differentiated neighbour" ratio: deep learning and tutorials are adjacent scopes.

## 5. MCP servers (near-simultaneous launch; third mover won)

| Repo | Stars | First commit (UTC) | Days after earliest | Entries now | desc_ratio | Authors | Commits 365d | Days since last | In index |
|---|---|---|---|---|---|---|---|---|---|
| punkpeye/awesome-mcp-servers | 96,800 | 2024-11-30 05:03 | 1.7 | 4,648 | 0.98 | 4,508 | 11,312 | 1 | no |
| appcypher/awesome-mcp-servers | 5,800 | 2024-11-28 23:53 | 0.5 | 205 | ~1.0** | 139 | 1 | 172 | no |
| wong2/awesome-mcp-servers | 4,400 | 2024-11-28 12:27 | 0 | 539 | 0.99 | 378 | 21 | 104 | no |

\** appcypher puts an icon `<img>` before each link, which the parser reads as 0.10.

- **All three launched 3–5 days after MCP's announcement** (2024-11-25), under the same repo name.
- **The winner copied the runner-up.** punkpeye's launch intro is word for word the intro appcypher had committed about 27 hours earlier: "MCP is an open protocol that enables AI models to securely interact with local and remote resources… This list focuses on production-ready and experimental MCP servers…". It also used the same emoji-category ToC.
- **Velocity.** Entries at +7, +30 and +90 days were 86 / 170 / 202 for punkpeye, against 59 / 73 / 85 for appcypher and 32 / 67 / 75 for wong2. By 2025-06 it was 661 against 161 and 349.
- **Community and distribution machinery, built in week 1.**
  - A Chinese README on 2024-12-05.
  - Discord and r/mcp links on 2024-12-06.
  - A merge-everything workflow: 5,527 merge commits and 4,508 authors.
  - A bot comment on every merged PR inviting the author into the Discord with a "server-author" flair.
  - A `check-glama.yml` workflow tying entries to the owner's glama.ai directory.
  - The effect is that every MCP server author has a reason to submit, and to star.
- **The rivals throttled themselves.** wong2 posted "We do not accept PRs. Please submit your MCP on the website" on 2025-09-21. appcypher has been dormant since mid-2025, with 1 commit in the last year.
- **Footnote: YuzeHao2023/Awesome-MCP-Servers (1.1k).** Its real first commit is 2025-11-06. On 2025-12-23 it added 3,489 back-dated commits titled "真实贡献" ("real contribution") plus a commit named "Add realistic commit history for 1400 days". Fake activity did not buy stars.

## 6. Claude Code

| Repo | Stars | First commit | Days after earliest | Entries now | desc_ratio | Authors | Commits 365d | Days since last | In index |
|---|---|---|---|---|---|---|---|---|---|
| hesreallyhim/awesome-claude-code | 56,400 | 2025-04-19 | 0 | 253 | 1.00 | 18 | 1,973 | 0 | yes (day 53) |
| ccplugins/awesome-claude-code-plugins | 986 | 2025-10-13 | 176 | 295 | 0.30 | 158 | 283 | 73 | no |
| jqueryscript/awesome-claude-code | 534 | 2025-07-13 | 85 | 757 | 1.00 | 1 | 82 | 9 | no |

- **The winner launched almost empty.** The first README held 3 links, two of them the author's own toy commands (`/say-hello`, `/say-goodbye`: "A simple hello-world command that prints 'Hello, world!'"). That is the weakest launch in this study.
- **The rival launched stronger and still lost 100x.** jqueryscript had 82 entries in week 1 and 143 at +30 days, more than hesreallyhim at the same age. It now has 757 entries, all described. But it has one author, the header promotes the author's own blog post ("Read my article… 7 Best CLI AI Coding Agents"), and its star counts are static.
- **What the winner had.**
  - It was first, about 8 weeks after Claude Code's preview.
  - It got the index slot "Claude Code" on 2025-06-11.
  - Its daily activity is visible: 2,229 commits, 1,823 of them by github-actions. Submissions go through an issue-form pipeline, with a CSV as the single source of truth since 2025-06-30 and a regenerated README.
  - Curation is openly selective: "the point of an Awesome List is to be *selective*".
- ccplugins narrows the scope to plugins (it ships a `.claude-plugin` directory) and is 176 days late.

## 7. Claude Skills (first mover lost within hours)

| Repo | Stars | First commit (UTC) | Days after earliest | Entries now | desc_ratio | Authors | Commits 365d | Days since last | In index |
|---|---|---|---|---|---|---|---|---|---|
| ComposioHQ/awesome-claude-skills | 77,800 | 2025-10-17 09:09 | 0.5 | 178 | 0.99 | 30 | 75 | 93 | no |
| VoltAgent/awesome-agent-skills | 36,300 | 2025-10-28 | 12 | 1,170 | 0.99 | 251 | 834 | 1 | no |
| travisvn/awesome-claude-skills | 15,500 | 2025-10-16 20:42 | 0 | 54 | 0.80 | 2 | 22 | 179 | no |

- **Same day as the topic's launch.** travisvn launched on the day Agent Skills was announced; ComposioHQ followed about 12 hours later.
- **The winner borrowed the first mover's words.** ComposioHQ's GitHub About line is travisvn's launch tagline word for word: "A curated list of awesome Claude Skills, resources, and tools for customizing Claude AI workflows".
- **Content beats links.** ComposioHQ ships the skills themselves: 864 `SKILL.md` files across about 30 folders. Some folders mirror the names of Anthropic's official skills (`document-skills`, `skill-creator`, `mcp-builder`). travisvn is links only.
- **Company distribution.** ComposioHQ's banner links to Composio signup with `utm_medium=Youtube`. VoltAgent (also company-backed) arrived 12 days late with a broader cross-assistant scope and 1,170 entries, and already has 2.3x the first mover's stars.
- **Curation effort is not what won.** ComposioHQ has 77 commits and 178 entries in total; VoltAgent has 834 commits in the last year. The ranking follows brand plus usable content, not work.

## 8. iOS and Swift (two pairs, both launched July 2014)

| Repo | Stars | First commit | Days after earliest (in pair) | Entries now | desc_ratio | Authors | Commits 365d | Days since last | In index |
|---|---|---|---|---|---|---|---|---|---|
| vsouza/awesome-ios | 53,800 | 2014-07-10 | 0 | 1,867 | 0.96 | 1,033 | 37 | 58 | yes (day 2) |
| ivanvorobei/awesome-ios | 1,700 | 2019-06-01 | 1,787 | 160 | 1.00 | 14 | 0 | 1,329 | no |
| *dkhamsing/open-source-ios-apps (different scope)* | *52,800* | *2015-01-26* | *200* | *1,972* | *0.40* | *471* | *998* | *0* | *no* |
| matteocrippa/awesome-swift | 26,300 | 2014-07-10 | 0 | 1,113 | 1.00 | 751 | 91 | 1 | yes (day 2) |
| Wolg/awesome-swift | 5,900 | 2014-07-12 | 2.1 | 177 | 0.98 | 85 | 2 | 223 | no |

- **Five weeks after Swift's announcement.** vsouza and matteocrippa were both created on 2014-07-10. Both were added to the index on 2014-07-12 (commit "moar lists"), when they were two days old.
- **A 2-day head start decided the Swift slot.** Wolg launched 2.1 days after matteocrippa, after the index had already chosen.
  - At +30 days it was 74 entries against Wolg's 40.
  - Wolg then stalled: 131 commits in 2015, 13 in 2016.
  - matteocrippa did 835 and 988 commits in 2015–16.
- **Distribution hustle from day one.** matteocrippa's launch line already says "listed on awesome-awesomeness", the other index of the time.
- **A late, polished rival.** ivanvorobei launched 5 years late with GIF previews and 179 entries, then was abandoned in 2022.
- **dkhamsing nearly ties vsouza** by answering a different question: apps with source code, rather than libraries. It is also far more active (998 vs 37 commits a year). Differentiated scope can match a winner; a same-scope clone cannot.

## 9. Hacking / pentest (overtaking case)

| Repo | Stars | First commit | Days after earliest | Entries now | desc_ratio | Authors | Commits 365d | Days since last | In index |
|---|---|---|---|---|---|---|---|---|---|
| Hack-with-Github/Awesome-Hacking | 123,467 | 2016-03-30 | 605 | 83 | 0.98 | 38 | 15 | 91 | no |
| enaqx/awesome-pentest | 27,500 | 2014-08-03 | 0 | 593 | 0.93 | 153 | 24 | 92 | no |
| carpedm20/awesome-hacking | 17,300 | 2014-12-16 | 135 | 191 | 0.64 | 82 | 0 | 1,053 | yes ("Hacking", 2015-06) |

- **The challenger moved up one abstraction level.**
  - Hack-with-Github is "A collection of awesome lists for hackers, pentesters & security researchers": a security index of lists.
  - It had about 20 sub-lists within its first month (in heading format, which the script misses).
  - It lists both rivals as entries ("Hacking", "Pentest"), so it sits upstream of them.
- **Distribution.** It is an organization-branded account with Twitter and Facebook (@HackwithGithub) and a pre-filled Tweet button in the header. carpedm20's README even points readers to Hack-with-Github's Free-Security-eBooks repo.
- **Minimal curation, no index slot, biggest stars.** It has 141 commits, 83 entries and 38 authors in 10 years, and 4.5x enaqx's stars. It is the clearest case of positioning plus distribution beating effort.
- **The incumbents stalled early.** carpedm20 stayed at 65 entries for its first 18 months (+7 days through +365 days) and has made no commits since 2023. Its tagline is vague: "A curated list of awesome Hacking."

## 10. Design tools (overtaking case)

| Repo | Stars | First commit | Days after earliest | Entries now | desc_ratio | Authors | Commits 365d | Days since last | In index |
|---|---|---|---|---|---|---|---|---|---|
| goabstract/Awesome-Design-Tools | 41,600 | 2019-02-12 | 888 | 603 | 0.99 | 237 | 0 | 2,217 | no |
| gztchan/awesome-design | 17,700 | 2016-09-07 | 0 | 431 | 0.58 | 58 | 0 | 1,958 | no |

- **The incumbent froze in its second year.** gztchan launched with 385 entries in week 1, then made 145 commits in 2016, 40 in 2017 and 1 in 2018. Entries stayed between 431 and 459 from 2017 on.
- **The challenger was a team burst.**
  - Lisa Dziuba's Flawless App team made 1,508 commits in 2019 alone, from three or four core committers with 170–400 commits each.
  - It reached 509 entries by +90 days.
  - Every entry is described (0.99), many with free and open-source badges.
  - Plugins, UI kits and conferences are split into separate files, with a landing page on flawlessapp.io. The repo later "joins Abstract", hence the goabstract org.
- **Sharper question.** "Tools", meaning which tool for task X, versus gztchan's "resources and tools which can be used by UI/UX designers", which mixes stock photos, logo galleries and inspiration sites (desc_ratio 0.58).
- **The lead locked in during 2019.** Both lists have been frozen since 2020–21, and the 2.4x gap persists.

## 11. Self-hosted

| Repo | Stars | First commit | Days after earliest | Entries now | desc_ratio | Authors | Commits 365d | Days since last | In index |
|---|---|---|---|---|---|---|---|---|---|
| awesome-selfhosted/awesome-selfhosted | 329,734 | 2015-06-01 | 0 | 1,365 | 0.95 | 1,367 | 254 | 2 | yes (day 23) |
| mikeroyal/Self-Hosting-Guide | 23,300 | 2022-02-06 | 2,443 | 2,657 | 0.76 | 21 | 0 | 485 | no |
| Atarity/deploy-your-own-saas | 10,100 | 2019-08-19 | 1,540 | 151 | 0.99 | 35 | 249 | 0 | no |

- **First mover, institutionalized.**
  - It started under Kickball in 2015 and was in the index within 23 days.
  - It has made 200–930 commits a year for 12 years.
  - It moved to an org, has an HTML site (awesome-selfhosted.net, now "recommended"), and keeps a separate data repo with dead-link checks.
  - Its scope is strict: "Free Software network services and web applications", with proprietary software split into `non-free.md`.
- **A huge late launch could not dent it.** mikeroyal launched with 957 entries (now 2,657 in a 589 KB README), but it is a one-person guide that went dead in 2024: its maintenance badge is stuck at "yes/2024". It has 7% of the winner's stars.
- **Re-framing earns a niche.** Atarity's "Deploy your own X" framing, with star counts and freshness emoji, is actively maintained and has 3%.

## 12. Public APIs

| Repo | Stars | First commit | Days after earliest | Entries now | desc_ratio | Authors | Commits 365d | Days since last | In index |
|---|---|---|---|---|---|---|---|---|---|
| public-apis/public-apis | 491,697 | 2016-03-20 | 0 | 2,244 | 0.99 | 2,103 | 1,813 | 1 | no |
| public-api-lists/public-api-lists | 16,200 | 2020-01-05 | 1,386 | 843 | 0.99 | 347 | 248 | 41 | no |
| TonnyL/Awesome_APIs | 13,200 | 2017-01-13 | 299 | 315 | 0.94 | 37 | 0 | 2,452 | no |
| marcelscruz/public-apis (fork) | 9,600 | 2022-05-11 (diverged) | 2,242 | 1,903 | 1.00 | 2,027 | 1,416 | 0 | no |

- **A viral launch.** Todd Motto's list ("A collective list of JSON APIs for use in web development") had 90 table rows within 8 days, and PR #49 was merged by day 3. It has never been in the index.
- **The position held through neglect and commercialization.** Commits fell to 2 in 2023, 6 in 2024 and 2 in 2025. The README now opens with an APILayer product ad. It is still the #3 repo in the corpus.
- **Rivals formed out of frustration and got about 3%.**
  - public-api-lists launched as "Forked from public-apis" and imported public-apis' open PRs on day 2. That gave it 740 entries at launch, more than public-apis had that day.
  - marcelscruz forked after the APILayer takeover (diverging 2022-05-11). It now has 1,416 commits a year and 2,027 authors.
  - Better maintenance plus identical content did not recapture stars.
- TonnyL (bilingual, Open Collective) was abandoned by 2020.

---

## Extended sample: 12 quick-check pairs

These pairs use only first commit, stars and index status; I did no deep read.

| Topic | Earlier list (stars, first commit) | Later rival (stars, first commit) | Earlier won? | Note |
|---|---|---|---|---|
| CLI apps | agarrharr/awesome-cli-apps (20.6k, 2015-07) | toolleeo/awesome-cli-apps-in-a-csv (2.7k, 2017-02) | yes | the later list is CSV-backed and more active (468 vs 151 commits/yr) |
| Kubernetes | ramitsurana/awesome-kubernetes (15k, 2015-10) | tomhuang12/awesome-k8s-resources (4.2k, 2020-07) | yes | |
| Java | akullpp/awesome-java (49.3k, 2014-07) | Vedenin/useful-java-links (6.2k, 2016-02) | yes | |
| Go | avelino/awesome-go (190k, 2014-07) | uhub/awesome-go (1.8k, 2015-08) | yes | uhub is the same scraper as uhub/awesome-python |
| Android | JStumpp/awesome-android (12.4k, 2014-07-13) | wasabeef/awesome-android-ui (58.1k, 2014-12-24) | **no** | narrower UI-only scope, 216 GIF previews, 108 vs 92 entries on its launch date |
| ChatGPT prompts | f/awesome-chatgpt-prompts (172k, 2022-12) | ai-boost/awesome-prompts (9.1k, 2024-01) | yes | |
| Design systems | alexpate/awesome-design-systems (26.2k, 2017-06) | klaufel/awesome-design-systems (885, 2020-04) | yes | **the later list holds the index slot (2021)** |
| React Hooks | rehooks/awesome-react-hooks (10.3k, 2018-10-25 21:38 UTC) | glauberfc/awesome-react-hooks (1.2k, 21:46 UTC) | yes (by 8 min) | launched the day Hooks were announced, both with 44 entries at +7 days; rehooks was started by James Kyle (thejameskyle); glauberfc got the index slot in 2019-05 and still trails 9x |
| Privacy | pluja/awesome-privacy (20.1k, 2020-12) | Lissy93/awesome-privacy (10k, 2022-07) | yes | the later list launched with 525 entries (vs 428), from a well-known author with a website and API, and is far more active (723 vs 58 commits/yr) |
| Docker | veggiemonk/awesome-docker (37.1k, 2014-09) | Friz-zy/awesome-linux-containers (1.6k, 2015-08) | yes | |
| Interview Qs | DopplerHQ/awesome-interview-questions (85.2k, 2015-11) | Chalarangelo/30-seconds-of-interviews (12.1k, 2018-04) | yes | |
| Free tiers | ripienaar/free-for-dev (140k, 2015-03) | hilmanski/freeStuffDev (2k, 2024-02) | yes | |

---

## Synthesis

### First-mover win rate

- **Main 12 topics:** the earliest list won in **7 of 12 (58%)**.
  - The losses are macOS, MCP, Claude Skills, Hacking and Design.
  - Two of those losses (MCP, Skills) were launches less than 2 days apart, effectively ties. Excluding them, the first mover won **7 of 10 (70%)**.
- **With the 12 quick checks:** **18 of 24 (75%)**.
  - The quick-check rivals are mostly weak, and survivorship bias inflates this number. Treat about 70% as an upper-middle estimate.
- **Near-simultaneous launches are a coin flip.** There are four cases with gaps under 2 days: MCP, Skills, Swift and React Hooks. The literal first mover won only 2. When everyone arrives within hours of a topic's birth, distribution decides, not timing:
  - punkpeye's community machinery,
  - Composio's company channel,
  - James Kyle's personal reach (rehooks),
  - matteocrippa's day-one submission to both indexes.
- **The real timing variable is "near the topic's big bang", not "before the rival".**
  - Winners launched within days or weeks of the topic's birth: Swift and iOS within 5 weeks of WWDC 2014; MCP within 5 days of its announcement; Skills and Hooks on announcement day; Claude Code within 8 weeks of the preview; Python, React, ML, Go and Java in the mid-2014 "awesome" wave.
  - The overtakers came 400–900 days late, but into a field where the incumbent had stalled.

### Factors ranked by how often they separate winner from rival (12 main topics)

| Rank | Factor | Separates winner from main rival | Counterexamples / caveats |
|---|---|---|---|
| 1 | **Activity in the formative 1–2 years** | 10/12. The winner out-committed rivals early in every topic except Hacking and Skills (ComposioHQ has 77 commits in total; VoltAgent has 834 in a year). Examples: jaywcjlove 501/352 vs iCHAIT 255/35; goabstract 1,508 in 2019 vs gztchan 15; matteocrippa 835/988 vs Wolg 131/13; punkpeye 11k+ vs ~200. | Partly endogenous, since stars bring PRs. Highly active late rivals do **not** overtake a live incumbent: marcelscruz 1,416/yr, Lissy93 723/yr, toolleeo 468/yr. Late-life dormancy does not cost the lead (public-apis 2023–25; goabstract frozen since 2020). |
| 2 | **Timing: present at the topic's birth** | 9/12 (first, or within 2 days of first). | The three non-early winners (macOS, Hacking, Design) all overtook an incumbent that stalled within 18 months. |
| 3 | **Distribution / brand / external audience** | about 6/12, and **5 of the 5 overtakes**: WeChat article (jaywcjlove), Glama, Discord and Reddit (punkpeye), Composio (Skills), @HackwithGithub social accounts, Flawless App/Abstract team. | Hard to measure offline. It never rescued a same-scope clone against a maintained incumbent (Lissy93 vs pluja). |
| 4 | **Scope clarity / differentiation** | about 6/12 (goabstract "tools" vs "resources"; josephmisiti "by language"; Hack-with-Github one level up; serhii-londar OSS-only). | Differentiation mostly creates **coexistence** (40–65% of the winner's stars), not victory: brillout, Christos, serhii-londar, VoltAgent, dkhamsing. |
| 5 | **Index slot** | 5/12 (only the winner holds it: Python, React, Claude Code, iOS/Swift, Self-hosted). | It follows timing: slots were granted 2–53 days after launch. Holders lost in Hacking (carpedm20) and macOS (iCHAIT), and in the quick checks glauberfc and klaufel hold slots but trail 9x and 30x. 5 of the 12 topic winners never held one: public-apis, Hack-with-Github, punkpeye, ComposioHQ, goabstract. |
| 6 | **Launch completeness at matched age** | 5/12 (macOS, ML, MCP, Swift, Skills). | Big late launches lost every time against a live incumbent: uhub 869 vs vinta 632, public-api-lists 740 vs 682, mikeroyal 957, Lissy93 525 vs 428, best-of-python 577. hesreallyhim won after launching with 3 toy links. |
| 7 | **Entry description quality** | about 4/12 (ML 0.95 vs 0.32/0.05; Design 0.99 vs 0.58; Hacking 0.98 vs 0.64; DjangoEx 0.00). | It matters only against weak rivals. Many losers score 0.99–1.00: marcelscruz, jqueryscript, Atarity, public-api-lists, ivanvorobei, serhii-londar. |
| 8 | **Repo name** | 0/12. 7 of the 12 topics had **identical** repo names (awesome-python, awesome-ios, awesome-swift, awesome-mcp-servers ×3, awesome-claude-code, awesome-claude-skills, Awesome-Hacking). | An org-style namespace (public-apis/, awesome-selfhosted/, Hack-with-Github/, ComposioHQ/, rehooks/) shows up among winners, but it is a brand signal, not a name effect. |

### The overtaking cases: what they share

There are four overtakes with a real lead (macOS, Hacking, Design, Android UI) and two near-tie overtakes (MCP, Skills). The same three-part recipe recurs:

1. **The incumbent stalled early, not late.**
   - iCHAIT: 4 entries for a month, then 35 commits a year from 2017.
   - carpedm20: 65 entries for 18 months.
   - gztchan: frozen in 2017.
   - travisvn: 54 entries.
   - wong2 and appcypher: PRs closed or dormant within 10 months.
   - No list in this sample was overtaken after it had sustained activity through its first two years.
2. **The challenger offered a different product, not a better copy.**
   - Chinese-first, for developers and designers (jaywcjlove).
   - Open-source-only with JSON data (serhii-londar).
   - A list of lists (Hack-with-Github).
   - "Tools", every entry described, badges (goabstract).
   - UI-only with GIF previews (wasabeef).
   - Installable skill files instead of links (ComposioHQ).
   - A submission and community flywheel (punkpeye).
3. **The challenger brought an audience.** This holds in every overtake (see factor 3).

The inverse is just as consistent. Six late, same-scope entrants each launched bigger, fresher or better-maintained than the incumbent, and each got 1–7% of its stars:
- uhub/awesome-python
- best-of-python
- public-api-lists
- marcelscruz/public-apis
- mikeroyal/Self-Hosting-Guide
- Lissy93/awesome-privacy

**A head-on clone does not beat a live incumbent.**

### Other regularities

- **Size is not the product.** In 6 of the 12 topics a rival has more entries than the winner:
  - uhub 1,843 vs vinta 552
  - brillout 564 vs enaqx 149
  - jqueryscript 757 vs hesreallyhim 253
  - VoltAgent 1,170 vs ComposioHQ 178
  - enaqx/awesome-pentest 593 vs Hack-with-Github 83
  - mikeroyal 2,657 vs awesome-selfhosted 1,365
  - Winners often prune instead (enaqx 960 → 149) and lose nothing.
- **Copying is common and is not punished.**
  - punkpeye took appcypher's intro paragraph.
  - ComposioHQ's About line is travisvn's tagline.
  - jaywcjlove reused iCHAIT's OSS/Freeware legend.
  - public-api-lists cloned public-apis' content.
  - Formats and wording are not a moat; position, audience and momentum are.
- **Leads are sticky in both directions.** Winners survive:
  - radical pruning (enaqx),
  - near-dormancy (public-apis 2023–25),
  - a full freeze (goabstract since 2020),
  - commercialization (an APILayer ad atop public-apis; sponsor slots on vinta).
  - Losers do not recover with effort: marcelscruz, Lissy93 and toolleeo are all highly active, and all far behind.
- **Fake signals do not work.** YuzeHao2023 back-dated 3,489 commits to fake a 1,400-day history; it has 1.1k stars.

### Bottom line

A same-topic winner is best predicted by **being there when the topic is born and staying visibly alive for the first 18–24 months**. The index slot, complete launches and good descriptions mostly come along with that, or only matter against weak rivals. The only reliable way for a later list to win is to find an incumbent that stalled early and attack it with a *different* product backed by an *existing audience*. Better maintenance or more entries for the same thing has never been enough in this sample.
