from Carte import Carte

class Bottes(Carte):
    def __init__(self, cartetype):
        self.cartetype = cartetype
        self.__famille = 'Bottes'

    def getFamille(self):
        return self.__famille

    @property
    def cartetype(self):
        return self.__cartetype

    @cartetype.setter
    def cartetype(self, cartetype):
        if cartetype in ['As du volant', 'Camion citerne', 'Increvable', 'Prioritaire']:
            self.__cartetype = cartetype
        else:
            print("Erreur: Veuillez eentrer un type de carte 'Bottes' present dans la liste suivante:")
            print("'As du volant', 'Camion citerne', 'Increvable', 'Prioritaire'")

    def __str__(self):
        return f'{self.__famille}:  {self.cartetype}\n'

