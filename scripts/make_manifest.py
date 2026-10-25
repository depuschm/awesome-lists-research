"""Write the list of studied repositories, pinned to the commit that was analysed.

Usage: python3 make_manifest.py [CLONES_DIR]   (default: <repo>/clones)
Outputs: data/repositories.tsv (machine-readable) and REPOSITORIES.md (rendered list with snapshot links)
"""
import csv, os, subprocess, sys
import pandas as pd

R = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/'
CLONES = (sys.argv[1] if len(sys.argv) > 1 else R + 'clones').rstrip('/') + '/'


def git(d, *a):
    return subprocess.run(['git', '-C', d, *a], capture_output=True, text=True).stdout.strip()


master = pd.read_csv(R + 'data/master_stars.tsv', sep='\t')
corpus = pd.read_csv(R + 'data/corpus.csv', usecols=['repo', 'kind', 'stars', 'rank_awesome_list', 'in_index', 'first_year', 'root_commit'])
dups = pd.read_csv(R + 'data/duplicates_dropped.csv')
excluded = set(open(R + 'data/excluded.txt').read().split())
LISTS = {'list', 'collection', 'list_unparsed'}
KIND = {'list': 'link list', 'collection': 'artifact collection', 'list_unparsed': 'multi-file / unusual format', 'other': 'not a curated list'}

by_key = {r.repo.lower(): r for r in master.itertuples()}
in_corpus = {r.repo.lower(): r for r in corpus.itertuples()}
root_to_kept = {r.root_commit: r.repo for r in corpus.itertuples() if isinstance(r.root_commit, str)}
# a 'duplicate' whose kept twin has the same name is one repo cloned twice under different capitalisation
dup_of = {r.repo.lower(): root_to_kept.get(r.root_commit, '') for r in dups.itertuples()
          if root_to_kept.get(r.root_commit, '').lower() != r.repo.lower()}

rows = []
cloned = {}
for d in sorted(os.listdir(CLONES)):
    path = CLONES + d
    if not os.path.isdir(path + '/.git'):
        continue
    cloned[d.replace('__', '/', 1).lower()] = path
names = {k: (by_key[k].repo if k in by_key else p.rsplit('/', 1)[1].replace('__', '/', 1)) for k, p in cloned.items()}

for key in sorted(set(by_key) | set(cloned)):
    m = by_key.get(key)
    repo = m.repo if m is not None else names[key]
    stars = '' if m is None or pd.isna(m.stars) else int(m.stars)
    rec = {'repo': repo, 'url': f'https://github.com/{repo}', 'stars': stars,
           'star_source': '' if m is None or pd.isna(m.star_source) else m.star_source,
           'in_official_index': int(m.in_index) if m is not None else 0, 'in_census': 0, 'kind': '', 'status': '',
           'duplicate_of': '', 'first_commit_year': '', 'head_sha': '', 'head_commit_date': '', 'branch': ''}
    if key in cloned:
        p = cloned[key]
        rec['head_sha'] = git(p, 'rev-parse', 'HEAD')
        rec['head_commit_date'] = git(p, 'log', '-1', '--format=%cs', 'HEAD')
        rec['branch'] = git(p, 'symbolic-ref', '--short', 'HEAD')
    c = in_corpus.get(key)
    if repo in excluded:
        rec['status'] = 'excluded (oversized non-list; clone abandoned)'
    elif key not in cloned:
        rec['status'] = 'clone failed (repository unavailable)'
    elif key in dup_of:
        rec['status'] = 'duplicate (same root commit; counted once)'
        rec['duplicate_of'] = dup_of[key]
    elif m is None:
        rec['status'] = 'cloned for qualitative comparison only'
    elif c is not None:
        rec['kind'] = KIND.get(c.kind, c.kind)
        rec['first_commit_year'] = '' if pd.isna(c.first_year) else int(c.first_year)
        if c.kind not in LISTS:
            rec['status'] = 'excluded (not a curated list)'
        elif pd.isna(c.stars):
            rec['status'] = 'no star data (not in statistics)'
        else:
            rec['status'] = 'analysed'
            rec['in_census'] = int(pd.notna(c.rank_awesome_list))
    rows.append(rec)

df = pd.DataFrame(rows)
df['_s'] = pd.to_numeric(df['stars'], errors='coerce').fillna(-1)
df = df.sort_values(['_s', 'repo'], ascending=[False, True]).drop(columns='_s')
df.to_csv(R + 'data/repositories.tsv', sep='\t', index=False, quoting=csv.QUOTE_MINIMAL)


def kfmt(s):
    if s == '':
        return '–'
    s = int(s)
    return f'{s/1000:.0f}k' if s >= 10000 else (f'{s/1000:.1f}k' if s >= 1000 else str(s))


def snap(r):
    return f'[`{r.head_sha[:7]}`]({r.url}/tree/{r.head_sha}) ({r.head_commit_date})' if r.head_sha else '–'


counts = df['status'].value_counts().to_dict()
an = df[df.status == 'analysed']
out = ['# Repositories studied', '',
       f'Every repository in this study, pinned to the commit that was analysed (cloned on 25 October 2026). '
       f'Each snapshot link opens the repository exactly as it was analysed. The same data, machine-readable, is in '
       f'[`data/repositories.tsv`](data/repositories.tsv); `scripts/clone_one.sh owner/repo <sha>` re-clones a snapshot.', '',
       '| Status | Repositories |', '|---|---|']
order = ['analysed', 'excluded (not a curated list)', 'no star data (not in statistics)', 'duplicate (same root commit; counted once)',
         'cloned for qualitative comparison only', 'clone failed (repository unavailable)', 'excluded (oversized non-list; clone abandoned)']
for s in order:
    if counts.get(s):
        out.append(f'| {s[0].upper() + s[1:]} | {counts[s]:,} |')
out.append(f'| **Total** | **{len(df):,}** |')
out += ['', 'Stars are the snapshot used in the study (GitHub topic pages, trackawesomelist or EvanLi/Github-Ranking). '
        '"Census" marks lists among the 1,000 most-starred repositories tagged `awesome-list`; "Index" marks lists in '
        '[sindresorhus/awesome](https://github.com/sindresorhus/awesome).', '']
out += ['## Contents', '', '- [Analysed curated lists](#analysed-curated-lists)', '- [Not a curated list](#not-a-curated-list)',
        '- [No star data](#no-star-data)', '- [Duplicates](#duplicates)', '- [Qualitative comparison only](#qualitative-comparison-only)',
        '- [Not cloned](#not-cloned)', '']


def table(title, sub, cols, fmt):
    out.extend([f'## {title}', '', sub, '', '| ' + ' | '.join(cols) + ' |', '|' + '---|' * len(cols)])
    for i, r in enumerate(fmt[0].itertuples(), 1):
        out.append('| ' + ' | '.join(fmt[1](i, r)) + ' |')
    out.append('')


table('Analysed curated lists', f'{len(an):,} lists, sorted by stars.', ['#', 'Repository', 'Stars', 'Kind', 'Started', 'Census', 'Index', 'Snapshot'],
      (an, lambda i, r: [str(i), f'[{r.repo}]({r.url})', kfmt(r.stars), r.kind, str(r.first_commit_year), '✓' if r.in_census else '',
                         '✓' if r.in_official_index else '', snap(r)]))
for title, s, sub in [('Not a curated list', 'excluded (not a curated list)', 'Code, books, guides, apps and cheat sheets that appeared in the rankings; cloned and classified, then excluded.'),
                      ('No star data', 'no star data (not in statistics)', 'Official-index lists with no star count in any source; features were extracted but they are not in the statistics.')]:
    sel = df[df.status == s]
    table(title, sub, ['Repository', 'Stars', 'Snapshot'], (sel, lambda i, r: [f'[{r.repo}]({r.url})', kfmt(r.stars), snap(r)]))
sel = df[df.status.str.startswith('duplicate')]
table('Duplicates', 'Renamed repositories and forks that share a root commit with a repository above; each was counted once.',
      ['Repository', 'Same history as', 'Snapshot'], (sel, lambda i, r: [f'[{r.repo}]({r.url})', f'[{r.duplicate_of}](https://github.com/{r.duplicate_of})' if r.duplicate_of else '–', snap(r)]))
sel = df[df.status == 'cloned for qualitative comparison only']
table('Qualitative comparison only', 'Cloned by the analysts for the deep dives and rivals study; not part of the ranked corpus.',
      ['Repository', 'Snapshot'], (sel, lambda i, r: [f'[{r.repo}]({r.url})', snap(r)]))
sel = df[df.status.isin(['clone failed (repository unavailable)', 'excluded (oversized non-list; clone abandoned)'])]
table('Not cloned', 'In the rankings but not analysed.', ['Repository', 'Stars', 'Reason'],
      (sel, lambda i, r: [f'[{r.repo}]({r.url})', kfmt(r.stars), r.status]))
open(R + 'REPOSITORIES.md', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print(df['status'].value_counts().to_string())
print('rows', len(df), '| census', int(df.in_census.sum()), '| md bytes', os.path.getsize(R + 'REPOSITORIES.md'))
