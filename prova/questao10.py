class Usuario:
    def __init__(self, nome, idade, contato):
        self.nome= nome
        self.idade= idade
        self.contato = contato

class Contato:
    def __init__(self, telefone, email):
        self.telefone = telefone
        self.email = email

contato = Contato("123456789", "leo@gmail.com")
usuario = Usuario("Leo", 20, contato)

print(usuario.nome, usuario.contato.telefone, usuario.contato.email)




