import logging

logger = logging.getLogger(__name__)
logging.basicConfig(filename='erros.log', level=logging.ERROR)

def calculo():
    try:
        numero = int(input("Digite um número: "))
        if numero == 5:
            raise ValueError("Numero igual a 5")
        resultado = 10 / numero
        print(f"Resultado: {resultado}")
    except ValueError as ve:
        print("Erro: entrada inválida.")
        logger.error("Erro de valor: %s", ve)
        calculo()
    except ZeroDivisionError as zde:
        print("Erro: divisão por zero.")
        logger.error("Erro de divisão por zero: %s", zde)
        calculo()
    else:
        print("Codigo executado com sucesso!")

calculo()