from data_chatbot import data
from random import randint
from fonction_main import *

def phrase_recognition(phrase):
    for i in data :
        for k in i[0]:
            if phrase == k:
                text = str(i[1][randint(0, len(i[1])-1)])
                say(text)
                print("say -> " + text)

if __name__ == "__main__":
    phrase_recognition("quel est ton nom")