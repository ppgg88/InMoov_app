from body import *
from arduino import *

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
    main.moteur_1_h.set(0)

def see_right():
    import main
    main.moteur_1_h.set(180)

def see_front():
    import main
    main.moteur_1_h.set(90)