#!/bin/bash
set -e
mkdir temp
for file_path in ./docs/*.md
do
  echo "Generating Pseudo HTML Code"
  echo '================================================'
  echo "$file_path"
  file_name=$(echo "$file_path" | sed 's/^\.\/docs\///')
  marked -i "$file_path" -o "temp/$file_name"
  echo "Generating HTML Formatted Document"
  echo '================================================'
  python3 $PWD/scripts/format-pseudo-html.py "temp/$file_name"
  file_name_without_extension=$(echo "$file_name" | sed 's/\.md$//')
  mv "temp/$file_name" "pages/$file_name_without_extension.html"
  echo "Generating Styles"
  echo '================================================'
  sed -i 's/<pre><code>/<pre><code class="language-py">/g' "pages/$file_name_without_extension.html"
done
rm -rf temp
python3 ./scripts/generate-list.py
echo "Done"
