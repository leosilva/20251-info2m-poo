import tkinter as tk

janela = tk.Tk()
opcao = tk.StringVar()
opcao.set("EF")

tk.Radiobutton(janela, text="Ensino Fundamental", variable=opcao, value="EF").pack(anchor='w')
tk.Radiobutton(janela, text="Ensino Médio", variable=opcao, value="EM").pack(anchor='w')
tk.Radiobutton(janela, text="Graduação", variable=opcao, value="G").pack(anchor='w')
tk.Radiobutton(janela, text="Mestrado", variable=opcao, value="M").pack(anchor='w')
tk.Radiobutton(janela, text="Doutorado", variable=opcao, value="D").pack(anchor='w')

janela.mainloop()