import json
import os
from models.livro import Livro
import utils as ut


# indica o caminho do arquivo a ser manipulado
CAMINHO_ARQUIVO = "data/livro.json"


def carregar_livros():
    lista_livros = []
    try:
        if not os.path.exists(CAMINHO_ARQUIVO):
            return lista_livros
        f = open(CAMINHO_ARQUIVO, "r")
        livros = json.load(f)
        for l in livros:
            obj_livro = Livro(**l)
            lista_livros.append(obj_livro)
        return lista_livros
    except Exception as e:
        print(e)
        
        
def salvar_livros(lista):
    try:
        dados = [livro.to_dict() for livro in lista]
        
        f = open(CAMINHO_ARQUIVO, "w")
        json.dump(dados, f, indent=4)
            
        return True
    except Exception as e:
        print(e)
        return False


def adicionar_livro(livro):
    try:
        # le arquivo em formato de adicao (append)
        livros = carregar_livros()
        
        # gera novo id
        proximo_id = ut.calcular_proximo_id(livros)
        
        # atribui novo id a editora que quer inserir
        livro.id = proximo_id
            
        # adiciona a nova editora na lista
        livros.append(livro)
                
        # salva a nova lista no arquivo
        return salvar_livros(livros)
    except Exception as e:
        print(e)
        return None
    
def buscar_livro_por_id(id):  
    try:  
        livros = carregar_livros()
        for l in livros:
            if l.id == id:
                return l
    except Exception as e:
        print(e)
        return None
    
    
def buscar_livro_por_titulo(titulo):
    try:
        livros = carregar_livros()
        for livro in livros:
            if livro.titulo == titulo:        
                # se achou um livro com o titulo, retorna o a linha completa do livro
                return livro
    except:
        # deveria adicionar um arquivo de log para armazenar o erro
        return None


def atualizar_livro(livro):
    try:
        livros = carregar_livros()
        for idx, l in enumerate(livros):
            if l.id == livro.id:
                livros[idx] = livro
                salvar_livros(livros)
                return True
    except Exception as e:
        print(e)
        return False
    
    
def remover_livro(id):
    try:
        livros = carregar_livros()
        novos_livros = []
        for l in livros:
            if l.id != id:
                novos_livros.append(l)
        return salvar_livros(novos_livros)
    except Exception as e:
        print(e)
        return False