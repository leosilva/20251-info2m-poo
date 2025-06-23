import tkinter as tk
from tkinter import ttk


def exibir_dados():
    print("usuario:", entry_usuario.get())
    print("interesses:")
    print("prog: ", var_check_interesses_prog.get())
    print("bd: ", var_check_interesses_bd.get())
    print("man: ", var_check_interesses_man.get())
    print("redes: ", var_check_interesses_redes.get())
    print("genero: ", opcao.get())
    print("linguagens:")
    for index in listbox_linguagens.curselection():
        print(listbox_linguagens.get(index))
    print("experiencia: ", combobox_experiencia.get())


janela = tk.Tk()
janela.title("Cadastro de Participante")
janela.geometry("500x500")

frame = tk.Frame(janela)
frame.pack(anchor="center")

tk.Label(frame, text="Nome:").grid(row=0, column=0, padx=5, pady=5, sticky='E')
entry_usuario = tk.Entry(frame, width=30)
entry_usuario.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame, text="Interesses:").grid(row=1, column=0, padx=5, pady=5, sticky='E')
var_check_interesses_prog = tk.BooleanVar()
var_check_interesses_bd = tk.BooleanVar()
var_check_interesses_man = tk.BooleanVar()
var_check_interesses_redes = tk.BooleanVar()
check_interesses_prog = tk.Checkbutton(frame, text="Programação", variable=var_check_interesses_prog)
check_interesses_bd = tk.Checkbutton(frame, text="Banco de Dados", variable=var_check_interesses_bd)
check_interesses_man = tk.Checkbutton(frame, text="Manutenção", variable=var_check_interesses_man)
check_interesses_redes = tk.Checkbutton(frame, text="Redes", variable=var_check_interesses_redes)
check_interesses_prog.grid(row=1, column=1, padx=5, pady=5, sticky='W')
check_interesses_bd.grid(row=2, column=1, padx=5, pady=5, sticky='W')
check_interesses_man.grid(row=3, column=1, padx=5, pady=5, sticky='W')
check_interesses_redes.grid(row=4, column=1, padx=5, pady=5, sticky='W')

opcao = tk.StringVar()
opcao.set("M")

tk.Label(frame, text="Gênero:").grid(row=5, column=0, padx=5, pady=5, sticky='E')
radio_masc = tk.Radiobutton(frame, text="Masculino", variable=opcao, value="M")
radio_masc.grid(row=5, column=1, padx=5, pady=5, sticky='W')
radio_fem = tk.Radiobutton(frame, text="Feminino", variable=opcao, value="F")
radio_fem.grid(row=6, column=1, padx=5, pady=5, sticky='W')
radio_outro = tk.Radiobutton(frame, text="Outro", variable=opcao, value="O")
radio_outro.grid(row=7, column=1, padx=5, pady=5, sticky='W')

tk.Label(frame, text="Linguagens Favoritas:").grid(row=8, column=0, padx=5, pady=5, sticky='NE')
listbox_linguagens = tk.Listbox(frame, selectmode="extended", height=6)
listbox_linguagens.grid(row=8, column=1, padx=5, pady=5, sticky='W')

linguagens = ["Python", "Java", "C++", "JavaScript", "Ruby"]

for item in linguagens:
    listbox_linguagens.insert(tk.END, item)
    
    
tk.Label(frame, text="Experiência em Programação:").grid(row=9, column=0, padx=5, pady=5, sticky='E')
opcoes_experiencia = ["Iniciante", "Intermediário", "Avançado"]
combobox_experiencia = ttk.Combobox(frame, values=opcoes_experiencia)
combobox_experiencia.grid(row=9, column=1, padx=5, pady=5, sticky='W')

combobox_experiencia.set("Iniciante")

button = tk.Button(frame, text="Enviar", command=exibir_dados)
button.grid(row=10, column=0, padx=5, pady=5, columnspan=2)

janela.mainloop()