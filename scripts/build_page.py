"""Build the report page (page/awesome-lists-study.html) from REPORT.md + data/analysis/viz.json."""
import json, os, re
import markdown
import pandas as pd

R = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/'
md_text = open(R + 'REPORT.md', encoding='utf-8').read()
viz = json.load(open(R + 'data/analysis/viz.json'))

# ---------- chart data (compact) ----------
t = pd.read_csv(R + 'data/github_top100_classified.tsv', sep='\t')
group = {'curated_list': 'list', 'educational_guide_book_course': 'guide', 'ai_agent_skills_config': 'coll',
         'artifact_collection': 'coll', 'other_non_software': 'coll', 'software': 'soft'}
top100 = [[int(r['rank']), r['repo'], int(r['stars']), group[r['class']]] for _, r in t.iterrows()]

coh = [c for c in viz['cohorts'] if c['first_year'] >= 2014]
cohorts = [[int(c['first_year']), int(c['n']), int(c['n_ge_10k']), int(c['median_stars'])] for c in coh]

feat = {f['feature']: f for f in viz['features_census']}
dumb_rows = [
    ('same', 'desc_ratio', 'Entries with a description'),
    ('same', 'has_toc', 'Table of contents'),
    ('same', 'has_awesome_badge', 'Awesome badge'),
    ('same', 'cc_license', 'Creative Commons licence'),
    ('more', 'has_contributing', 'CONTRIBUTING file'),
    ('more', 'ci_any', 'Any CI workflow'),
    ('more', 'has_pr_template', 'Pull request template'),
    ('more', 'has_issue_template', 'Issue templates or forms'),
    ('more', 'has_header_image', 'Header image or logo'),
    ('more', 'sponsor', 'Sponsors section or FUNDING.yml'),
    ('more', 'active_365', 'Commit in the last 12 months'),
    ('more', 'h_grew_after_y1', 'More than doubled after year one'),
    ('more', 'h_below_peak_10', 'Now 10%+ smaller than its peak'),
]
dumbbell = []
for g, k, label in dumb_rows:
    f = feat[k]
    t1, t4 = f['T1 >=50k'], f['T4 <2k']
    if k == 'desc_ratio':
        t1, t4 = t1 * 100, t4 * 100
    dumbbell.append([g, label, round(t1, 1), round(t4, 1), f['spearman_rho']])

scatter = [[s['repo'], int(s['stars']), int(s['n_entries']), int(s['first_year'])] for s in viz['scatter']]
growth_pick = [
    ('vinta/awesome-python', 'Shortlist policy: 739 → 498'),
    ('ripienaar/free-for-dev', 'Eight cleanup PRs in Jan 2026'),
    ('enaqx/awesome-react', 'Owner purges in 2019 and 2023'),
    ('vuejs/awesome-vue', 'Community prune, Nov 2024'),
    ('awesome-selfhosted/awesome-selfhosted', 'Held flat by nightly checks'),
    ('avelino/awesome-go', 'Hygiene bar: grows steadily'),
    ('josephmisiti/awesome-machine-learning', 'Never pruned: accretes'),
    ('punkpeye/awesome-mcp-servers', 'AI era: 0 → 4,648 in under 2 years'),
]
growth = []
for repo, note in growth_pick:
    pts = [[d if d <= '2026-10-25' else '2026-10-25', e] for d, e in viz['growth'][repo]]
    growth.append([repo.split('/')[1], note, pts])
dormant = [[d['bucket'], int(d['count']), round(d['median'], 3)] for d in viz['dormant']]
DATA = {'top100': top100, 'cohorts': cohorts, 'dumbbell': dumbbell, 'scatter': scatter, 'growth': growth, 'dormant': dormant}

# ---------- markdown -> html ----------
body_md = md_text.split('\n## Contents', 1)[1]
body_md = '## Contents' + body_md
html = markdown.markdown(body_md, extensions=['tables', 'toc', 'sane_lists'], extension_configs={'toc': {'permalink': False}})
html = re.sub(r'<table>', '<div class="table-wrap"><table>', html)
html = html.replace('</table>', '</table></div>')
html = re.sub(r'<a href="(https?://[^"]+)"', r'<a href="\1" target="_blank" rel="noopener"', html)

FIG = {
    'top100': ('GitHub\'s 100 most-starred repositories, by kind', 'Each square is one repository, in rank order from the top left. Ten per row. Hover for details.'),
    'cohorts': ('Share of lists that reached 10,000 stars, by year of first commit', 'Census sample (861 lists). Highlighted: the 2014–15 genesis and the 2025–26 AI wave.'),
    'dumbbell': ('Top lists versus small lists, feature by feature', 'Census sample: lists with 50k+ stars (n = 22) against lists under 2k stars (n = 350). ρ = Spearman correlation with stars across all 861 lists.'),
    'scatter': ('Entries in the README versus stars', 'Census sample, both axes logarithmic. Spearman ρ = 0.27: bigger lists tend to have more stars, loosely.'),
    'growth': ('Entries over time: the best-kept lists cut', 'README entries reconstructed quarter by quarter from git history. Each panel has its own vertical scale.'),
    'dormant': ('Stars keep coming while the content sits still', 'Median ratio of today\'s stars to stars at the last content update, by time since that update (trackawesomelist snapshots, 296 lists).'),
}


def fig(name):
    title, cap = FIG[name]
    return (f'<figure class="chart" id="fig-{name}" data-chart="{name}"><figcaption><span class="fig-title">{title}</span>'
            f'<span class="fig-cap">{cap}</span></figcaption><div class="chart-body" role="img" aria-label="{title}"></div></figure>')


for name in FIG:
    html = html.replace(f'<!-- chart:{name} -->', fig(name))
html = html.replace('<!-- chart:archetypes -->', '')
html = re.sub(r'<p>\s*(<figure)', r'\1', html)
html = re.sub(r'(</figure>)\s*</p>', r'\1', html)

css = open(R + 'scripts/page.css', encoding='utf-8').read()
js = open(R + 'scripts/page.js', encoding='utf-8').read()
hero = open(R + 'scripts/page_hero.html', encoding='utf-8').read()
page = f'''<title>What Makes Awesome Lists Great</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500&family=IBM+Plex+Sans+Condensed:wght@500;600;700&family=IBM+Plex+Serif:ital,wght@0,400;0,600;1,400&display=swap">
<style>
{css}
</style>
<div class="page">
{hero}
<main class="article">
{html}
</main>
<footer class="colophon"><p>Research and analysis: Claude, 25 October 2026. Data from GitHub topic pages, the sindresorhus/awesome index, trackawesomelist and EvanLi/Github-Ranking, plus 1,609 cloned repositories. Stars are rounded snapshots.</p></footer>
</div>
<div class="tip" id="tip" hidden></div>
<script>
const DATA = {json.dumps(DATA, separators=(',', ':'))};
{js}
</script>
'''
import os
os.makedirs(R + 'page', exist_ok=True)
open(R + 'page/awesome-lists-study.html', 'w', encoding='utf-8').write(page)
print('page bytes', len(page.encode('utf-8')))
