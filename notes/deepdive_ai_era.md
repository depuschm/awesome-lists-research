# Deep dive: AI-era fast risers (2023-2026)

Analyst notes, written 2026-10-25. Sources: the local clones (README, CONTRIBUTING, `.github/`, `git log`, old README versions via `git show`). Star counts come from `data/master_stars.tsv` and `raw/EvanLi_*`; three were read from github.com via WebFetch: punkpeye 96.8k, wong2 4.4k, ComposioHQ/awesome-claude-skills 77.8k. To check first-mover claims I also cloned wong2/awesome-mcp-servers, ComposioHQ/awesome-claude-skills, jqueryscript/awesome-claude-code and pontusab/directories (cursor.directory).

**Caveat for the quant team:** in this archetype, raw commit counts mostly measure automation, not curation.
- hesreallyhim: 1,823 of 2,229 commits are `github-actions[bot]`, including 1,508 "update repo ticker" commits.
- prompts.chat: 3,160 commits in Dec 2025 came from its website-to-git sync, which writes one commit per prompt edit. "Update prompt: Code Review Assistant" alone appears 427 times.

---

## 1. hesreallyhim/awesome-claude-code (~56k stars)

**Value & scope.** Resources for Claude Code: skills, orchestrators, status lines, hooks, observability, guides. The tagline parodies awesome-list puffery ("a delectable showcase of top tier skills, ambidextrous agents, scintillating status lines... and also we have plugins"). Scope rule: resources "that focus on the unique features and functionality of Claude Code"; the issue form requires the checkbox "This resource is specific to Claude Code".

**Curation policy.** Deliberately small: 263 rows in `THE_RESOURCES_TABLE_NEW.csv`, against 4.6k in the MCP list. Hard gates:
- Age or adoption: "at least 14 days old... AND show signs of active development" OR "at least 100 stars".
- "one resource at a time".

`validate-new-issue.yml` enforces both through the GitHub API, auto-closes failures (label `auto-closed`), and even dates the true first commit ("Not repo.created_at: history pushed to a fresh repo predates it").

The list was reset in 2026. On 2026-04-27 the README became "Update in progress" ("The old ways have come and gone"). The relaunch (`4f91064`, "release - renovation", 2026-07-02) shipped a list "deliberately selected to be non-overlapping with the previous list", and 226 legacy rows were frozen in `README_ALTERNATIVES/`. Pruning also shows up in commits ("remove inactive resource", "remove stale resources") and in an `Active` flag in the CSV (11 FALSE).

**Entry format.** `[Name](link) by [Author](link) - description` plus four shields badges (created-at, last-commit, license, stars). Descriptions are long (mean 264 characters) and often first-person and evaluative: "Hints of Rumsfeld epistemology, but otherwise it's a great piece". Entries are alphabetical within sections, hard-coded in `config.yaml`.

**Navigation.** 30 sections plus subsections. Some track community memes ("Agent Orchestration > Ralph Wiggum"); "From Anthropic" is `submittable: false`. Extras: a "Claude Code Ticker" SVG refreshed every 3 hours, a "Recently Added" carousel, and before the renovation a "Pick Your Style" switcher (Awesome / Extra / Classic / Flat A-Z).

**Contribution & governance.** Issue-only submission: "Do not open a PR. Just fill out the form." Also: "It is **not** possible to submit a resource recommendation using the `gh` CLI." The flow:
1. A bot validates the issue.
2. The owner comments `/approve`.
3. `create_resource_pr.py` opens the PR, and the README is regenerated from the CSV.

There are 187 "Add resource:" bot commits while item numbers reach #3202, so very few submissions become entries. Bus factor is one: "Really Him" made 386 human commits and 54 of 56 merges. FUNDING.yml was removed on 2025-12-16, so there is no monetization.

Anti-spam measures go further than any other list I read:
- **Cooldown policy** (#811, Feb 2026), later escalated to "7d/14d/30d/ban". It states: "Users are personally responsible for the activity of AI agents that they have instructed".
- **OpenClaw ban:** a temporary ban on "any submissions relating to OpenClaw" after "aggressive spamming".
- **Honeypot checkbox:** "Do not check the following box... By checking this box, I admit that I am not reading any of these statements."
- **Claude review prompt.** `.claude/commands/evaluate-repository.md` (dropped in the renovation) had Claude do a static, read-only review. It scored repos 1-10, ran a Claude-Code checklist ("Hooks execute shell scripts", "Performs implicit execution without explicit confirmation"), and ended in a "Fast-Reject Heuristic".
- **Disclosure rule:** the March 2026 CONTRIBUTING required disclosing "network calls except to Anthropic servers... telemetry, or requires 'bypass-permissions' mode".

**Maintenance.** First commit 2025-04-19, 54 days after Claude Code. Slow start: 7 entries (Apr 2025), about 101 (Jun 2025), 133 (Sep 2025). 2026 runs 214-302 commits/month (mostly bot), with 51 approvals in Oct 2026.

**Secret sauce.**
1. An authorial voice: descriptions read like reviews.
2. A CSV as single source of truth with issue-form → bot-PR → regenerated-README automation. Even the maintainer doesn't hand-edit.
3. API-enforced maturity gates.
4. Security framing for executable artifacts.
5. A growth loop: `notify-on-merge.yml` opens a "🎉 Your project has been featured in Awesome Claude Code!" issue with a badge snippet on every listed repo.

**Weaknesses.** The renovation dropped 226 entries and needed explaining in both README and CONTRIBUTING. Punitive rules plus a snarky tone. Frozen legacy READMEs are still linked. Policy churn (cooldown regime Feb-Jul 2026, then removed).

**Quotes.**
- “If "getting on the list" is any part of a promotional strategy for your project, you should be prepared to have a backup plan.”
- "Although resources themselves may be partially or entirely written by a coding agent, resource recommendations must be created by human beings."
- "it's direspectful to Claude, who is supposed to be the star of the show; second of all, it is extremely obvious, and embarrassing." (COOLDOWN.md, Mar 2026, sic)

---

## 2. punkpeye/awesome-mcp-servers (~96.8k stars)

**Value & scope.** "A curated list of awesome Model Context Protocol (MCP) servers", restricted to "servers with a GitHub repo you install and run yourself". Remote-only servers go to awesome-remote-mcp-servers, clients to awesome-mcp-clients.

**Curation policy.** Mostly permissive; CONTRIBUTING is the generic fork-and-PR template. Since 2026-03-05 ("chore: automate parts of curation"), `check-glama.yml` labels each PR (`has-glama`/`missing-glama`, emoji, `invalid-name`, `duplicate`, `non-github-url`). New servers must also pass Glama checks ("start and respond to introspection requests") and show a Glama score badge. Pruning is minimal; many removal commits are merge-damage repairs ("Restore entries removed by #16032").

**Entry format.** `- [owner/repo](github) [Glama badge] 🐍 🏠 🍎 🪟 🐧 - description`. The bot enforces full `owner/repo` names and a whitelist of 15 emojis (language, scope, OS). Glama badges appear on 3,346 of 4,636 lines; 🎖️ (official) on 462. Lines average 347 characters and read like vendor copy. The alphabetical rule is loose: 898 of 4,572 adjacent pairs are out of order.

**Navigation.** 60 categories plus an emoji legend, the best scanning aid on the page. The README is 1.6 MB; "Developer Tools" alone has 558 entries and "Finance & Fintech" 490. Seven translations are stale (300-943 entries each). A synced web directory lives at glama.ai/mcp/servers.

**Contribution & governance.** A PR firehose: numbers reach #17,395, and Frank Fiegel made 5,037 of 5,527 merges (91%), plus 455 "Fix entry formatting" commits.

AI handling is unique. Since 2026-03-18, CONTRIBUTING says agents should append `🤖🤖🤖` to PR titles to be "fast-tracked". It is a real lane, not a trap:
- 1,410 merged PRs carry the tag.
- In Sep 2026 that was 472 of 893 merges, and about 37% of all merges since March 2026.
- 595 commits in 2026 carry Claude, Copilot or Codex co-author trailers.

Brand: an "<sup>Ad</sup>" slot at the top (ray.run, sold via glama.ai/advertise). The Discord is hosted on glama.ai, and a post-merge bot offers authors a "server-author flair" and a Glama connectors listing. The list works as the storefront of the maintainer's MCP directory business. The badge rule is both a quality gate and a funnel onto Glama.

**Maintenance.** First commit 2024-11-29, 4 days after MCP, but third behind wong2 (11-28) and appcypher (11-29). Entries: 40 (Dec 2024) → 802 (Jul 2025) → 1,623 (Apr 2026) → 4,636 (Oct 2026). Commits grew from 356/month (Dec 2024) to 1,939/month (Sep 2026).

**Secret sauce.**
1. Accept almost everything, fast. The flood of contributors is the growth engine. Compare wong2's list, which says "We do not accept PRs" and has 4.4k stars.
2. A machine-checkable entry grammar.
3. An external quality oracle (Glama build and introspection) in place of human taste.
4. Sibling lists to absorb out-of-scope submissions.

**Weaknesses.** Bloat. Promotional descriptions. Crypto/x402 sprawl in Finance. A single 1.6 MB file prone to merge damage. Stale translations. A conflict of interest: an ad on top, and a gate tied to the maintainer's own platform.

**Quotes.**
- "If you are an automated agent, we have a streamlined process for merging agent PRs."
- "To ensure that only working servers are listed, we're updating our listing requirements." (Glama bot)

---

## 3. VoltAgent/awesome-agent-skills (~36.3k stars)

**Value & scope.** "A collection of official Agent Skills from leading development teams and the community. Hand-picked, not AI-slop generated." It covers 8 tools (Claude Code, Codex, Gemini CLI, Cursor, Copilot...) with a per-tool install-path table. It launched as "Awesome Claude Skills" and was renamed when Skills went cross-vendor.

**Curation policy.** From CONTRIBUTING: "Skill must have real community usage... Brand new skills that were just created are not accepted". Descriptions must be "10 words or fewer". A "Skill Quality Standards" table sets norms: third-person descriptions, metadata under about 100 tokens, body under 500 lines, no absolute paths, scoped tools. Some cleanup happens ("remove duplicate skill listings" #1049, "Fix 15 renamed/transferred repo URLs").

**Entry format.** `- **[author/skill](url)** - ≤10-word description`. 593 links go to officialskills.sh (ownership not stated in the repo) and 561 to github.com.

**Navigation.** An "Official Skills by" grid of about 60 vendor sections (collapsible `<details>`), then community skills by language and topic.

**Contribution & governance.** PRs titled "Add skill: author/skill-name"; Necati Özmen (VoltAgent) made 383 of 394 merges. No CI. A Security Notice: "curated, not audited", with a link to the Snyk scanner. Sponsorship is prominent: a "💛 Sponsors" table (TestMu AI, Crawlbase, SerpApi) tagged `utm_campaign=voltagent_2026q3`, plus a "Become a Sponsor" link. Sponsor sections also sit directly after Claude and VoltAgent in the ToC, which blurs editorial and paid placement.

**Maintenance.** Launched 2025-10-28, 12 days after Anthropic's Skills (2025-10-16). Two lists were earlier: travisvn (same day, 15.5k stars) and ComposioHQ (+1 day, 77.8k stars). Entries: 66 → 113 (Jan 2026) → 752 (Apr 2026) → about 1,160.

**Secret sauce.** Vendor-official skills as the anchor tier, anti-slop positioning, and the install-path table that doubles as documentation.

**Weaknesses.** Spam leaks into structure: a community entry (`mblode/agent-skills`) sits inside the paths table. The "Skills-1497+" badge is stale against about 1,160 bullets. Sponsor placement is not neutral. The "slop" meme has become its own skill sub-genre in the list (unslop, zero-slop, slop-grader).

**Quotes.**
- "Hand-picked, not AI-slop generated."
- "Brand new skills that were just created are not accepted. Give your skill time to mature and gain users before submitting."

---

## 4. VoltAgent/awesome-openclaw-skills (~53.3k stars)

**Value & scope.** A filtered mirror of ClawHub, OpenClaw's skill registry: "Discover 5300+ community-built OpenClaw skills". It launched 2026-01-25 as awesome-clawdbot-skills, and badges and issue links still use that name.

**Curation policy.** Algorithmic, with published exclusion statistics. The Feb 28 version reads: "13,729 community-built skills... This awesome list has 5,494". The current exclusion table:

| Exclusion reason | Count |
|---|---|
| Possibly spam (bulk accounts, bot accounts, test/junk) | 4,065 |
| Duplicate / similar name | 1,040 |
| Crypto | 886 |
| Low-quality | 851 |
| Malicious | 373 |
| **Total excluded** | **7,215** |

A committed `.claude/settings.local.json` allows `Bash(python3 /tmp/categorize.py)`, which shows the categorization was done by script and agent. Rules: the skill must be on ClawHub with "tests on ClawHub... passing", must not be "flagged as suspicious", "No crypto", and "Brand new skills are not accepted". Security removals happen: "remove pr-risk-analyzer (security: token exfiltration, #594)".

**Entry format.** `- [slug](https://clawskills.sh/skills/...) - description`. Descriptions are often machine-truncated ("Automate Bitbucket repositories, pull.") or garbled ("- Neill explicitly requests Billy system repair."). Despite the no-crypto rule, "blinko" ("on-chain Plinko") is listed.

**Navigation.** The README shows a sample per category with "View all N" links into 31 `categories/*.md` files (5,209 entries). Counts disagree: 167, 159 and 160 for the same category.

**Contribution & governance.** `pr-check.yml` requires a ClawHub URL. Since 2026-02-28 ("remove clawhub links"), entries point to VoltAgent's own clawskills.sh, which the repo describes as "managed and deployed by us separately". Sponsor blocks include Cloudways with "promo code **VOLTAGENT**". Necati Özmen made about 329 of 558 commits.

**Maintenance.** 565 entries at launch → 3,002 (Feb 7) → 5,494 (Feb 28). Activity peaked at 140 commits/month in Feb-Mar 2026 and has since fallen to 22-42/month.

**Secret sauce.** Quantified "what we threw out" filtering. A registry as the upstream gate. A sampled README with full category pages.

**Weaknesses.** Machine-grade descriptions. Inconsistent counts ("5200" / "5300+" / "5,400+"). Unenforced rules. Traffic redirected to an owned domain.

**Quotes.**
- "If an author has multiple skills in the same area, please don't add them one by one."

---

## 5. VoltAgent/awesome-design-md (~123.2k stars)

**Value & scope.** DESIGN.md files (the Google Stitch format) "extracted from real websites": Claude, Vercel, Apple, BMW, Binance, a "Retro Web" set and others. The pitch: "Copy a DESIGN.md into your project, tell your AI agent 'build me a page that looks like this'". Each file is a block of YAML design tokens plus prose sections, ending in an "Agent Prompt Guide".

**Curation policy.** Closed authorship: "We cannot accept DESIGN.md pull requests to maintain the quality of the existing collection." Requests go through an issue form that asks for a delivery **email** and offers paid priority ("Yes, I'll prioritize at getdesign.md/request").

**Entry format.** `- [**Brand**](https://getdesign.md/<brand>/design-md) - category. style keywords` ("Warm terracotta accent, clean editorial layout"). 83 entries (badge says 84) in 10 categories.

**Contribution & governance.** 66 commits: 63 by Necati Özmen, 3 external. The first commit shipped 128 files and 51,549 lines (31 brands, each with DESIGN.md plus light and dark preview HTML). By 2026-04-20 the links had moved to getdesign.md, and per-brand READMEs now say "Design system details have been moved to: https://getdesign.md/...". The sponsor pitch: "Ranked #150 globally on GitHub."

**Maintenance.** Launched 2026-03-31. 31 → 54 (Apr 5) → 66 (Apr 12) → 84 entries. Near-dormant since June 2026.

**Secret sauce.** The best stars-to-effort ratio in the dataset: a new artifact type at the right moment, famous brands as content, and use that takes one copied file.

**Weaknesses.** It reproduces third-party brand design systems, which raises IP questions (one entry is a crypto casino, "1win"). There is no community authorship. Value is moving to a commercial site, and the "awesome list" label fits poorly.

**Quotes.**
- "It's just a markdown file. No Figma exports, no JSON schemas, no special tooling."

---

## 6. PatrickJS/awesome-cursorrules (~41k stars)

**Value & scope.** The repo is the rule files themselves: 257 `rules/*.mdc` Cursor Project Rules, indexed by the README. External directories (cursor.directory, CursorList) get only a two-line section.

**Curation policy.** The PR template rejects "standalone external tool, product, directory, marketplace, or service listings". Its checklist includes "The text is neutral and useful, not sales copy" and "No secrets, tokens, affiliate links, tracking links". A May 2026 overhaul ("Restructure rules: consolidate, rename, and clean files (#286)") cut 1,289 legacy files (folders with `.cursorrules` plus README) to 253 flat `.mdc` files and "Salvage[d] useful cursor rules from PR backlog".

**Entry format.** `[Framework (Variant)](link to .mdc) - one-sentence purpose`. 236 entries in 13 categories. Each `.mdc` needs `description`, `globs` and `alwaysApply` frontmatter.

**Contribution & governance.** The most security-engineered CI of the eight:
- **Account-age gate:** `check-pr-author.mjs` blocks accounts younger than 30 days.
- **Prompt-file linter:** the 919-line `check-repo-hygiene.mjs` rejects invisible Unicode and bidi overrides ("Hidden Unicode and terminal controls can conceal prompt-injection text"), credential exfiltration (`~/.ssh` or `.npmrc` combined with curl/wget), `curl | sh`, and TLS-disabling flags.
- **Issue scope:** templates exclude "license sharing, or license bypasses", which suggests a history of Cursor-piracy spam.
- **Lockdown:** CODEOWNERS pins workflows to @PatrickJS.

Three UTM-tagged sponsors (CodeRabbit, Unblocked, Warp). PatrickJS made 61 of 170 commits.

**Maintenance.** First commit 2024-09-16, 23 days after cursor.directory (2024-08-24), so not first. Bulk-seeded with 140 entries by day 2. Dormant Nov 2025-Feb 2026, then a 47-commit security and format revival in May 2026.

**Secret sauce.** The artifacts are the content, so the core value doesn't suffer link rot. It migrated to the vendor's current format. It treats prompt files as an attack surface and lints them like code.

**Weaknesses.** Long dormancy. Legacy filenames ("-cursorrules-prompt-file.mdc"). Vendor rules that read as product docs. contributing.md still holds copied sindresorhus boilerplate ("Adding an awesome list").

**Quotes.**
- "This repo trust policy blocks very fresh GitHub accounts because they are higher risk for spam, prompt-injection, promotional, and other abuse risk."

---

## 7. f/prompts.chat (formerly f/awesome-chatgpt-prompts, ~174.3k stars)

**Value & scope.** It began as "a collection of prompt examples to be used with the ChatGPT model" ("Act as a Linux Terminal"). Now: "The world's largest open-source prompt library for AI". It is a self-hostable Next.js app with a CLI, an MCP server, a Claude Code plugin and a Hugging Face dataset. Content lives in `prompts.csv` (8 MB, 2,627 prompts, median 1,038 characters); the README is 11 KB.

**Curation policy.** Light: "Test your prompt", "Be original", "Be appropriate". Trust comes from credentials at the top of the README (Forbes, Harvard/Columbia, "40+ academic citations", "Most liked dataset" on Hugging Face, Brockman and Zaremba endorsements).

**Entry format.** CSV columns `act, prompt, for_devs, type, contributor` (TEXT 2,262 / STRUCTURED 344 / IMAGE 21). A CSV existed from 2022-12-14 and a Hugging Face dataset by late Dec 2022, so the list was machine-readable from week 2. An unofficial ChatGPT desktop app imported the prompts as slash commands.

**Contribution & governance.**
- **Website-only submission.** The PR template says "Please don't edit `prompts.csv` directly!" Submissions happen on the site, and `update-contributors.yml` commits them on the user's behalf ("You'll also appear on the Contributors page"). GitHub credit becomes the reward. Side effect: 806 of 1,407 git author names, and 1,308 CSV contributor fields, are raw email addresses (a privacy weakness).
- **LLM moderation.** `spam-check.md` (2026-02-18) is a GitHub Agentic Workflow with `engine: copilot`. It closes CSV-editing PRs, prompt-submission issues, keyword-matched spam ("casino", "SEO service") and self-promotion ("my youtube", "promo code").
- **Governance on paper vs. in practice.** GOVERNANCE.md describes lazy consensus, but OWNERS.md lists a single maintainer.
- **Monetization:** a Gumroad book, a Neon sponsorship, and daily "generation credits" in the web app.

**Maintenance.** First commit 2022-12-05, 5 days after ChatGPT. humanloop's and saharmor's lists date from Dec 4 but list tools, not prompts. The launch spike reached 136 prompts and 257 commits by Dec 31, 2022. Then near-stagnation: 224 prompts by Dec 2025. The v2 web app ("Initialize v2 work", 2025-12-10) took the count to 828 (Jan 2026) and 2,627 (Oct 2026).

**Secret sauce.** A 5-day launch with an instantly copyable format. Machine-readable data from week 2. A pivot from list to product that keeps GitHub as sync target and contributor-credit engine. Stacked social proof.

**Weaknesses.** Volume over vetting ("Add prompt: Migros TEST"). Stale self-reported stats ("⭐ 143k+ GitHub stars" vs 174k). Email exposure. An "awesome" badge on what is now an app repo.

**Quotes.**
- "We encourage you to add your own prompts to the list, and to use ChatGPT to generate new prompts as well." (Dec 2022)
- "You are an automated moderation agent for the **prompts.chat** repository."

---

## 8. Shubhamsaboo/awesome-llm-apps (~142.8k stars)

**Value & scope.** "100+ open-source AI agents, agent skills, and RAG apps. Hand-built, tested end-to-end, Apache-2.0." Every entry is runnable code inside the repo: 122 README entries, 1,984 files.

**Curation policy.** Authored, not aggregated. Shubham Saboo and collaborator Madhu Shantan wrote most apps, and Shubham made 271 of 289 merges. There is no CONTRIBUTING; external PRs are mostly fixes ("[ApiPatch] Migrate deprecated langchain... API calls"). Skills have real CI: `skill-evals.yml` runs deterministic evals plus "skill lint (strict)" against the SKILL.md spec.

**Entry format.** `* [emoji Name](relative/path/) - one-line outcome`. Descriptions are playful and benefit-led ("Project Graveyard: an agent that autopsies your dead side projects"). Each category has a one-line explainer.

**Navigation.** A 3×2 screenshot gallery, then "🚀 Run one now" (`npx skills add`, or clone and run "in 30 seconds"), then 18 categories. Machine-translated READMEs via readme-i18n.com.

**Contribution & governance.**
- **AI in the loop:** `claude.yml` runs claude-code-action on @claude mentions; about 100 commits carry AI co-author trailers; a "ci" identity made 56 commits.
- **Monetization:** sponsor sections were removed in Sep and Oct 2026. The funnel is now the Unwind AI newsletter.
- **Star prompt:** the README ends with "⭐ Star the repo to get notified when new templates drop", which is misleading since stars don't notify.

**Maintenance.** First commit 2024-04-29, 516 days after ChatGPT. It rode successive waves: RAG, then agents (130 commits/month in Jan 2025), MCP, then skills (125 in Jul 2026). Entries: 20 (Sep 2024) → 47 (Jan 2025) → 122.

**Secret sauce.** Runnable apps named by outcome, with screenshots and a time-to-first-run quickstart. Constant re-skinning to the current buzzword ("Always-on Agents", "Generative UI").

**Weaknesses.** Code rot replaces link rot (many deprecated-API migrations). Model-name chasing ("Claude Fable 5.1 as advisor, GPT-6 Astra as orchestrator"). A single-author portfolio rather than a curated list.

**Quotes.**
- "Clone it, ship it, sell it - 100% free and open-source"

---

## Cross-list patterns for this archetype

**Timeline**

| List | First commit | Tech launch | Lag (days) | Earlier rivals (first commit, stars) |
|---|---|---|---|---|
| f/prompts.chat | 2022-12-05 | ChatGPT 2022-11-30 | 5 | humanloop & saharmor awesome-chatgpt, 2022-12-04 (tool lists; 1.5k / 0.6k) |
| Shubhamsaboo/awesome-llm-apps | 2024-04-29 | ChatGPT 2022-11-30 | 516 | n/a (rode later waves) |
| PatrickJS/awesome-cursorrules | 2024-09-16 | Cursor rules ~2024 | n/a (23 after cursor.directory) | cursor.directory 2024-08-24 |
| punkpeye/awesome-mcp-servers | 2024-11-29 | MCP 2024-11-25 | 4 | wong2 2024-11-28 (4.4k); appcypher 2024-11-29 (5.8k) |
| hesreallyhim/awesome-claude-code | 2025-04-19 | Claude Code 2025-02-24 | 54 | none found (jqueryscript list: 2025-07-13) |
| VoltAgent/awesome-agent-skills | 2025-10-28 | Agent Skills 2025-10-16 | 12 | travisvn 2025-10-16 (15.5k); ComposioHQ 2025-10-17 (77.8k) |
| VoltAgent/awesome-openclaw-skills | 2026-01-25 | Clawdbot/OpenClaw surge, Jan 2026 (rename ~01-30, approx.) | ≈ -5 vs rename | launched under the Clawdbot name |
| VoltAgent/awesome-design-md | 2026-03-31 | Stitch DESIGN.md (date not verified) | n/a | n/a |

1. **Speed is necessary, not sufficient.** Every link list here launched within 0-54 days of its technology, but only hesreallyhim (and prompts.chat in prompts) was first.
   - MCP: punkpeye was third, about 1.5 days after wong2, and now leads 96.8k to 4.4k.
   - Skills: VoltAgent was third and 12 days late; ComposioHQ (+1 day) leads it 77.8k to 36.3k.

   What separated winners came after day 4: throughput, distribution and maintainer stamina.

2. **Bulk-seeded launches.** Winners arrived full, not as stubs:
   - cursorrules: 140 entries by day 2.
   - prompts.chat: 58 by day 5.
   - openclaw: 565 on day 1, then 5,494 in five weeks through registry scraping.
   - design-md: 31 complete artifacts (51,549 lines) in its first commit.

3. **Why artifacts out-star links.** The three most-starred repos hold artifacts: prompts.chat 174k, llm-apps 143k, design-md 123k (with only 66 commits). The pure link lists sit at 36-97k. Likely reasons:
   - Value is consumed straight from the repo (copy a file, `npx skills add`, "Act as..."), so a star bookmarks a toolbox, not a reading list.
   - Artifacts are agent-consumable (CSV and HF dataset, `.mdc` frontmatter, SKILL.md, DESIGN.md YAML tokens). The consumer is increasingly an AI that needs a file.
   - The core value doesn't depend on outbound links, though runnable code rots with APIs.
   - Brand-name content (Claude's or Apple's design system) spreads on social media.

4. **GitHub as acquisition channel, value moved off-repo.** Several lists later redirected to owned properties:
   - design-md → getdesign.md, within about 3 weeks.
   - openclaw → clawskills.sh.
   - agent-skills → officialskills.sh.
   - prompts.chat → web app with credits.
   - punkpeye → Glama badges and ads.
   - llm-apps → Unwind AI newsletter.

   The repo stays the star magnet; conversion happens elsewhere.

5. **Submissions leave the PR.** The alternatives in use:
   - issue form + bot PR (hesreallyhim: "Do not open a PR");
   - website + git sync (prompts.chat);
   - upstream registry gate (ClawHub URL check);
   - external build oracle (Glama);
   - full closure (design-md).

   wong2 sent submissions to an off-GitHub site with no GitHub credit and sits at 4.4k stars. prompts.chat avoided that trap by syncing web submissions back as user-credited commits.

6. **The AI-spam arms race is explicit and dated (2026).**
   - hesreallyhim: "7d/14d/30d/ban" cooldowns, an OpenClaw ban, a `gh` CLI block and a honeypot checkbox.
   - prompts.chat: a Copilot-engine LLM moderator (Feb 2026).
   - cursorrules: a 30-day account-age gate (May 2026).
   - openclaw: 4,065 bot or bulk-account skills excluded.
   - agent-skills: "Hand-picked, not AI-slop generated."

   **punkpeye is the counter-model:** a declared agent lane (🤖🤖🤖). It has about 1,410 merged agent PRs, roughly 37% of merges since March 2026, gated by machine checks instead of human taste.

7. **Maturity and social proof replace taste as the first filter.** When AI makes a plausible repo nearly free, time and adoption become the proxy:
   - hesreallyhim: 14 days of activity or 100 stars.
   - VoltAgent: "Brand new skills... are not accepted".
   - cursorrules: account age of at least 30 days.
   - punkpeye: a passing Glama score.
   - ClawHub: tests must pass.

8. **Security is a new curation axis for executable artifacts.** Skills, hooks and rules are instructions an agent will run. The responses:
   - "curated, not audited" disclaimers and scanner links (Snyk);
   - published malicious-exclusion counts (373);
   - exfiltration-based removals;
   - CI linting for prompt injection (cursorrules);
   - a Claude-run static-review prompt with a "Fast-Reject Heuristic" (hesreallyhim).

   None of this exists in classic awesome lists.

9. **Company backing is the norm, and neutrality is traded away.**
   - **VoltAgent** runs a portfolio of about 247k stars (design-md 123k, openclaw 53k, agent-skills 36k, claude-code-subagents 26k, codex-subagents 6.4k, ai-agent-papers 1.9k). It sells placement (`voltagent_2026q3` UTMs, "Ranked #150 globally on GitHub", promo code VOLTAGENT), puts sponsor sections right after Claude in the ToC, and cross-promotes its own repos through badges.
   - **punkpeye** sells an ad slot.
   - **cursorrules** carries three sponsors.
   - **hesreallyhim** is the only independent list (FUNDING.yml removed).

   Backing buys launch speed, bulk seeding and staff time. It costs disinterestedness.

10. **Bus factor of one, masked by bots.** Merge shares: Fiegel 91%; Özmen 383/394 (agent-skills) and 63/66 commits (design-md); Saboo 271/289. hesreallyhim has one human approver behind a bot, and prompts.chat's OWNERS.md lists one maintainer. Bots and coding agents add capacity without adding people: AI co-author trailers number 681 in punkpeye, 215 in hesreallyhim and about 100 in llm-apps.

11. **Two winning shapes: selective editorial or exhaustive directory.** hesreallyhim (263 voiced, reviewed entries) and the MCP and openclaw directories (4.6k and 5.2k entries) both reached 50-100k stars. Directories replace voice with machine-checkable grammars: the emoji whitelist, enforced `owner/repo` names, score badges, ≤10-word descriptions. The losing rivals sit in the uniform-links middle.

12. **Growth loops are wired into the workflows.** Each listed author becomes a distributor:
    - an auto "🎉 featured" issue with a badge snippet on every listed repo (hesreallyhim);
    - a Discord flair for merged authors (punkpeye);
    - contributor-graph credit for web submissions (prompts.chat);
    - a "⭐ Star... to get notified" prompt (llm-apps);
    - a celebrity social-proof wall (prompts.chat).

13. **Name and format churn follow the platform.**
    - Renames: awesome-chatgpt-prompts → prompts.chat; awesome-claude-skills → awesome-agent-skills; awesome-clawdbot-skills → awesome-openclaw-skills.
    - Format migrations: `.cursorrules` → `.mdc` (1,289 → 253 files); hesreallyhim's July 2026 renovation.

    Survivors re-platform instead of freezing. The cost is stale self-references: old repo names in badges, counts that disagree (openclaw "5200" / "5300+" / "5,400+"; agent-skills "1497+" vs about 1,160; prompts.chat "143k+" vs 174k) and abandoned translations (MCP Chinese README: 455 entries vs 4,636).

14. **Bursty, wave-riding activity.** Maintenance comes in bursts tied to platform news (agents, MCP, skills, OpenClaw), and maintainers rename categories to the current term ("Always-on Agents", "Ralph Wiggum").
    - prompts.chat: about 90 prompts in three years (2023-2025), then about 2,400 in ten months.
    - cursorrules: silent for four months, then 47 commits in May 2026.
    - design-md: 57 of its 66 commits in its first two months.
