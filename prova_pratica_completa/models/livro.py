class Livro:
    def __init__(self, titulo, autor, isbn, editora_id, id=None):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.editora_id = editora_id
        self.id = id
                
        
    def to_dict(self):
        return {
            'id': self.id,
            'titulo': self.titulo,
            'autor': self.autor,
            'isbn': self.isbn,
            'editora_id': self.editora_id
        }