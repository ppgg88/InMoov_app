from script_personelle import *
from main import *
from body import *
from speechrecognition_ import *

def position_init():
    moove.head.rotation(int(cfg["moteurs"]["rotation_tete_ini"]))
    moteur_1_h.set(int(cfg["moteurs"]["rotation_tete_ini"]))
    moteur_1_f.set(int(cfg["moteurs"]["rotation_tete_ini"]))

    moove.head.up_down(int(cfg["moteurs"]["elevation_tete_ini"]))
    moteur_2_h.set(int(cfg["moteurs"]["elevation_tete_ini"]))
    moteur_2_f.set(int(cfg["moteurs"]["elevation_tete_ini"]))

    moove.head.mouth(int(cfg["moteurs"]["bouche_tete_ini"]))
    moteur_3_h.set(int(cfg["moteurs"]["bouche_tete_ini"]))
    moteur_3_f.set(int(cfg["moteurs"]["bouche_tete_ini"]))

    moove.head.eyes_x(int(cfg["moteurs"]["yeux_x_tete_ini"]))
    moteur_4_h.set(int(cfg["moteurs"]["yeux_x_tete_ini"]))
    moteur_4_f.set(int(cfg["moteurs"]["yeux_x_tete_ini"]))

    moove.head.eyes_y(int(cfg["moteurs"]["yeux_y_tete_ini"]))
    moteur_5_h.set(int(cfg["moteurs"]["yeux_y_tete_ini"]))
    moteur_5_f.set(int(cfg["moteurs"]["yeux_y_tete_ini"]))

    moove.left_arm.shoulder_x(int(cfg["moteurs"]["epaule_x_left_ini"]))
    moteur_1_la.set(int(cfg["moteurs"]["epaule_x_left_ini"]))
    moteur_6_f.set(int(cfg["moteurs"]["epaule_x_left_ini"]))

    moove.left_arm.shoulder_y(int(cfg["moteurs"]["epaule_y_left_ini"]))
    moteur_2_la.set(int(cfg["moteurs"]["epaule_y_left_ini"]))
    moteur_7_f.set(int(cfg["moteurs"]["epaule_y_left_ini"]))

    moove.left_arm.shoulder_z(int(cfg["moteurs"]["epaule_z_left_ini"]))
    moteur_3_la.set(int(cfg["moteurs"]["epaule_z_left_ini"]))
    moteur_8_f.set(int(cfg["moteurs"]["epaule_z_left_ini"]))

    moove.left_arm.elbow(int(cfg["moteurs"]["coude_left_ini"]))
    moteur_4_la.set(int(cfg["moteurs"]["coude_left_ini"]))
    moteur_9_f.set(int(cfg["moteurs"]["coude_left_ini"]))

    moove.right_arm.shoulder_x(int(cfg["moteurs"]["epaule_x_right_ini"]))
    moteur_1_ra.set(int(cfg["moteurs"]["epaule_x_right_ini"]))
    moteur_10_f.set(int(cfg["moteurs"]["epaule_x_right_ini"]))

    moove.right_arm.shoulder_y(int(cfg["moteurs"]["epaule_y_right_ini"]))
    moteur_2_ra.set(int(cfg["moteurs"]["epaule_y_right_ini"]))
    moteur_11_f.set(int(cfg["moteurs"]["epaule_y_right_ini"]))

    moove.right_arm.shoulder_z(int(cfg["moteurs"]["epaule_z_right_ini"]))
    moteur_3_ra.set(int(cfg["moteurs"]["epaule_z_right_ini"]))
    moteur_12_f.set(int(cfg["moteurs"]["epaule_z_right_ini"]))

    moove.right_arm.elbow(int(cfg["moteurs"]["coude_right_ini"]))
    moteur_4_ra.set(int(cfg["moteurs"]["coude_right_ini"]))
    moteur_13_f.set(int(cfg["moteurs"]["coude_right_ini"]))

    moove.left_hand.all(int(cfg["moteurs"]["hand_left_ini"]))
    moteur_lh.set(int(cfg["moteurs"]["hand_left_ini"]))
    moteur_14_f.set(int(cfg["moteurs"]["hand_left_ini"]))

    moove.right_hand.all(int(cfg["moteurs"]["hand_right_ini"]))
    moteur_rh.set(int(cfg["moteurs"]["hand_right_ini"]))
    moteur_15_f.set(int(cfg["moteurs"]["hand_right_ini"]))

    moove.pelvis.rocker(int(cfg["moteurs"]["bascule_bassin_ini"]))
    moteur_1_b.set(int(cfg["moteurs"]["bascule_bassin_ini"]))
    moteur_17_f.set(int(cfg["moteurs"]["bascule_bassin_ini"]))

    moove.pelvis.rotation(int(cfg["moteurs"]["rotation_bassin_ini"]))
    moteur_2_b.set(int(cfg["moteurs"]["rotation_bassin_ini"]))
    moteur_16_f.set(int(cfg["moteurs"]["rotation_bassin_ini"]))


### AJOUT DES FONCTIONS PERSSONEL AU MENU ###
fonction_perso_menu = Menu(menu_root, tearoff = 0)
for i in fonction_liste :
    fonction_perso_menu.add_command(label=(i[0]), command=i[1])
menu_root.add_cascade(label="Fonctions Personalisées", menu=fonction_perso_menu)

### TEST DE CONEXION PAR DEFAUT AUX CARTES ARDUINO ###
conect_1()
conect_2()

position_init()

### AFFICHAGE DU PROGRAME ###
screen[0].pack(fill=X)
say("Bonjour, je suis" + cfg["robot"]["robot_name"])

root.mainloop()