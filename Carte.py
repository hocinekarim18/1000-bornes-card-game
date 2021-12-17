from abc import ABC
from abc import abstractmethod


class Carte (ABC):
    def __init__(self, carteType):
        self.cartetype = carteType

    @abstractmethod
    def getFamille(self):
        pass

    @abstractmethod
    def cartetype(self):
        pass

    @abstractmethod
    def __str__(self):
        pass





