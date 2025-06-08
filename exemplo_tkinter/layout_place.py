import tkinter as tk

janela = tk.Tk()
janela.geometry("300x200")

botao = tk.Button(janela, text="Clique Aqui")
botao.place(relx=0.5, rely=0.5, anchor="center")

janela.mainloop()