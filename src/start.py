import sys
import subprocess

subprocess.check_call([sys.executable, "-m", "pip",
                       "install", "-r", "../requirement.txt"])

if __name__ == '__main__':
    import menu
    menu.menuPrincipal()
