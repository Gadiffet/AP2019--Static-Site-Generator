import sys
from subprocess import check_call
import os

check_call([sys.executable, "-m", "pip",
                       "install", "-r", "../requirements.txt"])

if __name__ == '__main__':
    import menu
    menu.menuPrincipal()
