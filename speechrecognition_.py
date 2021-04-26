import speech_recognition as sr
from data_chatbot import *
from random import randint
import os
from arduino import *

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
            else :
                for j in data_mots_suplementaire:
                    if phrase == (k + " " + j):
                        text = str(i[1][randint(0, len(i[1])-1)])
                        print("say -> " + text)
                        say(text)
                        reponse = False
    if reponse :
        say("je ne vous ai pas compris, il me reste encore beaucoup de chose à apprendre")


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