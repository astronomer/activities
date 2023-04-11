echo "Generating Pseudo HTML Code"
marked -i README.md -o pseudo.html
echo "Generating HTML Formatted Document"
python3 ./static/format-pseudo-html.py
rm pseudo.html
echo "Generating Styles"
sed -i 's/<pre><code>/<pre><code class="language-py">/g' index.html
echo "Done"
