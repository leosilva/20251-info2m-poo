import tkinter as tk
import manipulacao_arquivos.manipulador_arquivos_autor as maa
import utils as ut
from models.autor import Autor


class JanelaCadastroAutor:
    def __init__(self, janela):
        self.frame = tk.Frame(janela, width=420, height=350)
        self.frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        label_nome = tk.Label(self.frame, text="Nome: ")
        label_nome.grid(row=0, column=0, sticky='E', padx=5, pady=5)

        self.entrada_nome = tk.Entry(self.frame)
        self.entrada_nome.grid(row=0, column=1, sticky='W', padx=5, pady=5)
        self.entrada_nome.focus()

        label_cpf = tk.Label(self.frame, text="CPF: ")
        label_cpf.grid(row=1, column=0, sticky='E', padx=5, pady=5)
        
        self.entrada_cpf = tk.Entry(self.frame)
        self.entrada_cpf.grid(row=1, column=1, sticky='W', padx=5, pady=5)
        
        label_email = tk.Label(self.frame, text="Email: ")
        label_email.grid(row=2, column=0, sticky='E', padx=5, pady=5)
        
        self.entrada_email = tk.Entry(self.frame)
        self.entrada_email.grid(row=2, column=1, sticky='W', padx=5, pady=5)

        botao = tk.Button(self.frame, text="Salvar", command=self.cadastrar_autor)
        botao.grid(row=3, column=0, padx=5, pady=5, columnspan=2)


    def limpar_campos(self):
        self.entrada_nome.delete(0 ,'end')
        self.entrada_email.delete(0 ,'end')
        self.entrada_cpf.delete(0 ,'end')
        self.entrada_nome.focus()
        

    def cadastrar_autor(self):
        # recupera dados digitados na tela
        nome = self.entrada_nome.get()
        cpf = self.entrada_cpf.get()
        email = self.entrada_email.get()
        
        # cria objeto da classe Autor
        novo_autor = Autor(nome, cpf, email)

        # envia o objeto para ser salvo no arquivo
        resultado = maa.adicionar_autor(novo_autor)
        
        # exibe mensagem de sucesso ou falha
        ut.exibir_mensagem(resultado, "Autor adiconado com sucesso!", "Erro ao adicionar autor.")
        
        # limpa os campos do formulario
        self.limpar_campos()