class Livro:
    
    def __init__(self, tituloLivro, isbnLivro, editoraLivro):
        self.titulo = tituloLivro
        self.isbn = isbnLivro
        self.editora = editoraLivro
        self.autores = []

    def adicionarAutor(self, autor):
        self.autores.append(autor)