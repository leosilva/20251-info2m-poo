import tkinter as tk

janela = tk.Tk()
janela.geometry("300x200")

rotulo = tk.Label(
    janela,
    text="Mensagem personalizada",
    font=("Helvetica", 16, "italic"),
    fg="white",
    bg="darkblue"
)

rotulo.pack()
janela.mainloop()