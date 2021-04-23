#entrer ici vos script perssonel
from main import *
#/!\ ne pas suprimer les import

def fonction_test_1() :
    tkinter.messagebox.showerror('fonction 1','info : fonction n°1')

def fonction_test_2() :
    tkinter.messagebox.showerror('foncrion 2','info : fonction n°2')

fonction_liste = [
        #["nom de la fonction pour le menu", nom_de_la_fonction_dans_python]
        ["fonction n°1", fonction_test_1], 
        ["fonction n°2", fonction_test_2]
    ]