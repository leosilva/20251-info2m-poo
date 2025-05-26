class Calculadora:

    def realizar_operacao(self, operacao, a, b):
        if operacao == '+':
            return self.somar(a, b)
        elif operacao == '-':
            return self.subtrair(a, b)
        elif operacao == '*':
            return self.multiplicar(a, b)
        elif operacao == '/':
            return self.dividir(a, b)
        else:
            raise ValueError("Operação inválida.")

    def somar(self, a, b):
        return a + b

    def subtrair(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        return a / b