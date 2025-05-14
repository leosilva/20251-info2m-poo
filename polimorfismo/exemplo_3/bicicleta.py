from transporte import Transporte

class Bicicleta(Transporte):

    def calcular_tempo(self):
        return self.distancia / 15