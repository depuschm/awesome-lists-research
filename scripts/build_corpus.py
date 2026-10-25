"""Join extracted features with star data, dedupe renamed repos, classify repo type.

Inputs : data/master_stars.tsv, data/features.jsonl (one JSON per clone), clones/ (for root-commit dedupe)
Output : data/corpus.csv
"""
import csv, json, os, re, subprocess
import pandas as pd

R = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/'
stars = pd.read_csv(R + 'data/master_stars.tsv', sep='\t', dtype={'index_section': str, 'tal_category': str, 'desc': str})
stars['key'] = stars['repo'].str.lower()
feats = [json.loads(l) for l in open(R + 'data/features.jsonl', encoding='utf-8')]
F = pd.DataFrame(feats)
F['key'] = F['repo'].str.lower()
F = F.drop(columns=['repo'])
df = stars.merge(F, on='key', how='inner')


def root_commit(repo):
    d = R + 'clones/' + repo.replace('/', '__', 1)
    out = subprocess.run(['git', '-C', d, 'rev-list', '--max-parents=0', 'HEAD'], capture_output=True, text=True).stdout.split()
    return min(out) if out else None


df['root_commit'] = df['repo'].map(root_commit)
# renamed / duplicate repos share the same root commit: keep the row with the most stars (newest name usually)
df = df.sort_values('stars', ascending=False)
dups = df[df.duplicated('root_commit', keep='first') & df['root_commit'].notna()]
dups[['repo', 'root_commit']].to_csv(R + 'data/duplicates_dropped.csv', index=False)
# carry index membership / tal stars over to the kept row
for rc, g in df[df['root_commit'].notna()].groupby('root_commit'):
    if len(g) > 1:
        i = g.index[0]
        df.loc[i, 'in_index'] = g['in_index'].max()
        if not isinstance(df.loc[i, 'index_section'], str) or not df.loc[i, 'index_section']:
            sec = g['index_section'].dropna()
            df.loc[i, 'index_section'] = sec.iloc[0] if len(sec) else ''
df = df.drop(dups.index)

df['awesome_named'] = df['repo'].str.contains('awesome', case=False)
df['log_stars'] = (df['stars'].clip(lower=1)).apply(lambda x: __import__('math').log10(x))
df['entries_per_100w'] = df['n_entries'] / (df['readme_words'].clip(lower=1) / 100)


def classify(r):
    """list = README of curated external entries; collection = entries are files in the repo
    (prompts, rules, skills); other = code, books, guides, apps."""
    e = r['n_entries'] if pd.notna(r['n_entries']) else 0
    if e < 25:
        return 'other'
    if pd.notna(r.get('internal_link_share')) and r['internal_link_share'] >= 0.5:
        return 'collection'
    code_heavy = r['n_code_files'] > max(60, 0.5 * r['n_files'])
    if code_heavy and e < 200:
        return 'other'
    if r['entries_per_100w'] < 1.0 and e < 150:
        return 'other'  # prose guide with a few links
    return 'list'


df['kind'] = df.apply(classify, axis=1)
manual = R + 'data/manual_kind.csv'
if os.path.exists(manual):
    for row in csv.DictReader(open(manual)):
        df.loc[df['key'] == row['repo'].lower(), 'kind'] = row['kind']
    content_cols = ['n_entries', 'desc_ratio', 'avg_desc_words', 'n_sections_with_items', 'median_items_per_section', 'max_items_per_section', 'sorted_pair_ratio', 'code_tag_item_ratio', 'star_annot_item_ratio', 'entries_per_100w']
    df.loc[df['kind'] == 'list_unparsed', content_cols] = float('nan')


def tier(s):
    return 'T1 >=50k' if s >= 50000 else 'T2 10k-50k' if s >= 10000 else 'T3 2k-10k' if s >= 2000 else 'T4 <2k'


df['tier'] = df['stars'].map(tier)
df.to_csv(R + 'data/corpus.csv', index=False)
print(len(df), 'repos;', df['kind'].value_counts().to_dict())
print(df.groupby(['tier', 'kind']).size().unstack(fill_value=0))
print('dropped duplicates:', len(dups), dups['repo'].tolist()[:10])
