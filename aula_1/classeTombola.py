import random

class Tombola:
    """Classe que implementa uma tombola"""

    def __init__(self, itens):
        self.itens = list(itens)

    def misturar(self):
        random.shuffle(self.itens)

    def sortear(self):
        return self.itens.pop()