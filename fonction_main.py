from tkinter import *
from arduino import *
from speechrecognition_ import *
from body import *
import configparser
import os
import tkinter.messagebox
import threading
import time

cfg = configparser.ConfigParser()
cfg.read('config/info.ini')

scal = -1
index = 0

#changement de page du menu
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

def voice_page():
    import main
    global index
    main.screen[index].pack_forget()
    index = 7
    print("page de reconaissance vocal")
    main.screen[index].pack(fill = X)

def full_controle_page():
    import main
    global index
    main.screen[index].pack_forget()
    index = 8
    print("page de controle general")
    main.screen[index].pack(fill = X)

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
    if index == 4 :
        def moteur_selectioner(x):
            moteur_bassin_1(x)
        scal = main.moteur_1_b
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
    if index == 4 :
        def moteur_selectioner(x):
            moteur_bassin_2(x)
        scal = main.moteur_2_b
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
    import main
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
#touche entrer
def entrer_clavier(k):
    import main
    print("entrer")
    global index
    if index == 6 :
        say(main.entrer_text.get())


#fonction pour la parole
def fonction_speak():
    import main
    say(main.entrer_text.get())

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

i = 99

def vocal_start_stop_thread():
    import main
    global i 
    i = main.vocal_etat.get()
    print("vocal start")
    print(i)
    t = threading.Thread(target=vocal_start_stop)
    t.start()

def vocal_start_stop():
    global i
    while i == 1 :
        speak_recognition()

def position_init():
    import main

    print("-->Position de repos")

    moove.head.rotation(int(cfg["moteurs"]["rotation_tete_ini"]))
    main.moteur_1_h.set(int(cfg["moteurs"]["rotation_tete_ini"]))
    main.moteur_1_f.set(int(cfg["moteurs"]["rotation_tete_ini"]))

    moove.head.up_down(int(cfg["moteurs"]["elevation_tete_ini"]))
    main.moteur_2_h.set(int(cfg["moteurs"]["elevation_tete_ini"]))
    main.moteur_2_f.set(int(cfg["moteurs"]["elevation_tete_ini"]))

    moove.head.mouth(int(cfg["moteurs"]["bouche_tete_ini"]))
    main.moteur_3_h.set(int(cfg["moteurs"]["bouche_tete_ini"]))
    main.moteur_3_f.set(int(cfg["moteurs"]["bouche_tete_ini"]))

    moove.head.eyes_x(int(cfg["moteurs"]["yeux_x_tete_ini"]))
    main.moteur_4_h.set(int(cfg["moteurs"]["yeux_x_tete_ini"]))
    main.moteur_4_f.set(int(cfg["moteurs"]["yeux_x_tete_ini"]))

    moove.head.eyes_y(int(cfg["moteurs"]["yeux_y_tete_ini"]))
    main.moteur_5_h.set(int(cfg["moteurs"]["yeux_y_tete_ini"]))
    main.moteur_5_f.set(int(cfg["moteurs"]["yeux_y_tete_ini"]))

    moove.left_arm.shoulder_x(int(cfg["moteurs"]["epaule_x_left_ini"]))
    main.moteur_1_la.set(int(cfg["moteurs"]["epaule_x_left_ini"]))
    main.moteur_6_f.set(int(cfg["moteurs"]["epaule_x_left_ini"]))

    moove.left_arm.shoulder_y(int(cfg["moteurs"]["epaule_y_left_ini"]))
    main.moteur_2_la.set(int(cfg["moteurs"]["epaule_y_left_ini"]))
    main.moteur_7_f.set(int(cfg["moteurs"]["epaule_y_left_ini"]))

    moove.left_arm.shoulder_z(int(cfg["moteurs"]["epaule_z_left_ini"]))
    main.moteur_3_la.set(int(cfg["moteurs"]["epaule_z_left_ini"]))
    main.moteur_8_f.set(int(cfg["moteurs"]["epaule_z_left_ini"]))

    moove.left_arm.elbow(int(cfg["moteurs"]["coude_left_ini"]))
    main.moteur_4_la.set(int(cfg["moteurs"]["coude_left_ini"]))
    main.moteur_9_f.set(int(cfg["moteurs"]["coude_left_ini"]))

    moove.right_arm.shoulder_x(int(cfg["moteurs"]["epaule_x_right_ini"]))
    main.moteur_1_ra.set(int(cfg["moteurs"]["epaule_x_right_ini"]))
    main.moteur_10_f.set(int(cfg["moteurs"]["epaule_x_right_ini"]))

    moove.right_arm.shoulder_y(int(cfg["moteurs"]["epaule_y_right_ini"]))
    main.moteur_2_ra.set(int(cfg["moteurs"]["epaule_y_right_ini"]))
    main.moteur_11_f.set(int(cfg["moteurs"]["epaule_y_right_ini"]))

    moove.right_arm.shoulder_z(int(cfg["moteurs"]["epaule_z_right_ini"]))
    main.moteur_3_ra.set(int(cfg["moteurs"]["epaule_z_right_ini"]))
    main.moteur_12_f.set(int(cfg["moteurs"]["epaule_z_right_ini"]))

    moove.right_arm.elbow(int(cfg["moteurs"]["coude_right_ini"]))
    main.moteur_4_ra.set(int(cfg["moteurs"]["coude_right_ini"]))
    main.moteur_13_f.set(int(cfg["moteurs"]["coude_right_ini"]))

    moove.left_hand.all(int(cfg["moteurs"]["hand_left_ini"]))
    main.moteur_lh.set(int(cfg["moteurs"]["hand_left_ini"]))
    main.moteur_14_f.set(int(cfg["moteurs"]["hand_left_ini"]))

    moove.right_hand.all(int(cfg["moteurs"]["hand_right_ini"]))
    main.moteur_rh.set(int(cfg["moteurs"]["hand_right_ini"]))
    main.moteur_15_f.set(int(cfg["moteurs"]["hand_right_ini"]))

    moove.pelvis.rocker(int(cfg["moteurs"]["bascule_bassin_ini"]))
    main.moteur_1_b.set(int(cfg["moteurs"]["bascule_bassin_ini"]))
    main.moteur_17_f.set(int(cfg["moteurs"]["bascule_bassin_ini"]))

    moove.pelvis.rotation(int(cfg["moteurs"]["rotation_bassin_ini"]))
    main.moteur_2_b.set(int(cfg["moteurs"]["rotation_bassin_ini"]))
    main.moteur_16_f.set(int(cfg["moteurs"]["rotation_bassin_ini"]))
