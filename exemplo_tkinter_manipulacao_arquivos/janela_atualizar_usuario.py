import tkinter as tk
import manipulador_arquivos as ma
import utils as ut
        

def limpar_campos():
    entrada_usuario.delete(0 ,'end')
    entrada_email.delete(0 ,'end')
    entrada_senha.delete(0 ,'end')


def atualizar_usuario():
    nome = entrada_usuario.get()
    email = entrada_email.get()
    senha = entrada_senha.get()
    resultado = ma.atualizar_usuario(nome, email, senha)
    ut.exibir_mensagem(resultado, "Usuário atualizado com sucesso!", "Erro ao atualizar usuário.")
    limpar_campos()
    

janela = tk.Tk()
janela.title("Atualizar Usuário")
janela.geometry("400x260")

label_nome = tk.Label(janela, text="Nome: ")
label_nome.pack(pady=5)

entrada_usuario = tk.Entry(janela)
entrada_usuario.pack(pady=5)

label_email = tk.Label(janela, text="Email: ")
label_email.pack(pady=5)

entrada_email = tk.Entry(janela)
entrada_email.pack(pady=5)

label_senha = tk.Label(janela, text="Senha: ")
label_senha.pack(pady=5)

entrada_senha = tk.Entry(janela, show="*")
entrada_senha.pack(pady=5)

botao = tk.Button(janela, text="Atualizar", command=atualizar_usuario)
botao.pack(pady=5)

janela.mainloop()