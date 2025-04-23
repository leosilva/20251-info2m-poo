class Disciplina:
    def __init__(self, codigoDisciplina, nomeDisciplina, cursoDisciplina, professorDisciplina = None):
        self.codigo = codigoDisciplina
        self.nome = nomeDisciplina
        self.curso = cursoDisciplina
        self.professor = professorDisciplina