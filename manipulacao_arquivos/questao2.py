def ler_arquivo():
    arquivo = open("manipulacao_arquivos/questao2.txt", "r")
    linhas_arquivo = arquivo.readlines()
    print(len(linhas_arquivo))

ler_arquivo()