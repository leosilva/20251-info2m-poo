from gerente import Gerente
from atendente import Atendente
from vendedor import Vendedor

valorVenda = 500

gerente = Gerente()
print(gerente.calcular_comissao(valorVenda))

atendente = Atendente()
print(atendente.calcular_comissao(valorVenda))

vendedor = Vendedor()
print(vendedor.calcular_comissao(valorVenda))