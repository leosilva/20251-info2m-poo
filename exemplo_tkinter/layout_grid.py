import tkinter as tk

janela = tk.Tk()
janela.geometry("300x200")
janela.title("Tela de Login")

tk.Label(janela, text="Usuário:").grid(row=0, column=0, padx=10, pady=10, sticky="E")
tk.Entry(janela).grid(row=0, column=1, padx=10, pady=10, sticky="W")

tk.Label(janela, text="Senha:").grid(row=1, column=0, padx=10, pady=10, sticky="E")
tk.Entry(janela, show="*").grid(row=1, column=1, padx=10, pady=10, sticky="W")

tk.Button(janela, text="Entrar").grid(row=2, column=0, columnspan=2, pady=20)

janela.mainloop()