"""
O arquivo a ser manipulado deve estar no formato em que cada linha contém os dados do usuário separados por ponto e vírgula (';').

Exemplo:

joao;joao@gmail.com;123456
caio;caio@gmail.com;654321
maria;maria@hotmail.com;987654
julia;julia@gmail.com;123987
"""

# indica o caminho do arquivo a ser manipulado
caminho_arquivo = "usuario.txt"


def ler_arquivo(nome, mode):
    """
    Abre um arquivo com o nome e modo especificados.
    """
    f = open(nome, mode)
    return f


def adicionar_usuario(nome, email, senha):
    """
    Adiciona um novo usuário ao arquivo. Retorna True se o usuário foi adicionado com sucesso, False caso ocorra algum erro.
    """
    try:
        # lê o arquivo em modo de escrita
        arquivo = ler_arquivo(caminho_arquivo, "a+")
        # cria a linha a ser inserida a partir dos parâmetros recebidos no método
        linha = f"{nome};{email};{senha}"
        # escreve a linha no arquivo, adicionando uma quebra de linha ao final do arquivo
        arquivo.write(linha + "\n")
        # fecha o arquivo
        arquivo.close()
        return True
    except:
        # deveria adicionar um arquivo de log para armazenar o erro
        return False
    
    
def buscar_usuario_por_nome(nome):
    """
    Busca um usuário pelo nome no arquivo manipulado. Retorna a linha correspondente ao usuário, caso encontrado. Retorna None se o usuário não for encontrado ou ocorrer um erro.
    """
    try:
        # lê o arquivo em modo de leitura
        arquivo = ler_arquivo(caminho_arquivo, "r")
        # lê todas as linhas do arquivo e itera sobre elas
        for linha in arquivo.readlines():
            """ Executa a função split na linha. Como cada linha é possui um separador (';') entre os dados, o método split criará uma lista de elementos a partir desse separador. Por exemplo:
            
            Linha do arquivo: leo;leo@gmail.com;123
            Após o split: ['leo', 'leo@gmail.com', '123']
            """
            linhaSlitted = linha.split(';')
            
            # caso o nome encontrado na linha seja igual ao nome que se quer buscar, retorna a linha encontrada
            if linhaSlitted[0] == nome:
                arquivo.close()
                return linha
        arquivo.close()
    except:
        # deveria adicionar um arquivo de log para armazenar o erro
        return None


def atualizar_usuario(nome, email, senha):
    """
    Atualiza as informações de um usuário no arquivo. Necessariamente, o nome no parâmetro deve ser igual ao nome do usuário que se quer atualizar. Retorna True se o usuário foi atualizado com sucesso, False caso contrário.
    """
    try:
        atualizou_usuario = False
        # lê o arquivo em modo de leitura e escrita
        arquivo = ler_arquivo(caminho_arquivo, "r+")
        # lê as linhas do arquivo
        linhas = arquivo.readlines()
        
        # itera sobre as linhas do arquivo
        for linha in linhas:
            # recupera o índice da linha atual na lista de linhas
            idx = linhas.index(linha)
            # realiza o split, conforme explicado na função anterior
            linha_splitted = linha.split(";")
            # caso o nome encontrado na linha seja igual ao nome que se quer atualizar, cria uma nova linha
            if linha_splitted[0] == nome:
                nova_linha = f"{nome};{email};{senha}\n"
                # atualiza a lista de linhas com a nova linha, no mesmo índice da linha anterior
                linhas[idx] = nova_linha
                
                # posiciona o cursor no início do arquivo.
                arquivo.seek(0)
                
                # a partir do início do arquivo, escreve todas as linhas novamente, sobrescrevendo as linhas antigas. Isso fará com que a nova linha seja escrita no arquivo.
                arquivo.writelines(linhas)
                arquivo.close()
                
                # indica que conseguiu atualizar o usuário
                atualizou_usuario = True
                
        return atualizou_usuario
    except:
        # deveria adicionar um arquivo de log para armazenar o erro
        return atualizou_usuario
    
    
def remover_usuario(nome):
    """
    Remove um usuário do arquivo com base no nome fornecido. Retorna True se o usuário foi removido com sucesso, False caso contrário.
    """
    try:
        # cria uma variavel responsável por armazenar as novas linhas. A remoção é, na prática, uma sobrescrita no arquivo com uma linha a menos (a que se quer remover)
        novas_linhas = []
        
        # lê o arquivo em modo leitura e escrita
        arquivo = ler_arquivo(caminho_arquivo, "r+")
        
        # lê as linhas do arquivo.
        linhas = arquivo.readlines()
        
        # itera sobre as linhas
        for linha in linhas:
            # realiza o split, conforme explicado em métodos acima
            linha_splitted = linha.split(";")
            
            # caso o nome do usuário da linha atual seja diferente do nome que se quer remover, adiciona a linha atual nas novas linhas. Dessa forma, apenas não será adicionada nas novas linhas a linha que se quer remover.
            if linha_splitted[0] != nome:
                novas_linhas.append(linha)
                
        # se o tamanho da lista de linhas do arquivo for igual ao tamanho da nova lista de linhas, significa que não conseguiu remover nenhum usuário (por não encontra-lo).
        if len(linhas) == len(novas_linhas):
            return False
        else:
            # Se o if acima for falso, então conseguiu-se remover um usuário
            # posiciona o cursor no início do arquivo
            arquivo.seek(0)
            
            # o método truncate() apaga o arquivo a partir da posição do cursor. Como o cursor está na posição zero, todo o arquivo será apagado.
            arquivo.truncate()
            
            # escreve todas as novas linhas.
            arquivo.writelines(novas_linhas)
            return True
    except:
        # deveria adicionar um arquivo de log para armazenar o erro
        return False