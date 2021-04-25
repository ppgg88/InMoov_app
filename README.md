# InMoov_app
 
 **déveloper en Francais par Paul Giroux : paul.giroux87@gmail.com
 Pour le projet InMoov -> https://inmoov.fr/**

 ***/!\ le fonctionement n'est garantie que sous Windows***
 
Toute les configurations se trouves dans le fichier ".\config\info.ini"
pour l'instalation d'une voix masculine un tuto est à réaliser

s'assurer que les librairie _tkinter, configparser, pyttsx3, random, multiprocessing et time_ sont corectements instaler sur la machine : 

 Avec pip :
```python
pip install nom_librairie
```


## Utilisation des fonctions arduino :

Pour utiliser la librairie arduino dans script_perssonel.py verifier que la ligne ```from arduino import *``` se trouve bien au debut du fichier

le port de la/les carte(s) arduino doit etre renseigner dans config/info.ini rubrique [robot]

pour envoyer une comande sur la carte ardunino n°1 (resp 2) utiliser la class : arduino1 (resp arduino2)

les fonction disponnible sont les suiventes :
* ```pinMode(pin, etat)``` /!\ etat==0 : INPUT & etat==1 : OUTPUT
* ```digitalWrite(pin, etat)```
* ```digitalRead(pin)```
* ```analogWrite(pin, valeur)```
* ```analogRead(pin)```
* ```connection()``` permets de connecter la carte et le programe python
* ```deconnection()``` permets de deconnecter la carte et le programe python

pour plus d'information sur l'utilisation de ces fonctions vous pouvez vous referer à la reference arduno : https://www.arduino.cc/reference/en/

### Exemple : faire clignoter une led 10 fois (sur le pin 13 de l'arduino n°1)

```python
from arduino import *
from time import sleep

arduino1.connection()
ardunio1.pinMode(13, 1)

for i in range(0,10):
  arduino1.digitalWrite(13, 1) #on allume la led 13
  sleep(1) #on attend une seconde
  arduino1.digitalWrite(13, 0) #on etein la led 13
  sleep(1) #on attend une seconde
```

## Utilisation des fonctions de mouvements

*cette fonctionalité est en developement
