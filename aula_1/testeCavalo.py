from cavalo import Cavalo


c1 = Cavalo("Pe de pano", "Pangare", "Marrom", 7, 247)
c2 = Cavalo("Francisco", "Pangare", "Branco", 14, 210)
c1.andar()
c2.andar()
c2.correr()

print(c1.idade)
c1.idade = c1.idade + 1
