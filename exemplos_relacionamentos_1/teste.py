import classeEditora as e
import livro as l
import autor as a


ed1 = e.Editora("Editora Rocco")
print(ed1.nome)
ed2 = e.Editora("Editora XPTO")

l1 = l.Livro("Harry Potter e a Pedra Filosofal", "12345", ed2)
print(l1.titulo)
print(l1.editora.nome)

l2 = l.Livro("Harry Potter X", "12345qweqw", ed2)

# criando autores
a1 = a.Autor("Leo Silva")
a2 = a.Autor("Bianca Ester")

# adiciona os autores ao livro
l1.adicionarAutor(a1)
l1.adicionarAutor(a2)
l2.adicionarAutor(a2)

# adiciona o livro aos autores
a1.adicionarLivro(l1)
a2.adicionarLivro(l1)
a2.adicionarLivro(l2)

# print(l1.autores)
# print(a1.livros)

print("Autores do livro {}".format(l1.titulo))
for autor in l1.autores:
    print(autor.nome)

print("Autores do livro {}".format(l2.titulo))
for autor in l2.autores:
    print(autor.nome)