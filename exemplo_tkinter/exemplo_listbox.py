import tkinter as tk

janela = tk.Tk()

lista = tk.Listbox(janela)
lista.insert(1, "Python")
lista.insert(2, "Java")
lista.insert(3, "C++")

lista.pack()

janela.mainloop()