import generator
import deploy
import sys
import os


def menuPrincipal():
    while "the answer is invalid":
        print("*----*\n ")
        print("*-- Bienvenue dans le generateur de site Web Static --*\n")
        print("*-- 1: Convertir 1 fichier MarkDown en fichier HTML --*")
        print("*-- 2: Convertir 1 dossier MarkDown en dossier HTML --*")
        print("*-- 3: Convertir 1 projet Git en dossier HTML       --*")
        print("*-- 4: Convertir 1 preojet HTTP en dossier HTML     --*\n")
        print("*-- 0: Quitter le generateur                        --*\n")
        print("*----*\n ")
        reponse = str(
            input("Que souhaitez vous faire : ")).lower().strip()
        if reponse[:1] == '1':
            menuOneFile()
        if reponse[:1] == '2':
            menuFolder()
        if reponse[:1] == '0':
            sys.exit()
    return reponse[:1]


def menuOneFile():
    while "the answer is invalid":
        print("\n*----*\n ")
        print("*-- Vous avez choisi de convertir 1 fichier MarkDown--*")
        print("*-- 1: Convertir mon fichier MarkDown               --*\n")
        print("*-- 0: Retour au Menu Principal                     --*\n")
        print("*----*\n ")
        reponse = str(
            input("Que souhaitez vous faire : ")).lower().strip()

        if reponse[:1] == '1':
            markdownFile = str(
                input("Veuillez entrer le nom de votre fichier MarkDown : "))

            name, extension = os.path.splitext(markdownFile)
            if not extension:
                markdownFile = markdownFile + '.md'

            htmlFile = str(
                input("Veuillez entrer le nom que vous souhaitez pour votre fichier HTML : "))

            name, extension = os.path.splitext(htmlFile)
            if not extension:
                htmlFile = htmlFile + '.html'

            generator.oneFile(markdownFile, htmlFile)

        if reponse[:1] == '0':
            menuPrincipal()

def menuFolder():
    while "the answer is invalid":
        print("\n*----*\n ")
        print("*-- Vous avez choisi de convertir 1 dossier MarkDown --*")
        print("*-- 1: Convertir mon dossier MarkDown                --*\n")
        print("*-- 0: Retour au Menu Principal                      --*\n")
        print("*----*\n ")
        reponse = str(
            input("Que souhaitez vous faire : ")).lower().strip()

        if reponse[:1] == '1':
            markdownFolder = str(
                input("Veuillez entrer le nom de votre dossier MarkDown : "))


            htmlFolder = str(
                input("Veuillez entrer le nom que vous souhaitez pour votre dossier HTML : "))

            generator.oneFile(markdownFolder, htmlFolder)

        if reponse[:1] == '0':
            menuPrincipal()

def menuDeploy():
    while "the answer is invalid":
        print("\n*----*\n ")
        print("*-- Votre Projet est converti, et maintenant :      --*")
        print("*-- 1: Lancer un serveur Local                      --*")
        print("*-- 2: Deployer mon Projet au monde entier          --*\n")
        print("*-- 3: Quitter                                      --*\n")
        print("*----*\n ")
        reponse = str(
            input("Que souhaitez vous faire ?")).lower().strip()
        if reponse[:1] == '1':
            deploy.local()
        if reponse[:1] == '2':
            return False
        if reponse[:1] == '3':
            return False
    return reponse[:1]
