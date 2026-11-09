"""Timing or exposure? Separates "started early" from "has been live longer".

1. Census cohorts: stars per year live next to raw stars.
2. Within the 2014-15 wave: half-year launch windows (exposure differs by months, not years).
3. Lists whose content did not change for a year or more: is star growth proportional to size?
Writes data/analysis/timing_exposure.json.
"""
import json, os
import pandas as pd
from scipy import stats

R = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/'
A = R + 'data/analysis/'
L = pd.read_csv(A + 'lists_enriched.csv')
L = L.merge(pd.read_csv(R + 'data/corpus.csv', usecols=['repo', 'rank_awesome_list', 'first_commit_ts']), on='repo', how='left')
out = {}

# 1. cohorts, census sample
cen = L[L['rank_awesome_list'].notna()].copy()
cen['stars_per_year'] = cen['stars'] / cen['age_years'].clip(lower=0.25)
rows = []
for a, b in [(2014, 2015), (2016, 2018), (2019, 2022), (2023, 2024), (2025, 2026)]:
    g = cen[(cen['first_year'] >= a) & (cen['first_year'] <= b)]
    rows.append({'cohort': f'{a}-{b}', 'n': len(g), 'median_years_live': round(g['age_years'].median(), 1),
                 'share_10k': round((g['stars'] >= 10000).mean(), 3), 'median_stars': int(g['stars'].median()),
                 'median_stars_per_year': int(g['stars_per_year'].median())})
out['cohorts_census'] = rows

# 2. half-year windows inside the genesis wave, all analysed lists
L['start'] = pd.to_datetime(L['first_commit_ts'], unit='s')
rows = []
for lo, hi, label in [('2014-01-01', '2014-08-01', 'Jan-Jul 2014'), ('2014-08-01', '2015-01-01', 'Aug-Dec 2014'),
                      ('2015-01-01', '2015-07-01', 'Jan-Jun 2015'), ('2015-07-01', '2016-01-01', 'Jul-Dec 2015')]:
    g = L[(L['start'] >= lo) & (L['start'] < hi)]
    rows.append({'window': label, 'n': len(g), 'share_10k': round((g['stars'] >= 10000).mean(), 3), 'median_stars': int(g['stars'].median())})
out['wave_windows'] = rows

# 3. proportional growth among lists unchanged for a year or more (trackawesomelist snapshots)
d = pd.read_csv(A + 'dormant_star_growth.csv')
d = d[d['yrs_since'] >= 1].copy()
d['gain_per_year'] = (d['stars_topic'] - d['stars']) / d['yrs_since']
d['growth_per_year'] = (d['stars_topic'] / d['stars']) ** (1 / d['yrs_since']) - 1
r_abs = stats.spearmanr(d['stars'], d['gain_per_year'])
r_rel = stats.spearmanr(d['stars'], d['growth_per_year'])
d['size'] = pd.qcut(d['stars'], 3, labels=['smallest third', 'middle third', 'largest third'])
terc = d.groupby('size', observed=True).agg(n=('repo', 'size'), median_stars=('stars', 'median'),
                                             median_gain_per_year=('gain_per_year', 'median'),
                                             median_growth_per_year=('growth_per_year', 'median')).reset_index()
out['proportional_growth'] = {
    'n': len(d),
    'rho_size_vs_stars_gained_per_year': round(r_abs.statistic, 2), 'p_abs': float(r_abs.pvalue),
    'rho_size_vs_relative_growth_per_year': round(r_rel.statistic, 2), 'p_rel': float(r_rel.pvalue),
    'terciles': [{'size': str(t['size']), 'n': int(t['n']), 'median_stars': int(t['median_stars']),
                  'median_gain_per_year': int(round(t['median_gain_per_year'])),
                  'median_growth_per_year': round(t['median_growth_per_year'], 3)} for _, t in terc.iterrows()],
}
json.dump(out, open(A + 'timing_exposure.json', 'w'), indent=1)
print(json.dumps(out, indent=1))
