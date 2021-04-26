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
        [("celas dépent de l'humeur de " + cfg["robot"]["maker_name"]), ("en fonction de l'humeur de " + cfg["robot"]["maker_name"])]
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
        ["Bonjour comment vas-tu", "Bonjour comment tu vas", ("Bonjour " + cfg["robot"]["robot_name"] + " comment vas-tu"),("Bonjour " + cfg["robot"]["robot_name"] + " comment tu vas"), "Salut comment vas-tu", "Salut comment tu vas", ("Salut " + cfg["robot"]["robot_name"] + " comment vas-tu"), ("Salut " + cfg["robot"]["robot_name"] + " comment tu vas")],
        ["je vais bien mais tu sais je suis un robot ! et toi comment va-tu ?", "tu sais je suis un robot je vais toujour bien ! et toi comment va-tu ?"]
    ],
    [
        ["comment vas-tu", "comment tu vas"],
        ["bonjour, je vais bien mais tu sais je suis un robot ! et toi comment va-tu ?", "bonjour, tu sais je suis un robot je vais toujour bien ! et toi comment va-tu ?"]
    ],
    [
        ["ça va", "tout va bien", "je vais bien", "tu vas bien", "moi ça va", "moi tout va bien", "moi je vais bien", "moi tu vas bien"],
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
        ["regarde à droite", "regarde à ta droite", "regarde sur ta droite", "regarde sur la droite"],
        ["je regarde à droite", "je regarde sur la droite"],
        [see_left]
    ],
    [
        ["regarde à gauche", "regarde à ta gauche", "regarde sur ta gauche", "regarde sur la gauche"],
        ["je regarde à gauche", "je regarde sur la gauche"],
        [see_right]
    ],
    [
        ["regarde devant toi", "regarde devant", "regarde au centre"],
        ["je regarde vers l'avans", "je regarde devans moi"],
        [see_front]
    ],
    [
        ["es-tu un Terminator"],
        ["non mais méfie toi je pourait le devenir", "non,   et toi est tu saraconorre"]
    ],
    [
        ["qui suis-je", "sais-tu qui je suis"],
        ["un humain mais je ne peut pas en etre sur", "un humain mais je ne suis pas certain"]
    ],
    [
        ["as-tu un site internet", "peut-on te trouver sur internet"],
        ["tu peut retrouver la page du projet InMouv à l'adresse internet suivante : trois W point InMouv point F R"]
    ],
    ### CAPITAL DU MONDE ###
    '''[
        ["quelle est la capitale de l'Allemagne", "de quel pays Berlin est la capitale"],
        ["Berlin est la capitale de l'Allemagne", "la capitale de l'Allemagne est berlin"]
    ],
    [
        ["quelle est la capitale des Emirats arabes unis", "de quel pays Abou Dabi est la capitale"],
        ["Abou Dabi est la capitale des Emirats arabe unis", "la capitale des Emirats arabe unis est Abou Dabi"]
    ],
    [
        ["quelle est la capitale du Nigeria", "de quel pays Abuja est la capitale"],
        ["Abuja est la capitale du Nigeria", "la capitale du Nigeria est Abuja"]
    ],
    [
        ["quelle est la capitale du Ghana", "de quel pays Accra est la capitale"],
        ["Accra est la capitale du Ghana", "la capitale du Gahna est accra"]
    ],
    [
        ["quelle est la capitale du Turkménistan", "de quel pays Avhgabat est la capitale"],
        ["Avhgabatest la capitale du Turkménistan", "la capitale du Turkménistan est Avhgabat"]
    ],
    [
        ["quelle est la capitale de l'Éthiopie", "de quel pays Addis-Abeba est la capitale"],
        ["Addis-Abeba est la capitale de l'Éthiopie", "la capitale de l'Éthiopie est Addis-Abeba"]
    ],
    [
        ["quelle est la capitale de l'Algérie", "de quel pays Alger est la capitale"],
        ["Alger est la capitale de l'Algérie", "la capitale de l'Algérie est Alger"]
    ],
    [
        ["quelle est la capitale de la Jordanie", "de quel pays Amman est la capitale"],
        ["Amman est la capitale de la Jordanie", "la capitale de la Jordanie est Amman"]
    ],
    [
        ["quelle est la capitale des Pays-Bas", "de quel pays Amsterdam est la capitale"],
        ["Amsterdam est la capitale des Pays-Bas", "la capitale des Pays-Bas est Amsterdam"]
    ],'''
] 

data_mots_suplementaire_end = [
    "merci",
    "merci beaucoup",
    "merci à toi",
    "merci bien",
    "s'il te plaît",
    cfg["robot"]["robot_name"],
]

data_mots_suplementaire_start = [
    "s'il te plaît",
    cfg["robot"]["robot_name"],
    "et",
    "dit moi"
]