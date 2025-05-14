from transporte import Transporte

class Carro(Transporte):

    def calcular_tempo(self):
        return self.distancia / 60