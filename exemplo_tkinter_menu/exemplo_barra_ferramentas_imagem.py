import tkinter as tk
from tkinter import PhotoImage

def novo_arquivo():
    print("Novo arquivo criado.")

def salvar_arquivo():
    print("Arquivo salvo.")
   

janela = tk.Tk()
janela.title("Toolbar com Ícones")
janela.geometry("400x200")

toolbar = tk.Frame(janela, bg="#e0e0e0")
toolbar.pack(side="top", fill="x")

img_novo = PhotoImage(file="exemplo_tkinter_menu/add.png")
img_salvar = PhotoImage(file="exemplo_tkinter_menu/save.png")
img_sair = PhotoImage(file="exemplo_tkinter_menu/exit.png")

btn_novo = tk.Button(toolbar, image=img_novo, command=novo_arquivo)
btn_novo.pack(side="left", padx=5, pady=5)

btn_salvar = tk.Button(toolbar, image=img_salvar, command=salvar_arquivo)
btn_salvar.pack(side="left", padx=5, pady=5)

btn_sair = tk.Button(toolbar, image=img_sair, command=janela.quit)
btn_sair.pack(side="left", padx=5, pady=5)

janela.mainloop()