from bicicleta import Bicicleta
from carro import Carro
from aviao import Aviao

distancia = 200

bike = Bicicleta(distancia)
print(bike.calcular_tempo())

carro = Carro(distancia)
print(carro.calcular_tempo())

aviao = Aviao(distancia)
print(aviao.calcular_tempo())