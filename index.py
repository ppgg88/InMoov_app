from script_personelle import *
from main import *

### AJOUT DES FONCTIONS PERSSONEL AU MENU ###
fonction_perso_menu = Menu(menu_root, tearoff = 0)
for i in fonction_liste :
    fonction_perso_menu.add_command(label=(i[0]), command=i[1])
    print(str(i))
menu_root.add_cascade(label="Fonctions Personalisées", menu=fonction_perso_menu)

### TEST DE CONEXION PAR DEFAUT AU CARTE ARDUINO ###
conect_1()
conect_2()

### AFFICHAGE DU PROGRAME ###
screen[0].pack(fill=X)
say("Bonjour, je suis" + cfg["robot"]["robot_name"])
root.mainloop()