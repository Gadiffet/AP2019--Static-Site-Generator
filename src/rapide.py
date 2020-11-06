import os
import sys
import subprocess

subprocess.check_call([sys.executable, "-m", "pip",
                       "install", "-r", "../requirements.txt"])

from jinja2 import Environment, FileSystemLoader
from markdown2 import markdown

env = Environment(loader=FileSystemLoader(searchpath='./'))
template = env.get_template('template.html')

markdownFile = sys.argv[1]
htmlFile = sys.argv[2]

nameHtmlFile, extension = os.path.splitext(htmlFile)

if len(sys.argv) < 3:
    print('usage: main.py some_markdown.md name_of_fill_you_want.html')
    sys.exit()


if markdownFile.endswith('.md') and htmlFile.endswith('html') and nameHtmlFile.isalpha() is True:

    with open(markdownFile, 'r') as infile:
        site = markdown(
            infile.read(),
            extras=['tables', 'codehilite', 'toc', 'nl2br', 'fenced-code-blocks',
                    'abbr', 'attr_list', 'def_list', 'footnotes', 'md_in_html', 'pymdownx.emoji']
        )
        infile.close()

    if os.path.exists(htmlFile):
        os.remove(htmlFile)

    with open(htmlFile, 'x') as outfile:
        outfile.write(
            template.render(
                article=site,
                title=nameHtmlFile
            )
        )
        outfile.close()

    print('Conversion %s vers %s success!' % (markdownFile, htmlFile))

else:
    print("\n*----*\n ")
    print("*-- Votre fichier comporte une extension différente du MarkDown ou bien le nom de votre fichier HTML n’est pas correct --*")
    print("*-- Merci de bien vouloir réessayer --*\n")
    print("*----*\n ")