import tkinter as tk
import manipulacao_arquivos.manipulador_arquivos_editora as mae
import utils as ut
from models.editora import Editora
        

class JanelaAtualizarEditora:
    def __init__(self, janela, editora):
        self.editora = editora
        self.frame = tk.Frame(janela, width=420, height=350)
        self.frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        label_nome = tk.Label(self.frame, text="Nome: ")
        label_nome.grid(row=0, column=0, sticky='E', padx=5, pady=5)

        self.entrada_nome = tk.Entry(self.frame)
        self.entrada_nome.grid(row=0, column=1, sticky='W', padx=5, pady=5)
        self.entrada_nome.insert(0, editora.nome)
        self.entrada_nome.focus()

        label_pais = tk.Label(self.frame, text="País: ")
        label_pais.grid(row=1, column=0, sticky='E', padx=5, pady=5)
        
        self.entrada_pais = tk.Entry(self.frame)
        self.entrada_pais.grid(row=1, column=1, sticky='W', padx=5, pady=5)
        self.entrada_pais.insert(0, editora.pais)

        botao = tk.Button(self.frame, text="Atualizar", command=self.atualizar_editora)
        botao.grid(row=4, column=0, padx=5, pady=5, columnspan=2)
               
        
    def limpar_campos(self):
        self.entrada_nome.delete(0 ,'end')
        self.entrada_pais.delete(0 ,'end')


    def atualizar_editora(self):
        # recupera dados digitados na tela
        nome = self.entrada_nome.get()
        pais = self.entrada_pais.get()
                      
        # cria objeto da classe Editora
        nova_editora = Editora(nome, pais, self.editora.id)
        
        # envia o objeto para ser atualizado no arquivo
        resultado = mae.atualizar_editora(nova_editora)
        
        # exibe mensagem de sucesso ou falha
        ut.exibir_mensagem(resultado, "Editora atualizada com sucesso!", "Erro ao atualizar editora.")
        
        # limpa os campos do formulario
        self.limpar_campos()
        
        self.frame.destroy()