def copiar_conteudo():
    arquivo = open("manipulacao_arquivos/questao2.txt", "r")
    arquivo_destino = open("manipulacao_arquivos/questao3.txt", "w")

    linhas_arquivo = arquivo.readlines()
    arquivo_destino.writelines(linhas_arquivo)
    
    arquivo.close()
    arquivo_destino.close()

copiar_conteudo()