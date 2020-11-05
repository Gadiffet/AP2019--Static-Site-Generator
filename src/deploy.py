import sys
from subprocess import check_call

def local():
    check_call([sys.executable, "-m", "http.server"])