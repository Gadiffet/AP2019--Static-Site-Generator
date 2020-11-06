import os
import sys
import subprocess
import shutil

subprocess.check_call([sys.executable, "-m", "pip",
                       "install", "-r", "../requirements.txt"])

from jinja2 import Environment, FileSystemLoader
from markdown2 import markdown


env = Environment(loader=FileSystemLoader(searchpath='./'))
template = env.get_template('template.html')

markdownFolder = sys.argv[1]
htmlFolder = sys.argv[2]


if len(sys.argv) < 3:
    print('usage: main.py markdown_folder html_folder')
    sys.exit()

x = 0

if os.path.exists(htmlFolder):
    shutil.rmtree(htmlFolder)
    os.mkdir(htmlFolder)
else:
    os.mkdir(htmlFolder)

with os.scandir(markdownFolder) as markdownFileInFolder:
    for fileMarkdown in markdownFileInFolder:
        markdownName = str(fileMarkdown.name)
        if markdownName.endswith('.md') :
            with open('./' + markdownFolder + '/' + markdownName, 'r') as infile:
                site = markdown(
                    infile.read(),
                    extras=['tables', 'codehilite', 'toc', 'nl2br', 'fenced-code-blocks',
                            'abbr', 'attr_list', 'def_list', 'footnotes', 'md_in_html', 'pymdownx.emoji']
                )
                infile.close()

            #On récupère le nom du fichier MarkDown SANS l'extension
            nameFileMarkdown, extension = os.path.splitext(markdownName)

            #Ecriture de la convertion dans un fichier HTML
            with open('./' + htmlFolder + '/' + nameFileMarkdown + '.html', 'x') as outfile:
                outfile.write(
                    template.render(
                        article=site,
                        title=nameFileMarkdown
                    )
                )
                outfile.close()
        else :
            x = x + 1
            print("\n*----*\n ")
            print("*-- " + str(x) + " fichier n'ont pas était converti car il ne comporte pas l'extension MarkDown --*\n")
            print("*----*\n ")