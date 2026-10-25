"""Statistical analysis of the awesome-list corpus.

Inputs : data/corpus.csv, data/readme_history_*.jsonl
Outputs: data/analysis/*.csv|json (tables used in the report)
"""
import glob, json, math, os
import numpy as np
import pandas as pd
from scipy import stats
import statsmodels.formula.api as smf

R = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/'
OUT = R + 'data/analysis/'
os.makedirs(OUT, exist_ok=True)
df = pd.read_csv(R + 'data/corpus.csv')
excluded = set(open(R + 'data/excluded.txt').read().split()) if os.path.exists(R + 'data/excluded.txt') else set()
df = df[~df['repo'].isin(excluded)]
L = df[df['kind'].isin(['list', 'collection', 'list_unparsed'])].copy()
L = L[L['stars'].notna()]
print('lists:', len(L), '| all repos:', len(df))

# ---------- derived features ----------
L['log_entries'] = np.log10(L['n_entries'].clip(lower=1))
L['active_365'] = (L['commits_last_365d'] > 0).astype(int)
L['human_active_365'] = (L['authors_last_365d'] > 0).astype(int)
L['dormant_2y'] = (L['days_since_last_commit'] > 730).astype(int)
L['log_authors'] = np.log10(L['n_authors'].clip(lower=1))
L['log_commits'] = np.log10(L['n_commits'].clip(lower=1))
L['alphabetical'] = (L['sorted_pair_ratio'] >= 0.9).astype(float).where(L['sorted_pair_ratio'].notna())
L['has_translations'] = (L['n_readme_translations'] > 0).astype(int)
L['ci_linkcheck_any'] = (L['ci_link_check'] | L['ci_awesome_bot']).astype(int)
L['has_back_to_top'] = (L['back_to_top_links'] > 2).astype(int)
L['cc_license'] = L['license'].fillna('').str.startswith('CC').astype(int)
L['cc0_license'] = (L['license'] == 'CC0').astype(int)
L['no_license'] = L['license'].isna().astype(int)
L['chinese'] = (L['cjk_ratio'] > 0.02).astype(int)
L['emoji_per_entry'] = L['emoji_count'] / L['n_entries'].clip(lower=1)
L['has_badges'] = (L['n_badges'] > 0).astype(int)
L['has_metadata_tags'] = ((L['code_tag_item_ratio'] > 0.3) | (L['star_annot_item_ratio'] > 0.3) | L['table_based'].fillna(False)).astype(int)
L['big_section_share'] = L['max_items_per_section'] / L['n_entries'].clip(lower=1)
L['sponsor'] = (L['has_sponsor_section'] | L['has_funding']).astype(int)
L['log_max_issue_ref'] = np.log10(L['max_issue_ref'].clip(lower=1))
L['org_owned'] = 0  # filled below where known
for c in ['has_toc', 'has_contributing', 'has_pr_template', 'has_issue_template', 'has_code_of_conduct', 'ci_any',
          'ci_awesome_lint', 'has_awesome_badge', 'has_header_image', 'has_details_collapsible', 'has_website',
          'mentions_criteria', 'awesome_named', 'in_index', 'has_funding', 'has_sponsor_section', 'mentions_unmaintained_marker',
          'has_license_section', 'has_contributing_section', 'readme_generated_marker', 'has_blockquote_tagline', 'has_centered_header']:
    L[c] = L[c].fillna(False).astype(int)

# ---------- README history-derived ----------
hist = {}
for fn in [R + 'data/readme_history_final.jsonl']:
    for line in open(fn):
        try:
            h = json.loads(line)
        except json.JSONDecodeError:
            continue
        hist[h['repo'].lower()] = h['points']


def hist_feats(key):
    pts = hist.get(key)
    if not pts or len(pts) < 2:
        return pd.Series(dtype=float)
    e = [p[2] for p in pts]
    first_nonzero = next((i for i, x in enumerate(e) if x > 0), None)
    peak = max(e)
    cur = e[-1]
    s = {'h_peak_entries': peak, 'h_cur_entries': cur, 'h_drop_from_peak': (peak - cur) / peak if peak else np.nan,
         'h_entries_q1': e[0], 'h_entries_1y': e[min(4, len(e) - 1)], 'h_entries_2y': e[min(8, len(e) - 1)],
         'h_quarters': len(e)}
    s['h_share_at_1y'] = s['h_entries_1y'] / peak if peak else np.nan
    # largest single-quarter drop (pruning event)
    drops = [(e[i - 1] - e[i]) / e[i - 1] for i in range(1, len(e)) if e[i - 1] >= 30]
    s['h_max_q_drop'] = max(drops) if drops else 0
    s['h_any_prune_20'] = int(any(d >= 0.20 for d in drops))
    s['h_any_prune_10'] = int(any(d >= 0.10 for d in drops))
    return pd.Series(s)


H = L['key'].apply(hist_feats)
L = pd.concat([L, H], axis=1)
L['h_below_peak_10'] = (L['h_drop_from_peak'] >= 0.10).astype(float).where(L['h_drop_from_peak'].notna())
L['h_grew_after_y1'] = (L['h_share_at_1y'] <= 0.5).astype(float).where(L['h_share_at_1y'].notna())
print('history coverage:', L['h_peak_entries'].notna().sum())

order = ['T1 >=50k', 'T2 10k-50k', 'T3 2k-10k', 'T4 <2k']
FEATURES = {
    # name: (column, kind[bin|num], group, label)
    'first_year': ('first_year', 'num', 'Timing & positioning', 'Year of first commit'),
    'awesome_named': ('awesome_named', 'bin', 'Timing & positioning', 'Name contains "awesome"'),
    'in_index': ('in_index', 'bin', 'Timing & positioning', 'Listed in sindresorhus/awesome'),
    'chinese': ('chinese', 'bin', 'Timing & positioning', 'README mostly Chinese/Japanese/Korean'),
    'n_entries': ('n_entries', 'num', 'Content', 'Entries (links) in README'),
    'desc_ratio': ('desc_ratio', 'num', 'Content', 'Share of entries with a description'),
    'avg_desc_words': ('avg_desc_words', 'num', 'Content', 'Words per description'),
    'n_sections_with_items': ('n_sections_with_items', 'num', 'Content', 'Categories with entries'),
    'median_items_per_section': ('median_items_per_section', 'num', 'Content', 'Median entries per category'),
    'big_section_share': ('big_section_share', 'num', 'Content', 'Largest category share of entries'),
    'has_metadata_tags': ('has_metadata_tags', 'bin', 'Content', 'Structured per-entry metadata (tags/stars/table)'),
    'alphabetical': ('alphabetical', 'bin', 'Content', 'Entries alphabetized (>=90% sorted pairs)'),
    'github_link_share': ('github_link_share', 'num', 'Content', 'Share of links pointing to GitHub repos'),
    'readme_words': ('readme_words', 'num', 'Content', 'README words'),
    'intro_words': ('intro_words', 'num', 'Presentation', 'Words before first section'),
    'has_toc': ('has_toc', 'bin', 'Presentation', 'Table of contents'),
    'has_back_to_top': ('has_back_to_top', 'bin', 'Presentation', 'Back-to-top links'),
    'has_badges': ('has_badges', 'bin', 'Presentation', 'Any badges'),
    'has_awesome_badge': ('has_awesome_badge', 'bin', 'Presentation', 'Awesome badge'),
    'has_header_image': ('has_header_image', 'bin', 'Presentation', 'Header image/logo'),
    'has_centered_header': ('has_centered_header', 'bin', 'Presentation', 'Centered HTML header'),
    'emoji_per_entry': ('emoji_per_entry', 'num', 'Presentation', 'Emoji per entry'),
    'has_details_collapsible': ('has_details_collapsible', 'bin', 'Presentation', 'Collapsible <details> sections'),
    'has_translations': ('has_translations', 'bin', 'Presentation', 'Translated READMEs'),
    'has_website': ('has_website', 'bin', 'Presentation', 'Companion website config in repo'),
    'has_contributing': ('has_contributing', 'bin', 'Process & governance', 'CONTRIBUTING file'),
    'contributing_words': ('contributing_words', 'num', 'Process & governance', 'CONTRIBUTING length (words)'),
    'has_pr_template': ('has_pr_template', 'bin', 'Process & governance', 'PR template'),
    'has_issue_template': ('has_issue_template', 'bin', 'Process & governance', 'Issue template/forms'),
    'has_code_of_conduct': ('has_code_of_conduct', 'bin', 'Process & governance', 'Code of conduct'),
    'mentions_criteria': ('mentions_criteria', 'bin', 'Process & governance', 'README states inclusion criteria'),
    'ci_any': ('ci_any', 'bin', 'Process & governance', 'Any CI (Actions/Travis)'),
    'ci_linkcheck_any': ('ci_linkcheck_any', 'bin', 'Process & governance', 'Automated link checking'),
    'ci_awesome_lint': ('ci_awesome_lint', 'bin', 'Process & governance', 'awesome-lint in CI'),
    'cc_license': ('cc_license', 'bin', 'Process & governance', 'Creative Commons license'),
    'no_license': ('no_license', 'bin', 'Process & governance', 'No license file'),
    'sponsor': ('sponsor', 'bin', 'Process & governance', 'Sponsors section or FUNDING.yml'),
    'mentions_unmaintained_marker': ('mentions_unmaintained_marker', 'bin', 'Process & governance', 'Flags unmaintained/archived entries'),
    'n_commits': ('n_commits', 'num', 'Activity & community', 'Commits (all time)'),
    'n_authors': ('n_authors', 'num', 'Activity & community', 'Distinct commit authors'),
    'top1_author_share': ('top1_author_share', 'num', 'Activity & community', 'Top author share of commits'),
    'n_mergers': ('n_mergers', 'num', 'Activity & community', 'People who merged PRs'),
    'max_issue_ref': ('max_issue_ref', 'num', 'Activity & community', 'Highest issue/PR number referenced'),
    'active_365': ('active_365', 'bin', 'Activity & community', 'Commit in last 12 months'),
    'human_active_365': ('human_active_365', 'bin', 'Activity & community', 'Human commit in last 12 months'),
    'dormant_2y': ('dormant_2y', 'bin', 'Activity & community', 'No commit for 2+ years'),
    'active_years': ('active_years', 'num', 'Activity & community', 'Calendar years with commits'),
    'h_entries_1y': ('h_entries_1y', 'num', 'History', 'Entries one year after launch'),
    'h_share_at_1y': ('h_share_at_1y', 'num', 'History', 'Share of peak size reached by year 1'),
    'h_any_prune_10': ('h_any_prune_10', 'bin', 'History', 'Ever cut >=10% of entries in a quarter'),
    'h_below_peak_10': ('h_below_peak_10', 'bin', 'History', 'Currently >=10% smaller than its peak'),
    'h_grew_after_y1': ('h_grew_after_y1', 'bin', 'History', 'More than doubled in size after year 1'),
}


def run(L, tag):
    print('\n\n######## SAMPLE:', tag, 'n =', len(L))
    # ---------- tiers ----------
    L['tier'] = pd.Categorical(L['tier'], order, ordered=True)

    rows = []
    y = L['log_stars']
    age_rank = L['first_commit_ts'].rank()
    for name, (col, kind, group, label) in FEATURES.items():
        x = L[col].astype(float)
        m = x.notna() & y.notna()
        rho, p = stats.spearmanr(x[m], y[m])
        # partial Spearman controlling for age: residualize ranks on age rank
        xr, yr, ar = x[m].rank(), y[m].rank(), age_rank[m]
        bx = np.polyfit(ar, xr, 1); by = np.polyfit(ar, yr, 1)
        prho, pp = stats.pearsonr(xr - np.polyval(bx, ar), yr - np.polyval(by, ar))
        rec = {'feature': name, 'label': label, 'group': group, 'kind': kind, 'n': int(m.sum()),
               'spearman_rho': round(rho, 3), 'p': p, 'partial_rho_age': round(prho, 3), 'p_partial': pp}
        for t in order:
            v = x[(L['tier'] == t) & x.notna()]
            rec[t] = round(v.mean() * 100, 1) if kind == 'bin' else round(v.median(), 3)
        # top-50 lists (by stars)
        top50 = L.nlargest(50, 'stars')[col].astype(float).dropna()
        rec['top50'] = round(top50.mean() * 100, 1) if kind == 'bin' else round(top50.median(), 3)
        rows.append(rec)
    C = pd.DataFrame(rows)
    C.to_csv(OUT + f'feature_tiers_{tag}.csv', index=False)
    pd.set_option('display.width', 250); pd.set_option('display.max_rows', 200); pd.set_option('display.max_colwidth', 45)
    print(C[['label', 'n', 'spearman_rho', 'partial_rho_age'] + order + ['top50']].to_string(index=False))

    # ---------- tier sizes ----------
    ts = L.groupby('tier', observed=True).agg(n=('repo', 'size'), median_stars=('stars', 'median'), total_stars=('stars', 'sum')).reset_index()
    ts.to_csv(OUT + f'tier_sizes_{tag}.csv', index=False)
    print(ts)

    # ---------- star concentration ----------
    s = L['stars'].sort_values(ascending=False).values
    conc = {'n_lists': int(len(s)), 'total_stars': int(s.sum()), 'top10_share': float(s[:10].sum() / s.sum()),
            'top1pct_share': float(s[:max(1, len(s) // 100)].sum() / s.sum()), 'top10pct_share': float(s[:len(s) // 10].sum() / s.sum()),
            'median_stars': float(np.median(s))}
    x = np.sort(s); n = len(x)
    conc['gini'] = float((2 * np.arange(1, n + 1) - n - 1).dot(x) / (n * x.sum()))
    print(conc)

    # ---------- cohort analysis ----------
    coh = L.groupby('first_year').agg(n=('repo', 'size'), median_stars=('stars', 'median'), mean_log=('log_stars', 'mean'),
                                      n_ge_50k=('stars', lambda v: int((v >= 50000).sum())), n_ge_10k=('stars', lambda v: int((v >= 10000).sum()))).reset_index()
    coh.to_csv(OUT + f'cohorts_{tag}.csv', index=False)
    print(coh.to_string(index=False))
    top = L.nlargest(100, 'stars')
    conc['top100_first_year_counts'] = top['first_year'].value_counts().sort_index().to_dict()
    conc['top100_share_2014_2015'] = float((top['first_year'] <= 2015).mean())
    conc['top50_share_2014_2015'] = float((L.nlargest(50, 'stars')['first_year'] <= 2015).mean())
    conc['all_share_2014_2015'] = float((L['first_year'] <= 2015).mean())

    # ---------- regression ----------
    M = L.copy()
    M['desc_ratio_f'] = M['desc_ratio'].fillna(M['desc_ratio'].median())
    M['top1_f'] = M['top1_author_share'].fillna(1)
    M['age'] = M['age_years']
    M['ai_era'] = (M['first_year'] >= 2023).astype(int)
    formulas = {
        'design_only': 'log_stars ~ age + ai_era + log_entries + desc_ratio_f + has_toc + has_contributing + has_pr_template + ci_linkcheck_any + has_translations + awesome_named + in_index + has_metadata_tags + chinese',
        'design_plus_activity': 'log_stars ~ age + ai_era + log_entries + desc_ratio_f + has_toc + has_contributing + has_pr_template + ci_linkcheck_any + has_translations + awesome_named + in_index + has_metadata_tags + chinese + active_365 + top1_f',
        'with_community': 'log_stars ~ age + ai_era + log_entries + desc_ratio_f + has_toc + has_contributing + ci_linkcheck_any + has_translations + awesome_named + in_index + chinese + log_authors',
    }
    reg = {}
    for k, f in formulas.items():
        fit = smf.ols(f, data=M).fit(cov_type='HC3')
        reg[k] = {'r2': fit.rsquared, 'n': int(fit.nobs),
                  'coef': {n: {'b': float(fit.params[n]), 'p': float(fit.pvalues[n]), 'x_fold': float(10 ** fit.params[n])} for n in fit.params.index}}
        print('\n==', k, 'R2=%.3f n=%d' % (fit.rsquared, fit.nobs))
        print(pd.DataFrame({'b': fit.params, 'p': fit.pvalues, 'x_fold': 10 ** fit.params}).round(4).to_string())
    json.dump({'concentration': conc, 'regressions': reg}, open(OUT + f'summary_{tag}.json', 'w'), indent=1, default=float)

    return C, conc, reg


SAMPLES = {
    'census': L[L['rank_awesome_list'].notna()].copy(),   # all lists among the 1,000 most-starred repos tagged awesome-list
    'index': L[L['in_index'] == 1].copy(),               # all official-index lists with known stars
    'all': L.copy(),
}
results = {k: run(v, k) for k, v in SAMPLES.items()}
L = SAMPLES['all']

# ---------- entries vs stars bins ----------
bins = [0, 50, 100, 200, 400, 800, 1600, 100000]
L['entries_bin'] = pd.cut(L['n_entries'], bins)
eb = L.groupby('entries_bin', observed=True).agg(n=('repo', 'size'), median_stars=('stars', 'median'), p90_stars=('stars', lambda v: v.quantile(.9))).reset_index()
eb['entries_bin'] = eb['entries_bin'].astype(str)
eb.to_csv(OUT + 'entries_bins.csv', index=False)
print(eb.to_string(index=False))

# ---------- save enriched list table ----------
keep = ['repo', 'stars', 'tier', 'kind', 'first_year', 'age_years', 'n_entries', 'desc_ratio', 'avg_desc_words', 'n_sections_with_items',
        'n_authors', 'top1_author_share', 'n_mergers', 'n_commits', 'commits_last_365d', 'authors_last_365d', 'days_since_last_commit',
        'max_issue_ref', 'has_toc', 'has_contributing', 'contributing_words', 'has_pr_template', 'has_issue_template', 'ci_any', 'ci_linkcheck_any',
        'ci_awesome_lint', 'license', 'sponsor', 'has_translations', 'n_readme_translations', 'in_index', 'index_section', 'awesome_named',
        'chinese', 'has_metadata_tags', 'alphabetical', 'readme_generated_marker', 'bot_share_last_365d',
        'h_peak_entries', 'h_cur_entries', 'h_drop_from_peak', 'h_entries_1y', 'h_max_q_drop', 'desc']
L[keep].sort_values('stars', ascending=False).to_csv(OUT + 'lists_enriched.csv', index=False)
print('saved')
