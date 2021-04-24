#entrer ici vos script perssonel
from main import *
from arduino import *
#/!\ ne pas suprimer les imports

etat_1 = False

def fonction_test_1() :
    global etat_1
    arduino1.pinMode(13,1)
    arduino1.digitalWrite(13, not(etat_1))
    etat_1 = not(etat_1)

def fonction_test_2() :
    arduino2.pinMode(14,0)
    valeur_pin_A0 = arduino2.analogRead(14)
    tkinter.messagebox.showerror('fonction 2',('pin A0 : ' + str(valeur_pin_A0)))

#ajouter dans cette liste vos fontion pour les retrouver dans le menu de l'aplication
fonction_liste = [
        #["nom de la fonction pour le menu", nom_de_la_fonction_dans_python]
        ["switch arduino n°1 pin 13", fonction_test_1], 
        ["lecture analogique A0 de ardunio n°2", fonction_test_2]
    ]