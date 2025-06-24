import tkinter as tk
from janelas.livro.janela_cadastrar_livro import JanelaCadastroLivro
from janelas.livro.janela_buscar_livro import JanelaBuscaLivro
from janelas.livro.janela_atualizar_livro import JanelaAtualizarLivro
from janelas.livro.janela_remover_livro import JanelaRemoverLivro
from janelas.editora.janela_cadastrar_editora import JanelaCadastroEditora


class JanelaPrincipal:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("Sistema de Cadastro de Livros")
        self.centralizar_janela()

        # barra de menu
        self.menu_bar = tk.Menu(self.janela)
        self.janela.config(menu=self.menu_bar)

        # itens de menu
        menu_livros = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Livros", menu=menu_livros)
        menu_livros.add_command(label="Cadastrar Livro", command=self.abrir_janela_cadastro)
        menu_livros.add_command(label="Buscar Livro", command=self.abrir_janela_busca)
        
        menu_livros.add_separator()
        menu_livros.add_command(label="Sair", command=self.janela.quit)
        
        menu_editoras = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Editoras", menu=menu_editoras)
        menu_editoras.add_command(label="Cadastrar Editora", command=self.abrir_janela_cadastro_editora)

        self.janela.mainloop()

    def centralizar_janela(self):
        largura = 350
        altura = 300
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
        JanelaCadastroLivro(self.janela)

    def abrir_janela_busca(self):
        self.limpar_widgets()
        JanelaBuscaLivro(self.janela)

    # def abrir_janela_atualizacao(self):
    #     self.limpar_widgets()
    #     JanelaAtualizarLivro(self.janela)

    # def abrir_janela_remocao(self):
    #     self.limpar_widgets()
    #     JanelaRemoverLivro(self.janela)
        
    def abrir_janela_cadastro_editora(self):
        self.limpar_widgets()
        JanelaCadastroEditora(self.janela)