import tkinter as tk
import manipulacao_arquivos.manipulador_arquivos_livro as ma
import utils as ut


class JanelaRemoverLivro:
    def __init__(self, janela):
        self.frame = tk.Frame(janela, width=420, height=300)
        self.frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        label_titulo = tk.Label(self.frame, text="Titulo: ")
        label_titulo.pack(pady=5)

        self.entrada_titulo = tk.Entry(self.frame)
        self.entrada_titulo.pack(pady=5)
        self.entrada_titulo.focus()

        self.botao = tk.Button(self.frame, text="Remover", command=self.remover_livro)
        self.botao.pack(pady=5)


    def limpar_campos(self):
        self.entrada_titulo.delete(0 ,'end')
        

    def remover_livro(self):
        # recupera o titulo do livro digitado como parametro
        titulo = self.entrada_titulo.get()
        
        # manda remover o livro, passando o titulo como parametro
        resultado = ma.remover_livro(titulo)
        
        # exibe mensagem de sucesso ou falha
        ut.exibir_mensagem(resultado, "Livro removido com sucesso!", "Livro não encontrado.")
        
        # limpa os campos do formulario
        self.limpar_campos()