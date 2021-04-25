from tkinter import *
from arduino import *
import configparser

cfg = configparser.ConfigParser()
cfg.read('config/info.ini')


### TETE ###
def moteur_head_1(position):
    #rotation tete
    angle = int(cfg["moteurs"]["rotation_tete_max"])-int(cfg["moteurs"]["rotation_tete_min"])
    angle = ((float(position)/100) * angle) + float(cfg["moteurs"]["rotation_tete_min"])
    print("head 1 : " + str(int(angle)))
    if int(cfg["moteurs"]["rotation_tete_arduino"]) == 1 :
        controle_moteur_1(int(cfg["moteurs"]["rotation_tete_pin"]), int(angle))
    else :
        controle_moteur_2(int(cfg["moteurs"]["rotation_tete_pin"]), int(angle))
    
def moteur_head_2(position):
    #mouvement haut bas
    angle = int(cfg["moteurs"]["elevation_tete_max"])-int(cfg["moteurs"]["elevation_tete_min"])
    angle = ((float(position)/100) * angle) + float(cfg["moteurs"]["elevation_tete_min"])
    print("head 2 : " + str(int(angle)))
    if int(cfg["moteurs"]["elevation_tete_arduino"]) == 1 :
        controle_moteur_1(int(cfg["moteurs"]["elevation_tete_pin"]), int(angle))
    else :
        controle_moteur_2(int(cfg["moteurs"]["elevation_tete_pin"]), int(angle))

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

def moteur_head_4(position):
    #mouvement yeux X
    angle = int(cfg["moteurs"]["yeux_x_tete_max"])-int(cfg["moteurs"]["yeux_x_tete_min"])
    angle = ((float(position)/100) * angle) + float(cfg["moteurs"]["yeux_x_tete_min"])
    print("head 4 : " + str(int(angle)))
    if int(cfg["moteurs"]["yeux_x_tete_arduino"]) == 1 :
        controle_moteur_1(int(cfg["moteurs"]["yeux_x_tete_pin"]), int(angle))
    else :
        controle_moteur_2(int(cfg["moteurs"]["yeux_x_tete_pin"]), int(angle))

def moteur_head_5(position):
    #mouvement yeux Y
    angle = int(cfg["moteurs"]["yeux_y_tete_max"])-int(cfg["moteurs"]["yeux_y_tete_min"])
    angle = ((float(position)/100) * angle) + float(cfg["moteurs"]["yeux_y_tete_min"])
    print("head 5 : " + str(int(angle)))
    if int(cfg["moteurs"]["yeux_y_tete_arduino"]) == 1 :
        controle_moteur_1(int(cfg["moteurs"]["yeux_y_tete_pin"]), int(angle))
    else :
        controle_moteur_2(int(cfg["moteurs"]["yeux_y_tete_pin"]), int(angle))

### LEFT ARM ###
def moteur_left_arm_1(position):
    #mouvement epaule gauche x
    angle = int(cfg["moteurs"]["epaule_x_left_max"])-int(cfg["moteurs"]["epaule_x_left_min"])
    angle = ((float(position)/100) * angle) + float(cfg["moteurs"]["epaule_x_left_min"])
    print("left arm 1 : " + str(int(angle)))
    if int(cfg["moteurs"]["epaule_x_left_arduino"]) == 1 :
        controle_moteur_1(int(cfg["moteurs"]["epaule_x_left_pin"]), int(angle))
    else :
        controle_moteur_2(int(cfg["moteurs"]["epaule_x_left_pin"]), int(angle))

def moteur_left_arm_2(position):
    #mouvement epaule gauche y
    angle = int(cfg["moteurs"]["epaule_y_left_max"])-int(cfg["moteurs"]["epaule_y_left_min"])
    angle = ((float(position)/100) * angle) + float(cfg["moteurs"]["epaule_y_left_min"])
    print("left arm 2 : " + str(int(angle)))
    if int(cfg["moteurs"]["epaule_y_left_arduino"]) == 1 :
        controle_moteur_1(int(cfg["moteurs"]["epaule_y_left_pin"]), int(angle))
    else :
        controle_moteur_2(int(cfg["moteurs"]["epaule_y_left_pin"]), int(angle))

def moteur_left_arm_3(position):
    #mouvement epaule gauche z
    angle = int(cfg["moteurs"]["epaule_z_left_max"])-int(cfg["moteurs"]["epaule_z_left_min"])
    angle = ((float(position)/100) * angle) + float(cfg["moteurs"]["epaule_z_left_min"])
    print("left arm 3 : " + str(int(angle)))
    if int(cfg["moteurs"]["epaule_z_left_arduino"]) == 1 :
        controle_moteur_1(int(cfg["moteurs"]["epaule_z_left_pin"]), int(angle))
    else :
        controle_moteur_2(int(cfg["moteurs"]["epaule_z_left_pin"]), int(angle))

def moteur_left_arm_4(position):
    #mouvement coude droit
    angle = int(cfg["moteurs"]["coude_left_max"])-int(cfg["moteurs"]["coude_left_min"])
    angle = ((float(position)/100) * angle) + float(cfg["moteurs"]["coude_left_min"])
    print("left arm 4 : " + str(int(angle)))
    if int(cfg["moteurs"]["coude_left_arduino"]) == 1 :
        controle_moteur_1(int(cfg["moteurs"]["coude_left_pin"]), int(angle))
    else :
        controle_moteur_2(int(cfg["moteurs"]["coude_left_pin"]), int(angle))

### RIGHT ARM ###
def moteur_right_arm_1(position):
    #mouvement epaule droite x
    angle = int(cfg["moteurs"]["epaule_x_right_max"])-int(cfg["moteurs"]["epaule_x_right_min"])
    angle = ((float(position)/100) * angle) + float(cfg["moteurs"]["epaule_x_right_min"])
    print("right arm 1 : " + str(int(angle)))
    if int(cfg["moteurs"]["epaule_x_right_arduino"]) == 1 :
        controle_moteur_1(int(cfg["moteurs"]["epaule_x_right_pin"]), int(angle))
    else :
        controle_moteur_2(int(cfg["moteurs"]["epaule_x_right_pin"]), int(angle))

def moteur_right_arm_2(position):
    #mouvement epaule droite y
    angle = int(cfg["moteurs"]["epaule_y_right_max"])-int(cfg["moteurs"]["epaule_y_right_min"])
    angle = ((float(position)/100) * angle) + float(cfg["moteurs"]["epaule_y_right_min"])
    print("right arm 2 : " + str(int(angle)))
    if int(cfg["moteurs"]["epaule_y_right_arduino"]) == 1 :
        controle_moteur_1(int(cfg["moteurs"]["epaule_y_right_pin"]), int(angle))
    else :
        controle_moteur_2(int(cfg["moteurs"]["epaule_y_right_pin"]), int(angle))

def moteur_right_arm_3(position):
    #mouvement epaule droite z
    angle = int(cfg["moteurs"]["epaule_z_right_max"])-int(cfg["moteurs"]["epaule_z_right_min"])
    angle = ((float(position)/100) * angle) + float(cfg["moteurs"]["epaule_z_right_min"])
    print("right arm 3 : " + str(int(angle)))
    if int(cfg["moteurs"]["epaule_z_right_arduino"]) == 1 :
        controle_moteur_1(int(cfg["moteurs"]["epaule_z_right_pin"]), int(angle))
    else :
        controle_moteur_2(int(cfg["moteurs"]["epaule_z_right_pin"]), int(angle))

def moteur_right_arm_4(position):
    #mouvement coude droit
    angle = int(cfg["moteurs"]["coude_right_max"])-int(cfg["moteurs"]["coude_right_min"])
    angle = ((float(position)/100) * angle) + float(cfg["moteurs"]["coude_right_min"])
    print("right arm 4 : " + str(int(angle)))
    if int(cfg["moteurs"]["coude_right_arduino"]) == 1 :
        controle_moteur_1(int(cfg["moteurs"]["coude_right_pin"]), int(angle))
    else :
        controle_moteur_2(int(cfg["moteurs"]["coude_right_pin"]), int(angle))

### BASSIN ###
def moteur_bassin_1(position):
    #rotation tete
    angle = int(cfg["moteurs"]["bascule_bassin_max"])-int(cfg["moteurs"]["bascule_bassin_min"])
    angle = ((float(position)/100) * angle) + float(cfg["moteurs"]["bascule_bassin_min"])
    print("bassin 1 : " + str(int(angle)))
    if int(cfg["moteurs"]["bascule_bassin_arduino"]) == 1 :
        controle_moteur_1(int(cfg["moteurs"]["bascule_bassin_pin"]), int(angle))
    else :
        controle_moteur_2(int(cfg["moteurs"]["bascule_bassin_pin"]), int(angle))
    
def moteur_bassin_2(position):
    #rotation tete
    angle = int(cfg["moteurs"]["rotation_bassin_max"])-int(cfg["moteurs"]["rotation_bassin_min"])
    angle = ((float(position)/100) * angle) + float(cfg["moteurs"]["rotation_bassin_min"])
    print("bassin 2 : " + str(int(angle)))
    if int(cfg["moteurs"]["rotation_bassin_arduino"]) == 1 :
        controle_moteur_1(int(cfg["moteurs"]["rotation_bassin_pin"]), int(angle))
    else :
        controle_moteur_2(int(cfg["moteurs"]["rotation_tete_pin"]), int(angle))
    
### LEFT HAND ###
def moteur_hand_left_1(position):
    angle = int(cfg["moteurs"]["pouce_left_max"])-int(cfg["moteurs"]["pouce_left_min"])
    angle = ((float(position)/100) * angle) + float(cfg["moteurs"]["pouce_left_min"])
    print("hand left 1 : " + str(int(angle)))
    if int(cfg["moteurs"]["pouce_left_arduino"]) == 1 :
        controle_moteur_1(int(cfg["moteurs"]["pouce_left_pin"]), int(angle))
    else :
        controle_moteur_2(int(cfg["moteurs"]["pouce_left_pin"]), int(angle))

def moteur_hand_left_2(position):
    angle = int(cfg["moteurs"]["index_left_max"])-int(cfg["moteurs"]["index_left_min"])
    angle = ((float(position)/100) * angle) + float(cfg["moteurs"]["index_left_min"])
    print("hand left 2 : " + str(int(angle)))
    if int(cfg["moteurs"]["index_left_arduino"]) == 1 :
        controle_moteur_1(int(cfg["moteurs"]["index_left_pin"]), int(angle))
    else :
        controle_moteur_2(int(cfg["moteurs"]["index_left_pin"]), int(angle))

def moteur_hand_left_3(position):
    angle = int(cfg["moteurs"]["majeur_left_max"])-int(cfg["moteurs"]["majeur_left_min"])
    angle = ((float(position)/100) * angle) + float(cfg["moteurs"]["majeur_left_min"])
    print("hand left 3 : " + str(int(angle)))
    if int(cfg["moteurs"]["majeur_left_arduino"]) == 1 :
        controle_moteur_1(int(cfg["moteurs"]["majeur_left_pin"]), int(angle))
    else :
        controle_moteur_2(int(cfg["moteurs"]["majeur_left_pin"]), int(angle))

def moteur_hand_left_4(position):
    angle = int(cfg["moteurs"]["annulaire_left_max"])-int(cfg["moteurs"]["annulaire_left_min"])
    angle = ((float(position)/100) * angle) + float(cfg["moteurs"]["annulaire_left_min"])
    print("hand left 4 : " + str(int(angle)))
    if int(cfg["moteurs"]["annulaire_left_arduino"]) == 1 :
        controle_moteur_1(int(cfg["moteurs"]["annulaire_left_pin"]), int(angle))
    else :
        controle_moteur_2(int(cfg["moteurs"]["annulaire_left_pin"]), int(angle))

def moteur_hand_left_5(position):
    angle = int(cfg["moteurs"]["auriculaire_left_max"])-int(cfg["moteurs"]["auriculaire_left_min"])
    angle = ((float(position)/100) * angle) + float(cfg["moteurs"]["auriculaire_left_min"])
    print("hand left 5 : " + str(int(angle)))
    if int(cfg["moteurs"]["auriculaire_left_arduino"]) == 1 :
        controle_moteur_1(int(cfg["moteurs"]["auriculaire_left_pin"]), int(angle))
    else :
        controle_moteur_2(int(cfg["moteurs"]["auriculaire_left_pin"]), int(angle))

def moteur_hand_left(position):
    import main
    main.moteur_1_lh.set(position)
    main.moteur_2_lh.set(position)
    main.moteur_3_lh.set(position)
    main.moteur_4_lh.set(position)
    main.moteur_5_lh.set(position)

### RIGHT HAND ###
def moteur_hand_right_1(position):
    angle = int(cfg["moteurs"]["pouce_right_max"])-int(cfg["moteurs"]["pouce_right_min"])
    angle = ((float(position)/100) * angle) + float(cfg["moteurs"]["pouce_right_min"])
    print("hand right 1 : " + str(int(angle)))
    if int(cfg["moteurs"]["pouce_right_arduino"]) == 1 :
        controle_moteur_1(int(cfg["moteurs"]["pouce_right_pin"]), int(angle))
    else :
        controle_moteur_2(int(cfg["moteurs"]["pouce_right_pin"]), int(angle))

def moteur_hand_right_2(position):
    angle = int(cfg["moteurs"]["index_right_max"])-int(cfg["moteurs"]["index_right_min"])
    angle = ((float(position)/100) * angle) + float(cfg["moteurs"]["index_right_min"])
    print("hand right 2 : " + str(int(angle)))
    if int(cfg["moteurs"]["index_right_arduino"]) == 1 :
        controle_moteur_1(int(cfg["moteurs"]["index_right_pin"]), int(angle))
    else :
        controle_moteur_2(int(cfg["moteurs"]["index_right_pin"]), int(angle))

def moteur_hand_right_3(position):
    angle = int(cfg["moteurs"]["majeur_right_max"])-int(cfg["moteurs"]["majeur_right_min"])
    angle = ((float(position)/100) * angle) + float(cfg["moteurs"]["majeur_right_min"])
    print("hand right 3 : " + str(int(angle)))
    if int(cfg["moteurs"]["majeur_right_arduino"]) == 1 :
        controle_moteur_1(int(cfg["moteurs"]["majeur_right_pin"]), int(angle))
    else :
        controle_moteur_2(int(cfg["moteurs"]["majeur_right_pin"]), int(angle))

def moteur_hand_right_4(position):
    angle = int(cfg["moteurs"]["annulaire_right_max"])-int(cfg["moteurs"]["annulaire_right_min"])
    angle = ((float(position)/100) * angle) + float(cfg["moteurs"]["annulaire_right_min"])
    print("hand right 4 : " + str(int(angle)))
    if int(cfg["moteurs"]["annulaire_right_arduino"]) == 1 :
        controle_moteur_1(int(cfg["moteurs"]["annulaire_right_pin"]), int(angle))
    else :
        controle_moteur_2(int(cfg["moteurs"]["annulaire_right_pin"]), int(angle))

def moteur_hand_right_5(position):
    angle = int(cfg["moteurs"]["auriculaire_right_max"])-int(cfg["moteurs"]["auriculaire_right_min"])
    angle = ((float(position)/100) * angle) + float(cfg["moteurs"]["auriculaire_right_min"])
    print("hand right 5 : " + str(int(angle)))
    if int(cfg["moteurs"]["auriculaire_right_arduino"]) == 1 :
        controle_moteur_1(int(cfg["moteurs"]["auriculaire_right_pin"]), int(angle))
    else :
        controle_moteur_2(int(cfg["moteurs"]["auriculaire_right_pin"]), int(angle))

def moteur_hand_right(position):
    import main
    main.moteur_1_rh.set(position)
    main.moteur_2_rh.set(position)
    main.moteur_3_rh.set(position)
    main.moteur_4_rh.set(position)
    main.moteur_5_rh.set(position)
