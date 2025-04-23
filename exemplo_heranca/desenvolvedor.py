from funcionario import Funcionario

class Desenvolvedor(Funcionario):
    def __init__(self, nome, cpf, sal, ling):
        super().__init__(nome, cpf, sal)
        self.linguagem = ling

    def trocarLinguagem(self, novaLing):
        self.linguagem = novaLing