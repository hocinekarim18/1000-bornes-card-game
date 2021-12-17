from Carte import Carte


class Distance(Carte):
    def __init__(self, cartetype):
        self.cartetype = cartetype
        self.__famille = 'Distance'
        if self.cartetype == 'Escargot':
            self.distance = 25
        if self.cartetype == 'Canard':
            self.distance = 50
        if self.cartetype == 'Papillon':
            self.distance = 75
        if self.cartetype == 'Lievre':
            self.distance = 100
        if self.cartetype == 'Hirondelle':
            self.distance = 200

    def getFamille(self):
        return self.__famille

    @property
    def cartetype(self):
        return self.__cartetype

    @cartetype.setter
    def cartetype(self, cartetype):
        if cartetype in ['Escargot', 'Canard', 'Papillon', 'Lievre', 'Hirondelle']:
            self.__cartetype = cartetype
        else:
            print("Erreur: Veuillez eentrer un type de carte 'Distance' present dans la liste suivante:")
            print("'Escargot', 'Canard', 'Papillon', 'Lievre', 'Hirondelle'")

    def __str__(self):
        return f'{self.__famille}:  {self.cartetype}, {self.distance} kms\n'
