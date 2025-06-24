import tkinter as tk

janela = tk.Tk()
janela.title("Exemplo de Menu")
janela.geometry("400x300")

menu_bar = tk.Menu(janela)
janela.config(menu=menu_bar)

menu_arquivo = tk.Menu(menu_bar)
menu_bar.add_cascade(label="Arquivo", menu=menu_arquivo)

menu_arquivo.add_command(label="Novo")
menu_arquivo.add_command(label="Abrir")
menu_arquivo.add_separator()
menu_arquivo.add_command(label="Sair", command=janela.quit)

menu_ajuda = tk.Menu(menu_bar)
menu_bar.add_cascade(label="Ajuda", menu=menu_ajuda)

menu_ajuda.add_command(label="Sobre")

janela.mainloop()