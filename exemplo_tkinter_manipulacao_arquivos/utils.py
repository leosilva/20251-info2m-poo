from tkinter import messagebox


def exibir_mensagem(resultado, msg_sucesso, msg_erro):
    if resultado:
        messagebox.showinfo("Sucesso!", msg_sucesso)
    else:
        messagebox.showerror("Erro!", msg_erro)