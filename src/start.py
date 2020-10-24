import sys
import subprocess
import menu

subprocess.check_call([sys.executable, "-m", "pip",
                       "install", "-r", "../requirement.txt"])

if __name__ == '__main__':
    menu.menuPrincipal()
