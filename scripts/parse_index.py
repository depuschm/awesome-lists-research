"""Parse sindresorhus/awesome readme.md into (section, subsection, repo, name, description)."""
import re, sys, csv
path, out = sys.argv[1], sys.argv[2]
sec = sub = ''
rows = []
item = re.compile(r'^(\s*)- \[([^\]]+)\]\((https?://github\.com/([^/)#\s]+)/([^/)#\s]+))[^)]*\)\s*(?:-\s*(.*))?$')
for line in open(path, encoding='utf-8'):
    if line.startswith('## '): sec, sub = line[3:].strip(), ''
    elif line.startswith('### '): sub = line[4:].strip()
    m = item.match(line.rstrip('\n'))
    if m and sec not in ('Contents', 'Related', 'Footnotes'):
        indent, name, url, owner, repo, desc = m.groups()
        repo = repo.removesuffix('.git')
        rows.append([sec, sub if not indent else sub, f'{owner}/{repo}', name, (desc or '').strip(), 1 if indent else 0])
w = csv.writer(open(out, 'w', newline=''), delimiter='\t')
w.writerow(['section', 'subsection', 'repo', 'name', 'description', 'nested'])
w.writerows(rows)
print(len(rows), 'entries;', len({r[2].lower() for r in rows}), 'unique repos;', len({r[0] for r in rows}), 'sections')
