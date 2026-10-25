#!/bin/bash
# Partial, sparse clone: all commits+trees, only root files (+ .github) checked out.
# Usage: clone_one.sh owner/repo [sha]   (sha: pin to the snapshot listed in data/repositories.tsv)
repo="$1"; sha="$2"; dest="$(cd "$(dirname "$0")/.." && pwd)/clones/${repo/\//__}"
[ -d "$dest/.git" ] && exit 0
if timeout 600 git clone -q --filter=blob:none --sparse "https://github.com/$repo" "$dest" 2>/tmp/clone_err_$$; then
  timeout 120 git -C "$dest" sparse-checkout add .github >/dev/null 2>&1
  if [ -n "$sha" ]; then
    git -C "$dest" checkout -q --detach "$sha" 2>/dev/null ||
      { timeout 120 git -C "$dest" fetch -q --filter=blob:none origin "$sha" 2>/dev/null && git -C "$dest" checkout -q --detach "$sha" 2>/dev/null; } ||
      echo "WARN $repo: pinned commit $sha not found; using current HEAD"
  fi
  echo "OK $repo"
else
  echo "FAIL $repo $(tr '\n' ' ' </tmp/clone_err_$$ | cut -c1-200)"; rm -rf "$dest"
fi
rm -f /tmp/clone_err_$$
