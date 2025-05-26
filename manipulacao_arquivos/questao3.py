def copiar_conteudo():
    arquivo = open("manipulacao_arquivos/questao2.txt", "r")
    arquivo_destino = open("manipulacao_arquivos/questao3.txt", "w")

    linhas_arquivo = arquivo.readlines()
    for linha in linhas_arquivo:
        arquivo_destino.write(linha)

    arquivo.close()
    arquivo_destino.close()

copiar_conteudo()