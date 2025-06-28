import json
import os
from models.editora import Editora
import utils as ut


# indica o caminho do arquivo a ser manipulado
CAMINHO_ARQUIVO = "data/editoras.json"


def ler_arquivo(nome, mode):
    f = open(nome, mode)
    return f


def carregar_editoras():
    lista_editoras = []
    try:
        if not os.path.exists(CAMINHO_ARQUIVO):
            return lista_editoras
        f = open(CAMINHO_ARQUIVO, "r")
        editoras = json.load(f)
        for e in editoras:
            """
            {
                "id": 2,
                "nome": "Bookman",
                "pais": "Brasil"
            }
            """
            obj_editora = Editora(**e)
            lista_editoras.append(obj_editora)
        return lista_editoras
    except Exception as e:
        print(e)
        
        
def buscar_editora_por_id(id):
    editoras = carregar_editoras()
    for e in editoras:
        if e.id == id:
            return e
    return None

        
def salvar_editoras(lista):
    try:
        dados = [editora.to_dict() for editora in lista]
        
        f = open(CAMINHO_ARQUIVO, "w")
        json.dump(dados, f, indent=4)
            
        return True
    except Exception as e:
        print(e)
        return False


def adicionar_editora(editora):
    # le arquivo em formato de adicao (append)
    editoras = carregar_editoras()
    
    # gera novo id
    proximo_id = ut.calcular_proximo_id(editoras)
    
    # atribui novo id a editora que quer inserir
    editora.id = proximo_id
        
    # adiciona a nova editora na lista
    editoras.append(editora)
        
    # salva a nova lista no arquivo
    return salvar_editoras(editoras)
    
    
def buscar_editora_por_nome(nome):
    try:
        editoras = carregar_editoras()
        for editora in editoras:
            if editora.nome == nome:        
                # se achou uma editora com o nome, retorna a linha completa da editora
                return editora
    except:
        # deveria adicionar um arquivo de log para armazenar o erro
        return None
        
        
def atualizar_editora(editora):
    try:
        editoras = carregar_editoras()
        for idx, e in enumerate(editoras):
            if e.id == editora.id:
                editoras[idx] = editora
                salvar_editoras(editoras)
                return True
    except Exception as e:
        print(e)
        return False

    
def remover_editora(id):
    try:
        editoras = carregar_editoras()
        novas_editoras = []
        for e in editoras:
            if e.id != id:
                novas_editoras.append(e)
        return salvar_editoras(novas_editoras)
    except Exception as e:
        print(e)
        return False