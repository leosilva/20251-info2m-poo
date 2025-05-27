def escrever_arquivo():
    texto = input("digite alguma coisa: ")
    arquivo = open("manipulacao_arquivos/questao_1.txt", "a")
    arquivo.write(texto + "\n")
    arquivo.close()

def ler_arquivo():
    arquivo = open("manipulacao_arquivos/questao_1.txt", "r")
    texto = arquivo.read()
    print(texto)
    arquivo.close()

escrever_arquivo()
ler_arquivo()