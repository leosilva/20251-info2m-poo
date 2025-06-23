import tkinter as tk
from tkinter import ttk
import manipulacao_arquivos.manipulador_arquivos_livro as mal
import manipulacao_arquivos.manipulador_arquivos_editora as mae
import utils as ut
from models.livro import Livro


class JanelaCadastroLivro:
    def __init__(self, janela):
        self.frame = tk.Frame(janela, width=420, height=350)
        self.frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        label_titulo = tk.Label(self.frame, text="Título: ")
        label_titulo.grid(row=0, column=0, sticky='E', padx=5, pady=5)

        self.entrada_titulo = tk.Entry(self.frame)
        self.entrada_titulo.grid(row=0, column=1, sticky='W', padx=5, pady=5)
        self.entrada_titulo.focus()

        label_autor = tk.Label(self.frame, text="Autor: ")
        label_autor.grid(row=1, column=0, sticky='E', padx=5, pady=5)

        self.entrada_autor = tk.Entry(self.frame)
        self.entrada_autor.grid(row=1, column=1, sticky='W', padx=5, pady=5)

        label_isbn = tk.Label(self.frame, text="ISBN: ")
        label_isbn.grid(row=2, column=0, sticky='E', padx=5, pady=5)

        self.entrada_isbn = tk.Entry(self.frame)
        self.entrada_isbn.grid(row=2, column=1, sticky='W', padx=5, pady=5)
        
        label_editora = tk.Label(self.frame, text="Editora: ")
        label_editora.grid(row=3, column=0, sticky='E', padx=5, pady=5)
        
        nomes_editoras = self.reset_editoras()
        
        self.combobox_editoras = ttk.Combobox(self.frame, state="readonly", values=nomes_editoras)
        self.combobox_editoras.set("Selecione uma editora")
        self.combobox_editoras.grid(row=3, column=1, padx=5, pady=5)

        botao = tk.Button(self.frame, text="Salvar", command=self.cadastrar_livro)
        botao.grid(row=4, column=0, padx=5, pady=5, columnspan=2)
        
        
    def reset_editoras(self):
        self.editoras = mae.carregar_editoras()
        nomes_editoras = [editora.nome for editora in self.editoras]
        return nomes_editoras
        

    def limpar_campos(self):
        self.entrada_titulo.delete(0 ,'end')
        self.entrada_autor.delete(0 ,'end')
        self.entrada_isbn.delete(0 ,'end')
        
        nomes_editoras = self.reset_editoras()
        self.combobox_editoras.config(values=nomes_editoras)
        self.entrada_titulo.focus()


    def cadastrar_livro(self):
        # recupera dados digitados na tela
        titulo = self.entrada_titulo.get()
        autor = self.entrada_autor.get()
        isbn = self.entrada_isbn.get()
        editora_selecionada = self.combobox_editoras.current()
        
        editora = self.editoras[editora_selecionada]
                
        # cria objeto da classe Livro
        livro = Livro(titulo, autor, isbn, editora.id)
        
        # envia o objeto para ser salvo no arquivo
        resultado = mal.adicionar_livro(livro)
        
        # exibe mensagem de sucesso ou falha
        ut.exibir_mensagem(resultado, "Livro adiconado com sucesso!", "Erro ao adicionar livro.")
        
        self.limpar_campos()