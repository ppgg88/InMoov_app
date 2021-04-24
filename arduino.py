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
        print("connection en cours à arduino n°1:")
        try :
            arduino_1 = serial.Serial(cfg["robot"]["arduino_1_com"], int(cfg["robot"]["arduino_1_speed"]), timeout=1)
            sio = io.TextIOWrapper(io.BufferedRWPair(arduino_1, arduino_1))
            print("conection arduino n°1 OK")
            conexion = True
            return(conexion)
        except :
            print("erreur inconue sur le port : " + cfg["robot"]["arduino_1_com"])
            print("conection arduino n°1 echouer")
            conexion = False
            return(conexion)
    else :
        print("erreur d'ouverture du port : " + cfg["robot"]["arduino_1_com"])
        print("conection arduino n°1 echouer")
        conexion = False
        return(conexion)


def connection_robot_2():
    global conexion_2, arduino_2, sio_2
    port_available = serial.tools.list_ports.comports(include_links=False)
    #print(port_available)
    if len(port_available)>0 :
        print("connection en cours à arduino n°2 :")
        try :
            arduino_2 = serial.Serial(cfg["robot"]["arduino_2_com"], int(cfg["robot"]["arduino_2_speed"]), timeout=1)
            sio_2 = io.TextIOWrapper(io.BufferedRWPair(arduino_2, arduino_2))
            print("conection arduino n°2 OK")
            conexion_2 = True
            return(conexion_2)
        except :
            print("erreur inconue sur le port : " + cfg["robot"]["arduino_2_com"])
            print("conection arduino n°2 echouer")
            conexion_2 = False
            return(conexion_2)
    else :
        print("erreur d'ouverture du port : " + cfg["robot"]["arduino_2_com"])
        print("conection arduino n°2 echouer")
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
    print("arduino n°1 : deconecter")

def deconnection_robot_2():
    arduino_2.close()
    print("arduino n°2 : deconecter")

def deconnection_robot():
    global conexion_2, arduino_2, conexion, arduino_1
    if conexion :
        deconnection_robot_1()
    if conexion_2 :
        deconnection_robot_2()

def connection_robot():
    connection_robot_1()
    connection_robot_2()

def digitalWrite_arduino_1(pin, etat):
    """digitalWrite executer sur la carte ardunio 1"""
    global conexion, arduino_1, sio
    if conexion == False :
        print("l'arduino n°1 n'est pas conecter")
        connection_robot_1()
    if conexion == True :
        v = (100000 + (pin*100) + etat)
        send_arduino_1(v)

def analogRead_arduino_1(pin):
    """analogRead executer sur la carte ardunio 1"""
    global conexion, arduino_1, sio
    if conexion == False :
        print("l'arduino n°1 n'est pas conecter")
        connection_robot_1()
    if conexion == True :
        v = (110000 + pin)
        send_arduino_1(v)
        sio.flush()
        result = sio.readline()
        return(int(result))

def digitalRead_arduino_1(pin):
    """analogRead executer sur la carte ardunio 1"""
    global conexion, arduino_1, sio
    if conexion == False :
        print("l'arduino n°1 n'est pas conecter")
        connection_robot_1()
    if conexion == True :
        v = (120000 + pin)
        send_arduino_1(v)
        sio.flush()
        result = sio.readline()
        return(int(result))

def analogWrite_arduino_1(pin, valeur):
    """analoglWrite executer sur la carte ardunio 1 -- val entre 0 et 255"""
    global conexion, arduino_1, sio
    if conexion == False :
        print("l'arduino n°1 n'est pas conecter")
        connection_robot_1()
    if conexion == True :
        v = (200000 + (pin*1000) + valeur)
        send_arduino_1(v)

def pinMode_arduino_1(pin, etat):
    """analoglWrite executer sur la carte ardunio 1 -- val entre 0 et 255"""
    global conexion, arduino_1, sio
    if conexion == False :
        print("l'arduino n°1 n'est pas conecter")
        connection_robot_1()
    if conexion == True :
        v = (130000 + (pin*100) + etat)
        send_arduino_1(v)

def send_arduino_1(data):
    arduino_1.write(str(data).encode("ascii"))
    print("arduino n°1 <-- " + str(data))
    sleep(0.01)

def digitalWrite_arduino_2(pin, etat):
    """digitalWrite executer sur la carte ardunio 2"""
    global conexion_2, arduino_2, sio_2
    if conexion_2 == False :
        print("l'arduino n°2 n'est pas conecter")
        connection_robot_2()
    if conexion_2 == True :
        v = (100000 + (pin*100) + etat)
        send_arduino_2(v)

def analogRead_arduino_2(pin):
    """analogRead executer sur la carte ardunio 2"""
    global conexion_2, arduino_2, sio_2
    if conexion_2 == False :
        print("l'arduino n°1 n'est pas conecter")
        connection_robot_2()
    if conexion_2 == True :
        v = (110000 + pin)
        send_arduino_2(v)
        sio_2.flush()
        result = sio_2.readline()
        return(int(result))

def digitalRead_arduino_2(pin):
    """analogRead executer sur la carte ardunio 2"""
    global conexion_2, arduino_2, sio_2
    if conexion_2 == False :
        print("l'arduino n°1 n'est pas conecter")
        connection_robot_2()
    if conexion_2 == True :
        v = (120000 + pin)
        send_arduino_2(v)
        sio_2.flush()
        result = sio_2.readline()
        return(int(result))

def analogWrite_arduino_2(pin, valeur):
    """analoglWrite executer sur la carte ardunio 2 -- val entre 0 et 255"""
    global conexion_2, arduino_2, sio_2
    if conexion_2 == False :
        print("l'arduino n°1 n'est pas conecter")
        connection_robot_2()
    if conexion_2 == True :
        v = (200000 + (pin*1000) + valeur)
        send_arduino_2(v)

def pinMode_arduino_2(pin, etat):
    """analoglWrite executer sur la carte ardunio 2 -- val entre 0 et 255"""
    global conexion_2, arduino_2, sio_2
    if conexion_2 == False :
        print("l'arduino n°1 n'est pas conecter")
        connection_robot_2()
    if conexion_2 == True :
        v = (130000 + (pin*100) + etat)
        send_arduino_2(v)

def send_arduino_2(data):
    arduino_2.write(str(data).encode("ascii"))
    print("arduino n°2 <-- " + str(data))
    sleep(0.01)

class arduino1 :
    def pinMode(pin, etat):
        """etat == 0 : INPUT // etat==1 : OUTPUT"""
        pinMode_arduino_1(pin, etat)
    def digitalWrite(pin,etat):
        """etat == 0 : LOW // etat==1 : HIGH"""
        digitalWrite_arduino_1(pin, etat)
    def analogWrite(pin,valeur):
        """valeur dans [ 0 ; 255 ]""" 
        analogWrite_arduino_1(pin, valeur)
    def analogRead(pin):
        return analogRead_arduino_1(pin)
    def digitalRead(pin):
        return digitalRead_arduino_1(pin)
    def connection():
        connection_robot_1()
    def deconnection():
        deconnection_robot_1()

class arduino2 :
    def pinMode(pin, etat):
        """etat == 0 : INPUT // etat==1 : OUTPUT"""
        pinMode_arduino_2(pin, etat)
    def digitalWrite(pin,etat):
        """etat == 0 : LOW // etat==1 : HIGH"""
        digitalWrite_arduino_2(pin, etat)
    def analogWrite(pin,valeur):
        """valeur dans [ 0 ; 255 ]""" 
        analogWrite_arduino_2(pin, valeur)
    def analogRead(pin):
        return analogRead_arduino_2(pin)
    def digitalRead(pin):
        return digitalRead_arduino_2(pin)
    def connection():
        connection_robot_2()
    def deconnection():
        deconnection_robot_2()