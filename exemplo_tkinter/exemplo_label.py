import tkinter as tk

janela = tk.Tk()
janela.title("Exemplo com Entry")
janela.geometry("400x300")

# Criar o campo de entrada
entrada = tk.Entry(janela)
entrada.pack()

janela.mainloop()