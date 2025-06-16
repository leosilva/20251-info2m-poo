import tkinter as tk

janela = tk.Tk()
janela.title("Lista de Linguagens")

lista_linguagens = ["Python", "Java", "C++", "JavaScript", "Ruby"]

lista_tela = tk.Listbox(janela) 
lista_tela.pack()

for item in lista_linguagens:
    lista_tela.insert(tk.END, item)

janela.mainloop()