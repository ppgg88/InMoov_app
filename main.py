from tkinter import *
from arduino import *
from body import *
from fonction_main import *
import configparser
import os
import tkinter.messagebox

cfg = configparser.ConfigParser()
cfg.read('config/info.ini')

scal = -1

# fenetre principal
root = Tk()

#personalisation de la fenaitre principale
root.title("InMoov : " + cfg["robot"]["robot_name"])
root.geometry("1080x625")
root.minsize(480,360)
root.iconbitmap("images/logo-inmoov.ico")
root.config(background = str(cfg["page"]["background"]))

#creation des diferents ecrans
screen = [Frame(root, bg=str(cfg["page"]["background"])) for i in range(0,8)]

menu_root = Menu(root)

corps_menu = Menu(menu_root, tearoff = 0)
corps_menu.add_command(label="Tête", command=show_head)
corps_menu.add_command(label="Bras droit", command=right_arm_page)
corps_menu.add_command(label="Bras gauche", command=left_arm_page)
corps_menu.add_command(label="Ventre", command=stomach_page)
corps_menu.add_command(label="Main", command=hand_page)

fonction_menu = Menu(menu_root, tearoff = 0)
fonction_menu.add_command(label="paroles", command=speak_page)

menu_root.add_cascade(label="accueil", command=show_accueil)
menu_root.add_cascade(label="Gestion du Corps", menu=corps_menu)
menu_root.add_cascade(label="fonction", menu=fonction_menu)
root.config(menu=menu_root)


#screen[0] : acccueil
#screen[1] : mouvement tête
#screen[2] : mouvement bras gauche
#screen[3] : mouvement bras droit
#screen[4] : mouvement bassin
#screen[5] : gestion des main
#screen[6] : fonction parole 
#screen[7] : 

###### ACCUEIL #######
acc = Frame(screen[0], bg=str(cfg["page"]["background"]))
acc_full = Frame(screen[0], bg=str(cfg["page"]["background"]))
#ajouter du texte
bienvenue = Label(acc, text="Bienvenue sur l'interface de controle : tu retrouvera ici toutes les informations relative à ton robot :", background = str(cfg["page"]["background"]), font=("Courrier", 12))
bienvenue.grid(row=0,column=1, sticky=W)
#info robot
info_robot = Label(acc_full, justify="left", text=(
    "Robot : \n   Nom : " + cfg["robot"]["robot_name"] +"\n   Age : " + cfg["robot"]["robot_age"] + " ans\n\nCarte Arduino n°1 : \n   Port : " + cfg["robot"]["arduino_1_com"] + "\n   Baudrate : " + cfg["robot"]["arduino_1_speed"] + "\n\nCarte Arduino n°2 : \n   Port : " + cfg["robot"]["arduino_2_com"] + "\n   Baudrate : " + cfg["robot"]["arduino_2_speed"]
    ), background = cfg["page"]["background"], font=("Courrier", 12))
info_robot.pack()
#ajouter un bouton
btn = Button(acc_full, text="conexion arduino n°1", bg="black", fg="white", command=conect_1)
btn.pack(pady = 25, fill=X)
btn2 = Button(acc_full, text="conexion arduino n°2", bg="black", fg="white", command=conect_2)
btn2.pack(pady = 25, fill=X)
#ajouter une image
width, height = 300, 150
image_acc = PhotoImage(file="images/logo.png").zoom(100).subsample(100)
canvas = Canvas(acc, width=width, height=height, bg = cfg["page"]["background"], bd=0, highlightthickness=0)
canvas.create_image(width/2,height/2,image=image_acc)
canvas.grid(row=0, column=0, sticky=W)
#afficher
acc.pack(fill = X)
acc_full.pack(fill = X)


###### HEAD #######
head = Frame(screen[1], bg=str(cfg["page"]["background"]))
head_full = Frame(screen[1], bg=str(cfg["page"]["background"]))
#ajouter du texte
bienvenue = Label(head, text="Bienvenue sur l'interface de controle de la tête :", background = str(cfg["page"]["background"]), font=("Courrier", 12))
bienvenue.grid(row=0,column=1, sticky=W)
#images
width, height = 300, 150
image_head = PhotoImage(file="images/logo.png").zoom(100).subsample(100)
canvas = Canvas(head, width=width, height=height, bg = cfg["page"]["background"], bd=0, highlightthickness=0)
canvas.create_image(width/2,height/2,image=image_head)
canvas.grid(row=0, column=0, sticky=W)
#controle moteur
moteur_1_h = Scale(head_full, orient='horizontal', from_=0, to=100, resolution=1, tickinterval=10, label=("Rotation tête : "), bg = cfg["page"]["background"], bd=0, highlightthickness=0, command=moteur_head_1, activebackground= "black")
moteur_1_h.pack(fill= X)
moteur_2_h = Scale(head_full, orient='horizontal', from_=0, to=100, resolution=1, tickinterval=10, label=("Elévation tête : "), bg = cfg["page"]["background"], bd=0, highlightthickness=0, command=moteur_head_2 , activebackground= "black")
moteur_2_h.pack(fill= X)
moteur_3_h = Scale(head_full, orient='horizontal', from_=0, to=100, resolution=1, tickinterval=10, label=("Mouvement bouche : "), bg = cfg["page"]["background"], bd=0, highlightthickness=0, command=moteur_head_3, activebackground= "black")
moteur_3_h.pack(fill= X)
moteur_4_h = Scale(head_full, orient='horizontal', from_=0, to=100, resolution=1, tickinterval=10, label=("Mouvement yeux X : "), bg = cfg["page"]["background"], bd=0, highlightthickness=0, command=moteur_head_4, activebackground= "black")
moteur_4_h.pack(fill= X)
moteur_5_h = Scale(head_full, orient='horizontal', from_=0, to=100, resolution=1, tickinterval=10, label=("Mouvement yeux Y : "), bg = cfg["page"]["background"], bd=0, highlightthickness=0, command=moteur_head_5, activebackground= "black")
moteur_5_h.pack(fill= X)
#afficher
head.pack(fill=X)
head_full.pack(fill=X)


###### LEFT ARM #######
left_arm = Frame(screen[2], bg=str(cfg["page"]["background"]))
left_arm_full = Frame(screen[2], bg=str(cfg["page"]["background"]))
#ajouter du texte
bienvenue = Label(left_arm, text="Bienvenue sur l'interface de controle du bras gauche :", background = str(cfg["page"]["background"]), font=("Courrier", 12))
bienvenue.grid(row=0,column=1, sticky=W)
#images
width, height = 300, 150
image_left_arm = PhotoImage(file="images/logo.png").zoom(100).subsample(100)
canvas = Canvas(left_arm, width=width, height=height, bg = cfg["page"]["background"], bd=0, highlightthickness=0)
canvas.create_image(width/2,height/2,image=image_left_arm)
canvas.grid(row=0, column=0, sticky=W)
#controle moteur
moteur_1_la = Scale(left_arm_full, orient='horizontal', from_=0, to=100, resolution=1, tickinterval=10, label=("epaule X : "), bg = cfg["page"]["background"], bd=0, highlightthickness=0, command=moteur_left_arm_1, activebackground= "black")
moteur_1_la.pack(fill= X)
moteur_2_la = Scale(left_arm_full, orient='horizontal', from_=0, to=100, resolution=1, tickinterval=10, label=("epaule Y : "), bg = cfg["page"]["background"], bd=0, highlightthickness=0, command=moteur_left_arm_2 , activebackground= "black")
moteur_2_la.pack(fill= X)
moteur_3_la = Scale(left_arm_full, orient='horizontal', from_=0, to=100, resolution=1, tickinterval=10, label=("epaule Z : "), bg = cfg["page"]["background"], bd=0, highlightthickness=0, command=moteur_left_arm_3, activebackground= "black")
moteur_3_la.pack(fill= X)
moteur_4_la = Scale(left_arm_full, orient='horizontal', from_=0, to=100, resolution=1, tickinterval=10, label=("Coude : "), bg = cfg["page"]["background"], bd=0, highlightthickness=0, command=moteur_left_arm_4, activebackground= "black")
moteur_4_la.pack(fill= X)
#afficher
left_arm.pack(fill=X)
left_arm_full.pack(fill=X)


###### RIGHT ARM #######
right_arm = Frame(screen[3], bg=str(cfg["page"]["background"]))
right_arm_full = Frame(screen[3], bg=str(cfg["page"]["background"]))
#ajouter du texte
bienvenue = Label(right_arm, text="Bienvenue sur l'interface de controle du bras droite :", background = str(cfg["page"]["background"]), font=("Courrier", 12))
bienvenue.grid(row=0,column=1, sticky=W)
#images
width, height = 300, 150
image_right_arm = PhotoImage(file="images/logo.png").zoom(100).subsample(100)
canvas = Canvas(right_arm, width=width, height=height, bg = cfg["page"]["background"], bd=0, highlightthickness=0)
canvas.create_image(width/2,height/2,image=image_right_arm)
canvas.grid(row=0, column=0, sticky=W)
#controle moteur
moteur_1_ra = Scale(right_arm_full, orient='horizontal', from_=0, to=100, resolution=1, tickinterval=10, label=("epaule X : "), bg = cfg["page"]["background"], bd=0, highlightthickness=0, command=moteur_right_arm_1, activebackground= "black")
moteur_1_ra.pack(fill= X)
moteur_2_ra = Scale(right_arm_full, orient='horizontal', from_=0, to=100, resolution=1, tickinterval=10, label=("epaule Y : "), bg = cfg["page"]["background"], bd=0, highlightthickness=0, command=moteur_right_arm_2 , activebackground= "black")
moteur_2_ra.pack(fill= X)
moteur_3_ra = Scale(right_arm_full, orient='horizontal', from_=0, to=100, resolution=1, tickinterval=10, label=("epaule Z : "), bg = cfg["page"]["background"], bd=0, highlightthickness=0, command=moteur_right_arm_3, activebackground= "black")
moteur_3_ra.pack(fill= X)
moteur_4_ra = Scale(right_arm_full, orient='horizontal', from_=0, to=100, resolution=1, tickinterval=10, label=("Coude : "), bg = cfg["page"]["background"], bd=0, highlightthickness=0, command=moteur_right_arm_4, activebackground= "black")
moteur_4_ra.pack(fill= X)
#afficher
right_arm.pack(fill=X)
right_arm_full.pack(fill=X)

###### BASSIN #######
bassin = Frame(screen[4], bg=str(cfg["page"]["background"]))
bassin_full = Frame(screen[4], bg=str(cfg["page"]["background"]))
#ajouter du texte
bienvenue = Label(bassin, text="Bienvenue sur l'interface de controle du bassin :", background = str(cfg["page"]["background"]), font=("Courrier", 12))
bienvenue.grid(row=0,column=1, sticky=W)
#images
width, height = 300, 150
image_bassin = PhotoImage(file="images/logo.png").zoom(100).subsample(100)
canvas = Canvas(bassin, width=width, height=height, bg = cfg["page"]["background"], bd=0, highlightthickness=0)
canvas.create_image(width/2,height/2,image=image_bassin)
canvas.grid(row=0, column=0, sticky=W)
#controle moteur
moteur_1_b = Scale(bassin_full, orient='horizontal', from_=0, to=100, resolution=1, tickinterval=10, label=("bascule : "), bg = cfg["page"]["background"], bd=0, highlightthickness=0, command=moteur_bassin_1, activebackground= "black")
moteur_1_b.pack(fill= X)
moteur_2_b = Scale(bassin_full, orient='horizontal', from_=0, to=100, resolution=1, tickinterval=10, label=("rotation : "), bg = cfg["page"]["background"], bd=0, highlightthickness=0, command=moteur_bassin_2 , activebackground= "black")
moteur_2_b.pack(fill= X)
#afficher
bassin.pack(fill=X)
bassin_full.pack(fill=X)

###### HAND #######
hand = Frame(screen[5], bg=str(cfg["page"]["background"]))
hand_1 = Frame(screen[5], bg=str(cfg["page"]["background"]))
hand_2 = Frame(screen[5], bg=str(cfg["page"]["background"]))
#ajouter du texte
bienvenue = Label(hand, text="Bienvenue sur l'interface de controle de la tête :", background = str(cfg["page"]["background"]), font=("Courrier", 12))
bienvenue.grid(row=0,column=1, sticky=W)
#images
width, height = 300, 150
image_hand = PhotoImage(file="images/logo.png").zoom(100).subsample(100)
canvas = Canvas(hand, width=width, height=height, bg = cfg["page"]["background"], bd=0, highlightthickness=0)
canvas.create_image(width/2,height/2,image=image_hand)
canvas.grid(row=0, column=0, sticky=W)
#controle moteur
Grid.rowconfigure(hand_1, 0, weight=1)
Grid.columnconfigure(hand_1, 0, weight=1)
Grid.columnconfigure(hand_1, 1, weight=1)
moteur_lh = Scale(hand_1, orient='horizontal', from_=0, to=100, resolution=1, tickinterval=10, label=("MAIN GAUCHE : "),bg="#dddddd", bd=0, highlightthickness=0, command=moteur_hand_left, activebackground= "black")
moteur_lh.grid(row=0, column=0, padx=(10, 10), sticky=N+S+E+W)
moteur_rh = Scale(hand_1, orient='horizontal', from_=0, to=100, resolution=1, tickinterval=10, label=("MAIN DROITE : "), bg="#dddddd", bd=0, highlightthickness=0, command=moteur_hand_right , activebackground= "black")
moteur_rh.grid(row=0, column=1, padx=(10,10), sticky=N+S+E+W)
    #hand
Grid.rowconfigure(hand_2, 0, weight=1)
Grid.columnconfigure(hand_2, 1, weight=1)
Grid.columnconfigure(hand_2, 0, weight=1)
    #left hand
moteur_1_lh = Scale(hand_2, orient='horizontal', from_=0, to=100, resolution=1, tickinterval=10, label=("pouce : "), bg = cfg["page"]["background"], bd=0, highlightthickness=0, command=moteur_hand_left_1, activebackground= "black")
moteur_1_lh.grid(row=0, column=0, sticky=N+S+E+W, padx=(10, 10))
moteur_2_lh = Scale(hand_2, orient='horizontal', from_=0, to=100, resolution=1, tickinterval=10, label=("index : "), bg = cfg["page"]["background"], bd=0, highlightthickness=0, command=moteur_hand_left_2 , activebackground= "black")
moteur_2_lh.grid(row=1, column=0, sticky=N+S+E+W, padx=(10, 10))
moteur_3_lh = Scale(hand_2, orient='horizontal', from_=0, to=100, resolution=1, tickinterval=10, label=("majeur : "), bg = cfg["page"]["background"], bd=0, highlightthickness=0, command=moteur_hand_left_3, activebackground= "black")
moteur_3_lh.grid(row=2, column=0, sticky=N+S+E+W, padx=(10, 10))
moteur_4_lh = Scale(hand_2, orient='horizontal', from_=0, to=100, resolution=1, tickinterval=10, label=("annulaire : "), bg = cfg["page"]["background"], bd=0, highlightthickness=0, command=moteur_hand_left_4, activebackground= "black")
moteur_4_lh.grid(row=3, column=0, sticky=N+S+E+W, padx=(10, 10))
moteur_5_lh = Scale(hand_2, orient='horizontal', from_=0, to=100, resolution=1, tickinterval=10, label=("auriculaire : "), bg = cfg["page"]["background"], bd=0, highlightthickness=0, command=moteur_hand_left_5, activebackground= "black")
moteur_5_lh.grid(row=4, column=0, sticky=N+S+E+W, padx=(10, 10))
    #Right hand
moteur_1_rh = Scale(hand_2, orient='horizontal', from_=0, to=100, resolution=1, tickinterval=10, label=("pouce : "), bg = cfg["page"]["background"], bd=0, highlightthickness=0, command=moteur_hand_right_1, activebackground= "black")
moteur_1_rh.grid(row=0, column=1, sticky=N+S+E+W, padx=(10,10))
moteur_2_rh = Scale(hand_2, orient='horizontal', from_=0, to=100, resolution=1, tickinterval=10, label=("index : "), bg = cfg["page"]["background"], bd=0, highlightthickness=0, command=moteur_hand_right_2 , activebackground= "black")
moteur_2_rh.grid(row=1, column=1, sticky=N+S+E+W, padx=(10,10))
moteur_3_rh = Scale(hand_2, orient='horizontal', from_=0, to=100, resolution=1, tickinterval=10, label=("majeur : "), bg = cfg["page"]["background"], bd=0, highlightthickness=0, command=moteur_hand_right_3, activebackground= "black")
moteur_3_rh.grid(row=2, column=1, sticky=N+S+E+W, padx=(10,10))
moteur_4_rh = Scale(hand_2, orient='horizontal', from_=0, to=100, resolution=1, tickinterval=10, label=("annulaire : "), bg = cfg["page"]["background"], bd=0, highlightthickness=0, command=moteur_hand_right_4, activebackground= "black")
moteur_4_rh.grid(row=3, column=1, sticky=N+S+E+W, padx=(10,10))
moteur_5_rh = Scale(hand_2, orient='horizontal', from_=0, to=100, resolution=1, tickinterval=10, label=("auriculaire : "), bg = cfg["page"]["background"], bd=0, highlightthickness=0, command=moteur_hand_right_5, activebackground= "black")
moteur_5_rh.grid(row=4, column=1, sticky=N+S+E+W, padx=(10,10))
#afficher
hand.pack(fill=X)
hand_1.pack(fill=X)
hand_2.pack(fill=X)

###### SPEAK #######
speak = Frame(screen[6], bg=str(cfg["page"]["background"]))
speak_full = Frame(screen[6], bg=str(cfg["page"]["background"]))
#ajouter du texte
bienvenue_speak = Label(speak, text="Bienvenue sur l'interface de controle de la parole :", background = str(cfg["page"]["background"]), font=("Courrier", 12))
bienvenue_speak.grid(row=0,column=1, sticky=W)
#info robot
entrer_text = Entry(speak_full)
entrer_text.pack(fill=X)
#ajouter un bouton
btn_send = Button(speak_full, text="lancer parole", bg="black", fg="white", command=fonction_speak)
btn_send.pack(pady = 25, fill=X)
#moteur bouche
moteur_speak = Scale(speak_full, orient='horizontal', from_=0, to=100, resolution=1, tickinterval=10, label=("Mouvement bouche : "), bg = cfg["page"]["background"], bd=0, highlightthickness=0, command=moteur_head_3_speak, activebackground= "black")
moteur_speak.pack(fill= X)
#ajouter une image
width, height = 300, 150
image_speak = PhotoImage(file="images/logo.png").zoom(100).subsample(100)
canvas = Canvas(speak, width=width, height=height, bg = cfg["page"]["background"], bd=0, highlightthickness=0)
canvas.create_image(width/2,height/2,image=image_speak)
canvas.grid(row=0, column=0, sticky=W)
#afficher
speak.pack(fill = X)
speak_full.pack(fill = X)

root.bind("<KeyPress-a>", moteur_1_clavier)
root.bind("<KeyPress-z>", moteur_2_clavier)
root.bind("<KeyPress-e>", moteur_3_clavier)
root.bind("<KeyPress-r>", moteur_4_clavier)
root.bind("<KeyPress-t>", moteur_5_clavier)
root.bind("<KeyPress-A>", moteur_1_clavier)
root.bind("<KeyPress-Z>", moteur_2_clavier)
root.bind("<KeyPress-E>", moteur_3_clavier)
root.bind("<KeyPress-R>", moteur_4_clavier)
root.bind("<KeyPress-T>", moteur_5_clavier)
root.bind("<Left>", soustraction_clavier)
root.bind("<Right>", adition_clavier)
root.bind('<Return>', entrer_clavier)

conect_1()
conect_2()