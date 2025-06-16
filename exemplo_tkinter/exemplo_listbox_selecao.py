import tkinter as tk

janela = tk.Tk()
janela.title("Seleção de Linguagens")

lista = tk.Listbox(janela, selectmode="extended")
lista.pack()

linguagens = ["Python", "Java", "C++", "JavaScript", "Ruby"]

for item in linguagens:
    lista.insert(tk.END, item)

janela.mainloop()