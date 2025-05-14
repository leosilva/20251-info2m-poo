from funcionario import Funcionario

class Gerente(Funcionario):
    def calcular_comissao(self, valorVenda):
        return valorVenda * 0.20 + 10