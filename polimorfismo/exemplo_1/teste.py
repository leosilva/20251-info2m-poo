from animal import Animal
from cachorro import Cachorro
from gato import Gato

# comportamento polimorfico
animais = [Cachorro(), Gato(), Animal()]
for animal in animais:
    print(animal.emitir_som())  # Chama o metodo sobrescrito baseado no tipo do objeto