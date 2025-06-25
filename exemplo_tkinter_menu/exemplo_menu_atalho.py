import tkinter as tk

def novo_arquivo(event=None):
    print("Novo arquivo criado!")


janela = tk.Tk()
janela.title("Aceleradores")

menu_bar = tk.Menu(janela)
janela.config(menu=menu_bar)

menu_arquivo = tk.Menu(menu_bar)
menu_bar.add_cascade(label="Arquivo", menu=menu_arquivo)

menu_arquivo.add_command(label="Novo\tCtrl+N", command=novo_arquivo)

janela.bind("<Control-n>", novo_arquivo)

janela.mainloop()