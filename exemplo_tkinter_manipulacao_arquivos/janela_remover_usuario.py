import tkinter as tk
import manipulador_arquivos as ma
import utils as ut


def limpar_campos():
    entrada_usuario.delete(0 ,'end')
        

def remover_usuario():
    nome = entrada_usuario.get()
    resultado = ma.remover_usuario(nome)
    ut.exibir_mensagem(resultado, "Usuário removido com sucesso!", "Usuário não encontrado.")
    limpar_campos()
    

janela = tk.Tk()
janela.title("Remover Usuário")
janela.geometry("400x200")

label_nome = tk.Label(janela, text="Nome: ")
label_nome.pack(pady=5)

entrada_usuario = tk.Entry(janela)
entrada_usuario.pack(pady=5)

botao = tk.Button(janela, text="Remover", command=remover_usuario)
botao.pack(pady=5)

janela.mainloop()