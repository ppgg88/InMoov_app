from tkinter import *
import serial
import io
import serial.tools.list_ports
import configparser
from time import *

cfg = configparser.ConfigParser()
cfg.read('config/info.ini')

conexion = False

def connection_robot():
    global conexion, arduino, sio
    port_available = serial.tools.list_ports.comports(include_links=False)
    print(port_available)
    if len(port_available)>0 :
        print("connection en cours :")
        try :
            arduino = serial.Serial(cfg["robot"]["arduino_com"], int(cfg["robot"]["arduino_speed"]), timeout=1)
            sio = io.TextIOWrapper(io.BufferedRWPair(arduino, arduino))
            print("conection OK")
            conexion = True
            return(conexion)
        except :
            print("erreur inconue sur le port : " + cfg["robot"]["arduino_com"])
            conexion = False
            return(conexion)
    else :
        print("erreur d'ouverture du port : " + cfg["robot"]["arduino_com"])
        conexion = False
        return(conexion)

def controle_moteur(pin, valeur):
    """prend en entrer le pin du moteur à controler et le positionement en angle de ce moteurs"""
    """la trame de controle du moteur en hexadecimal sera : 22 pin angle"""
    global conexion, arduino, sio
    if conexion == False :
        print("l'arduino n'est pas conecter")
    else :
        v = (pin * 1000)
        v += valeur
        arduino.write(str(v).encode("ascii"))
        print(str(v))
        sleep(0.01)
