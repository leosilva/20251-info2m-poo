class Autor:

    def __init__(self, nomeAutor):
        self.nome = nomeAutor
        self.livros = []

    def adicionarLivro(self, livro):
        self.livros.append(livro)