import tkinter as tk
import manipulacao_arquivos.manipulador_arquivos_editora as mae
from tkinter import messagebox
from janelas.editora.janela_atualizar_editora import JanelaAtualizarEditora
import utils as ut


class JanelaBuscaEditora:
    def __init__(self, janela):
        self.janela = janela
        self.frame = tk.Frame(janela, width=420, height=350)
        self.frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        label_nome = tk.Label(self.frame, text="Nome: ")
        label_nome.grid(row=0, column=0, sticky='E', padx=5, pady=5)

        self.entrada_nome = tk.Entry(self.frame)
        self.entrada_nome.grid(row=0, column=1, sticky='W', padx=5, pady=5)
        self.entrada_nome.focus()

        self.botao = tk.Button(self.frame, text="Buscar", command=self.buscar_editora)
        self.botao.grid(row=1, column=0, padx=5, pady=5, columnspan=2)

        self.label_nome_resultado = tk.Label(self.frame)
        self.label_nome_resultado.grid(row=2, column=0, sticky='W', padx=5, pady=5, columnspan=2)

        self.label_pais_resultado = tk.Label(self.frame)
        self.label_pais_resultado.grid(row=3, column=0, sticky='W', padx=5, pady=5, columnspan=2)

        self.botao_atualizar = tk.Button(self.frame, text="Atualizar", command=self.atualizar_editora, state='disabled')
        self.botao_atualizar.grid(row=6, column=0, padx=5, pady=5, sticky='E')
        
        self.botao_remover = tk.Button(self.frame, text="Remover", command=self.remover_editora, state='disabled')
        self.botao_remover.grid(row=6, column=1, padx=5, pady=5, sticky='W')

        self.reset_textos_labels()


    def limpar_campos(self):
        self.entrada_nome.delete(0 ,'end')

    
    def reset_textos_labels(self):
        self.label_nome_resultado.config(text="Nome: ")
        self.label_pais_resultado.config(text="País: ")
    
    
    def exibir_resultado(self, resultado):
        self.reset_textos_labels()
        
        texto_atual = self.label_nome_resultado.cget("text")
        texto_atual = texto_atual + resultado.nome
        self.label_nome_resultado.config(text=texto_atual)
        
        texto_atual = self.label_pais_resultado.cget("text")
        texto_atual = texto_atual + resultado.pais
        self.label_pais_resultado.config(text=texto_atual)
    
    
    def buscar_editora(self):
        nome = self.entrada_nome.get()
        resultado = mae.buscar_editora_por_nome(nome)
        if resultado:
            self.editora_buscada = resultado
            self.exibir_resultado(resultado)
            self.habilitar_botoes()
        else:
            self.editora_buscada = None
            self.reset_textos_labels()
            messagebox.showinfo("Não encontrado!", "Editora não encontrada.")

        self.limpar_campos()
        
    
    def habilitar_botoes(self):
        self.botao_atualizar.config(state='normal')
        self.botao_remover.config(state='normal')
        
        
    def atualizar_editora(self):
        if self.editora_buscada:
            JanelaAtualizarEditora(self.janela, self.editora_buscada)
            self.frame.destroy()
    
    
    def remover_editora(self):
        pass
        # pergunta se quer remover
        tem_ctz = messagebox.askyesno("Tem certeza?", "Tem certeza de que deseja remover esta editora?")
        
        if tem_ctz:
            # manda remover a editora, passando o id como parametro
            resultado = mae.remover_editora(self.editora_buscada.id)
            
            # exibe mensagem de sucesso ou falha
            ut.exibir_mensagem(resultado, "Editora removida com sucesso!", "Editora não encontrada.")
            
            # limpa os campos do formulario
            self.frame.destroy()