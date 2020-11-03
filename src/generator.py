from markdown2 import markdown
from jinja2 import Environment, FileSystemLoader
import menu
import os
import sys
import subprocess
from shutil import copyfile

env = Environment(loader=FileSystemLoader(searchpath='./'))
template = env.get_template('template.html')

def oneFile(markdownFile, htmlFile):

    nameHtmlFile, extension = os.path.splitext(htmlFile)

    if markdownFile.endswith('.md') and htmlFile.endswith('html') and nameHtmlFile.isalpha() is True :

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
        print("\n*----*\n ")
        print("*-- FICHIER CONVERTI --*")
        print("*----*\n ")
    else:
        print("\n*----*\n ")
        print("*-- Votre fichier comporte une extension différente du MarkDown ou bien le nom de votre fichier HTML n’est pas correct --*")
        print("*-- Merci de bien vouloir réessayer --*\n")
        print("*----*\n ")
        menu.menuOneFile()
