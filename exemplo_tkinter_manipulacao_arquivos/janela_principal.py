import tkinter as tk
from janela_cadastrar_usuario import JanelaCadastroUsuario
from janela_buscar_usuario import JanelaBuscaUsuario
from janela_atualizar_usuario import JanelaAtualizarUsuario
from janela_remover_usuario import JanelaRemoverUsuario


class JanelaPrincipal:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("Sistema de Cadastro de Usuário")
        self.centralizar_janela()

        frame_botoes = tk.Frame(self.janela, width=420, height=50)
        frame_botoes.grid(row=0, column=0, padx=10, pady=10)

        botao = tk.Button(frame_botoes, text="Cadastrar", command=self.abrir_janela_cadastro)
        botao.pack(padx=5, side='left')

        botao = tk.Button(frame_botoes, text="Buscar", command=self.abrir_janela_busca)
        botao.pack(padx=5, side='left')

        botao = tk.Button(frame_botoes, text="Atualizar", command=self.abrir_janela_atualizacao)
        botao.pack(padx=5, side='left')

        botao = tk.Button(frame_botoes, text="Remover", command=self.abrir_janela_remocao)
        botao.pack(padx=5, side='left')

        self.janela.mainloop()


    def centralizar_janela(self):
        largura = 420
        altura = 350
        
        largura_tela = self.janela.winfo_screenwidth()
        altura_tela = self.janela.winfo_screenheight()
        
        x = (largura_tela // 2) - (largura // 2)
        y = (altura_tela // 2) - (altura // 2)
        self.janela.geometry(f"{largura}x{altura}+{x}+{y}")


    def limpar_widgets(self):
        if len(self.janela.winfo_children()) > 1:
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