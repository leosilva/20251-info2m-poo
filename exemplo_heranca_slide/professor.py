from funcionario import Funcionario

class Professor(Funcionario):
    def __init__(self, nome, cpf, codigo, salario, disciplina):
        super().__init__(nome, cpf, codigo, salario)
        self.disciplina = disciplina

    def aumentar_salario(self, aumento):
        self.salario = self.salario * aumento