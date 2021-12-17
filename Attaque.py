from Carte import Carte

class Attaque(Carte):
    def __init__(self, cartetype):
        self.cartetype = cartetype
        self.__famille = 'Attaque'

    def getFamille(self):
        return self.__famille

    @property
    def cartetype(self):
        return self.__cartetype

    @cartetype.setter
    def cartetype(self, cartetype):
        if cartetype in ['Accident de la route', "Panne d'essence", 'Crevaison', 'Limitation de vitesse', 'Feu rouge']:
            self.__cartetype = cartetype
        else:
            print("Erreur: Veuillez eentrer un type de carte 'Attaque' present dans la liste suivante:")
            print("'Accident de la route', 'Panne d'essence', 'Crevaison', 'Limitation de vitesse', 'Feu rouge'")

    def __str__(self):
        return f'{self.__famille}:  {self.cartetype}\n'