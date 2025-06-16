import tkinter as tk
from tkinter import ttk

def mostrar_selecao(event):
    print("Selecionado:", combobox.get())

janela = tk.Tk()
janela.title("Combobox com .get() e .bind()")

opcoes = ["Python", "Java", "C++", "JavaScript"]
combobox = ttk.Combobox(janela, values=opcoes)
combobox.pack()

combobox.bind("<<ComboboxSelected>>", mostrar_selecao)

janela.mainloop()