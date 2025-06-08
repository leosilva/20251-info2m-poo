"""
Arquivo exemplo:

joao;joao@gmail.com;123456
caio;caio@gmail.com;654321
maria;maria@gmail.com;987654
julia;julia@gmail.com;123987
"""


def ler_arquivo(nome, mode):
    f = open(nome, mode)
    return f


def adicionar_usuario(nome, email, senha):
    try:
        arquivo = ler_arquivo("exemplo_tkinter_manipulacao_arquivos/usuario.txt", "a+")
        linha = f"{nome};{email};{senha}"
        arquivo.write(linha + "\n")
        arquivo.close()
        return True
    except:
        # deveria adicionar um arquivo de log para armazenar o erro
        return False
    
    
def buscar_usuario_por_nome(nome):
    try:
        arquivo = ler_arquivo("exemplo_tkinter_manipulacao_arquivos/usuario.txt", "r")
        for linha in arquivo.readlines():
            linhaSlitted = linha.split(';')
            if linhaSlitted[0] == nome:
                return linha
    except:
        # deveria adicionar um arquivo de log para armazenar o erro
        return None


def atualizar_usuario(nome, email, senha):
    try:
        atualizou_usuario = False
        arquivo = ler_arquivo("exemplo_tkinter_manipulacao_arquivos/usuario.txt", "r+")
        linhas = arquivo.readlines()
        
        for linha in linhas:
            idx = linhas.index(linha)
            linha_splitted = linha.split(";")
            if linha_splitted[0] == nome:
                nova_linha = f"{nome};{email};{senha}\n"
                linhas[idx] = nova_linha
                arquivo.seek(0)
                arquivo.writelines(linhas)
                atualizou_usuario = True
                
        return atualizou_usuario
    except:
        # deveria adicionar um arquivo de log para armazenar o erro
        return atualizou_usuario
    
    
def remover_usuario(nome):
    try:
        novas_linhas = []
        arquivo = ler_arquivo("exemplo_tkinter_manipulacao_arquivos/usuario.txt", "r+")
        linhas = arquivo.readlines()
        
        for linha in linhas:
            linha_splitted = linha.split(";")
            if linha_splitted[0] != nome:
                novas_linhas.append(linha)
                
        if len(linhas) == len(novas_linhas):
            return False
        else:        
            arquivo.seek(0)
            arquivo.truncate()
            arquivo.writelines(novas_linhas)
            return True
    except:
        # deveria adicionar um arquivo de log para armazenar o erro
        return False