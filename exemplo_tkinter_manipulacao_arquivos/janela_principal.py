import tkinter as tk
from janela_cadastrar_usuario import JanelaCadastroUsuario
from janela_buscar_usuario import JanelaBuscaUsuario
from janela_atualizar_usuario import JanelaAtualizarUsuario
from janela_remover_usuario import JanelaRemoverUsuario


"""
Janela principal. Contém botões para as quatro funcionalidades.
"""
class JanelaPrincipal:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("Sistema de Cadastro de Usuário")
        self.centralizar_janela()

        """
        Cria um frame para os botões e o coloca na posicao 0,0 da tabela.
        """
        frame_botoes = tk.Frame(self.janela, width=420, height=50)
        frame_botoes.grid(row=0, column=0, padx=10, pady=10)

        botao_cadastro = tk.Button(frame_botoes, text="Cadastrar", command=self.abrir_janela_cadastro)
        # O side='left' faz com que o botao seja alinhado a esquerda
        botao_cadastro.pack(padx=5, side='left')

        botao_busca = tk.Button(frame_botoes, text="Buscar", command=self.abrir_janela_busca)
        botao_busca.pack(padx=5, side='left')

        botao_atualizar = tk.Button(frame_botoes, text="Atualizar", command=self.abrir_janela_atualizacao)
        botao_atualizar.pack(padx=5, side='left')

        botao_remover = tk.Button(frame_botoes, text="Remover", command=self.abrir_janela_remocao)
        botao_remover.pack(padx=5, side='left')

        self.janela.mainloop()


    def centralizar_janela(self):
        largura = 420
        altura = 350
        
        largura_tela = self.janela.winfo_screenwidth()
        altura_tela = self.janela.winfo_screenheight()
        
        x = (largura_tela // 2) - (largura // 2)
        y = (altura_tela // 2) - (altura // 2)
        self.janela.geometry(f"{largura}x{altura}+{x}+{y}")


    """
    Função para remover o frame da janela principal.
    A cada vez que o usuário clica em um botão para abrir uma
    funcionalidade, o frame da funcionalidade anterior é apagado.
    """
    def limpar_widgets(self):
        # se houver mais de um widget filho da janela principal, então há um frame criado
        if len(self.janela.winfo_children()) > 1:
            # remove o frame criado
            self.janela.winfo_children()[1].destroy()


    def abrir_janela_cadastro(self):
        self.limpar_widgets()
        JanelaCadastroUsuario(self.janela)
        

    def abrir_janela_busca(self):
        self.limpar_widgets()
        JanelaBuscaUsuario(self.janela)
        
        
    def abrir_janela_atualizacao(self):
        self.limpar_widgets()
        JanelaAtualizarUsuario(self.janela)


    def abrir_janela_remocao(self):
        self.limpar_widgets()
        JanelaRemoverUsuario(self.janela)