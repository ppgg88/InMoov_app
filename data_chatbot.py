import configparser
import csv
from fonction_chatbot import *

cfg = configparser.ConfigParser()
cfg.read('./config/info.ini')

data = [
    [
        ["quel est ton nom", "comment t'appelles-tu", "qui es-tu", "comment te prenomme tu", "quel est ton prénom"],
        [("mon nom est " + cfg["robot"]["robot_name"]), ("je m'appelle "  + cfg["robot"]["robot_name"])]
    ],
    [
        ["quel est ton âge", "quel âge as-tu", "depuis combien de temps es-tu né"],
        [("j'ai " + cfg["robot"]["robot_age"] + "ans"), ("j'ai " + cfg["robot"]["robot_age"] + "ans, mais l'age ne compte pas vraiment pour un robot !")]
    ],
    [
        ["kit à fabriquer", "qui est ton meilleur", "qui t'a fabriqué", "quelle est la personne qui t'a fabriqué", "qui est ton maker"],
        [("c'est " + cfg["robot"]["maker_name"] + "qui m'a fabriquer, j'apartien à la grande famille de robot InMouv")]
    ],
    [
        [("qui est " + cfg["robot"]["maker_name"]), ("connais-tu " + cfg["robot"]["maker_name"]), ("sais-tu qui est " + cfg["robot"]["maker_name"]),("voiture qui est " + cfg["robot"]["maker_name"]),("vois-tu qui est" + cfg["robot"]["maker_name"])],
        ["bien sur il s'agit de la perssone qui ma construite", "oui c'est un peut comme un membre de ma famille sans lui je n'existerais pas"]
    ],
    [
        ["as-tu des cheveux", "quelle est la couleur de tes cheveux", "de quelle couleur es-tu", "quelle est ta couleur", "comment t'habitues", "comment t'habilles tu"],
        [("celas depent de l'humeur de " + cfg["robot"]["maker_name"]), ("en fonction de l'humeur de " + cfg["robot"]["maker_name"])]
    ],
    [
        ["as-tu des enfants", "es-tu père", "es-tu papa", "et du perds"],
        ["je suis un robot je n'ai pas d'enfants", "cette question est etrange, je suis un robot"]
    ],
    [
        ["où es-tu né", "quel est ton lieu de naissance", "où tu es né"],
        ["je suis née sur une imprimante 3D comme tout les autre membre de la famille de robot InMouv"]
    ],
    [
        ["quelle est la capitale de la France", "quelle est la capitale française", "quelle est la capitale de la République française"],
        ["c'est Paris", "la capitale de la france est paris", "paris est la capitale de la france"]
    ],
    [
        ["Bonjour", "Salut"],
        ["Bonjour, que puit-je faire pour vous ?", "Bonjour, je peut vous aider ?", "Bonjour, je suis comptemps de vous voir"]
    ],
    [
        ["Bonjour comment vas-tu", ("Bonjour " + cfg["robot"]["robot_name"] + " comment vas-tu"), "Salut comment vas-tu", ("Salut " + cfg["robot"]["robot_name"] + " comment vas-tu")],
        ["bonjour, je vais bien mais tu sais je suis un robot ! et toi comment va-tu ?", "bonjour, tu sais je suis un robot je vais toujour bien ! et toi comment va-tu ?"]
    ],
    [
        ["ça va", "tout va bien", "je vais bien", "tu vas bien"],
        ["c'est une bonne nouvelle ! je peut faire quelque chose pour toi ?"]
    ],
    [
        ["ça ne va pas", "je vais mal", "je ne me sent pas bien"],
        ["ail ! si je peut faire quelque chose pour toi n'hesite pas !"]
    ],
    [
        ["merci","merci beaucoup","merci à toi","merci bien",],
        ["de rien !", "de rien, je peut faire autre chose ?", "de rien, je peut faire autre chose pour toi ?"]
    ],
    [
        [cfg["robot"]["robot_name"]],
        ["oui ? je peut faire quelque chose ?", "je suis là !", "c'est mon nom !", "c'est comme ça que les gents m'apelle"]
    ],
    [
        ["ouvre la bouche", "ouvre ta bouche"],
        ["j'ouvre ma bouche"],
        [open_mouth]
    ],
    [
        ["ferme la bouche", "ferme ta bouche"],
        ["je ferme ma bouche"],
        [close_mouth]
    ],
    [
        ["regarde à droite", "regarde à ta droite"],
        ["je regarde à droite", "je regarde sur la droite"],
        [see_left]
    ],
    [
        ["regarde à gauche", "regarde à ta gauche"],
        ["je regarde à gauche", "je regarde sur la gauche"],
        [see_right]
    ],
    [
        ["es-tu un terminator"],
        ["non mais mefie toi je pourais le devenir", "non et toi est tu saraconorre"]
    ],
]

data_mots_suplementaire = [
    "merci",
    "merci beaucoup",
    "merci à toi",
    "merci bien",
    "s'il te plaît",
    cfg["robot"]["robot_name"]
]
