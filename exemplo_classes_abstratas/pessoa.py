from abc import ABC

class Pessoa(ABC):
    def __init__(self, nome):
        self.nome = nome

    def imprimir_nome(self):
        print(self.nome)