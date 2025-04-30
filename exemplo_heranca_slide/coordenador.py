from funcionario import Funcionario

class Coordenador(Funcionario):
    def __init__(self, nome, cpf, codigo, salario, curso):
        super().__init__(nome, cpf, codigo, salario)
        self.curso = curso

    def aumentar_salario(self, aumento):
        self.salario = (self.salario + self.salario) + aumento