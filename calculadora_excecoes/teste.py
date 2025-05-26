from calculadora import Calculadora
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(filename='calculadora_excecoes/erros.log', level=logging.ERROR)


def main():
    resultado = None
    try:
        num1 = int(input("Digite o primeiro numero: "))
        num2 = int(input("Digite o segundo numero: "))

        operacao = input("Informe a operação desejada (+, -, *, /): ")

        calculadora = Calculadora()
        resultado = calculadora.realizar_operacao(operacao, num1, num2)
    except ValueError as ve:
        print("Erro: entrada inválida.")
        logger.error("Erro de entrada inválida: {}".format(ve))
        main()
    except ZeroDivisionError as zde:
        print("Erro: divisão por zero.")
        logger.error("Erro de divisão por zero: ".format(zde))
        main()
    else:
        print("Resultado: ", resultado)

main()