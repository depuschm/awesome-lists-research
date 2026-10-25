"""Collect the numbers the report page charts: writes data/analysis/viz.json."""
import json, os
import pandas as pd

R = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/'
A = R + 'data/analysis/'
out = {}

# 1. GitHub overall top-100 composition
t = pd.read_csv(R + 'data/github_top100_classified.tsv', sep='\t')
labels = {'software': 'Software', 'curated_list': 'Curated link lists', 'educational_guide_book_course': 'Guides, books & courses',
          'ai_agent_skills_config': 'AI agent skills & configs', 'artifact_collection': 'Artifact collections', 'other_non_software': 'Other non-software'}
out['top100'] = [{'cls': labels[k], 'n': int(v), 'top10': int((t.head(10)['class'] == k).sum()), 'top25': int((t.head(25)['class'] == k).sum())}
                 for k, v in t['class'].value_counts().items()]

# 2. cohorts (census)
c = pd.read_csv(A + 'cohorts_census.csv')
out['cohorts'] = c[c['first_year'] >= 2012].to_dict('records')

# 3/4. feature tiers + correlations
keep = ['n_entries', 'n_sections_with_items', 'desc_ratio', 'has_toc', 'has_awesome_badge', 'has_header_image', 'has_translations',
        'has_contributing', 'has_pr_template', 'has_issue_template', 'ci_any', 'ci_linkcheck_any', 'sponsor', 'active_365', 'dormant_2y',
        'n_authors', 'top1_author_share', 'n_mergers', 'h_entries_1y', 'h_below_peak_10', 'h_any_prune_10', 'cc_license', 'in_index',
        'mentions_criteria', 'big_section_share', 'h_grew_after_y1', 'awesome_named', 'has_metadata_tags', 'alphabetical', 'max_issue_ref', 'n_commits']
for tag in ['census', 'index']:
    f = pd.read_csv(A + f'feature_tiers_{tag}.csv')
    f = f[f['feature'].isin(keep)]
    out[f'features_{tag}'] = f.drop(columns=['p', 'p_partial']).to_dict('records')

# 5. growth curves
hist = {}
for line in open(R + 'data/readme_history_final.jsonl'):
    h = json.loads(line)
    hist[h['repo'].lower()] = h['points']
pick = ['vinta/awesome-python', 'ripienaar/free-for-dev', 'enaqx/awesome-react', 'vuejs/awesome-vue', 'sindresorhus/awesome',
        'awesome-selfhosted/awesome-selfhosted', 'avelino/awesome-go', 'josephmisiti/awesome-machine-learning', 'rust-unofficial/awesome-rust',
        'punkpeye/awesome-mcp-servers', 'hesreallyhim/awesome-claude-code', 'sindresorhus/awesome-nodejs', 'public-apis/public-apis']
out['growth'] = {r: [[p[0], p[2]] for p in hist[r.lower()] if p[2] > 0] for r in pick if r.lower() in hist}

# 6. scatter: census lists entries vs stars
L = pd.read_csv(A + 'lists_enriched.csv')
cen = pd.read_csv(R + 'data/corpus.csv')[['repo', 'rank_awesome_list']]
L = L.merge(cen, on='repo', how='left')
s = L[L['rank_awesome_list'].notna() & L['n_entries'].notna() & (L['n_entries'] > 0)]
out['scatter'] = s[['repo', 'stars', 'n_entries', 'first_year', 'tier']].to_dict('records')

# 7. dormant star growth
d = pd.read_csv(A + 'dormant_star_growth.csv')
d['bucket'] = pd.cut(d['yrs_since'], [-0.01, 0.5, 1, 2, 3, 5, 12], labels=['<6 mo', '6-12 mo', '1-2 y', '2-3 y', '3-5 y', '5+ y'])
g = d.groupby('bucket', observed=True)['ratio'].agg(['count', 'median']).reset_index()
g['bucket'] = g['bucket'].astype(str)
out['dormant'] = g.to_dict('records')

# 8. archetypes of top lists
a = pd.read_csv(R + 'data/archetypes_top.csv')
top = L.merge(a, on='repo', how='inner')
ag = top.groupby('archetype').agg(n=('repo', 'size'), stars=('stars', 'sum'), median_first_year=('first_year', 'median')).reset_index()
out['archetypes'] = ag.sort_values('stars', ascending=False).to_dict('records')
out['top_lists'] = top.sort_values('stars', ascending=False)[['repo', 'stars', 'archetype', 'first_year', 'n_entries', 'n_authors',
                                                               'days_since_last_commit', 'commits_last_365d']].head(60).to_dict('records')

# summaries
for tag in ['census', 'index', 'all']:
    out[f'summary_{tag}'] = json.load(open(A + f'summary_{tag}.json'))
json.dump(out, open(A + 'viz.json', 'w'), default=lambda o: None if o != o else (o.item() if hasattr(o, 'item') else str(o)))
print('wrote viz.json;', {k: (len(v) if hasattr(v, '__len__') else v) for k, v in out.items()})
