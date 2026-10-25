"""Merge star sources -> data/master_stars.tsv (one row per repo key)."""
import csv, os, re
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/'
D = R + 'data/'
def num(s):
    s = s.strip().lower().replace(',', '')
    m = re.match(r'^([\d.]+)\s*k$', s)
    return int(round(float(m.group(1)) * 1000)) if m else int(float(s))
def read(path, page_ok=None):
    rows = list(csv.DictReader(open(path, encoding='utf-8'), delimiter='\t'))
    if page_ok:
        rows = [r for r in rows if page_ok(int(r['page']))]
    return rows
al = read(D+'topic_awesome-list_p1-2.tsv') + read(D+'topic_awesome-list_p3-26.tsv', lambda p: 3 <= p <= 26) + read(D+'topic_awesome-list_p27-50.tsv', lambda p: 27 <= p <= 50)
aw = read(D+'topic_awesome_p1-25.tsv')
tal = read(D+'tal_lists.tsv')
idx = read(D+'awesome_index.tsv')
M = {}
def rec(repo):
    repo = repo.strip().strip('/')
    k = repo.lower()
    return M.setdefault(k, {'repo': repo, 'stars_topic': None, 'rank_awesome_list': None, 'rank_awesome': None, 'stars_tal': None, 'stars_exact': None, 'in_index': 0, 'index_section': '', 'tal_category': '', 'desc': ''})
ranks = sorted(int(r['rank']) for r in al)
assert ranks == list(range(1, len(ranks) + 1)), ('awesome-list ranks gap', len(ranks))
for r in al:
    m = rec(r['repo']); m['rank_awesome_list'] = int(r['rank']); m['stars_topic'] = num(r['stars_display']); m['desc'] = m['desc'] or r['description']
for r in aw:
    m = rec(r['repo']); m['rank_awesome'] = int(r['rank']); s = num(r['stars_display'])
    m['stars_topic'] = max(m['stars_topic'] or 0, s); m['desc'] = m['desc'] or r['description']
for r in tal:
    m = rec(r['repo']); m['stars_tal'] = int(r['stars']); m['tal_category'] = r['tal_category']; m['desc'] = m['desc'] or r['description']
for r in idx:
    m = rec(r['repo']); m['in_index'] = 1; m['index_section'] = r['section']
# exact stars from EvanLi overall top-100
for line in open(R + 'raw/EvanLi_Github-Ranking_master_Top100_Top-100-stars.md', encoding='utf-8'):
    mm = re.match(r'^\| \d+ \| \[[^\]]+\]\(https://github\.com/([^)]+)\) \| (\d+) \|', line)
    if mm and mm.group(1).lower() in M:
        M[mm.group(1).lower()]['stars_exact'] = int(mm.group(2))
for m in M.values():
    m['stars'] = m['stars_exact'] or m['stars_topic'] or m['stars_tal']
    m['star_source'] = 'exact' if m['stars_exact'] else 'topic' if m['stars_topic'] else 'tal' if m['stars_tal'] else ''
cols = ['repo', 'stars', 'star_source', 'stars_topic', 'stars_tal', 'stars_exact', 'rank_awesome_list', 'rank_awesome', 'in_index', 'index_section', 'tal_category', 'desc']
with open(D+'master_stars.tsv', 'w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, cols, delimiter='\t', extrasaction='ignore'); w.writeheader()
    for m in sorted(M.values(), key=lambda m: -(m['stars'] or 0)): w.writerow(m)
print('awesome-list rows', len(al), '| awesome rows', len(aw), '| tal', len(tal), '| index', len(idx))
print('unique repos', len(M), '| with stars', sum(1 for m in M.values() if m['stars']), '| index w/o stars', sum(1 for m in M.values() if m['in_index'] and not m['stars']))
# agreement between topic and tal star counts
pairs = [(m['stars_topic'], m['stars_tal']) for m in M.values() if m['stars_topic'] and m['stars_tal']]
import statistics
print('topic vs tal pairs', len(pairs), 'median ratio', round(statistics.median(a/b for a,b in pairs),3))
