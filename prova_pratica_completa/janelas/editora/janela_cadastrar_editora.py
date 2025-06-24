import tkinter as tk
import manipulacao_arquivos.manipulador_arquivos_editora as mae
import utils as ut
from models.editora import Editora


class JanelaCadastroEditora:
    def __init__(self, janela):
        self.frame = tk.Frame(janela, width=420, height=350)
        self.frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        label_nome = tk.Label(self.frame, text="Nome: ")
        label_nome.grid(row=0, column=0, sticky='E', padx=5, pady=5)

        self.entrada_nome = tk.Entry(self.frame)
        self.entrada_nome.grid(row=0, column=1, sticky='W', padx=5, pady=5)
        self.entrada_nome.focus()

        label_pais = tk.Label(self.frame, text="País: ")
        label_pais.grid(row=1, column=0, sticky='E', padx=5, pady=5)
        
        self.entrada_pais = tk.Entry(self.frame)
        self.entrada_pais.grid(row=1, column=1, sticky='W', padx=5, pady=5)

        botao = tk.Button(self.frame, text="Salvar", command=self.cadastrar_editora)
        botao.grid(row=2, column=0, padx=5, pady=5, columnspan=2)


    def limpar_campos(self):
        self.entrada_nome.delete(0 ,'end')
        self.entrada_pais.delete(0 ,'end')
        self.entrada_nome.focus()
        

    def cadastrar_editora(self):
        # recupera dados digitados na tela
        nome = self.entrada_nome.get()
        pais = self.entrada_pais.get()
        
        # cria objeto da classe Editora
        nova_editora = Editora(nome, pais)

        # envia o objeto para ser salvo no arquivo
        resultado = mae.adicionar_editora(nova_editora)
        
        # exibe mensagem de sucesso ou falha
        ut.exibir_mensagem(resultado, "Editora adiconada com sucesso!", "Erro ao adicionar editora.")
        
        # limpa os campos do formulario
        self.limpar_campos()