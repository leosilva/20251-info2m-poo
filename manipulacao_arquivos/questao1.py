def escrever_arquivo():
    texto = input("digite alguma coisa: ")
    arquivo = open("manipulacao_arquivos/questao_1.txt", "w")
    arquivo.write(texto)
    arquivo.close()

def ler_arquivo():
    arquivo = open("manipulacao_arquivos/questao_1.txt", "r")
    texto = arquivo.read()
    print(texto)
    arquivo.close()

escrever_arquivo()
ler_arquivo()