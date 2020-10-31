from markdown2 import markdown
from jinja2 import Environment, FileSystemLoader
from json import load
import menu
import os
import sys
import subprocess
from shutil import copyfile

env = Environment(loader=FileSystemLoader(searchpath='./'))
template = env.get_template('template.html')

def oneFile(markdownFile, htmlFile):

    if markdownFile.endswith('.md') and htmlFile.endswith('html'):

        with open(markdownFile, 'r') as infile :
            site = markdown(
                infile.read(),
                extras= ['tables', 'codehilite', 'toc', 'nl2br', 'fenced-code-blocks', 'abbr', 'attr_list', 'def_list', 'footnotes', "md_in_html"]
            )
            infile.close()

        with open("config.json") as config_file:
            config = load(config_file)

        if os.path.exists(htmlFile):
            os.remove(htmlFile)
        
        with open(htmlFile, 'x') as outfile :
            outfile.write(
                template.render(
                    article = site,
                    title = config['title']
                )
            )
            outfile.close()
    else:
        print("\n*----*\n ")
        print("*-- Votre fichier comporte une extension differente du MarkDown ou de l'HTML --*")
        print("*-- Merci de bien vouloir réessayer --*\n")
        print("*----*\n ")
        menu.menuOneFile()