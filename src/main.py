import markdown
import os
import sys

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

if __name__ == '__main__':

    if len(sys.argv) < 3:
        print('usage: convertToHTML source_filename target_file')
        sys.exit()

    infile = open(sys.argv[1],'r')
    md = infile.read()
    infile.close()

    
    if os.path.exists(sys.argv[2]):
        os.remove(sys.argv[2])


    outfile = open(sys.argv[2],'w')
    outfile.write(convertToHTML(md))
    outfile.close()

    print('convertToHTML %s to %s success!'%(sys.argv[1],sys.argv[2]))

    pip install -r requirement.txt
    gunicorn --bind 0.0.0.0:8000 sys.argv[2]