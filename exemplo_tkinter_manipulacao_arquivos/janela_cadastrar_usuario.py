import tkinter as tk
import manipulador_arquivos as ma
import utils as ut


class JanelaCadastroUsuario:
    def __init__(self, janela):        
        self.frame = tk.Frame(janela, width=420, height=300)
        self.frame.grid(row=1, column=0, padx=10, pady=10)

        label_nome = tk.Label(self.frame, text="Nome: ")
        label_nome.pack(pady=5)

        self.entrada_usuario = tk.Entry(self.frame)
        self.entrada_usuario.pack(pady=5)
        self.entrada_usuario.focus()

        label_email = tk.Label(self.frame, text="Email: ")
        label_email.pack(pady=5)

        self.entrada_email = tk.Entry(self.frame)
        self.entrada_email.pack(pady=5)

        label_senha = tk.Label(self.frame, text="Senha: ")
        label_senha.pack(pady=5)

        self.entrada_senha = tk.Entry(self.frame, show="*")
        self.entrada_senha.pack(pady=5)

        botao = tk.Button(self.frame, text="Salvar", command=self.cadastrar_usuario)
        botao.pack(pady=5)


    def limpar_campos(self):
        self.entrada_usuario.delete(0 ,'end')
        self.entrada_email.delete(0 ,'end')
        self.entrada_senha.delete(0 ,'end')


    def cadastrar_usuario(self):
        nome = self.entrada_usuario.get()
        email = self.entrada_email.get()
        senha = self.entrada_senha.get()
        resultado = ma.adicionar_usuario(nome, email, senha)
        ut.exibir_mensagem(resultado, "Usuário adiconado com sucesso!", "Erro ao adicionar usuário.")
        self.limpar_campos()