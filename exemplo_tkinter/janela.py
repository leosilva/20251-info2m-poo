import tkinter as tk
from tkinter import messagebox

janela = tk.Tk()
janela.title("Janela com Ícone")
janela.iconbitmap("calc_calculator_9599.ico")  # Substitua pelo nome do seu arquivo
janela.geometry("300x200")

def ao_fechar():
    resposta = messagebox.askyesno("Sair", "Tem certeza que deseja sair?", icon=messagebox.WARNING)
    if resposta:
        janela.destroy()

janela.protocol("WM_DELETE_WINDOW", ao_fechar)

janela.mainloop()