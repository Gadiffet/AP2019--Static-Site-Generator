import markdown
import os
import sys
import subprocess

subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "../requirement.txt"])

def convertToHTML(convertToHTML):
    exts = ['markdown.extensions.extra', 'markdown.extensions.codehilite','markdown.extensions.tables','markdown.extensions.toc']

    html = '''
<html lang="zh-cn">
<head>
<meta content="text/html; charset=utf-8" http-equiv="content-type" />
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous">
</head>
<body>
%s
</body>
</html>
           '''

    ret = markdown.markdown(convertToHTML,extensions=exts)
    return html % ret

def question():
    while "the answer is invalid":
        reponse = str(input("Voulez vous lancer un serveur ? [y/n] : ")).lower().strip()
        if reponse[:1] == 'y':
            return True
        if reponse[:1] == 'n':
            return False
    return reponse[:1]

if __name__ == '__main__':

    if len(sys.argv) < 3:
        print('usage: main.py some_markdown.md name_of_fill_you_want.html')
        sys.exit()

    infile = open(sys.argv[1],'r')
    md = infile.read()
    infile.close()

    
    if os.path.exists(sys.argv[2]):
        os.remove(sys.argv[2])


    outfile = open(sys.argv[2],'w')
    outfile.write(convertToHTML(md))
    outfile.close()

    print('Convertion %s vers %s success!'%(sys.argv[1],sys.argv[2]))

    if question() == True :
        subprocess.check_call([sys.executable, "-m", "http.server"])
    else :
        print('La convertion est faite sans un serveur')