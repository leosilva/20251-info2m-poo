import tkinter as tk

janela = tk.Tk()
var = tk.IntVar()

check = tk.Checkbutton(janela, text="Receber atualizações", variable=var)
check.pack()

janela.mainloop()