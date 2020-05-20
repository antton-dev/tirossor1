"""
tirage au sort.py  Version 2
l'utilisateur rentre plusieur noms, chiffres et le
programme tire au sort une donnée
Antton CHEVRIER, 2019-03-06
"""

import random

# variables et liste
donnee_utilisateur = []
invitation = "entrez un nom : "
tirage = " "
ajouter = "oui"
i = ""
intro = "Bienvenue dans TIROSSOR ! TIROSSOR choisit au hasard un nom que vous avez entré !"

#fonction principale main
print(intro)
donnee_utilisateur.append(raw_input(invitation))
while ajouter == "oui":
    ajouter = raw_input("voulez vous ajouter un nom ? oui / non\n")
    if ajouter == "oui":
        donnee_utilisateur.append(raw_input(invitation))
    else:
        print("vous avez saisi : ")
        print(donnee_utilisateur[:])
        print("TIROSSOR a choisit : "+random.choice(donnee_utilisateur) + " !")
        

