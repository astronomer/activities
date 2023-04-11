import markdown2

# Read in the markdown file
with open('temp.html', 'r') as file:
    markdown = file.read()

# Convert the markdown to HTML
# html = markdown2.markdown(markdown)
html = markdown
# Define a template for the GitHub README
template = """
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>My GitHub README</title>
  <link rel="stylesheet" href="./static/styles.css" />
</head>
<body>
  <article>
    {}
  </article>
  <script src="./static/script.js"></script>
</body>
</html>
"""

# Format the HTML with the template
formatted_html = template.format(html)

# Write the GitHub-formatted HTML to a file
with open('index.html', 'w') as file:
    file.write(formatted_html)
