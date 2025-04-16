import produto as p
import compra as com
import cliente as cli
import datetime


c1 = cli.Cliente("Leo Silva", "Rua das Flores", "leosilva", "123")
p1 = p.Produto(123, "Guaraná Antarctica", 3.50)
p2 = p.Produto(234, "Empada de Frango", 4.50)

compra1 = com.Compra("123", datetime.datetime.now(), c1)
compra1.adicinarProduto(p1)
compra1.adicinarProduto(p2)

c1.adicionarCompra(compra1)

print(c1.nome, c1.endereco, c1.login, c1.senha)
print(p1.codigo, p1.descricao, p1.preco)
print(p2.codigo, p2.descricao, p2.preco)
print(compra1.codigo, compra1.cliente.nome, compra1.data, len(compra1.produtos))