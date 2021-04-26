import speech_recognition as sr
from data_chatbot import *
from fonction_chatbot import *
from random import randint
import os
from arduino import *
import configparser

cfg = configparser.ConfigParser()
cfg.read('./config/info.ini')

def say(text):
    fichier = open("temp_lecture", "w")
    fichier.write(text)
    fichier.close()
    deconnection_robot()
    os.system("py speak.py")
    connection_robot()

def phrase_recognition(phrase):
    reponse = True
    for i in data :
        for k in i[0]:
            if phrase == k:
                text = str(i[1][randint(0, len(i[1])-1)])
                print("say -> " + text)
                say(text)
                reponse = False
                try :
                    i[2][0]()
                except:
                    pass
            else :
                for j in data_mots_suplementaire_end:
                    for t in data_mots_suplementaire_start:
                        if ((phrase == (k + " " + j)) or (phrase == (t + " " + k)) or (phrase == (t + " " + k + " " + j))) and reponse == True:
                            text = str(i[1][randint(0, len(i[1])-1)])
                            print("say -> " + text)
                            say(text)
                            reponse = False
                            try :
                                for fonction in i[2]:
                                    fonction()
                            except:
                                pass
    if reponse and capital(phrase)==False:
        say("je ne vous ai pas compris, il me reste encore beaucoup de chose à apprendre")

def capital(text):
    import csv;
    f= open("chatbot/capital.csv", encoding="utf8")
    capital = csv.reader(f) 
    capital_pays = []
    for row in capital :
        capital_pays = capital_pays + [row]
    pays_trouver = False
    pays = ""  
    i=0
    if (len(text)>22):
        while not(pays_trouver) and (len(text)-len(pays))>22:
            pays = text[len(text)-1-i] + pays
            if pays == (" " + cfg["robot"]["robot_name"]):
                pays = ""
            i+=1
            for liste in capital_pays :
                if pays == liste[0]:
                    print(liste[1])
                    say("la capitale de " + pays + " est " + liste[1])
                    pays_trouver = True

def speak_recognition():
    rec_vocal = sr.Recognizer()
    mic = sr.Microphone()
    rec_vocal.pause_threshold = 0.5
    rec_vocal.non_speaking_duration = 0.4
    global init_mic
    with mic as src:
        audio = rec_vocal.listen(src)
        try :
            text = rec_vocal.recognize_google(audio, language="fr-FR")
            print("reconaissance vocal ->" + str(text))
            phrase_recognition(str(text))
        except :
            pass

if __name__ == "__main__":
    while True :
        speak_recognition()