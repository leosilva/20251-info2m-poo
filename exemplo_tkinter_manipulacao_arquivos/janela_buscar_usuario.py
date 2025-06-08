import tkinter as tk
import manipulador_arquivos as ma
from tkinter import messagebox


def limpar_campos():
    entrada_usuario.delete(0 ,'end')
    

def reset_textos_labels():
    label_nome_resultado.config(text="Nome: ")
    label_email_resultado.config(text="Email: ")
    label_senha_resultado.config(text="Senha: ")
    
    
def exibir_resultado(resultado):
    reset_textos_labels()
    resultado_splitted = resultado.split(";")
    
    # atualizando label usuario
    texto_atual = label_nome_resultado.cget("text")
    texto_atual = texto_atual + resultado_splitted[0]
    label_nome_resultado.config(text=texto_atual)
    
    # atualizando label email
    texto_atual = label_email_resultado.cget("text")
    texto_atual = texto_atual + resultado_splitted[1]
    label_email_resultado.config(text=texto_atual)
    
    # atualizando label senha
    texto_atual = label_senha_resultado.cget("text")
    texto_atual = texto_atual + resultado_splitted[2]
    label_senha_resultado.config(text=texto_atual)


def buscar_usuario():
    nome = entrada_usuario.get()
    resultado = ma.buscar_usuario_por_nome(nome)
    if resultado:
        exibir_resultado(resultado)
    else:
        reset_textos_labels()
        messagebox.showinfo("Não encontrado!", "Usuário não encontrado.")

    limpar_campos()
    

janela = tk.Tk()
janela.title("Buscar Usuário")
janela.geometry("400x260")

label_nome = tk.Label(janela, text="Nome: ")
label_nome.pack(pady=5)

entrada_usuario = tk.Entry(janela)
entrada_usuario.pack(pady=5)

botao = tk.Button(janela, text="Buscar", command=buscar_usuario)
botao.pack(pady=5)

label_nome_resultado = tk.Label(janela)
label_nome_resultado.pack(pady=5)

label_email_resultado = tk.Label(janela)
label_email_resultado.pack(pady=5)

label_senha_resultado = tk.Label(janela)
label_senha_resultado.pack(pady=5)

reset_textos_labels()

janela.mainloop()