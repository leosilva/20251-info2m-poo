class Carro:

    def __init__(self, marcaCarro, corCarro,
                 placaCarro):
        self.marca = marcaCarro
        self.cor = corCarro
        self.placa = placaCarro
        self.velocidadeAtual = 0
        self.estaLigado = False

    def ligar(self):
        self.estaLigado = True

    def desligar(self):
        self.estaLigado = False

    def acelerar(self, velocidade):
        self.velocidadeAtual = self.velocidadeAtual + velocidade

    def frear(self):
        self.velocidadeAtual = self.velocidadeAtual - 10