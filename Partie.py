from random import shuffle
from Joueur import Joueur
from Defense import Defense
from Attaque import Attaque
from Bottes import Bottes
from Distance import Distance


class Partie:

    def __init__(self, nb):
        self.nb_joueurs = nb        # Nombre de joeurs dans la partie
        self.joueurs = []           # Joueurs participant à la partie
        self.paquetCarte = []       # Paquet de carte duquel les joueurs pichent leurs cartes

    # Créer les joueurs (objets) qui participent à la partie
    def creerJoueurs(self):
        for i in range(self.nb_joueurs):
            Nom_joueur = str(input(f'Veuillez entrer le nom du Joueur {i + 1}: '))
            # Le nom du Joueur doit être unique:
            for joueur in self.joueurs:
                if joueur.nom.lower() == Nom_joueur.lower():
                    print(f"Erreur: le nom: {Nom_joueur} est déja utilisé.")
                    Nom_joueur = str(input(f'Veuillez entrer le nom du Joueur {i + 1}: (different de {Nom_joueur}) '))
                    while joueur.nom.lower() == Nom_joueur.lower():
                        print(f"Erreur: le nom: {Nom_joueur} est déja utilisé.")
                        Nom_joueur = str(input(f'Veuillez entrer le nom du Joueur {i + 1}: (different de {Nom_joueur}) '))
            self.joueurs.append(Joueur(Nom_joueur))

    # Créer un paquet de carte
    def creerPaquetCartes(self):
        paquet = []
        # Creer les carte Defense
        for i in range(14):
            if i < 6:
                paquet.append(Defense('Reparation'))
                paquet.append(Defense('Essence'))
                paquet.append(Defense('Roue de secours'))
                paquet.append(Defense('Fin de limitation de vitesse'))
            paquet.append(Defense('Feu vert'))

        # Creer les cartes attaque
        for i in range(5):
            if i < 3:
                paquet.append(Attaque("Accident de la route"))
                paquet.append(Attaque("Panne d'essence"))
                paquet.append(Attaque("Crevaison"))
            if i < 4:
                paquet.append(Attaque("Limitation de vitesse"))

            paquet.append(Attaque("Feu rouge"))


        # Creer les carte Bottes
        paquet.append(Bottes('As du volant'))
        paquet.append(Bottes('Increvable'))
        paquet.append(Bottes('Camion citerne'))
        paquet.append(Bottes('Prioritaire'))

        # Creer les carte distance
        for i in range (12):
            if i < 4:
                paquet.append(Distance('Hirondelle'))
            if i < 10:
                paquet.append(Distance('Escargot'))
                paquet.append(Distance('Canard'))
                paquet.append(Distance('Papillon'))

            paquet.append(Distance('Lievre'))
        shuffle(paquet)
        shuffle(paquet)
        self.paquetCarte = paquet

    # Implémenter le coup fourré
    def coupFourre (self,indexJ1,  indexJ2, indexC):
        for i in range(len(self.joueurs[indexJ2].main)):
            botte = self.joueurs[indexJ2].main[i]
            if self.joueurs[indexJ1].main[indexC].cartetype == 'Feu rouge' and botte.cartetype == 'Prioritaire':
                choix = str(input(f" Votre adversaire vous attaque avec {self.joueurs[indexJ1].main[indexC].cartetype}. Voulez vous jouer le coup fourré avec la carte {botte.cartetype}. (Oui / Non):   "))
                if choix.lower() == "oui":
                    if self.joueurs[indexJ2].distanceParcourue + 300  <= 1000:
                        print(f"Coup fourré !! + 300 Kms pour le joueur: {self.joueurs[indexJ2].nom}")
                        self.joueurs[indexJ2].distanceParcourue += 300
                        self.joueurs[indexJ2].bottes.append(botte)
                        self.joueurs[indexJ2].poserCarte(i)
                        self.joueurs[indexJ1].poserCarte(indexC)
                        self.joueurs[indexJ2].piocherCarte(self.paquetCarte)

                        # Joueur ayant exécuté le coup fourré peut directement rejoué
                        self.joueurs[indexJ2].piocherCarte(self.paquetCarte)
                        self.jouerCarte(self.joueurs[indexJ2].nom)
                        return 1
                    else:
                        print("Vous ne pouvez pas jouer le coup fourré car vous allez dépassé les 1000 bornes.")
                        self.joueurs[indexJ2].pileBataille.append(self.joueurs[indexJ1].main[indexC])

                break
            elif self.joueurs[indexJ1].main[indexC].cartetype == 'Accident de la route' and botte.cartetype == 'As du volant':
                choix = str(input(f" Votre adversaire vous attaque avec {self.joueurs[indexJ1].main[indexC].cartetype}. Voulez vous jouer le coup fourré avec la carte {botte.cartetype}. (Oui / Non):   "))
                if choix.lower() == "oui":
                    if self.joueurs[indexJ2].distanceParcourue + 300 <= 1000:
                        print(f"Coup fourré !! + 300 Kms pour le joueur: {self.joueurs[indexJ2].nom}")
                        self.joueurs[indexJ2].distanceParcourue += 300
                        self.joueurs[indexJ2].bottes.append(botte)
                        self.joueurs[indexJ2].poserCarte(i)
                        self.joueurs[indexJ1].poserCarte(indexC)
                        # Joueur ayant exécuté le coup fourré peut directement rejoué
                        self.joueurs[indexJ2].piocherCarte(self.paquetCarte)
                        print(self.joueurs[indexJ2])
                        self.jouerCarte(self.joueurs[indexJ2].nom)
                        return 1
                    else:
                        print("Vous ne pouvez pas jouer le coup fourré car vous allez dépassé les 1000 bornes.")
                break

            elif  self.joueurs[indexJ1].main[indexC].cartetype == "Panne d'essence" and botte.cartetype == 'Camion citerne':
                choix = str(input( f" Votre adversaire vous attaque avec {self.joueurs[indexJ1].main[indexC].cartetype}. Voulez vous jouer le coup fourré avec la carte {botte.cartetype}. (Oui / Non):   "))
                if choix.lower() == "oui":
                    if self.joueurs[indexJ2].distanceParcourue + 300 <= 1000:
                        print(f"Coup fourré !! + 300 Kms pour le joueur: {self.joueurs[indexJ2].nom}")
                        self.joueurs[indexJ2].distanceParcourue += 300
                        self.joueurs[indexJ2].bottes.append(botte)
                        self.joueurs[indexJ2].poserCarte(i)
                        self.joueurs[indexJ2].piocherCarte(self.paquetCarte)
                        self.joueurs[indexJ1].poserCarte(indexC)
                        # Joueur ayant exécuté le coup fourré peut directement rejoué
                        self.joueurs[indexJ2].piocherCarte(self.paquetCarte)
                        print(self.joueurs[indexJ2])
                        self.jouerCarte(self.joueurs[indexJ2].nom)
                        return 1
                    else:
                        print("Vous ne pouvez pas jouer le coup fourré car vous allez dépassé les 1000 bornes.")
                break

            elif  self.joueurs[indexJ1].main[indexC].cartetype == 'Crevaison' and botte.cartetype == 'Increvable':
                choix = str(input( f" Votre adversaire vous attaque avec {self.joueurs[indexJ1].main[indexC].cartetype}. Voulez vous jouer le coup fourré avec la carte {botte.cartetype}. (Oui / Non):   "))
                if choix.lower() == "oui":
                    if self.joueurs[indexJ2].distanceParcourue + 300 <= 1000:
                        print(f"Coup fourré !! + 300 Kms pour le joueur: {self.joueurs[indexJ2].nom}")
                        self.joueurs[indexJ2].distanceParcourue += 300
                        self.joueurs[indexJ2].bottes.append(botte)
                        self.joueurs[indexJ2].poserCarte(i)
                        self.joueurs[indexJ2].piocherCarte(self.paquetCarte)
                        self.joueurs[indexJ1].poserCarte(indexC)
                        # Joueur ayant exécuté le coup fourré peut directement rejoué
                        self.joueurs[indexJ2].piocherCarte(self.paquetCarte)
                        print(self.joueurs[indexJ2])
                        self.jouerCarte(self.joueurs[indexJ2].nom)

                        return 1
                    else:
                        print("Vous ne pouvez pas jouer le coup fourré car vous allez dépassé les 1000 bornes.")
                break

    # Afficher les cartes actives présentes sur la table
    def afficherTable(self, indexJ):
        message = 'Table de jeu:\n'
        for i in range (len(self.joueurs)):
            if i != indexJ:
                message += f'Piles de cartes du joueur: {self.joueurs[i].nom}, ({self.joueurs[i].distanceParcourue} Kms): \n'
                # Afficher les obstacles
                message += f"Pile de Bataille : "
                if not len(self.joueurs[i].pileBataille) == 0:
                    message += f"{self.joueurs[i].pileBataille[-1].cartetype}  "
                message += "\n"

                # Afficher les parades jouées
                message += f"Pile de vitesse : "
                if not len(self.joueurs[i].pileVitesse) == 0:
                    message += f"{self.joueurs[i].pileVitesse[-1].cartetype}  "
                message += "\n"

                # Afficher les bottes jouées
                message += f"Bottes : "
                for carte in self.joueurs[i].bottes:
                    message += f"{carte.cartetype}  "
                message += "\n------------------------------------------------------\n"
        return message

    # Gérer les effets d'une carte attaque
    def attaquer(self, indexJ ,indexC):
        nameJ = str(input('Quel joueur voulez vous attaquer: '))
        j = 0
        for k in range(len(self.joueurs)):
            if nameJ.lower() == self.joueurs[k].nom.lower():
                j = k

        # Vérifier si un coup fourré a été joué
        coupfourre = self.coupFourre(indexJ, j, indexC)
        if coupfourre == 1:
            return j
        else:
            for botte in self.joueurs[j].bottes:
                if self.joueurs[indexJ].main[indexC].cartetype == 'Feu rouge' and botte.cartetype == 'Prioritaire':
                    print(f"Vous ne pouvez pas jouer une carte de type : {self.joueurs[indexJ].main[indexC].cartetype} "f"car votre adversaire detient la carte : {botte.cartetype}")
                    self.jouerCarte(self.joueurs[indexJ].nom)
                    return -1
                if self.joueurs[indexJ].main[indexC].cartetype == 'Limitation de vitesse' and botte.cartetype == 'Prioritaire':
                    print(f"Vous ne pouvez pas jouer une carte de type : {self.joueurs[indexJ].main[indexC].cartetype} "f"car votre adversaire detient la carte : {botte.cartetype}")
                    self.jouerCarte(self.joueurs[indexJ].nom)
                    return -1

                elif self.joueurs[indexJ].main[indexC].cartetype == 'Accident de la route' and botte.cartetype == 'As du volant':
                    print(f"Vous ne pouvez pas jouer une carte de type : {self.joueurs[indexJ].main[indexC].cartetype} "f"car votre adversaire detient la carte : {botte.cartetype}")
                    self.jouerCarte(self.joueurs[indexJ].nom)
                    return -1

                elif self.joueurs[indexJ].main[indexC].cartetype == "Panne d'essence" and botte.cartetype == 'Camion citerne':
                    print(f"Vous ne pouvez pas jouer une carte de type : {self.joueurs[indexJ].main[indexC].cartetype} "f"car votre adversaire detient la carte : {botte.cartetype}")
                    self.jouerCarte(self.joueurs[indexJ].nom)
                    return -1

                elif self.joueurs[indexJ].main[indexC].cartetype == 'Crevaison' and botte.cartetype == 'Increvable':
                    print(f"Vous ne pouvez pas jouer une carte de type : {self.joueurs[indexJ].main[indexC].cartetype} "f"car votre adversaire detient la carte : {botte.cartetype}")
                    self.jouerCarte(self.joueurs[indexJ].nom)
                    return -1

            if self.joueurs[indexJ].main[indexC].cartetype != 'Limitation de vitesse' and \
                    self.joueurs[j].pileBataille[-1].getFamille() == 'Defense':
                print(f"Vous venez de jouer la carte : {self.joueurs[indexJ].main[indexC]}")
                self.joueurs[j].pileBataille.append(self.joueurs[indexJ].main[indexC])
                print(f"Vous venez de jouer la carte {self.joueurs[indexJ].main[indexC].cartetype}")
                self.joueurs[indexJ].poserCarte(indexC)

            elif self.joueurs[indexJ].main[indexC].cartetype == 'Limitation de vitesse':
                if len(self.joueurs[j].pileVitesse) == 0:
                    print(f"Vous venez de jouer la carte : {self.joueurs[indexJ].main[indexC]}")
                    self.joueurs[j].pileVitesse.append(self.joueurs[indexJ].main[indexC])
                    print(f"Vous venez de jouer la carte {self.joueurs[indexJ].main[indexC].cartetype}")
                    self.joueurs[indexJ].poserCarte(indexC)

                elif self.joueurs[j].pileVitesse[-1].cartetype == "Fin de limitation de vitesse":
                    print(f"Vous venez de jouer la carte : {self.joueurs[indexJ].main[indexC]}")
                    self.joueurs[j].pileVitesse.append(self.joueurs[indexJ].main[indexC])
                    print(f"Vous venez de jouer la carte {self.joueurs[indexJ].main[indexC].cartetype}")
                    self.joueurs[indexJ].poserCarte(indexC)
            else:
                print(f"Vous ne pouvez pas jouer la carte {self.joueurs[indexJ].main[indexC]}")
                self.jouerCarte(self.joueurs[indexJ].nom)

            return -1

    # Gérer les effets d'une carte defense
    def parade(self, i, index):
        if self.joueurs[i].main[index].cartetype == 'Feu vert' and self.joueurs[i].pileBataille[-1].cartetype == 'Feu rouge':
            self.joueurs[i].pileBataille.append(self.joueurs[i].main[index])
            print(f"Vous venez de jouer la carte : {self.joueurs[i].main[index]}")
            self.joueurs[i].poserCarte(index)

        elif self.joueurs[i].main[index].cartetype == "Reparation" and self.joueurs[i].pileBataille[-1].cartetype == 'Accident de la route':
            self.joueurs[i].pileBataille.append(self.joueurs[i].main[index])
            print(f"Vous venez de jouer la carte : {self.joueurs[i].main[index]}")
            self.joueurs[i].poserCarte(index)

        elif self.joueurs[i].main[index].cartetype == "Essence" and self.joueurs[i].pileBataille[-1].cartetype == "Panne d'essence":
            self.joueurs[i].pileBataille.append(self.joueurs[i].main[index])
            print(f"Vous venez de jouer la carte : {self.joueurs[i].main[index]}")
            self.joueurs[i].poserCarte(index)

        elif self.joueurs[i].main[index].cartetype == "Roue de secours" and self.joueurs[i].pileBataille[-1].cartetype == 'Crevaison':
            self.joueurs[i].pileBataille.append(self.joueurs[i].main[index])
            print(f"Vous venez de jouer la carte : {self.joueurs[i].main[index]}")
            self.joueurs[i].poserCarte(index)

        elif self.joueurs[i].main[index].cartetype == "Fin de limitation de vitesse":
            if len(self.joueurs[i].pileVitesse) == 0:
                print(f"Vous ne pouvez pas jouer la carte {self.joueurs[i].main[index]}")
                self.jouerCarte(self.joueurs[i].nom)

            elif self.joueurs[i].pileVitesse[-1].cartetype == 'Limitation de vitesse':
                self.joueurs[i].pileVitesse.append(self.joueurs[i].main[index])
                print(f"Vous venez de jouer la carte : {self.joueurs[i].main[index]}")
                self.joueurs[i].poserCarte(index)
        else:
           print(f"Vous ne pouvez pas jouer la carte {self.joueurs[i].main[index]}")
           self.jouerCarte(self.joueurs[i].nom)

    # Gérer les effets d'une carte botte
    def jouerBotte(self, i, index):
        if self.joueurs[i].distanceParcourue + 100 <= 1000:
            self.joueurs[i].distanceParcourue += 100
            self.joueurs[i].bottes.append(self.joueurs[i].main[index])
            print(f"Vous venez de jouer la carte {self.joueurs[i].main[index].cartetype} : distance +100 kms")

            # Annuler l'effet de la carte attaque si presente en haut de la pile de bataille pour que le joueur
            # puisse poser une carte distance
            if self.joueurs[i].main[index].cartetype == "Prioritaire":
                print( "boucle prioritaire")
                # en jouant une botte prioritaire on met fin au feu rouge et à la limitation de vitesse
                if self.joueurs[i].pileBataille[-1].cartetype == "Feu rouge":
                    print("feu vert")
                    self.joueurs[i].pileBataille.append(Defense("Feu vert"))
                if len(self.joueurs[i].pileVitesse) != 0:
                    if self.joueurs[i].pileVitesse[-1].cartetype == "Limitation de vitesse":
                        self.joueurs[i].pileVitesse.append(Defense("Fin de limitation de vitesse"))

            # annuler l'effet de la carte panne d'essence
            elif self.joueurs[i].main[index].cartetype == "Camion citerne" and\
                    self.joueurs[i].pileBataille[-1].cartetype == "Panne d'essence":
                self.joueurs[i].pileBataille.append(Defense("Essence"))

            # annuler l'effet de la carte crevaison
            elif self.joueurs[i].main[index].cartetype == "Increvable" and\
                    self.joueurs[i].pileBataille[-1].cartetype == "Crevaison":
                self.joueurs[i].pileBataille.append(Defense("Roue de secours"))

            # Annuler l'effet de la carte accident de voiture
            elif self.joueurs[i].main[index].cartetype == "As du volant" and\
                    self.joueurs[i].pileBataille[-1].cartetype == "Accident de la route":
                self.joueurs[i].pileBataille.append(Defense("Reparation"))

            # Selon la carte botte jouées  les effets des cartes obstacles correspondante seront annulés
            self.joueurs[i].poserCarte(index)
            self.joueurs[i].piocherCarte(self.paquetCarte)
            # En posant une carte  bottes le joueur peux rejouer un second tour immediatement
            self.jouerCarte(self.joueurs[i].nom)
        else:
            print(f"Vous ne pouvez pas jouer la carte {self.joueurs[i].main[index]}, car vous allez dépasser les 1000 bornes")
            self.jouerCarte(self.joueurs[i].nom)

    # Gérer les effets d'une carte distance
    def etape(self, indexJ, indexC):
        if self.joueurs[indexJ].pileBataille[-1].getFamille() == "Attaque":
            # Cas d'un obstacle sur la pile de bataille
            print(f"Vous ne pouvez pas jouer une carte de type distance, il faudra d'abord se défaire des obstacles suivants: {self.joueurs[indexJ].pileBataille[-1].cartetype} ")
            self.jouerCarte(self.joueurs[indexJ].nom)
        elif len(self.joueurs[indexJ].pileVitesse) == 0:
            if self.joueurs[indexJ].distanceParcourue + self.joueurs[indexJ].main[indexC].distance <= 1000:
                self.joueurs[indexJ].distanceParcourue += self.joueurs[indexJ].main[indexC].distance
                print(f"Vous venez de jouer la carte {self.joueurs[indexJ].main[indexC].cartetype}")
                self.joueurs[indexJ].poserCarte(indexC)
            else:
                print("Vous ne pouvez pas dépasser les 1000 bornes")
                self.jouerCarte(self.joueurs[indexJ].nom)
        else:
            # Cas de la limitation de vitesse
            if self.joueurs[indexJ].pileVitesse[-1].cartetype == "Limitation de vitesse":
                if self.joueurs[indexJ].main[indexC].distance <= 50:
                    if self.joueurs[indexJ].distanceParcourue + self.joueurs[indexJ].main[indexC].distance <= 1000:
                        self.joueurs[indexJ].distanceParcourue += self.joueurs[indexJ].main[indexC].distance
                        print(f"Vous venez de jouer la carte {self.joueurs[indexJ].main[indexC].cartetype}")
                        self.joueurs[indexJ].poserCarte(indexC)
                    else:
                        print("Vous ne pouvez pas dépasser les 1000 bornes")
                        self.jouerCarte(self.joueurs[indexJ].nom)
                else:
                    print('Vous etes limité à une vitesse de 50 Kms')
                    self.jouerCarte(self.joueurs[indexJ].nom)
            else:
                # cas de fin de limitation de vitesse
                if self.joueurs[indexJ].distanceParcourue + self.joueurs[indexJ].main[indexC].distance <= 1000:
                    self.joueurs[indexJ].distanceParcourue += self.joueurs[indexJ].main[indexC].distance
                    print(f"Vous venez de jouer la carte {self.joueurs[indexJ].main[indexC].cartetype}")
                    self.joueurs[indexJ].poserCarte(indexC)
                else:
                    print("Vous ne pouvez pas dépasser les 1000 bornes")
                    self.jouerCarte(self.joueurs[indexJ].nom)

    # Gestion des carte lors de la partie
    def jouerCarte(self, nomJoueur):
        for i in range(self.nb_joueurs):
            if nomJoueur == self.joueurs[i].nom:
                break
            else:
                if i == self.nb_joueurs - 1:
                    print(f"Erreur: {nomJoueur} n'est pas dans la liste des participants.")
                    return -1
        print(self.joueurs[i])
        print(self.afficherTable(i))
        index = input('Quelle carte souhaiter vous jouer: ')
        while not(index in ["0", "1", "2", "3", "4", "5", "6", "7"]):
            # Saisir un index valide
            index = input('Choix invalide: Choisir un nombre entre 0 et 7: Choix? :  ')

        index = int(index)
        while(1):
            # Defausser une carte
            if index == 7:
                num = input("Quelle carte voulez vous défausser: ")
                while not (num in ["0", "1", "2", "3", "4", "5", "6"]):
                    num = input("Quelle carte voulez vous défausser: Choisir un nombre en 0 et 6: choix?: ")
                num = int(num)
                print(f"Vous venez de defausser la carte: {self.joueurs[i].main[num]}")
                self.joueurs[i].poserCarte(num)
                return -1

            # Ajouter une distance à son compteur
            if self.joueurs[i].main[index].getFamille() == 'Distance':
                self.etape(i, index)
                return -1

            # Se défendre contre un obstacle
            if self.joueurs[i].main[index].getFamille() == 'Defense':
                self.parade(i, index)
                return -1

            # Attaquer un adversaire
            if self.joueurs[i].main[index].getFamille() == 'Attaque':
                ind = self.attaquer(i, index)   # indJ sert a récuperer l'indice du joueur qui a éffectué un coup fourré
                return ind

            # Joueur une carte Botte:
            if self.joueurs[i].main[index].getFamille() == 'Bottes':
                self.jouerBotte(i, index)
                return -1

    # fonction qui verifie si le joueur a atteint les 1000 bornes
    def ifWin(self):
        # La partie se termine si l'un des joueurs atteint les 1000 bornes, soit si la piche est vide !
        for i in range(len(self.joueurs)):
            if self.joueurs[i].distanceParcourue == 1000:
                print("-------------------- Bravo !! ------------------------")
                print(f"Le joueur {self.joueurs[i].nom} a gagné la Partie !!!")

                return 0
        if len(self.paquetCarte) == 0:
            print("-------------------- Fin de la partie !! ------------------------")
            print(" Plus de carte de la piche !")
            return 0

        return 1


