from tkinter import *
from arduino import *
from body import *
import configparser
import os
import tkinter.messagebox

cfg = configparser.ConfigParser()
cfg.read('config/info.ini')

scal = -1

inti_arduino_1 = False
inti_arduino_2 = False

index = 0

def moteur_head_3(position):
    import main
    global moteur_speak
    main.moteur_speak.set(position)
    #mouvement bouche
    angle = int(cfg["moteurs"]["bouche_tete_max"])-int(cfg["moteurs"]["bouche_tete_min"])
    angle = ((float(position)/100) * angle) + float(cfg["moteurs"]["bouche_tete_min"])
    print("head 3 : " + str(int(angle)))
    if int(cfg["moteurs"]["bouche_tete_arduino"]) == 1 :
        controle_moteur_1(int(cfg["moteurs"]["bouche_tete_pin"]), int(angle))
    else :
        controle_moteur_2(int(cfg["moteurs"]["bouche_tete_pin"]), int(angle))

def moteur_head_3_speak(position):
    import main
    global moteur_3_h
    main.moteur_3_h.set(position)
    #mouvement bouche
    angle = int(cfg["moteurs"]["bouche_tete_max"])-int(cfg["moteurs"]["bouche_tete_min"])
    angle = ((float(position)/100) * angle) + float(cfg["moteurs"]["bouche_tete_min"])
    print("head 3 : " + str(int(angle)))
    if int(cfg["moteurs"]["bouche_tete_arduino"]) == 1 :
        controle_moteur_1(int(cfg["moteurs"]["bouche_tete_pin"]), int(angle))
    else :
        controle_moteur_2(int(cfg["moteurs"]["bouche_tete_pin"]), int(angle))

def show_accueil():
    import main
    global index
    main.screen[index].pack_forget()
    index = 0
    print("Page accueil")
    main.screen[index].pack(fill = X)

def show_head():
    import main
    global index
    main.screen[index].pack_forget()
    index = 1
    print("Page controle de la tête")
    main.screen[index].pack(fill = X)

def right_arm_page():
    import main
    global index
    main.screen[index].pack_forget()
    index = 3
    print("page de gestion du bras droit")
    main.screen[index].pack(fill = X)

def left_arm_page():
    import main
    global index
    main.screen[index].pack_forget()
    index = 2
    print("page de gestion du bras gauche")
    main.screen[index].pack(fill = X)

def hand_page():
    import main
    global index
    main.screen[index].pack_forget()
    index = 5
    print("page de gestion des mains")
    main.screen[index].pack(fill = X)

def stomach_page():
    import main
    global index
    main.screen[index].pack_forget()
    index = 4
    print("page de gestion du bassin")
    main.screen[index].pack(fill = X)


def speak_page():
    import main
    global index
    main.screen[index].pack_forget()
    index = 6
    print("page de gestion des paroles")
    main.screen[index].pack(fill = X)

def conect_1():
    import main
    global inti_arduino_1
    if connection_robot_1() :
        main.btn.config(bg = "green", command = NONE, text = "Arduino n°1 : CONNECTER")
        main.btn.update()
    else :
        main.btn.config(bg = "black")
        main.btn.update()
        if inti_arduino_1 :
            tkinter.messagebox.showerror('erreur','conexion à l\'arduino n°1 Impossible')
    inti_arduino_1 = True

def conect_2():
    import main
    global inti_arduino_2
    if connection_robot_2() :
        main.btn2.config(bg = "green", command = NONE, text = "Arduino n°2 : CONNECTER")
        main.btn2.update()
    else :
        main.btn2.config(bg = "black")
        main.btn2.update()
        if inti_arduino_2 :
            tkinter.messagebox.showerror('erreur','conexion à l\'arduino n°2 Impossible')
    inti_arduino_2 = True

# touche a
def moteur_1_clavier(k):
    import main
    global moteur_selectioner, index, scal
    if index == 1 :
        def moteur_selectioner(x):
            moteur_head_1(x)
        scal = main.moteur_1_h
    if index == 2 :
        def moteur_selectioner(x):
            moteur_left_arm_1(x)
        scal = main.moteur_1_la
    if index == 3 :
        def moteur_selectioner(x):
            moteur_right_arm_1(x)
        scal = main.moteur_1_ra

#touche z
def moteur_2_clavier(k):
    import main
    global moteur_selectioner, index, scal
    if index == 1 :
        def moteur_selectioner(x):
            moteur_head_2(x)
        scal = main.moteur_2_h
    if index == 2 :
        def moteur_selectioner(x):
            moteur_left_arm_2(x)
        scal = main.moteur_2_la
    if index == 3 :
        def moteur_selectioner(x):
            moteur_right_arm_2(x)
        scal = main.moteur_2_ra
    print("moteur 2 selectioner")

#touche e
def moteur_3_clavier(k):
    import main
    global moteur_selectioner, index, scal
    if index == 1 :
        def moteur_selectioner(x):
            moteur_head_3(x)
        scal = main.moteur_3_h
    if index == 2 :
        def moteur_selectioner(x):
            moteur_left_arm_3(x)
        scal = main.moteur_3_la
    if index == 3 :
        def moteur_selectioner(x):
            moteur_right_arm_3(x)
        scal = main.moteur_3_ra

#touche r
def moteur_4_clavier(k):
    import main
    global moteur_selectioner, index, scal
    if index == 1 :
        def moteur_selectioner(x):
            moteur_head_4(x)
        scal = main.moteur_4_h
    if index == 2 :
        def moteur_selectioner(x):
            moteur_left_arm_4(x)
        scal = main.moteur_4_la
    if index == 3 :
        def moteur_selectioner(x):
            moteur_right_arm_4(x)
        scal = main.moteur_4_ra

#touche t
def moteur_5_clavier(k):
    global moteur_selectioner, index, scal
    if index == 1 :
        def moteur_selectioner(x):
            moteur_head_5(x)
        scal = main.moteur_5_h

#touche <
def soustraction_clavier(k):
    global moteur_selectioner, scal
    if scal != -1 :
        val = scal.get()
        val += -2
        scal.set(val)
        print(val)

#touche >
def adition_clavier(k):
    global moteur_selectioner, scal
    if scal != -1 :
        val = scal.get()
        val += 2
        scal.set(val)
        print(val)

def fonction_speak():
    global entrer_text
    say(entrer_text.get())

#touche entrer
def entrer_clavier(k):
    print("entrer")
    global entrer_text, index
    if index == 6 :
        say(entrer_text.get())
        
def say(text):
    import main
    fichier = open("temp_lecture", "w")
    fichier.write(text)
    fichier.close()
    deconnection_robot()
    os.system("py speak.py")
    main.moteur_speak.set(0)
    main.moteur_3_h.set(0)
    connection_robot()
