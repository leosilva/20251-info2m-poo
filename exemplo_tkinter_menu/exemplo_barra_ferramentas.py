import tkinter as tk

def acao_novo():
    print("Novo arquivo")

def acao_sair():
    janela.quit()

janela = tk.Tk()
janela.title("Toolbar com Frame")

# Criando a toolbar
toolbar = tk.Frame(janela, bg="#dddddd")
toolbar.pack(side="top", fill="x")

# Botões na toolbar
btn_novo = tk.Button(toolbar, text="Novo", command=acao_novo)
btn_novo.pack(side="left", padx=2, pady=2)

btn_sair = tk.Button(toolbar, text="Sair", command=acao_sair)
btn_sair.pack(side="left", padx=2, pady=2)

janela.mainloop()