class Professor:
    def __init__(self, codigoProf,
                 nomeProf,
                 emailProf):
        self.codigo = codigoProf
        self.nome = nomeProf
        self.email = emailProf
        self.disciplinas = []

    def adicionarDisciplina(self, disc):
        self.disciplinas.append(disc)