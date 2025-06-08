import tkinter as tk
import manipulador_arquivos as ma
import utils as ut


class JanelaRemoverUsuario:
    def __init__(self, janela):
        self.frame = tk.Frame(janela, width=420, height=300)
        self.frame.grid(row=1, column=0, padx=10, pady=10)

        label_nome = tk.Label(self.frame, text="Nome: ")
        label_nome.pack(pady=5)

        self.entrada_usuario = tk.Entry(self.frame)
        self.entrada_usuario.pack(pady=5)
        self.entrada_usuario.focus()

        self.botao = tk.Button(self.frame, text="Remover", command=self.remover_usuario)
        self.botao.pack(pady=5)


    def limpar_campos(self):
        self.entrada_usuario.delete(0 ,'end')
        

    def remover_usuario(self):
        nome = self.entrada_usuario.get()
        resultado = ma.remover_usuario(nome)
        ut.exibir_mensagem(resultado, "Usuário removido com sucesso!", "Usuário não encontrado.")
        self.limpar_campos()