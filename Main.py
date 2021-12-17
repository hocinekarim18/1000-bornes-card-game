from Partie import Partie
from time import sleep

###############################################################
#                  Programme Principale                       #
###############################################################
print("Bienvenus dans le jeu des 1000 Bornes !!")
# Choisir le nombre de joueurs
nb = input("Combien de joueurs vont participer à la partie?  Choix: ")
while nb not in ["2", "3", "4", "5", "6"]:
    print("Pour commencer la partie il faut entre 2 et 6 joueurs")
    nb = input("Entrez le nombre de joueurs. Choix: ")

# Créer une partie des 1000 bornes selon le nombre de joueurs
nb = int(nb)
partie = Partie(nb)
partie.creerJoueurs()
for i in range(len(partie.joueurs)):
    # Afficher les joueurs qui participent à la partie
    print(f"Joueur {i} : {partie.joueurs[i].nom}")
print('')



# Créer un paquet de carte correpondant aux 106 cartes du jeu
partie.creerPaquetCartes()

# Les joeurs piochent 6 cartes pour commencer la partie
for i in range(6):
    for k in range(len(partie.joueurs)):
        partie.joueurs[k].piocherCarte(partie.paquetCarte)

partieEnCours = 1
Tour = 0
#############################   Debut de la Partie    ##############################################
while partieEnCours:
    Tour += 1
    i = 0

    print(f"\n-------------------- Tour {Tour} ---------------------------")
    while i < nb:
        print(f"Nombre de cartes dans la pioche: {len(partie.paquetCarte)} cartes.\n")
        # Les joueurs joue chacun leur tour selon l'ordre de création des joueurs
        # Le joueur commence son tour en piochant une carte puis joue une carte
        partie.joueurs[i].piocherCarte(partie.paquetCarte)
        # Le joueur joue une carte
        ind = partie.jouerCarte(partie.joueurs[i].nom)
        if ind != -1:
            # si ind !=-1 cela veut dire qu'il y'a eu coup fourré et l'ordre de jeu des joeurs a changer
            i = ind
        # Vérifier si un joueur à gagner
        partieEnCours = partie.ifWin()
        if partieEnCours == 0:
            break
        # Passer au joueur i+1
        i += 1

        # Temporisation pour passer la main au joueur suivant
        #sleep(2)

# Classement de l a partie
print("\n-----------------------  Classement  ----------------------------- ")
classement = []
for joueur in partie.joueurs:
    classement.append([joueur.nom, joueur.distanceParcourue])
classement = sorted(classement, key=lambda x: x[1], reverse = True)
# Affichage du classement en fin de partie
for i in range(len(classement)):
    print(f"{i+1}: {classement[i][0]}, { classement[i][1]} Kms")
