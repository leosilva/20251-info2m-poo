def criar_arquivo():
    arquivo = open("manipulacao_arquivos/questao4.txt", "w")
    for i in range(0,5):
        nome = input("digite o nome: ")
        cpf = input("digite o cpf: ")
        arquivo.write(cpf + ";" + nome + "\n")
    
    arquivo.close()
    
def ler_arquivo():
    arquivo = open("manipulacao_arquivos/questao4.txt", "r")
    linhas = arquivo.readlines()
    for linha in linhas:
        linha = linha.replace("\n", "")
        print(linha)

criar_arquivo()
ler_arquivo()