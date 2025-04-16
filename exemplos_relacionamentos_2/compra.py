class Compra:
    
    def __init__(self, codigoCompra, dataCompra, clienteCompra):
        self.codigo = codigoCompra
        self.data = dataCompra
        self.cliente = clienteCompra
        self.produtos = []

    def adicinarProduto(self, produto):
        self.produtos.append(produto)