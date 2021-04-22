from tkinter import *
import serial
import io
import serial.tools.list_ports
import configparser
from time import *

cfg = configparser.ConfigParser()
cfg.read('config/info.ini')

conexion = False
conexion_2 = False

def connection_robot_1():
    global conexion, arduino_1, sio
    port_available = serial.tools.list_ports.comports(include_links=False)
    #print(port_available)
    if len(port_available)>0 :
        print("connection en cours :")
        try :
            arduino_1 = serial.Serial(cfg["robot"]["arduino_1_com"], int(cfg["robot"]["arduino_1_speed"]), timeout=1)
            sio = io.TextIOWrapper(io.BufferedRWPair(arduino_1, arduino_1))
            print("conection OK")
            conexion = True
            return(conexion)
        except :
            print("erreur inconue sur le port : " + cfg["robot"]["arduino_1_com"])
            conexion = False
            return(conexion)
    else :
        print("erreur d'ouverture du port : " + cfg["robot"]["arduino_1_com"])
        conexion = False
        return(conexion)


def connection_robot_2():
    global conexion_2, arduino_2, sio_2
    port_available = serial.tools.list_ports.comports(include_links=False)
    #print(port_available)
    if len(port_available)>0 :
        print("connection en cours :")
        try :
            arduino_2 = serial.Serial(cfg["robot"]["arduino_2_com"], int(cfg["robot"]["arduino_2_speed"]), timeout=1)
            sio_2 = io.TextIOWrapper(io.BufferedRWPair(arduino_2, arduino_2))
            print("conection OK")
            conexion_2 = True
            return(conexion_2)
        except :
            print("erreur inconue sur le port : " + cfg["robot"]["arduino_2_com"])
            conexion_2 = False
            return(conexion_2)
    else :
        print("erreur d'ouverture du port : " + cfg["robot"]["arduino_2_com"])
        conexion_2 = False
        return(conexion_2)


def controle_moteur_1(pin, valeur):
    """prend en entrer le pin du moteur à controler et le positionement en angle de ce moteurs"""
    """la trame de controle du moteur en hexadecimal sera : 22 pin angle"""
    global conexion, arduino_1, sio
    if conexion == False :
        print("l'arduino n°1 n'est pas conecter")
        connection_robot_1()
    if conexion == True :
        v = (pin * 1000)
        v += valeur
        arduino_1.write(str(v).encode("ascii"))
        print(str(v))
        sleep(0.01)

def controle_moteur_2(pin, valeur):
    """prend en entrer le pin du moteur à controler et le positionement en angle de ce moteurs"""
    """la trame de controle du moteur en hexadecimal sera : 22 pin angle"""
    global conexion_2, arduino_2, sio_2
    if conexion_2 == False :
        print("l'arduino n°2 n'est pas conecter")
    else :
        v = (pin * 1000)
        v += valeur
        arduino_2.write(str(v).encode("ascii"))
        print(str(v))
        sleep(0.01)

def deconnection_robot_1():
    arduino_1.close()

def deconnection_robot_2():
    arduino_2.close()

def deconnection_robot():
    global conexion_2, arduino_2, conexion, arduino_1
    if conexion :
        arduino_1.close()
    if conexion_2 :
        arduino_2.close()

def connection_robot():
    connection_robot_1()
    connection_robot_2()