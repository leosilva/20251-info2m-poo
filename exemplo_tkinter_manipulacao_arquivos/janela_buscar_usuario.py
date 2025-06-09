import tkinter as tk
import manipulador_arquivos as ma
from tkinter import messagebox


class JanelaBuscaUsuario:
    """
    Classe que representa o frame do busca de usuario.
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

        self.botao = tk.Button(self.frame, text="Buscar", command=self.buscar_usuario)
        self.botao.pack(pady=5)

        # cria os labels para exibir o resultado da busca. Inicialmente, eles não tem texto nenhum.
        self.label_nome_resultado = tk.Label(self.frame)
        self.label_nome_resultado.pack(pady=5)

        self.label_email_resultado = tk.Label(self.frame)
        self.label_email_resultado.pack(pady=5)

        self.label_senha_resultado = tk.Label(self.frame)
        self.label_senha_resultado.pack(pady=5)

        # Aqui, os labels recebem texto.
        self.reset_textos_labels()


    def limpar_campos(self):
        """
        Método que limpa os campos do formulário. A função delete() remove o texto digitado no elemento desde o índice zero até o último índice ('end').
        """
        self.entrada_usuario.delete(0 ,'end')

    
    def reset_textos_labels(self):
        """
        Método que atribui o texto inicial padrão para os labels do resultado.
        """
        self.label_nome_resultado.config(text="Nome: ")
        self.label_email_resultado.config(text="Email: ")
        self.label_senha_resultado.config(text="Senha: ")
    
    
    def exibir_resultado(self, resultado):
        """
        Método que exibe o resultado nos labels de resultado.
        """
        # exibe os textos padrões nos labels de resultado
        self.reset_textos_labels()
        
        """ Executa a função split no resultado. Como o resultado é uma linha do arquivo com um separador (';'), o método split criará uma lista de elementos a partir desse separador. Por exemplo:
        
        Linha do arquivo: leo;leo@gmail.com;123
        Após o split: ['leo', 'leo@gmail.com', '123']
        """
        resultado_splitted = resultado.split(";")
        
        # recupera o valor atual do label resultante de usuario
        texto_atual = self.label_nome_resultado.cget("text")
        # atualiza o texto, adicionando o nome do usuario
        texto_atual = texto_atual + resultado_splitted[0]
        # atualiza o texto do label com o novo valor da variavel
        self.label_nome_resultado.config(text=texto_atual)
        
        # atualizando label email. Mesmo processo anterior.
        texto_atual = self.label_email_resultado.cget("text")
        texto_atual = texto_atual + resultado_splitted[1]
        self.label_email_resultado.config(text=texto_atual)
        
        # atualizando label senha. Mesmo processo anterior.
        texto_atual = self.label_senha_resultado.cget("text")
        texto_atual = texto_atual + resultado_splitted[2]
        self.label_senha_resultado.config(text=texto_atual)

    
    def buscar_usuario(self):
        """
        Busca um usuário pelo nome digitado no campo de entrada.

        Recupera o nome do usuário a partir do widget de entrada (entrada_usuario), busca o usuário usando a função 'ma.buscar_usuario_por_nome' e exibe o resultado se encontrado.
        Se o usuário não for encontrado, reseta os textos dos labels e exibe uma caixa de mensagem informativa. Por fim, limpa os campos de entrada.
        """
        nome = self.entrada_usuario.get()
        resultado = ma.buscar_usuario_por_nome(nome)
        if resultado:
            self.exibir_resultado(resultado)
        else:
            self.reset_textos_labels()
            messagebox.showinfo("Não encontrado!", "Usuário não encontrado.")

        self.limpar_campos()