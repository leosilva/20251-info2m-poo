import tkinter as tk

def mostrar_nome():
    nome = entrada.get()
    rotulo_resultado.config(text=f"Olá, {nome}!")

janela = tk.Tk()
janela.title("Saudação")
janela.geometry("300x150")

# Campo de entrada
entrada = tk.Entry(janela)
entrada.pack(pady=10)

# Botão
botao = tk.Button(janela, text="Exibir Nome", command=mostrar_nome)
botao.pack()

# Rótulo de saída
rotulo_resultado = tk.Label(janela, text="")
rotulo_resultado.pack(pady=10)

janela.mainloop()