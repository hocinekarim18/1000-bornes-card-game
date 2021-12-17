from Attaque import Attaque


class Joueur:
    def __init__(self, nom):
        self.nom = nom                               # Nom du joueur
        self.main = []                               # Main du joueur
        self.pileBataille = [Attaque("Feu rouge")]
        self.pileVitesse = []
        self.bottes = []                             # Bottes que le joueur a joué
        self.distanceParcourue = 0                   # Distance

    # Prendre une carte à la fin du paquet de carte
    def piocherCarte(self, paquetCarte):
        if len(paquetCarte) != 0:
            self.main.append(paquetCarte[-1])
            paquetCarte.pop(-1)
            self.arrangerMain()
        else:
            print("Pas de cartes dans le paquet, vous ne pouvez plus piocher !!!")

    # fonction qui permet d'arranger la main du joueur selon: Dsitance, attaque, defense et bottes
    def arrangerMain(self):
        main = []
        for carte in self.main:
            if carte.getFamille() == 'Distance':
                main.append(carte)
        for carte in self.main:
            if carte.getFamille() == 'Attaque':
                main.append(carte)
        for carte in self.main:
            if carte.getFamille() == 'Defense':
                main.append(carte)
        for carte in self.main:
            if carte.getFamille() == 'Bottes':
                main.append(carte)
        self.main = main

    # Afficher les information relatives aux joueurs
    def __str__(self):
        message = "------------------------------------------------------\n"
        message += f"C'est au joueur {self.nom} ({self.distanceParcourue} Kms) de joueur : \n"

        # Afficher la main du joueur
        for i,carte in enumerate(self.main):
             message += f'{i}: ' + carte.__str__()
        message += f"7: Defausser une carte.\n"

        # Afficher la pile de Bataille
        message += f"\nPile de bataille : "
        if not len(self.pileBataille) == 0:
            message += f"{self.pileBataille[-1].cartetype}  "
        message += "\n"

        # Afficher la pile de vitesse
        message += f"Pile de vitesse : "
        if not len(self.pileVitesse) == 0:
            message += f"{self.pileVitesse[-1].cartetype}  "
        message += "\n"

        # Afficher les bottes jouées
        message += f"Bottes : "
        for carte in self.bottes:
            message += f"{carte.cartetype}  "
        message += "\n------------------------------------------------------\n"

        return message

    # Retire une carte de la main du joueur
    def poserCarte(self, index):
        self.main.pop(index)
