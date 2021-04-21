from tkinter import *
from arduino import *
from body import *
import configparser


cfg = configparser.ConfigParser()
cfg.read('config/info.ini')

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

def stomach_page():
    print("page de gestion du ventre")

def conect():
    if connection_robot() :
        btn.config(bg = "green", command = NONE, text = "CONNECTER")
        btn.update()
    else :
        btn.config(bg = "black")
        btn.update()

# fenetre principal
root = Tk()

#personalisation de la fenaitre principale
root.title("InMoov : " + str(cfg["robot"]["robot_name"]))
root.geometry("1080x625")
root.minsize(480,360)
root.iconbitmap("images/logo-inmoov.ico")
root.config(background = str(cfg["page"]["background"]))

screen = [Frame(root, bg=str(cfg["page"]["background"])) for i in range(0,4)]

global index
index = 0
screen[0].pack(fill=X)

menu_root = Menu(root)
corps_menu = Menu(menu_root, tearoff = 0)
corps_menu.add_command(label="tête", command=show_head)
corps_menu.add_command(label="bras droit", command=right_arm_page)
corps_menu.add_command(label="bras gauche", command=left_arm_page)
corps_menu.add_command(label="ventre", command=stomach_page)
corps_menu.add_command(label="main", command=hand_page)
menu_root.add_cascade(label="Gestion du Corps", menu=corps_menu)
accueil_menu = Menu(menu_root, tearoff = 0)
accueil_menu.add_command(label="Accueil", command=show_accueil)
menu_root.add_cascade(label="Accueil", menu=accueil_menu)
root.config(menu=menu_root)


#screen[0] : acccueil
#screen[1] : mouvement tête
#screen[2] : mouvement bras gauche
#screen[3] : mouvement bras droit

###### ACCUEIL #######
acc = Frame(screen[0], bg=str(cfg["page"]["background"]))
acc_full = Frame(screen[0], bg=str(cfg["page"]["background"]))
#ajouter du texte
bienvenue = Label(acc, text="Bienvenue sur l'interface de controle : tu retrouvera ici toutes les informations relative à ton robot :", background = str(cfg["page"]["background"]), font=("Courrier", 12))
bienvenue.grid(row=0,column=1, sticky=W)
#info robot
info_robot = Label(acc_full, justify="left", text=(
    "Robot : \n   Nom : " + cfg["robot"]["robot_name"] +"\n   Age : " + cfg["robot"]["robot_age"] + " ans\n\nCarte Arduino : \n   Port : " + cfg["robot"]["arduino_com"] + "\n   Baudrate : " + cfg["robot"]["arduino_speed"]
    ), background = cfg["page"]["background"], font=("Courrier", 12))
info_robot.pack()
#ajouter un bouton
btn = Button(acc_full, text="conexion", bg="black", fg="white", command=conect)
btn.pack(pady = 25, fill=X)
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

root.mainloop()