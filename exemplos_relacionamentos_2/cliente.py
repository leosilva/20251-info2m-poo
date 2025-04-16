class Cliente:

    def __init__(self, nomeCliente, enderecoCliente, loginCliente, senhaCliente):
        self.nome = nomeCliente
        self.endereco = enderecoCliente
        self.login = loginCliente
        self.senha = senhaCliente
        self.compras = []

    def adicionarCompra(self, compra):
        self.compras.append(compra)