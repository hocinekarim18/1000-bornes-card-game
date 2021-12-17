from Carte import Carte


class Defense(Carte):
    def __init__(self, cartetype):
        self.cartetype = cartetype
        self.__famille = 'Defense'

    def getFamille(self):
        return self.__famille

    @property
    def cartetype(self):
        return self.__cartetype

    @cartetype.setter
    def cartetype(self, cartetype):
        if cartetype in ["Reparation","Essence","Roue de secours","Fin de limitation de vitesse","Feu vert"]:
            self.__cartetype = cartetype
        else:
            print("Erreur: Veuillez eentrer un type de carte 'Defense' present dans la liste suivante:")
            print("'Reparation','Essence','Roue de secours','Fin de limitation de vitesse','Feu vert'")

    def __str__(self):
        return f'{self.__famille}:  {self.cartetype}\n'