class Cavalo:

    def __init__(self, nomeCavalo, 
                 racaCavalo, corCavalo, idadeCavalo, pesoCavalo):
        self.nome = nomeCavalo
        self.raca = racaCavalo
        self.idade = idadeCavalo
        self.cor = corCavalo
        self.peso = pesoCavalo

    def andar(self):
        print("{} esta andando".format(self.nome))

    def correr(self):
        print("{} esta correndo".format(self.nome))

    def deitar(self):
        print("{} esta deitado".format(self.nome))