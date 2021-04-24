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


def moteur_head_3(position):
    global moteur_speak
    moteur_speak.set(position)
    #mouvement bouche
    angle = int(cfg["moteurs"]["bouche_tete_max"])-int(cfg["moteurs"]["bouche_tete_min"])
    angle = ((float(position)/100) * angle) + float(cfg["moteurs"]["bouche_tete_min"])
    print("head 3 : " + str(int(angle)))
    if int(cfg["moteurs"]["bouche_tete_arduino"]) == 1 :
        controle_moteur_1(int(cfg["moteurs"]["bouche_tete_pin"]), int(angle))
    else :
        controle_moteur_2(int(cfg["moteurs"]["bouche_tete_pin"]), int(angle))

def moteur_head_3_speak(position):
    global moteur_3_h
    moteur_3_h.set(position)
    #mouvement bouche
    angle = int(cfg["moteurs"]["bouche_tete_max"])-int(cfg["moteurs"]["bouche_tete_min"])
    angle = ((float(position)/100) * angle) + float(cfg["moteurs"]["bouche_tete_min"])
    print("head 3 : " + str(int(angle)))
    if int(cfg["moteurs"]["bouche_tete_arduino"]) == 1 :
        controle_moteur_1(int(cfg["moteurs"]["bouche_tete_pin"]), int(angle))
    else :
        controle_moteur_2(int(cfg["moteurs"]["bouche_tete_pin"]), int(angle))

def show_accueil():
    global index
    screen[index].pack_forget()
    index = 0
    print("Page accueil")
    screen[index].pack(fill = X)

def show_head():
    global index
    screen[index].pack_forget()
    index = 1
    print("Page controle de la tête")
    screen[index].pack(fill = X)

def right_arm_page():
    global index
    screen[index].pack_forget()
    index = 3
    print("page de gestion du bras droit")
    screen[index].pack(fill = X)

def left_arm_page():
    global index
    screen[index].pack_forget()
    index = 2
    print("page de gestion du bras gauche")
    screen[index].pack(fill = X)

def hand_page():
    print("page de gestion des mains")
    tkinter.messagebox.showerror('cette page est en developement','page de gestion des mains encore indisponible')

def stomach_page():
    global index
    screen[index].pack_forget()
    index = 4
    print("page de gestion du bassin")
    screen[index].pack(fill = X)


def speak_page():
    global index
    screen[index].pack_forget()
    index = 6
    print("page de gestion des paroles")
    screen[index].pack(fill = X)

def conect_1():
    global inti_arduino_1
    if connection_robot_1() :
        btn.config(bg = "green", command = NONE, text = "Arduino n°1 : CONNECTER")
        btn.update()
    else :
        btn.config(bg = "black")
        btn.update()
        if inti_arduino_1 :
            tkinter.messagebox.showerror('erreur','conexion à l\'arduino n°1 Impossible')
    inti_arduino_1 = True

def conect_2():
    global inti_arduino_2
    if connection_robot_2() :
        btn2.config(bg = "green", command = NONE, text = "Arduino n°2 : CONNECTER")
        btn2.update()
    else :
        btn2.config(bg = "black")
        btn2.update()
        if inti_arduino_2 :
            tkinter.messagebox.showerror('erreur','conexion à l\'arduino n°2 Impossible')
    inti_arduino_2 = True

# touche a
def moteur_1_clavier(k):
    global moteur_selectioner, index, scal,  moteur_1_h, moteur_2_la, moteur_3_ra
    if index == 1 :
        def moteur_selectioner(x):
            moteur_head_1(x)
        scal = moteur_1_h
    if index == 2 :
        def moteur_selectioner(x):
            moteur_left_arm_1(x)
        scal = moteur_1_la
    if index == 3 :
        def moteur_selectioner(x):
            moteur_right_arm_1(x)
        scal = moteur_1_ra

#touche z
def moteur_2_clavier(k):
    global moteur_selectioner, index, scal, moteur_2_h, moteur_2_la, moteur_2_ra
    if index == 1 :
        def moteur_selectioner(x):
            moteur_head_2(x)
        scal = moteur_2_h
    if index == 2 :
        def moteur_selectioner(x):
            moteur_left_arm_2(x)
        scal = moteur_2_la
    if index == 3 :
        def moteur_selectioner(x):
            moteur_right_arm_2(x)
        scal = moteur_2_ra
    print("moteur 2 selectioner")

#touche e
def moteur_3_clavier(k):
    global moteur_selectioner, index,  moteur_3_h, moteur_3_la, moteur_3_ra, scal
    if index == 1 :
        def moteur_selectioner(x):
            moteur_head_3(x)
        scal = moteur_3_h
    if index == 2 :
        def moteur_selectioner(x):
            moteur_left_arm_3(x)
        scal = moteur_3_la
    if index == 3 :
        def moteur_selectioner(x):
            moteur_right_arm_3(x)
        scal = moteur_3_ra

#touche r
def moteur_4_clavier(k):
    global moteur_selectioner, index, scal, moteur_4_h, moteur_4_la, moteur_4_ra
    if index == 1 :
        def moteur_selectioner(x):
            moteur_head_4(x)
        scal = moteur_4_h
    if index == 2 :
        def moteur_selectioner(x):
            moteur_left_arm_4(x)
        scal = moteur_4_la
    if index == 3 :
        def moteur_selectioner(x):
            moteur_right_arm_4(x)
        scal = moteur_4_la

#touche t
def moteur_5_clavier(k):
    global moteur_selectioner, index, scal,  moteur_5_h
    if index == 1 :
        def moteur_selectioner(x):
            moteur_head_5(x)
        scal = moteur_5_h

#touche <
def soustraction_clavier(k):
    global moteur_selectioner, scal
    if scal != -1 :
        val = scal.get()
        val += -2
        scal.set(val)
        moteur_selectioner(val)
        print(val)

#touche >
def adition_clavier(k):
    global moteur_selectioner, scal
    if scal != -1 :
        val = scal.get()
        val += 2
        scal.set(val)
        moteur_selectioner(val)
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
    fichier = open("temp_lecture", "w")
    fichier.write(text)
    fichier.close()
    deconnection_robot()
    os.system("py speak.py")
    moteur_speak.set(0)
    moteur_3_h.set(0)
    connection_robot()


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


global index
index = 0
#screen[0].pack(fill=X)

#parametre du menu

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
#screen[5] : 
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