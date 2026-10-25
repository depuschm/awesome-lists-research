"""Extract repository / history / README features from a partial sparse clone.

Usage: python3 -I extract.py <clone_dir> [<clone_dir> ...]  -> JSON lines on stdout
"""
import collections, json, os, re, subprocess, sys, unicodedata

NOW = 1792886400  # 2026-10-25T00:00:00Z
DAY = 86400
BOT = re.compile(r'\[bot\]|dependabot|github-actions|renovate|actions@github|noreply@github\.com>?$|^bot@|greenkeeper|imgbot|allcontributors|semantic-release', re.I)
CODE_EXT = {'py', 'js', 'ts', 'go', 'rb', 'java', 'c', 'cc', 'cpp', 'h', 'rs', 'php', 'sh', 'kt', 'swift', 'scala',
            'cs', 'jsx', 'tsx', 'vue', 'svelte', 'lua', 'pl', 'ex', 'exs', 'hs', 'clj', 'dart', 'r', 'jl', 'm', 'ipynb'}
IMG_EXT = {'png', 'jpg', 'jpeg', 'gif', 'svg', 'webp', 'ico', 'bmp'}
DATA_EXT = {'yml', 'yaml', 'json', 'toml', 'csv', 'tsv', 'xml'}
WF_KEYS = {
    'awesome_lint': r'awesome-lint|awesome_lint',
    'awesome_bot': r'awesome[_-]bot',
    'link_check': r'lychee|markdown-link-check|link-?check|linkinator|broken[-_ ]?links?|dead[-_ ]?links?|check[-_]?links|url[-_]?check|urlchecker|linkchecker|muffet|liche|htmlproofer|awesome_bot',
    'markdown_lint': r'markdownlint|remark-lint|remark-cli|mdl\b|textlint|prettier',
    'stale_bot': r'actions/stale|stale',
    'sort_check': r'\bsort|alphabetic|order',
    'duplicate_check': r'duplicate',
    'generate_readme': r'generat|build[-_ ]readme|render|make readme|update[-_ ]readme',
    'star_update': r'stars?|stargazer',
    'ai_or_spam': r'\bai\b|llm|openai|claude|spam|anthropic',
}
LICENSES = [('CC0', r'CC0|Creative Commons Zero|Public Domain Dedication|creativecommons\.org/publicdomain/zero'),
            ('CC-BY-SA', r'Attribution-ShareAlike|CC[- ]BY[- ]SA'), ('CC-BY-NC', r'NonCommercial|CC[- ]BY[- ]NC'),
            ('CC-BY', r'Creative Commons Attribution|CC[- ]BY\b'), ('MIT', r'\bMIT License|Permission is hereby granted, free of charge'),
            ('Apache', r'Apache License'), ('GPL', r'GNU (Affero )?General Public License'), ('Unlicense', r'unlicense\.org|This is free and unencumbered'),
            ('BSD', r'Redistribution and use in source and binary forms'), ('WTFPL', r'WTFPL|DO WHAT THE FUCK')]
EMOJI_RE = re.compile('[\U0001F300-\U0001FAFF☀-➿⭐⬆⬇✅❌\U0001F1E6-\U0001F1FF]')
SHORTCODE_RE = re.compile(r'(?<![\w/]):[a-z0-9_+-]{2,30}:(?![\w/])')
MD_LINK = re.compile(r'(?<!!)\[((?:[^\[\]]|\[[^\]]*\])*)\]\(\s*<?([^)\s>]+)>?(?:\s+"[^"]*")?\s*\)')
HTML_LINK = re.compile(r'<a\s[^>]*href=["\']([^"\']+)["\']', re.I)
REF_DEF = re.compile(r'^\s*\[[^\]]+\]:\s*(\S+)', re.M)
IMG = re.compile(r'!\[[^\]]*\]\(\s*<?([^)\s>]+)|<img\s[^>]*src=["\']([^"\']+)["\']', re.I)
BADGE = re.compile(r'shields\.io|badge|badgen|travis-ci|circleci|github\.com/[^)]+/workflows/|/actions/workflows/|codecov|gitter\.im|discord|awesome\.re|cdn\.rawgit\.com/sindresorhus/awesome|slack', re.I)
AWESOME_BADGE = re.compile(r'awesome\.re/(badge|mentioned)|sindresorhus/awesome/[^)]*media/(badge|mentioned)|cdn\.rawgit\.com/sindresorhus/awesome|\[!\[[^\]]*\]\([^)]*\)\]\(https?://(github\.com/sindresorhus/awesome/?|awesome\.re/?)\)', re.I)
ITEM = re.compile(r'^(\s*)(?:[-*+]|\d+[.)])\s+(.*)$')
CJK = re.compile('[぀-ヿ㐀-䶿一-鿿가-힯]')


def git(d, *args):
    return subprocess.run(['git', '-C', d, *args], capture_output=True, text=True, errors='replace').stdout


def history(d):
    out = git(d, 'log', '--format=%H%x1f%ae%x1f%an%x1f%at%x1f%ce%x1f%P%x1f%s', 'HEAD')
    rows = [l.split('\x1f') for l in out.splitlines() if l.count('\x1f') == 6]
    f = {}
    if not rows:
        return f
    ts = [int(r[3]) for r in rows]
    f['n_commits'] = len(rows)
    f['first_commit_ts'], f['last_commit_ts'] = min(ts), max(ts)
    f['age_years'] = round((NOW - min(ts)) / DAY / 365.25, 2)
    f['days_since_last_commit'] = round((NOW - max(ts)) / DAY, 1)
    f['first_year'] = int(git(d, 'log', '--reverse', '--format=%ad', '--date=format:%Y', 'HEAD').split('\n', 1)[0] or 0)
    merges = [r for r in rows if len(r[5].split()) > 1]
    nonmerge = [r for r in rows if len(r[5].split()) <= 1]
    human = [r for r in nonmerge if not BOT.search(r[1] + ' ' + r[2] + '>')]
    f['n_merge_commits'] = len(merges)
    f['n_pr_merge_commits'] = sum(1 for r in merges if r[6].startswith('Merge pull request #'))
    f['n_squash_pr_commits'] = sum(1 for r in nonmerge if re.search(r'\(#\d+\)\s*$', r[6]))
    refs = [int(x) for r in rows for x in re.findall(r'#(\d{1,6})\b', r[6])]
    f['max_issue_ref'] = max(refs) if refs else 0
    f['n_bot_commits'] = len(nonmerge) - len(human)
    f['n_web_commits'] = sum(1 for r in rows if r[4].lower() == 'noreply@github.com')
    by_author = collections.Counter(r[1].lower() for r in human)
    f['n_authors'] = len(by_author)
    tot = sum(by_author.values()) or 1
    top = by_author.most_common(3)
    f['top1_author_share'] = round(top[0][1] / tot, 3) if top else None
    f['top3_author_share'] = round(sum(c for _, c in top) / tot, 3) if top else None
    f['authors_1_commit_share'] = round(sum(1 for c in by_author.values() if c == 1) / max(len(by_author), 1), 3)
    mergers = collections.Counter(r[1].lower() for r in merges if r[6].startswith('Merge pull request #'))
    f['n_mergers'] = len(mergers)
    f['n_mergers_5plus'] = sum(1 for c in mergers.values() if c >= 5)
    yr = NOW - 365 * DAY
    f['commits_last_365d'] = sum(1 for t in ts if t >= yr)
    f['commits_last_90d'] = sum(1 for t in ts if t >= NOW - 90 * DAY)
    f['authors_last_365d'] = len({r[1].lower() for r in human if int(r[3]) >= yr})
    recent = [r for r in rows if int(r[3]) >= yr]
    f['bot_share_last_365d'] = round(sum(1 for r in recent if BOT.search(r[1] + ' ' + r[2] + '>') or r[6].startswith('[bot]')) / len(recent), 3) if recent else None
    f['pr_merges_last_365d'] = sum(1 for r in rows if int(r[3]) >= yr and (r[6].startswith('Merge pull request #') or re.search(r'\(#\d+\)\s*$', r[6])))
    months = {subprocess_free_month(t) for t in ts}
    f['active_months'] = len(months)
    span_months = max(1, (max(ts) - min(ts)) / DAY / 30.44)
    f['active_month_ratio'] = round(len(months) / span_months, 3)
    per_year = collections.Counter(subprocess_free_year(t) for t in ts)
    f['commits_by_year'] = dict(sorted(per_year.items()))
    f['active_years'] = len(per_year)
    # share of commits in first 90 days (launch burst)
    t0 = min(ts)
    f['first90d_commit_share'] = round(sum(1 for t in ts if t <= t0 + 90 * DAY) / len(ts), 3)
    st = sorted(ts)
    gaps = [(b - a) / DAY for a, b in zip(st, st[1:])]
    f['max_gap_days'] = round(max(gaps), 1) if gaps else 0
    return f


def subprocess_free_month(t):
    import time
    g = time.gmtime(t)
    return g.tm_year * 100 + g.tm_mon


def subprocess_free_year(t):
    import time
    return time.gmtime(t).tm_year


def files(d):
    names = git(d, 'ls-tree', '-r', '--name-only', 'HEAD').splitlines()
    f = {'n_files': len(names)}
    ext = collections.Counter(n.rsplit('.', 1)[-1].lower() if '.' in n.rsplit('/', 1)[-1] else '' for n in names)
    f['n_md_files'] = ext['md'] + ext['markdown'] + ext['rst'] + ext['mdx']
    f['n_code_files'] = sum(ext[e] for e in CODE_EXT)
    f['n_image_files'] = sum(ext[e] for e in IMG_EXT)
    f['n_data_files'] = sum(1 for n in names if not n.startswith('.github') and n.rsplit('.', 1)[-1].lower() in DATA_EXT)
    root = [n for n in names if '/' not in n]
    low = [n.lower() for n in names]
    rootlow = [n.lower() for n in root]
    tr = [n for n in root if re.match(r'(?i)^readme[._-]([a-z]{2,3}([-_][a-z]{2,4})?)\.(md|markdown|rst)$', n)]
    tr_dirs = [n for n in names if re.search(r'(?i)(^|/)(translations?|i18n|locales?|lang)/', n) and n.lower().endswith('.md')]
    f['n_readme_translations'] = len(tr) + len(tr_dirs)
    f['has_contributing'] = any(re.match(r'(\.github/|docs/)?contributing', n) for n in low)
    f['has_code_of_conduct'] = any(re.match(r'(\.github/|docs/)?code[-_]of[-_]conduct', n) for n in low)
    f['has_pr_template'] = any('pull_request_template' in n for n in low)
    f['has_issue_template'] = any(n.startswith('.github/issue_template') for n in low)
    f['has_funding'] = '.github/funding.yml' in low
    f['has_codeowners'] = any(n.endswith('codeowners') for n in low)
    f['has_security_md'] = any(re.match(r'(\.github/)?security\.md', n) for n in low)
    f['has_changelog'] = any(re.match(r'(changelog|history|changes)', n) for n in rootlow)
    f['has_travis'] = '.travis.yml' in rootlow
    wfs = [n for n in names if n.startswith('.github/workflows/') and n.endswith(('.yml', '.yaml'))]
    f['n_workflows'] = len(wfs)
    f['has_website'] = any(n in rootlow for n in ('cname', 'mkdocs.yml', '_config.yml', 'netlify.toml', 'vercel.json', 'docusaurus.config.js', 'hugo.toml', 'config.toml', 'astro.config.mjs', 'next.config.js', 'book.toml', 'gatsby-config.js'))
    f['has_package_json'] = 'package.json' in rootlow
    f['top_dirs'] = sorted({n.split('/', 1)[0] for n in names if '/' in n and not n.startswith('.')})[:25]
    # license
    lic = [n for n in root if re.match(r'(?i)^(license|licence|copying|unlicense)', n)]
    f['license'] = None
    if lic:
        txt = read_blob(d, lic[0])[:4000]
        f['license'] = next((k for k, pat in LICENSES if re.search(pat, txt, re.I)), 'other')
    # CI content keywords (workflows + travis)
    ci_text = ''
    for n in wfs + (['.travis.yml'] if f['has_travis'] else []):
        ci_text += '\n' + n + '\n' + read_blob(d, n)[:20000]
    for k, pat in WF_KEYS.items():
        f['ci_' + k] = bool(re.search(pat, ci_text, re.I)) if ci_text else False
    f['ci_any'] = bool(ci_text)
    contrib = [n for n in names if re.match(r'(?i)(\.github/|docs/)?contributing', n)]
    f['contributing_words'] = len(read_blob(d, contrib[0]).split()) if contrib else 0
    pr_t = [n for n in names if 'pull_request_template' in n.lower()]
    f['pr_template_words'] = len(read_blob(d, pr_t[0]).split()) if pr_t else 0
    f['pr_template_checkboxes'] = len(re.findall(r'- \[ \]', read_blob(d, pr_t[0]))) if pr_t else 0
    if f['has_funding']:
        fund = read_blob(d, [n for n in names if n.lower() == '.github/funding.yml'][0])
        f['funding_platforms'] = sorted({m for m in re.findall(r'^\s*([a-z_]+)\s*:\s*\S', fund, re.M)})
    gen_markers = [n for n in names if re.search(r'(?i)(^|/)(data|src|_data|source|entries|items|list)/.*\.(ya?ml|json|toml)$', n)]
    f['n_structured_entry_files'] = len(gen_markers)
    return f, root


def read_blob(d, path):
    p = os.path.join(d, path)
    if os.path.isfile(p):
        try:
            return open(p, encoding='utf-8', errors='replace').read()
        except OSError:
            pass
    return git(d, 'show', 'HEAD:' + path)


def pick_readme(root):
    cands = [n for n in root if re.match(r'(?i)^readme(\.(md|markdown|mdown|rst|txt|org|adoc))?$', n)]
    cands.sort(key=lambda n: (not n.lower().endswith(('.md', '.markdown')), n != 'README.md', len(n)))
    return cands[0] if cands else None


def normalize_md(txt):
    """Strip fenced code and HTML comments; convert setext headings to ATX."""
    body = re.sub(r'```.*?```', '', txt, flags=re.S)
    body = re.sub(r'<!--.*?-->', '', body, flags=re.S)
    body = re.sub(r'(?m)^([^\s|<>\-=*#][^\n|]*)\n=+[ \t]*$', r'# \1', body)
    body = re.sub(r'(?m)^([^\s|<>\-=*#][^\n|]*)\n-{3,}[ \t]*$', r'## \1', body)
    return body


def scan_entries(lines):
    f = {}
    # items: format-agnostic entry detection (md bullets, html anchors, tables, blockquotes, bare urls)
    LEAD = re.compile(r'^(?:\s|&nbsp;|&emsp;|>|[-*+](?=\s)|\d+[.)](?=\s)|:[a-z0-9_+-]+:|</?(?:p|li|ul|td|tr|b|strong|br|div|span|kbd)[^>]*>|\*\*|__|\||[\U0001F300-\U0001FAFF☀-➿⭐✅❌️])+')
    n_items = n_link_items = n_desc = 0
    desc_words = []
    max_indent = 0
    code_tag_items = star_items = 0
    sorted_pairs = total_pairs = 0
    prev = None
    section_sizes = []
    cur_section_items = 0
    in_toc = False
    table_link_rows = 0
    for l in lines:
        hm = re.match(r'^(#{1,6})\s+(.*)', l)
        if hm:
            htxt = re.sub(r'<[^>]+>|!?\[([^\]]*)\]\([^)]*\)', r'\1', hm.group(2)).strip(' *_:↑⬆')
            in_toc = bool(re.search(r'(?i)^(table of )?contents?$|^toc$|目录|^index$|^categories$', htxt))
            if cur_section_items:
                section_sizes.append(cur_section_items)
            cur_section_items = 0
            prev = None
            continue
        im = ITEM.match(l)
        if im:
            n_items += 1
        if in_toc or not l.strip():
            if l.strip():
                prev = None
            continue
        norm = LEAD.sub('', l)
        name = after = None
        mm = MD_LINK.match(norm) or re.match(r'\[((?:[^\[\]]|\[[^\]]*\])+)\]\[([^\]]*)\]', norm)
        if mm and not mm.group(2).startswith('#'):
            name, after = mm.group(1), norm[mm.end():]
        else:
            am = re.match(r'<a\s[^>]*href=["\'](?!#)([^"\']+)["\'][^>]*>(.*?)</a>', norm, re.I)
            if am:
                name, after = re.sub(r'<[^>]+>', '', am.group(2)), norm[am.end():]
            elif im and re.search(r'https?://\S+', im.group(2)):
                name, after = re.sub(r'https?://\S+', '', im.group(2)), ''
        if name is None:
            prev = None
            continue
        if '|' in l and not im:
            table_link_rows += 1
        indent = len(l) - len(l.lstrip(' \t'))
        n_link_items += 1
        cur_section_items += 1
        max_indent = max(max_indent, indent if im else 0)
        after = re.sub(r'^(?:\s|\*\*|__|</?(?:b|strong|a|kbd|sup|sub|code|em|i)[^>]*>|`[^`]*`|\([^)]*\)|\[!\[[^\]]*\]\([^)]*\)\]\([^)]*\)|!\[[^\]]*\]\([^)]*\)|★\s*[\d.,]+k?|⭐\s*[\d.,]+k?|[\U0001F300-\U0001FAFF☀-➿️])*', '', after)
        dm = re.match(r'^(?:[-–—:|]|<br\s*/?>)\s*(.+)$', after.strip()) or (re.match(r'^([A-Za-zÀ-ɏ぀-鿿].{8,})$', after.strip()) if after.strip() else None)
        if dm and len(re.sub(r'<[^>]+>', ' ', dm.group(1)).split()) >= 2:
            n_desc += 1
            desc_words.append(len(re.sub(r'\[[^\]]*\]\([^)]*\)|<[^>]+>', 'x', dm.group(1)).split()))
        if re.search(r'`[^`]+`|<kbd>', l):
            code_tag_items += 1
        if re.search(r'⭐|★|shields\.io/github/stars|\bstars?\b', l, re.I):
            star_items += 1
        key = re.sub(r'[^a-z0-9À-￿]', '', name.lower())
        if prev is not None and prev[0] == indent:
            total_pairs += 1
            sorted_pairs += key >= prev[1]
        prev = (indent, key)
    if cur_section_items:
        section_sizes.append(cur_section_items)
    f['n_list_items'] = n_items
    f['n_link_items'] = n_link_items
    f['n_table_link_rows'] = table_link_rows
    f['n_entries'] = n_link_items
    f['table_based'] = table_link_rows > n_link_items / 2
    f['desc_ratio'] = round(n_desc / n_link_items, 3) if n_link_items else None
    f['avg_desc_words'] = round(sum(desc_words) / len(desc_words), 1) if desc_words else None
    f['code_tag_item_ratio'] = round(code_tag_items / n_link_items, 3) if n_link_items else None
    f['star_annot_item_ratio'] = round(star_items / n_link_items, 3) if n_link_items else None
    f['max_item_indent'] = max_indent
    f['sorted_pair_ratio'] = round(sorted_pairs / total_pairs, 3) if total_pairs >= 20 else None
    f['n_sections_with_items'] = len(section_sizes)
    f['median_items_per_section'] = sorted(section_sizes)[len(section_sizes) // 2] if section_sizes else 0
    f['max_items_per_section'] = max(section_sizes) if section_sizes else 0
    return f


def readme(d, path, repo=''):
    txt = read_blob(d, path)
    f = {'readme_file': path, 'readme_bytes': len(txt.encode('utf-8')), 'readme_lines': txt.count('\n') + 1}
    f['readme_generated_marker'] = bool(re.search(r'(auto-?generated|this file is generated|generated (by|from|automatically)|do not edit (this|manually|directly)|don\'t edit this file|edit .*\.ya?ml instead)', txt[:6000] + txt[-3000:], re.I))
    # strip fenced code and html comments for structural analysis
    body = normalize_md(txt)
    lines = body.splitlines()
    f['readme_words'] = len(re.sub(r'\([^)]*\)', '', body).split())
    f['cjk_ratio'] = round(len(CJK.findall(body)) / max(len(body), 1), 4)
    heads = collections.Counter()
    heading_texts = []
    for l in lines:
        m = re.match(r'^(#{1,6})\s+(.*)', l)
        if m:
            heads[len(m.group(1))] += 1
            heading_texts.append((len(m.group(1)), m.group(2).strip()))
        for m in re.finditer(r'<h([1-6])[\s>]', l, re.I):
            heads[int(m.group(1))] += 1
    for i in range(1, 5):
        f[f'n_h{i}'] = heads[i]
    f['n_headings'] = sum(heads.values())
    links = MD_LINK.findall(body)
    urls = [u for _, u in links] + HTML_LINK.findall(body) + REF_DEF.findall(body)
    ext = [u for u in urls if u.startswith(('http://', 'https://'))]
    f['n_links'] = len(urls)
    f['n_ext_links'] = len(ext)
    f['n_unique_ext_links'] = len(set(u.rstrip('/').lower() for u in ext))
    f['dup_link_ratio'] = round(1 - f['n_unique_ext_links'] / max(len(ext), 1), 3)
    f['n_anchor_links'] = sum(1 for u in urls if u.startswith('#'))
    rel = [u for u in urls if not re.match(r'^(https?:|#|mailto:|//)', u)]
    f['n_relative_links'] = len(rel)
    selfp = re.compile(r'https?://(www\.)?github\.com/' + re.escape(repo) + r'/(blob|tree|raw)/', re.I)
    self_links = [u for u in ext if selfp.match(u)]
    f['n_self_links'] = len(self_links)
    f['internal_link_share'] = round((len(rel) + len(self_links)) / max(len(rel) + len(ext), 1), 3)
    f['relative_link_share'] = round(len(rel) / max(len(rel) + len(ext), 1), 3)
    gh = [u for u in ext if re.match(r'https?://(www\.)?github\.com/[^/]+/[^/#?]+', u)]
    f['n_github_repo_links'] = len(gh)
    f['github_link_share'] = round(len(gh) / max(len(ext), 1), 3)
    doms = collections.Counter(re.sub(r'^https?://(www\.)?', '', u).split('/')[0].lower() for u in ext)
    f['n_domains'] = len(doms)
    f['http_insecure_links'] = sum(1 for u in ext if u.startswith('http://'))
    f['n_utm_links'] = sum(1 for u in ext if 'utm_' in u or 'ref=' in u or 'via=' in u)
    f['n_affiliate_like'] = sum(1 for u in ext if re.search(r'aff(iliate)?[=_]|partner|refer(ral)?=|amzn\.to|/ref/', u, re.I))
    imgs = IMG.findall(body)
    img_urls = [a or b for a, b in imgs]
    badges = [u for u in img_urls if BADGE.search(u)]
    f['n_badges'] = len(badges)
    f['n_images'] = len(img_urls) - len(badges)
    f['has_awesome_badge'] = bool(AWESOME_BADGE.search(txt))
    head = '\n'.join(lines[:25])
    f['has_header_image'] = bool(IMG.search(head) and any(not BADGE.search(a or b) for a, b in IMG.findall(head)))
    f['has_centered_header'] = bool(re.search(r'align=["\']?center', head, re.I))
    f['has_blockquote_tagline'] = any(l.startswith('>') for l in lines[:30])
    f['emoji_count'] = len(EMOJI_RE.findall(body)) + len(SHORTCODE_RE.findall(body))
    f['back_to_top_links'] = len(re.findall(r'back to top|⬆|↑\s*\]|\[\s*top\s*\]|\(#readme\)|\(#table-of-contents\)|\(#contents\)|返回目录|回到顶部', body, re.I))
    toc_head = any(re.search(r'(?i)^(table of )?contents?$|^toc$|^index$|^目录|^categories$|^sections$', t.strip(' *:'))
                   for _, t in heading_texts) or bool(re.search(r'(?im)^\s*(\*\*)?(table of contents|contents)(\*\*)?\s*:?\s*$', body))
    first_third = '\n'.join(lines[:max(30, len(lines) // 4)])
    f['has_toc'] = toc_head or len(re.findall(r'\]\(#', first_third)) >= 6
    f['has_details_collapsible'] = '<details' in body.lower()
    f.update(scan_entries(lines))
    pre = body.split('\n## ', 1)[0]
    f['intro_words'] = len(re.sub(r'<[^>]+>|!\[[^\]]*\]\([^)]*\)|\[!\[.*?\)\]\([^)]*\)', ' ', pre).split())
    low = body.lower()
    f['mentions_sponsor'] = bool(re.search(r'sponsor|backers|supported by|brought to you|our partners', low))
    f['has_sponsor_section'] = any(re.search(r'(?i)sponsor|backers|supporters|partners', t) for _, t in heading_texts)
    f['has_contributing_section'] = any(re.search(r'(?i)contribut', t) for _, t in heading_texts)
    f['has_license_section'] = any(re.search(r'(?i)licen[cs]e', t) for _, t in heading_texts)
    f['mentions_criteria'] = bool(re.search(r'criteria|inclusion|requirements? for (adding|inclusion|submission)|we only (accept|include|list)|must (be|have)|not accepted|will be removed', low))
    f['mentions_unmaintained_marker'] = bool(re.search(r'unmaintained|deprecated|archived|no longer maintained|abandoned|⚠', low))
    f['has_legend'] = bool(re.search(r'(?im)^#+\s*(legend|symbols|icons|explanation|key)\b', body)) or bool(re.search(r'(?i)legend\b', head))
    f['first_h2'] = next((t for lv, t in heading_texts if lv == 2), '')[:60]
    return f


def main():
    for d in sys.argv[1:]:
        repo = os.path.basename(d.rstrip('/')).replace('__', '/', 1)
        rec = {'repo': repo}
        try:
            rec.update(history(d))
            ff, root = files(d)
            rec.update(ff)
            rp = pick_readme(root)
            if rp:
                rec.update(readme(d, rp, repo))
            else:
                rec['readme_file'] = None
        except Exception as e:  # keep going; record the failure
            rec['error'] = repr(e)[:300]
        print(json.dumps(rec, ensure_ascii=False), flush=True)


if __name__ == '__main__':
    main()
