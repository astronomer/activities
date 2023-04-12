import os
from jinja2 import Environment, FileSystemLoader

BASE_DIRECTORY = os.getcwd()

# Set up Jinja environment
env = Environment(loader=FileSystemLoader(BASE_DIRECTORY+'/templates'))

# Get list of file names in folder
folder_path = BASE_DIRECTORY+'/pages'
file_names = os.listdir(folder_path)

# Create list of chapter names
chapters = []
for file_name in file_names:
    if file_name.endswith('.html'):
        chapter_name = file_name.replace('.html', '').title()
        chapters.append(chapter_name)

# Update index.html using Jinja template
template = env.get_template('index_template.html')
output = template.render(chapters=chapters)
with open(BASE_DIRECTORY+'/index.html', 'w') as f:
    f.write(output)
