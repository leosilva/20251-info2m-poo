import tkinter as tk

janela = tk.Tk()

# Frame superior com grid
frame_formulario = tk.Frame(janela)
frame_formulario.pack()

tk.Label(frame_formulario, text="Nome:").grid(row=0, column=0)
tk.Entry(frame_formulario).grid(row=0, column=1)

# Frame inferior com pack
frame_botoes = tk.Frame(janela)
frame_botoes.pack(pady=10)

tk.Button(frame_botoes, text="Salvar").pack(side="left", padx=5)
tk.Button(frame_botoes, text="Cancelar").pack(side="right", padx=5)

janela.mainloop()