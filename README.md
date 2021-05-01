# InMoov App
 
 **déveloper en Francais par Paul Giroux : paul.giroux87@gmail.com
 Pour le projet InMoov -> https://inmoov.fr/**
 
 **n'hèsitez pas à me contacter si vous rencontrer la moindre dificulté lors de l'instalation et/ou l'utilisation**

 ***/!\ le fonctionement n'est garantie que sous Windows***
 
 ## INSTALATION :
 
 installer python 3.9 sur la machine et assurez vous que pip est bien ajouter au PATH
 
Toute les configurations se trouves dans le fichier ".\config\info.ini"
pour l'instalation d'une voix masculine un tuto est à réaliser

s'assurer que les librairie *tkinter, configparser, pyttsx3, random, multiprocessing, pafy, python-vlc, speech_recognition, PyAudio et youtube_dl* sont corectements instaler sur la machine : 

 Avec pip :
```python
pip install nom_librairie
```
en cas de probleme avec l'instalation de PyAudio c'est ici : https://www.journaldunet.fr/web-tech/developpement/1498829-comment-installer-pyaudio-sur-windows-et-eviter-l-erreur-error-microsoft-visual-c-14-0-is-required/

Assurez-vous que VLC est instaler sur la machine, si non : https://www.videolan.org/vlc/index.fr.html

Uploader le programe arduino comptenue dans le dossier prog_arduino sur la/les cartes de controles de votre robot (maximum 2 cartes)

## Utilisation de scripte perssonel:
le fichier ```script_personelle.py``` est à votre disposition pour ajouter vos propre script, n'oubliez pas d'ajouter vos fonction dans ```fonction_liste``` affin qu'elle puisse etre apeler depuis le menu de l'aplication 

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

arduino1.connection() #on conecte la carte arduino n°1
ardunio1.pinMode(13, 1) #on passe le pin 13 en mode OUTPUT

for i in range(0,10):
  arduino1.digitalWrite(13, 1) #on allume la led 13
  sleep(1) #on attend une seconde
  arduino1.digitalWrite(13, 0) #on etein la led 13
  sleep(1) #on attend une seconde
```

## Utilisation des fonctions de mouvements

Pour utiliser ces fonctions dans script_perssonel.py verifier que la ligne ```from body import *``` se trouve bien au debut du fichier

le port de la/les carte(s) arduino doit etre renseigner dans **config/info.ini** rubrique [robot]

la carte et le pin associer à chaques moteurs doit etre renseigner dans **config/info.ini** rubrique [moteurs]

la comande est la suivante : 

**```moove.partie_du_corp.moteur(valeur_en_% : int)```**

**liste de partie du corp :**
* ```moove.head``` : pour selectioner la tête
* ```moove.right_arm``` : pour selectioner le bras droit
* ```moove.left_arm``` : pour selectioner le bras gauche
* ```moove.right_hand``` : pour selectioner la main droite
* ```moove.left_hand``` : pour selectioner la main gauche
* ```moove.pelvis``` : pour selectioner les hanches

#### head : tête (liste des moteurs)
* ```rotation(valeur)``` : pour le mouvement de rotation
* ```up_down(valeur)``` : pour le mouvement haut-bas
* ```mouth(valeur)``` : pour le mouvement de la bouche
* ```eyes_x(valeur)``` : pour le mouvement des yeux en x
* ```eyes_y(valeur)``` : pour le mouvement des yeux en y

#### arm : bras (liste des moteurs)
* ```shoulder_x(valeur)``` : pour le mouvement de l'epaule en x
* ```shoulder_y(valeur)``` : pour le mouvement de l'epaule en y
* ```shoulder_y(valeur)``` : pour le mouvement de l'epaule en z
* ```elbow(valeur)``` : pour le mouvement du coude

#### pelvis : bassin (liste des moteurs)
* ```rocker(valeur)``` : pour le mouvement de balencier
* ```rotation(valeur)``` : pour le mouvement de rotation

#### hand : main (liste des moteurs)
* ```pouce(valeur)``` : pour le mouvement de rotation
* ```index(valeur)``` : pour le mouvement haut-bas
* ```majeur(valeur)``` : pour le mouvement de la bouche
* ```annulaire(valeur)``` : pour le mouvement des yeux en x
* ```auriculaire(valeur)``` : pour le mouvement des yeux en y
* ```all(valeur)``` : pour le mouvement des yeux en y

### Exemple : faire ouvrir et fermer la bouche 5 fois
```python
from body import *
from time import sleep

arduino1.connection()
ardunio1.pinMode(13, 1)

for i in range(0,5):
  moove.head.mouth(100) ### On ouvre la bouche à 100% (à la valeur max indiquer dans config/info.ini)
  sleep(1)
  moove.head.mouth(0) ### on ferme la bouche à 0% (à la valeur min indiquer dans config/info.ini)
  sleep(1)
```
## discutions :
l'enssemble des parole reconue par le robot se trouve dans ```data_chatbot.py```

En plus de celas, le robot est capable de vous donner le nom des capitals du monde et de mettre de la musique avec les comandes vocal :


```
lance la musique (nom de la music)
quelle est la capital du (nom du pays)
```
