from transporte import Transporte

class Aviao(Transporte):

    def calcular_tempo(self):
        return self.distancia / 800