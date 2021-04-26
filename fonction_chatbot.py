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
    moove.head.rotation(0)
    main.moteur_1_h.set(0)

def see_right():
    import main
    moove.head.rotation(100)
    main.moteur_1_h.set(100)

def see_front():
    import main
    moove.head.rotation(50)
    main.moteur_1_h.set(50)