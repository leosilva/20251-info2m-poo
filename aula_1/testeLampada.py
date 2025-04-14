from lampada import Lampada

l = Lampada(100)
l1 = Lampada(500)
print("Lampada L")
print(l.potencia)       # 100
print(l.estaLigada())   # False

print("Lampada L1")
print(l1.potencia)       # 100
print(l1.estaLigada())   # False

l.ligar()
print("Lampada L")
print(l.potencia)       # 100
print(l.estaLigada())   # True
print("Lampada L1")
print(l1.potencia)       # 100
print(l1.estaLigada())   # False

# l.potencia = 200
# print(l.potencia)       # 200
# print(l.estaLigada())   # True

# l.desligar()
# print(l.potencia)       # 200
# print(l.estaLigada())   # False