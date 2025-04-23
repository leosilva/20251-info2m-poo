from desenvolvedor import Desenvolvedor

d = Desenvolvedor("Leo Silva", "123.456.789-00", 4500, "Python")
print(d.nome, d.cpf, d.salario, d.linguagem)

d.aumentarSalario(500)
print(d.nome, d.cpf, d.salario, d.linguagem)