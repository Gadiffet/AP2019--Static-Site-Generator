import markdown
import menu
import os
import sys
import subprocess
from shutil import copyfile


def convertToHTML(convertToHTML):
    exts = ['markdown.extensions.extra', 'markdown.extensions.codehilite',
            'markdown.extensions.tables', 'markdown.extensions.toc']

    html = '''
<html lang="fr-en">
    <head>
        <meta content="text/html; charset=utf-8" http-equiv="content-type" />
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous">
    </head>
    <body>
        %s
    </body>
</html>
           '''

    ret = markdown.markdown(convertToHTML, extensions=exts)
    return html % ret


def oneFile(markdownFile, htmlFile):

    if markdownFile.endswith('.md') and htmlFile.endswith('html'):

        infile = open(markdownFile, 'r')
        md = infile.read()
        infile.close()

        if os.path.exists(htmlFile):
            os.remove(htmlFile)

        outfile = open(htmlFile, 'x')
        outfile.write(convertToHTML(md))
        outfile.close()
    else:
        print("\n*----*\n ")
        print("*-- Votre fichier comporte une extension differente du MarkDown ou de l'HTML --*")
        print("*-- Merci de bien vouloir réessayer --*\n")
        print("*----*\n ")
        menu.menuOneFile()
