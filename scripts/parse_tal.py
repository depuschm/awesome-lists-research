"""Parse trackawesomelist README (All Tracked List + Top 50) -> repo, name, stars, last_update, category."""
import re, sys, csv
src, out = sys.argv[1], sys.argv[2]
def num(s):
    s = s.replace(',', '').strip().upper()
    mult = 1000 if s.endswith('K') else 1
    return int(round(float(s.rstrip('K')) * mult))
rows, cat, mode = {}, '', None
for line in open(src, encoding='utf-8'):
    if line.startswith('## '):
        mode = line[3:].strip()
    elif line.startswith('### ') and mode == 'All Tracked List':
        cat = line[4:].strip()
    if mode == 'All Tracked List':
        m = re.match(r'^\s*- \[([^\]]+)\]\(/content/[^)]*\) - \(\[Source ⭐ ([\d.,Kk]+), 📝 ([^\]]+?)\s*\]\(https://github\.com/([^/]+/[^/)#]+)[^)]*\)\) - ?(.*)$', line)
        if m:
            name, st, upd, repo, desc = m.groups()
            rows.setdefault(repo.lower(), [repo, name, num(st), upd.replace('&#x2F;', '/'), cat, desc.strip()])
    elif mode == 'Top 50 Awesome List':
        m = re.match(r'^\d+\. \[([^\]]+)\]\(/content/[^)]*\) - \(\[Source\]\(https://github\.com/([^/]+/[^/)#]+)\) ⭐ ([\d.,Kk]+) 📝 ([^)]+)\) - ?(.*)$', line)
        if m:
            name, repo, st, upd, desc = m.groups()
            rows.setdefault(repo.lower(), [repo, name, num(st), upd.replace('&#x2F;', '/'), 'TOP50', desc.strip()])
w = csv.writer(open(out, 'w', newline=''), delimiter='\t')
w.writerow(['repo', 'name', 'stars', 'last_update', 'tal_category', 'description'])
for r in sorted(rows.values(), key=lambda r: -r[2]): w.writerow(r)
st = sorted([r[2] for r in rows.values()])
print(len(rows), 'lists; median stars', st[len(st)//2], '; >=10k:', sum(s>=10000 for s in st), '; <1k:', sum(s<1000 for s in st))
