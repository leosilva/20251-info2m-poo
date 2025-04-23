from aluno import Aluno
from turma import Turma
from disciplina import Disciplina
from professor import Professor
from curso import Curso
import datetime as dt


c1 = Curso(987, "Curso Tecnico em Informatica")

a1 = Aluno("Aluno1", "Rua das Flores", "aluno1@gmail.com")
a2 = Aluno("Aluno2", "Rua das Arvores", "aluno2@gmail.com")
a3 = Aluno("Aluno3", "Rua das Plantas", "aluno3@gmail.com")

p1 = Professor(123, "Leo Silva", "leo@gmail.com")

d1 = Disciplina(123, "POO", c1, p1)
d2 = Disciplina(456, "Matematica", c1)

t1 = Turma(123, dt.datetime.now())

t1.adicionarDisciplina(d1)
t1.adicionarDisciplina(d2)

t1.adicionarAluno(a1)
t1.adicionarAluno(a2)
t1.adicionarAluno(a3)

a1.adicionarTurma(t1)
a2.adicionarTurma(t1)
a3.adicionarTurma(t1)

for disc in t1.disciplinas:
    print(disc.codigo)
    print(disc.nome)
    print(disc.professor)
    print(disc.curso.nome)
    print("-----")

for a in t1.alunos:
    print(a.nome)
    print(a.email)
    print("-----")