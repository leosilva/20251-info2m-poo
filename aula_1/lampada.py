class Lampada:
    """Classe que modela uma lampada do mundo real"""
    
    def __init__(self, potencia):
        self.potencia = potencia
        self.ligada = False

    def ligar(self):
        self.ligada = True

    def desligar(self):
        self.ligada = False

    def estaLigada(self):
        return self.ligada