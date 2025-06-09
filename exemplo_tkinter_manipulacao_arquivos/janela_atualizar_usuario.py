import tkinter as tk
import manipulador_arquivos as ma
import utils as ut
        

class JanelaAtualizarUsuario:
    """
    Classe que representa o frame do atualização de usuario.
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

        self.botao = tk.Button(self.frame, text="Atualizar", command=self.atualizar_usuario)
        self.botao.pack(pady=5)
        
        
    def limpar_campos(self):
        """
        Método que limpa os campos do formulário. A função delete() remove o texto digitado no elemento desde o índice zero até o último índice ('end').
        """
        self.entrada_usuario.delete(0 ,'end')
        self.entrada_email.delete(0 ,'end')
        self.entrada_senha.delete(0 ,'end')


    def atualizar_usuario(self):
        """
        Atualiza as informações de um usuário com os dados fornecidos nos campos de entrada.
        Recupera o nome, e-mail e senha dos campos de entrada da interface gráfica, chama a função de atualização de usuário, exibe uma mensagem de sucesso ou erro conforme o resultado, e limpa os campos de entrada após a operação.
        """
        # recupera o valor digitado nos campos do formulário
        nome = self.entrada_usuario.get()
        email = self.entrada_email.get()
        senha = self.entrada_senha.get()
        
        # chama a função de atualizar usuario no manipulador de arquivos
        resultado = ma.atualizar_usuario(nome, email, senha)
        
        # Exibe a mensagem de retorno ao usuário
        ut.exibir_mensagem(resultado, "Usuário atualizado com sucesso!", "Erro ao atualizar usuário.")
        
        # limpa os campos do formulário
        self.limpar_campos()