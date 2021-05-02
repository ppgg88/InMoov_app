from body import *
from arduino import *
from random import randint
from time import sleep
import threading

def open_mouth():
    import main
    main.moteur_3_h.set(100)
    main.moteur_speak.set(100)

def close_mouth():
    import main
    main.moteur_3_h.set(0)
    main.moteur_speak.set(0)

def see_left():
    import main
    moove.head.rotation(10)
    main.moteur_1_h.set(10)

def see_right():
    import main
    moove.head.rotation(90)
    main.moteur_1_h.set(90)

def see_front():
    import main
    moove.head.rotation(50)
    main.moteur_1_h.set(50)

def see_up():
    import main
    moove.head.up_down(90)
    main.moteur_2_h.set(90)

def see_down():
    import main
    moove.head.up_down(10)
    main.moteur_2_h.set(10)

mvt_aleatoire = False

def mouvement_aleatoire():
    import tkinter.messagebox
    global mvt_aleatoire
    mvt_aleatoire = not(mvt_aleatoire)
    if mvt_aleatoire :
        tkinter.messagebox.showinfo("mouvement aléatoire","mouvement aléatoire demarer !")
    else :
        tkinter.messagebox.showinfo("mouvement aléatoire","mouvement aléatoire arreter !")
    alea = threading.Thread(target=tete_aleatoire)
    alea.start()

def tete_aleatoire():
    import main
    global mvt_aleatoire
    while mvt_aleatoire :
        v=randint(15, 85)
        main.moteur_2_h.set(v)
        moove.head.up_down(v)
        v=randint(15, 85)
        main.moteur_1_h.set(v)
        moove.head.rotation(v)
        sleep(randint(2,10))

def music_ytb(a_rechercher):
    global player
    a_rechercher = a_rechercher.replace('é', 'e')
    a_rechercher = a_rechercher.replace('è', 'e')
    a_rechercher = a_rechercher.replace('\'', ' ')
    a_rechercher = a_rechercher.replace('à', 'a')
    a_rechercher = a_rechercher.replace('ç', 'c')
    a_rechercher = a_rechercher.replace('ù', 'u')
    a_rechercher = a_rechercher.replace('î', 'i')
    a_rechercher = a_rechercher.replace('ê', 'e')
    print(a_rechercher)    
    import os
    import urllib.request
    import pafy
    import vlc #python-vlc
    import time
    #import youtube_dl
    fichier = open("ytb.html", "a", encoding="utf8")
    url = ""
    recherche = "https://www.youtube.com/results?search_query="
    print(recherche)
    for i in range(0, len(a_rechercher)):
        if a_rechercher[i] == " ":
            recherche = recherche + "+"
        else :
            recherche = recherche + a_rechercher[i]
    html = urllib.request.urlopen(recherche)
    print(recherche)
    x = html.read().decode()
    for i in range(0,(len(x)-7)):
        mots = x[i] + x[i+1] + x[i+2] + x[i+3] + x[i+4]+ x[i+5]+ x[i+6]
        if mots == "watch?v":
            val = ""
            for k in range(0,19):
                val = val + x[i+k]
            url = ("youtube.com/" + val)
            print(url)
            break 
    if url != "":
        video = pafy.new(url)
        best = video.getbest()
        playurl = best.url
        instance = vlc.Instance()
        player = instance.media_player_new()
        media = instance.media_new(playurl)
        media.get_mrl()
        player.set_media(media)
        player.play()

def stop_music():
    global player
    player.stop()

def actu_du_jour():
    music_ytb("les actus du jour hugo decripte")

def position_base():
    position_init()