from script_personelle import *

fonction_perso_menu = Menu(menu_root, tearoff = 0)
for i in fonction_liste :
    fonction_perso_menu.add_command(label=(i[0]), command=i[1])
    print(str(i))
menu_root.add_cascade(label="fonction perssonaliser", menu=fonction_perso_menu)

screen[0].pack(fill=X)
say("Bonjour je suis" + cfg["robot"]["robot_name"])
root.mainloop()