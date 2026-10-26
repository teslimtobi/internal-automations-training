#!/usr/bin/env bash
# Converts every blog draft in blogs/ to Word and runs the Appnable checker (seo_check.py).
# Fails (exit 1) if any draft has a FIX item, so the pipeline stops before review.
set -uo pipefail
mkdir -p build
status=0
echo "## Blog checklist results" >> "${GITHUB_STEP_SUMMARY:-/dev/null}"
for f in blogs/*.md; do
  name=$(basename "$f" .md)
  kw=$(grep -m1 '^Primary keyword:' "$f" | cut -d: -f2- | xargs)
  sk=$(grep -m1 '^Supporting keywords:' "$f" | cut -d: -f2- | xargs)
  pandoc "$f" -o "build/$name.docx"
  IFS=',' read -ra sup <<< "$sk"
  args=()
  for s in "${sup[@]}"; do s=$(echo "$s" | xargs); [ -n "$s" ] && args+=("$s"); done
  python scripts/seo_check.py "build/$name.docx" --keyword "$kw" --supporting "${args[@]}" | tee "build/$name-check.txt"
  fixes=$(grep -oE '^[0-9]+ FIX item' "build/$name-check.txt" | grep -oE '^[0-9]+')
  if [ "${fixes:-1}" -eq 0 ]; then
    echo "- ✅ **$name**: 0 FIX items, ready for review" >> "${GITHUB_STEP_SUMMARY:-/dev/null}"
  else
    echo "- ❌ **$name**: ${fixes:-?} FIX item(s), see the log" >> "${GITHUB_STEP_SUMMARY:-/dev/null}"
    grep '^\[FIX\]' "build/$name-check.txt" | sed 's/^/  - /' >> "${GITHUB_STEP_SUMMARY:-/dev/null}"
    status=1
  fi
done
exit $status
