from tkinter import messagebox


def exibir_mensagem(resultado, msg_sucesso, msg_erro):
    """
    Exibe uma mensagem de sucesso ou erro em uma caixa de diálogo.
    """
    if resultado:
        messagebox.showinfo("Sucesso!", msg_sucesso)
    else:
        messagebox.showerror("Erro!", msg_erro)