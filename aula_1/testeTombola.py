from classeTombola import Tombola


itens = [1,2,3,4,5,6,7,8,9,10]
t = Tombola(itens)

for i in itens:
    t.misturar()
    print(t.sortear())