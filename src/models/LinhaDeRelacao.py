from abc import ABC


class LinhaDeRelacao(ABC):

    def __init__(self):
        self.titulo = ""
        self.valores = []

    def adicionaValor(self, valor):
        self.valores.append(valor)

    def setarTitulo(self, name):
        self.titulo = name

    def __str__(self):
        return "Titulo: {}. Valores: {}".format(self.titulo, self.valores)
