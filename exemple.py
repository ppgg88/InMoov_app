"""from tkinter import *

def show_next():
    global index
    frames[index].grid_forget()
    index = (index + 1) % len(frames)
    frames[index].grid(row=0)

root = Tk()
frames = [ Frame(root, width=100, height=100, bg=color) for color in ('red', 'green', 'blue')]
index = 0
frames[index].grid(row=0)

acc = Frame(frames[1])
bienvenue = Label(acc, text="Bienvenue sur l'interface de controle de la tête p1 :")
bienvenue.pack()
acc.pack()

ac = Frame(frames[1])
bienvenue = Label(ac, text="Bienvenue sur l'interface de controle de la tête ligne 2 :")
bienvenue.pack()
ac.pack()

Button(root, text='next', command=show_next).grid(row=1)
root.mainloop()

from gtts import gTTS
import os
import time
import playsound

def speak(text):
    tts = gTTS(text=text, lang='fr',slow=False)
    filename ='speech.mp3'
    tts.save(filename)
    playsound.playsound(filename)

speak("bonjour tout le monde ")"""   
import speech_recognition as sr  
 
r  = sr.Recognizer()
with sr.Microphone() as source:
    print("Dites quelque chose")
    audio = r.listen(source)
try:
    text = r.recognize_google(audio)
    print("Vous avez dit : " + text)
except sr.UnknownValueError:
    print("L'audio n'as pas été compris")
except sr.RequestError as e:
    print("Le service Google Speech API ne fonctionne plus" + format(e))