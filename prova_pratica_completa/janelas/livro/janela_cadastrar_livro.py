import tkinter as tk
from tkinter import ttk, messagebox
import manipulacao_arquivos.manipulador_arquivos_livro as mal
import manipulacao_arquivos.manipulador_arquivos_editora as mae
import manipulacao_arquivos.manipulador_arquivos_autor as maa
import utils as ut
from models.livro import Livro


class JanelaCadastroLivro:
    def __init__(self, janela):
        self.frame = tk.Frame(janela, width=420, height=350)
        self.frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        label_titulo = tk.Label(self.frame, text="Título: ")
        label_titulo.grid(row=0, column=0, sticky='E', padx=5, pady=5)

        self.entrada_titulo = tk.Entry(self.frame)
        self.entrada_titulo.grid(row=0, column=1, sticky='W', padx=5, pady=5)
        self.entrada_titulo.focus()

        label_isbn = tk.Label(self.frame, text="ISBN: ")
        label_isbn.grid(row=1, column=0, sticky='E', padx=5, pady=5)

        self.entrada_isbn = tk.Entry(self.frame)
        self.entrada_isbn.grid(row=1, column=1, sticky='W', padx=5, pady=5)
        
        label_autor = tk.Label(self.frame, text="Autores: ")
        label_autor.grid(row=2, column=0, sticky='E', padx=5, pady=5)
        
        nomes_autores = self.reset_autores()
        
        self.listbox_autores = tk.Listbox(self.frame, selectmode="extended", height=5)
        self.listbox_autores.grid(row=2, column=1, sticky='W', padx=5, pady=5)
        for nome in nomes_autores:
            self.listbox_autores.insert(tk.END, nome)

        label_editora = tk.Label(self.frame, text="Editora: ")
        label_editora.grid(row=3, column=0, sticky='E', padx=5, pady=5)
        
        nomes_editoras = self.reset_editoras()
        
        self.combobox_editoras = ttk.Combobox(self.frame, state="readonly", values=nomes_editoras)
        self.combobox_editoras.set("Selecione uma editora")
        self.combobox_editoras.grid(row=3, column=1, padx=5, pady=5)

        botao = tk.Button(self.frame, text="Salvar", command=self.cadastrar_livro)
        botao.grid(row=4, column=0, padx=5, pady=5, columnspan=2)
        
        
    def recuperar_autores_selecionados(self):
        itens_selecionados = []
        indices_selecionados = self.listbox_autores.curselection()
        if indices_selecionados:
            for indice in indices_selecionados:
                item = self.autores[indice]
                if item:
                    itens_selecionados.append(item.id)
        return itens_selecionados
    
       
    def reset_autores(self):
        self.autores = maa.carregar_autores()
        nomes_autores = [autor.nome for autor in self.autores]
        return nomes_autores
    
        
    def reset_editoras(self):
        self.editoras = mae.carregar_editoras()
        nomes_editoras = [editora.nome for editora in self.editoras]
        return nomes_editoras
        

    def limpar_campos(self):
        self.entrada_titulo.delete(0 ,'end')
        self.entrada_isbn.delete(0 ,'end')
        self.listbox_autores.delete(0, 'end')
        
        nomes_autores = self.reset_autores()
        for nome in nomes_autores:
            self.listbox_autores.insert(tk.END, nome)
        
        nomes_editoras = self.reset_editoras()
        self.combobox_editoras.config(values=nomes_editoras)
        self.entrada_titulo.focus()


    def cadastrar_livro(self):
        # recupera dados digitados na tela
        titulo = self.entrada_titulo.get()
        isbn = self.entrada_isbn.get()
        editora_selecionada = self.combobox_editoras.current()
        editora = self.editoras[editora_selecionada]
        
        ids_autores = self.recuperar_autores_selecionados()
        
        if not ids_autores:
            messagebox.showwarning("Atenção", "Selecione pelo menos um autor.")
        else:
            # cria objeto da classe Livro
            livro = Livro(titulo, isbn, editora.id, ids_autores)
            
            # envia o objeto para ser salvo no arquivo
            resultado, livro = mal.adicionar_livro(livro)
            
            for id_autor in ids_autores:
                autor = maa.buscar_autor_por_id(id_autor)
                autor.livros.append(livro.id)
                maa.atualizar_autor(autor)
            
            # exibe mensagem de sucesso ou falha
            ut.exibir_mensagem(resultado, "Livro adiconado com sucesso!", "Erro ao adicionar livro.")
            
            self.limpar_campos()