from tkinter import *
from arduino import *
from body import *
import configparser
import pyttsx3
from random import randint
from multiprocessing import Process
from time import *

longeur = 17
engine = pyttsx3.init()
voices = engine.getProperty('voices')

engine.setProperty('rate', int(cfg["robot"]["read_speed"]))
engine.setProperty("voice", voices[3].id)

def speech(t):
    global longeur, text
    longeur = len(str(t))
    text = t

def play_speech():
    global text
    engine.say("       " + text)
    engine.runAndWait()

def speak_mouth():
    global longeur
    for i in range(0, int(longeur/5.5)):
        position_aleatoire = randint((int(cfg["moteurs"]["bouche_tete_min"])+10), int(cfg["moteurs"]["bouche_tete_max"])-10)
        moteur_head_3(position_aleatoire)
        print(position_aleatoire)
        sleep(randint(10,30)/100)
        moteur_head_3(0)
        sleep(randint(10,30)/100)


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