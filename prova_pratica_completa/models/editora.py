class Editora:
    def __init__(self, nome, pais, id=None):
        self.nome = nome
        self.pais = pais
        self.id = id
        
        
    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'pais': self.pais
        }