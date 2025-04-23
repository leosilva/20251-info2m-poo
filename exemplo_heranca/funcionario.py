class Funcionario:
    def __init__(self, nome, cpf, sal):
        self.nome = nome
        self.cpf = cpf
        self.salario = sal

    def aumentarSalario(self, aumento):
        self.salario = self.salario + aumento