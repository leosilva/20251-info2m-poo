import tkinter as tk
import manipulacao_arquivos.manipulador_arquivos_livro as mal
import manipulacao_arquivos.manipulador_arquivos_editora as mae
import manipulacao_arquivos.manipulador_arquivos_autor as maa
from janelas.livro.janela_atualizar_livro import JanelaAtualizarLivro
from tkinter import messagebox
import utils as ut


class JanelaBuscaLivro:
    def __init__(self, janela):
        self.janela = janela
        self.frame = tk.Frame(janela, width=420, height=350)
        self.frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        label_titulo = tk.Label(self.frame, text="Titulo: ")
        label_titulo.grid(row=0, column=0, sticky='E', padx=5, pady=5)

        self.entrada_titulo = tk.Entry(self.frame)
        self.entrada_titulo.grid(row=0, column=1, sticky='W', padx=5, pady=5)
        self.entrada_titulo.focus()

        self.botao = tk.Button(self.frame, text="Buscar", command=self.buscar_livro)
        self.botao.grid(row=1, column=0, padx=5, pady=5, columnspan=2)

        self.label_titulo_resultado = tk.Label(self.frame)
        self.label_titulo_resultado.grid(row=2, column=0, sticky='W', padx=5, pady=5, columnspan=2)

        self.label_autor_resultado = tk.Label(self.frame)
        self.label_autor_resultado.grid(row=3, column=0, sticky='W', padx=5, pady=5, columnspan=2)

        self.label_isbn_resultado = tk.Label(self.frame)
        self.label_isbn_resultado.grid(row=4, column=0, sticky='W', padx=5, pady=5, columnspan=2)
        
        self.label_editora_resultado = tk.Label(self.frame)
        self.label_editora_resultado.grid(row=5, column=0, sticky='W', padx=5, pady=5, columnspan=2)
        
        self.botao_atualizar = tk.Button(self.frame, text="Atualizar", command=self.atualizar_livro, state='disabled')
        self.botao_atualizar.grid(row=6, column=0, padx=5, pady=5, sticky='E')
        
        self.botao_remover = tk.Button(self.frame, text="Remover", command=self.remover_livro, state='disabled')
        self.botao_remover.grid(row=6, column=1, padx=5, pady=5, sticky='W')

        self.reset_textos_labels()


    def limpar_campos(self):
        self.entrada_titulo.delete(0 ,'end')

    
    def reset_textos_labels(self):
        self.label_titulo_resultado.config(text="Título: ")
        self.label_autor_resultado.config(text="Autores: ")
        self.label_isbn_resultado.config(text="ISBN: ")
        self.label_editora_resultado.config(text="Editora: ")
    
    
    def exibir_resultado(self, resultado):
        self.reset_textos_labels()
        
        texto_atual = self.label_titulo_resultado.cget("text")
        texto_atual = texto_atual + resultado.titulo
        self.label_titulo_resultado.config(text=texto_atual)
        
        texto_atual = self.label_autor_resultado.cget("text")
        for id in resultado.autores:
            autor = maa.buscar_autor_por_id(id)
            texto_atual = texto_atual + autor.nome + ', '
        
        # removendo os dois ultimos caracteres, para remover o ultimo ', '
        texto_atual = texto_atual[:-2]
            
        self.label_autor_resultado.config(text=texto_atual)
        
        texto_atual = self.label_isbn_resultado.cget("text")
        texto_atual = texto_atual + resultado.isbn
        self.label_isbn_resultado.config(text=texto_atual)
        
        texto_atual = self.label_editora_resultado.cget("text")
        editora = mae.buscar_editora_por_id(resultado.editora_id)
        texto_atual = texto_atual + editora.nome
        self.label_editora_resultado.config(text=texto_atual)
    
    
    def buscar_livro(self):
        titulo = self.entrada_titulo.get()
        resultado = mal.buscar_livro_por_titulo(titulo)
        if resultado:
            self.livro_buscado = resultado
            self.exibir_resultado(resultado)
            self.habilitar_botoes()
        else:
            self.livro_buscado = None
            self.reset_textos_labels()
            messagebox.showinfo("Não encontrado!", "Livro não encontrado.")

        self.limpar_campos()
        
    
    def habilitar_botoes(self):
        self.botao_atualizar.config(state='normal')
        self.botao_remover.config(state='normal')
        
        
    def atualizar_livro(self):
        if self.livro_buscado:
            JanelaAtualizarLivro(self.janela, self.livro_buscado)
            self.frame.destroy()
    
    
    def remover_livro(self):
        # pergunta se quer remover
        tem_ctz = messagebox.askyesno("Tem certeza?", "Tem certeza de que deseja remover este livro?")
        
        if tem_ctz:
            # manda remover o livro, passando o id como parametro
            resultado = mal.remover_livro(self.livro_buscado.id)
            
            # exibe mensagem de sucesso ou falha
            ut.exibir_mensagem(resultado, "Livro removido com sucesso!", "Livro não encontrado.")
            
            # limpa os campos do formulario
            self.frame.destroy()