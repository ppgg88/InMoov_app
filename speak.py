from arduino import *
import configparser
import pyttsx3
from random import randint
from multiprocessing import Process
from time import *

engine = pyttsx3.init()
voices = engine.getProperty('voices')

engine.setProperty('rate', int(cfg["robot"]["read_speed"]))
engine.setProperty("voice", voices[int(cfg["robot"]["voice_id"])].id)

def speech(t):
    print("say : " + t)
    global longeur, text
    longeur = len(str(t))
    text = t

def play_speech():
    global text
    engine.say("       " + text)
    engine.runAndWait()

def speak_mouth():
    global longeur
    for i in range(0, int(longeur/4.5)):
        position_aleatoire = randint((int(cfg["moteurs"]["bouche_tete_min"])+10), int(cfg["moteurs"]["bouche_tete_max"])-10)
        moteur_head_3(position_aleatoire)
        print(position_aleatoire)
        sleep(randint(10,30)/100)
        moteur_head_3(0)
        sleep(randint(10,30)/100)

def moteur_head_3(position):
    #mouvement bouche
    angle = int(cfg["moteurs"]["bouche_tete_max"])-int(cfg["moteurs"]["bouche_tete_min"])
    angle = ((float(position)/100) * angle) + float(cfg["moteurs"]["bouche_tete_min"])
    print("head 3 : " + str(int(angle)))
    if int(cfg["moteurs"]["bouche_tete_arduino"]) == 1 :
        controle_moteur_1(int(cfg["moteurs"]["bouche_tete_pin"]), int(angle))
    else :
        controle_moteur_2(int(cfg["moteurs"]["bouche_tete_pin"]), int(angle))


fichier = open("temp_lecture", "r")
text = str(fichier.read())
fichier.close()
speech(text)
if __name__ == '__main__':
    th2 = Process(target=play_speech)
    th1 = Process(target=speak_mouth)
    th1.start()
    th2.start()
    th1.join()
    th2.join()