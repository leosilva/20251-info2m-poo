import tkinter as tk
from tkinter import messagebox


# acao de login
def fazer_login():
    usuario_digitado = entry_usuario.get()
    senha_digitada = entry_senha.get()
    if usuario_digitado == "admin" and senha_digitada == "123456":
        messagebox.showinfo("Sucesso!", "Login realizado com sucesso!")
    else:
        messagebox.showinfo("Falha!", "Usuário ou senha incorretos.")
    

# cria a janela
janela = tk.Tk()
janela.title("Tela de Login")

janela.geometry("300x200")

# campos de usuario
label_usuario = tk.Label(janela, text="Usuário")
label_usuario.pack()

entry_usuario = tk.Entry(janela)
entry_usuario.pack(pady=10)

# campos de senha
label_senha = tk.Label(janela, text="Senha")
label_senha.pack()

entry_senha = tk.Entry(janela, show="*")
entry_senha.pack(pady=10)

button = tk.Button(janela, text="Entrar", command=fazer_login)
button.pack(pady=10)

janela.mainloop()