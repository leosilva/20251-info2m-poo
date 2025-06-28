import json
import os
from models.autor import Autor
import utils as ut


# indica o caminho do arquivo a ser manipulado
CAMINHO_ARQUIVO = "data/autor.json"


def carregar_autores():
    lista_autores = []
    try:
        if not os.path.exists(CAMINHO_ARQUIVO):
            return lista_autores
        f = open(CAMINHO_ARQUIVO, "r")
        autores = json.load(f)
        for a in autores:
            obj_autor = Autor(**a)
            lista_autores.append(obj_autor)
        return lista_autores
    except Exception as e:
        print(e)
        
        
def salvar_autores(lista):
    try:
        dados = [autor.to_dict() for autor in lista]
        
        f = open(CAMINHO_ARQUIVO, "w")
        json.dump(dados, f, indent=4)
            
        return True
    except Exception as e:
        print(e)
        return False


def adicionar_autor(autor):
    try:
        # le arquivo em formato de adicao (append)
        autores = carregar_autores()
        
        # gera novo id
        proximo_id = ut.calcular_proximo_id(autores)
        
        # atribui novo id ao autor que quer inserir
        autor.id = proximo_id
            
        # adiciona o novo autor na lista
        autores.append(autor)
                
        # salva a nova lista no arquivo
        return salvar_autores(autores)
    except Exception as e:
        print(e)
        return None
    
    
def buscar_autor_por_id(id):  
    autores = carregar_autores()
    for a in autores:
        if a.id == id:
            return a
    return None
    

def atualizar_autor(autor):
    try:
        autores = carregar_autores()
        for idx, a in enumerate(autores):
            if a.id == autor.id:
                autores[idx] = autor
                salvar_autores(autores)
                return True
    except Exception as e:
        print(e)
        return False
    
    
def remover_autor(id):
    pass