import tkinter as tk
from tkinter import ttk

janela = tk.Tk()
janela.title("Exemplo com Combobox")

opcoes = ["Python", "Java", "C++", "JavaScript"]
combobox = ttk.Combobox(janela, values=opcoes)
combobox.pack()

combobox.set("Selecione uma linguagem")

janela.mainloop()