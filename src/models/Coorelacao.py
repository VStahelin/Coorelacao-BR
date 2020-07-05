from abc import ABC
from src.models.LinhaDeRelacao import LinhaDeRelacao


class Coorelacao(ABC):

    def __init__(self):
        self.__cabecario = []
        self.__item1 = LinhaDeRelacao()
        self.__item2 = LinhaDeRelacao()

    def setaItem1(self, linha):
        self.__item1 = linha

    def setaItem2(self, linha):
        self.__item2 = linha

    def appendNoCabecario(self, item):
        self.__cabecario.append(item)

    def __str__(self):
        return "Cabecario: {}, item1: {}, item2: {}".format(self.__cabecario, str(self.__item1), str(self.__item2))
