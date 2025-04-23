class Curso:
    def __init__(self, codigoCurso, nomeCurso):
        self.codigo = codigoCurso
        self.nome = nomeCurso
        self.disciplinas = []

    def adicionarDisciplina(self, disc):
        self.disciplinas.append(disc)