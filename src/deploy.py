import sys
import os
import app
from subprocess import check_call

def local():
    check_call([sys.executable, "-m", "http.server"])

def web(htmlFile):
    app.route(htmlFile)
    os.system("git add .")
    os.system("git commit -am ' feat(deploy): Add "+ htmlFile+"'")
    os.system("git push heroku main")
