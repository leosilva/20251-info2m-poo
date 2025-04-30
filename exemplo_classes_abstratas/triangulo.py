from forma import Forma

class Triangulo(Forma):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        area = (self.base * self.altura) / 2
        return area
    
    def perimetro(self):
        perimetro = (self.altura * 2) + self.base
        return perimetro