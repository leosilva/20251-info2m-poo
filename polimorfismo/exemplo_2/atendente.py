from funcionario import Funcionario

class Atendente(Funcionario):
    def calcular_comissao(self, valorVenda):
        return valorVenda * 0.1