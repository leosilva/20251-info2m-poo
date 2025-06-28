class Autor:
    def __init__(self, nome, cpf, email, livros=None, id=None):
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.livros = livros
        self.id = id
                
        
    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'cpf': self.cpf,
            'email': self.email,
            'livros':self.livros
        }