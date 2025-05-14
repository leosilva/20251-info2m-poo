from animal import Animal

class Gato(Animal):
    def emitir_som(self):
        som_original = super().emitir_som()
        print(som_original)
        return "Gato miando"