def calculo():
    try:
        numero = int(input("Digite um número: "))
        resultado = 10 / numero
        print(f"Resultado: {resultado}")
    except ValueError:
        print("Erro: entrada inválida.")
        calculo()
    except ZeroDivisionError:
        print("Erro: divisão por zero.")
        calculo()

calculo()