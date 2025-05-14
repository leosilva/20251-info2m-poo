from funcionario import Funcionario

class Vendedor(Funcionario):
    def calcular_comissao(self, valorVenda):
        return valorVenda * 0.15 + 5