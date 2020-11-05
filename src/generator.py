from markdown2 import markdown
from jinja2 import Environment, FileSystemLoader
import menu
import os
import sys
import subprocess
import shutil

env = Environment(loader=FileSystemLoader(searchpath='./'))
template = env.get_template('template.html')


def oneFile(markdownFile, htmlFile):

    nameHtmlFile, extension = os.path.splitext(htmlFile)

    if markdownFile.endswith('.md') and htmlFile.endswith('html') and nameHtmlFile.isalpha() is True:

        with open('./conversion/' + markdownFile, 'r') as infile:
            site = markdown(
                infile.read(),
                extras=['tables', 'codehilite', 'toc', 'nl2br', 'fenced-code-blocks',
                        'abbr', 'attr_list', 'def_list', 'footnotes', 'md_in_html', 'pymdownx.emoji']
            )
            infile.close()

        if os.path.exists('./conversion/' + htmlFile):
            os.remove('./conversion/' + htmlFile)

        with open('./conversion/' + htmlFile, 'x') as outfile:
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

        menu.menuDeploy(htmlFile)

    else:
        print("\n*----*\n ")
        print("*-- Votre fichier comporte une extension différente du MarkDown ou bien le nom de votre fichier HTML n’est pas correct --*")
        print("*-- Merci de bien vouloir réessayer --*\n")
        print("*----*\n ")
        menu.menuOneFile()


def folder(markdownFolder, htmlFolder):
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