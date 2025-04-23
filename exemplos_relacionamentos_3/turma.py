class Turma:
    def __init__(self, codigoTurma, dataTurma):
        self.codigo = codigoTurma
        self.data = dataTurma
        self.alunos = []
        self.disciplinas = []

    def adicionarAluno(self, aluno):
        self.alunos.append(aluno)

    def adicionarDisciplina(self, disciplina):
        self.disciplinas.append(disciplina)