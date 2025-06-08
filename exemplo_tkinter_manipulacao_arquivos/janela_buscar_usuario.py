import tkinter as tk
import manipulador_arquivos as ma
from tkinter import messagebox


class JanelaBuscaUsuario:
    def __init__(self, janela):        
        self.frame = tk.Frame(janela, width=420, height=300)
        self.frame.grid(row=1, column=0, padx=10, pady=10)

        label_nome = tk.Label(self.frame, text="Nome: ")
        label_nome.pack(pady=5)

        self.entrada_usuario = tk.Entry(self.frame)
        self.entrada_usuario.pack(pady=5)
        self.entrada_usuario.focus()

        self.botao = tk.Button(self.frame, text="Buscar", command=self.buscar_usuario)
        self.botao.pack(pady=5)

        self.label_nome_resultado = tk.Label(self.frame)
        self.label_nome_resultado.pack(pady=5)

        self.label_email_resultado = tk.Label(self.frame)
        self.label_email_resultado.pack(pady=5)

        self.label_senha_resultado = tk.Label(self.frame)
        self.label_senha_resultado.pack(pady=5)

        self.reset_textos_labels()

    def limpar_campos(self):
        self.entrada_usuario.delete(0 ,'end')
    

    def reset_textos_labels(self):
        self.label_nome_resultado.config(text="Nome: ")
        self.label_email_resultado.config(text="Email: ")
        self.label_senha_resultado.config(text="Senha: ")
    
    
    def exibir_resultado(self, resultado):
        self.reset_textos_labels()
        resultado_splitted = resultado.split(";")
        
        # atualizando label usuario
        texto_atual = self.label_nome_resultado.cget("text")
        texto_atual = texto_atual + resultado_splitted[0]
        self.label_nome_resultado.config(text=texto_atual)
        
        # atualizando label email
        texto_atual = self.label_email_resultado.cget("text")
        texto_atual = texto_atual + resultado_splitted[1]
        self.label_email_resultado.config(text=texto_atual)
        
        # atualizando label senha
        texto_atual = self.label_senha_resultado.cget("text")
        texto_atual = texto_atual + resultado_splitted[2]
        self.label_senha_resultado.config(text=texto_atual)


    def buscar_usuario(self):
        nome = self.entrada_usuario.get()
        resultado = ma.buscar_usuario_por_nome(nome)
        if resultado:
            self.exibir_resultado(resultado)
        else:
            self.reset_textos_labels()
            messagebox.showinfo("Não encontrado!", "Usuário não encontrado.")

        self.limpar_campos()