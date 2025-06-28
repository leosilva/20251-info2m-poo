class Livro:
    def __init__(self, titulo, isbn, editora_id, autores=None, id=None):
        self.titulo = titulo
        self.isbn = isbn
        self.editora_id = editora_id
        self.autores = autores
        self.id = id
                
        
    def to_dict(self):
        return {
            'id': self.id,
            'titulo': self.titulo,
            'isbn': self.isbn,
            'editora_id': self.editora_id,
            'autores': self.autores
        }