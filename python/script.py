# coding: utf-8

import sys
print("Bonjour Monsieur le Detective !")
foundKey = 0
points = 0

while True:

    choice = input(
        "Entrez dans la maison et choisissez une piece pour commencer l'enquete. Choisis une piece: Cuisine, Chambre, Salon ")

    if choice == "Cuisine":
        # Cuisine
        print("Ton score est %i " % points)
        print(" Tu es maintenant dans la Cuisine")
        while True:
            print("Tu as trouvé deux tiroirs !")
            choice2 = input("quel tiroirs choisi tu ? 1 ou 2 ?")
            print("Ton score est %i " % points)

            if choice2 == "1":
                if foundKey == 0:
                    print(
                        "Le tiroir est bloqué il faut que tu essayes un autre tiroir ")
            else:

                print(
                    "Le tiroir est ouvert et tu as trouvé l'arme du crime. Tu as gagné")
                points = points + 5
                print("Ton score est %i " % points)
                sys.exit()

            if choice2 == "2":
                print("Ton score est %i " % points)
                print("Tu as trouvé une clé dans le tiroir. Retourne dans la cuisine !")
                foundKey = 1
                points = points + 5
                sys.exit()

        else:
            print("Je n'ai pas compris")

    if choice == "Chambre":
        # Chambre
        print("Ton score est %i " % points)
        print("Perdu ! Tu n'as rien trouvé...")
        points = points - 2

        sys.exit()

    if choice == "Salon":
        # Salon
        while True:
            print("Ton score est %i " % points)
            print(" Tu es dans le salon")

            choice3 = input("As tu trouvé une piece a conviction ?")
            if choice3 == "Un portefeuille":

                print("Ton score est %i " % points)
                print(
                    " Tu as trouvé le portefeuille. Tu gagnes 2 points mais tu as pas resolu l'enquete")
                points = points + 2

                print(
                    "Tu es dans le salon. Tu as le choix entre choisir une nouvelle piece ou sortir de la maison")
                choice4 = input("Veux-tu choisir une autre salle ?")
                if choice4 == "oui":
                    break
                elif choice4 == "non":
                    print(" C'est perdu ")
                    print("Ton score est %i " % points)
                    sys.exit()
                    points = points - 3

            elif choice3 == "rien":
                print("Tu as rien trouvé. Tu as perdu")
                sys.exit()
