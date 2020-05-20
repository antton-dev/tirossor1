"""
tirage au sort.py  Version 1
l'utilisateur rentre plusieurs noms, chiffres et le
programme tire au sort une donnee
"""

import random

# variables et liste
donnee_utilisateur = []
invitation = "entrez un nom : "
tirage = " "
ajouter = "oui"
i = ""
intro = "Bienvenue dans TIROSSOR ! TIROSSOR choisit au hasard un nom que vous avez entr� !"

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
        

