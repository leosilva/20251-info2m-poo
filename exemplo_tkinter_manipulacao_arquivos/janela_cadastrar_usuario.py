import tkinter as tk
import manipulador_arquivos as ma
import utils as ut


class JanelaCadastroUsuario:
    """
    Classe que representa o frame do cadastro de usuario.
    """
    def __init__(self, janela):
        # cria um frame e o posiciona na linha 1, coluna 0. Portanto, abaixo da linha dos botões.
        self.frame = tk.Frame(janela, width=420, height=300)
        self.frame.grid(row=1, column=0, padx=10, pady=10)

        # cria os elementos da janela. Notar que o elemento pai é o frame (e não a janela principal)
        label_nome = tk.Label(self.frame, text="Nome: ")
        label_nome.pack(pady=5)

        self.entrada_usuario = tk.Entry(self.frame)
        self.entrada_usuario.pack(pady=5)
        # o método focus() força que o foco da janela esteja sobre esse elemento. O foco significa o cursor do mouse habilitado no elemento.
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
        """
        Método que limpa os campos do formulário. A função delete() remove o texto digitado no elemento desde o índice zero até o último índice ('end').
        """
        self.entrada_usuario.delete(0 ,'end')
        self.entrada_email.delete(0 ,'end')
        self.entrada_senha.delete(0 ,'end')


    def cadastrar_usuario(self):
        """
        Método responsável pelo processo de cadastro de usuário recuperando os dados dos campos do formulário, adicionando o usuário via o manipulador de arquivos, exibindo uma mensagem de sucesso ou erro, e limpando os campos do formulário.
        Etapas realizadas:
            1. Recupera o nome, email e senha informados no formulário.
            2. Chama o manipulador de arquivos para adicionar o novo usuário.
            3. Exibe uma mensagem indicando sucesso ou falha para o usuário.
            4. Limpa os campos do formulário após tentar o cadastro.
        """
        # recupera o valor digitado nos campos do formulário
        nome = self.entrada_usuario.get()
        email = self.entrada_email.get()
        senha = self.entrada_senha.get()

        # chama a função de adicionar usuario no manipulador de arquivos
        resultado = ma.adicionar_usuario(nome, email, senha)
        
        # Exibe a mensagem de retorno ao usuário
        ut.exibir_mensagem(resultado, "Usuário adiconado com sucesso!", "Erro ao adicionar usuário.")
        
        # limpa os campos do formulário
        self.limpar_campos()