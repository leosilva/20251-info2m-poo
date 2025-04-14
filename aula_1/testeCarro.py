from carro import Carro

c1 = Carro("Honda", "Azul", "1234567")
print(c1.marca, c1.cor, c1.placa, c1.velocidadeAtual, c1.estaLigado)

c1.ligar()
print(c1.marca, c1.cor, c1.placa, c1.velocidadeAtual, c1.estaLigado)

c1.acelerar(40)
print(c1.marca, c1.cor, c1.placa, c1.velocidadeAtual, c1.estaLigado)
c1.acelerar(20)
print(c1.marca, c1.cor, c1.placa, c1.velocidadeAtual, c1.estaLigado)

c1.frear()
print(c1.marca, c1.cor, c1.placa, c1.velocidadeAtual, c1.estaLigado)

c1.desligar()
print(c1.marca, c1.cor, c1.placa, c1.velocidadeAtual, c1.estaLigado)