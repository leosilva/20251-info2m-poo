class Aluno:
    def __init__(self, nomeAluno,
                 enderecoAluno,
                 emailAluno):
        self.nome = nomeAluno
        self.endereco = enderecoAluno
        self.email = emailAluno
        self.turmas = []

    def adicionarTurma(self, turma):
        self.turmas.append(turma)