#!/bin/bash
# Partial, sparse clone: all commits+trees, only root files (+ .github) checked out.
repo="$1"; dest="$(cd "$(dirname "$0")/.." && pwd)/clones/${repo/\//__}"
[ -d "$dest/.git" ] && exit 0
if timeout 600 git clone -q --filter=blob:none --sparse "https://github.com/$repo" "$dest" 2>/tmp/clone_err_$$; then
  timeout 120 git -C "$dest" sparse-checkout add .github >/dev/null 2>&1
  echo "OK $repo"
else
  echo "FAIL $repo $(tr '\n' ' ' </tmp/clone_err_$$ | cut -c1-200)"; rm -rf "$dest"
fi
rm -f /tmp/clone_err_$$
