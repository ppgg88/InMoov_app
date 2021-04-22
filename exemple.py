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
root.mainloop()"""

from gtts import gTTS
import os
import time
import playsound

def speak(text):
    tts = gTTS(text=text, lang='fr',slow=False)
    filename ='speech.mp3'
    tts.save(filename)
    playsound.playsound(filename)

speak("bonjour tout le monde ")