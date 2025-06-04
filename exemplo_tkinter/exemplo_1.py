import tkinter as tk
from tkinter import messagebox

def ao_fechar():
    resposta = messagebox.askyesno("Sair", "Tem certeza de que deseja sair?", icon=messagebox.WARNING)
    if resposta:
        janela.destroy()
        
def exibir_texto():
    texto_digitado = entrada.get()
    label_resultado.config(text=f"Olá, {texto_digitado}")

janela = tk.Tk()
janela.title("Minha Primeira Janela")

janela.geometry("400x300")

rotulo = tk.Label(janela, text="Bem vindo!")
rotulo.pack()

entrada = tk.Entry(janela)
entrada.pack(pady=10)

button = tk.Button(janela, text="Mostrar", command=exibir_texto)
button.pack()

label_resultado = tk.Label(janela, text="")
label_resultado.pack(pady=10)

janela.protocol("WM_DELETE_WINDOW", ao_fechar)

janela.mainloop()