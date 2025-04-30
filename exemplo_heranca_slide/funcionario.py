from pessoa import Pessoa

class Funcionario(Pessoa):
    def __init__(self, nome, cpf, codigo, salario):
        super().__init__(nome, cpf)
        self.codigo = codigo
        self.salario = salario

    def aumentar_salario(self, aumento):
        self.salario = self.salario + aumento