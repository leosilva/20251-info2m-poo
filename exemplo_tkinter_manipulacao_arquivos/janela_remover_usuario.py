import tkinter as tk
import manipulador_arquivos as ma
import utils as ut


class JanelaRemoverUsuario:
    """
    Classe que representa o frame do remoção de usuario.
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

        self.botao = tk.Button(self.frame, text="Remover", command=self.remover_usuario)
        self.botao.pack(pady=5)


    def limpar_campos(self):
        """
        Método que limpa os campos do formulário. A função delete() remove o texto digitado no elemento desde o índice zero até o último índice ('end').
        """
        self.entrada_usuario.delete(0 ,'end')
        

    def remover_usuario(self):
        """
        Remove um usuário com base no nome inserido no campo de entrada.
        Obtém o nome do usuário a partir do widget de entrada (entrada_usuario), tenta remover o usuário usando a função 'ma.remover_usuario' e exibe uma mensagem de sucesso ou falha utilizando 'ut.exibir_mensagem'. Depois, limpa os campos de entrada.
        """
        # recupera o valor digitado nos campos do formulário
        nome = self.entrada_usuario.get()
        
        # chama a função de remover usuario no manipulador de arquivos
        resultado = ma.remover_usuario(nome)
        
        # Exibe a mensagem de retorno ao usuário
        ut.exibir_mensagem(resultado, "Usuário removido com sucesso!", "Usuário não encontrado.")
        
        # limpa os campos do formulário
        self.limpar_campos()