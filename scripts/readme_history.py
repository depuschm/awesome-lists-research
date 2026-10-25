"""Quarterly README growth history from a partial clone.

For each quarter end between the first commit and today, take the last commit on HEAD before that
date, find its root README blob, batch-fetch missing blobs, and record bytes / entries / headings.
Usage: python3 -I readme_history.py <clone_dir> ...   -> JSON lines {repo, points:[[date, bytes, entries, h2+h3]]}
"""
import datetime, json, os, re, subprocess, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from extract import normalize_md, scan_entries  # noqa: E402


def git(d, *args, inp=None):
    return subprocess.run(['git', '-C', d, *args], input=inp, capture_output=True, text=True, errors='replace').stdout


def count_entries(txt):
    body = normalize_md(txt)
    return scan_entries(body.splitlines())['n_entries'], len(re.findall(r'(?m)^#{2,3}\s', body))


def main():
    for d in sys.argv[1:]:
        repo = os.path.basename(d.rstrip('/')).replace('__', '/', 1)
        log = git(d, 'log', '--first-parent', '--format=%H %ct', 'HEAD').split()
        commits = list(zip(log[0::2], map(int, log[1::2])))  # newest first
        if not commits:
            continue
        first = min(t for _, t in commits)
        start = datetime.date.fromtimestamp(first)
        q = datetime.date(start.year, ((start.month - 1) // 3) * 3 + 1, 1)
        samples = []
        while True:
            q = datetime.date(q.year + (q.month + 3 > 12), (q.month + 3 - 1) % 12 + 1, 1)
            ts = int(datetime.datetime(q.year, q.month, q.day, tzinfo=datetime.timezone.utc).timestamp())
            sha = next((h for h, t in commits if t < ts), None)
            if sha:
                samples.append((q.isoformat(), sha))
            if q > datetime.date(2026, 10, 25):
                break
        # resolve README blob per sample
        blobs = {}
        for date, sha in samples:
            tree = git(d, 'ls-tree', sha)
            cands = []
            for line in tree.splitlines():
                meta, name = line.split('\t', 1)
                if re.match(r'(?i)^readme(\.(md|markdown|mdown|rst|txt))?$', name) and meta.split()[1] == 'blob':
                    cands.append((not name.lower().endswith(('.md', '.markdown')), name != 'README.md', meta.split()[2]))
            if cands:
                blobs[date] = sorted(cands)[0][2]
        oids = sorted(set(blobs.values()))
        missing = git(d, 'cat-file', '--batch-check=%(objectname) %(objecttype)', inp='\n'.join(oids) + '\n')
        need = [l.split()[0] for l in missing.splitlines() if l.endswith('missing')]
        if need:
            subprocess.run(['git', '-C', d, '-c', 'fetch.negotiationAlgorithm=noop', 'fetch', 'origin', '--no-tags',
                            '--no-write-fetch-head', '--recurse-submodules=no', '--filter=blob:none', '--stdin'],
                           input='\n'.join(need) + '\n', capture_output=True, text=True, timeout=600)
        cache, points = {}, []
        for date, _ in samples:
            oid = blobs.get(date)
            if not oid:
                points.append([date, 0, 0, 0])
                continue
            if oid not in cache:
                txt = git(d, 'cat-file', '-p', oid)
                cache[oid] = (len(txt.encode('utf-8')),) + count_entries(txt)
            points.append([date, *cache[oid]])
        print(json.dumps({'repo': repo, 'points': points}), flush=True)


if __name__ == '__main__':
    main()
