import tkinter as tk
import json
import matplotlib

# Apenas para o MacOS. COMENTE A PROXIMA LINHA SE USAR O WINDOWS
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt


# Carregar os dados do arquivo JSON
with open("exemplo_graficos/vendas_concessionaria.json", "r") as f:
    dados = json.load(f)


modelos = []
for item in dados["vendas"]:
    modelo = item["modelo"]
    modelos.append(modelo)
    
quantidades = []
for item in dados["vendas"]:
    quantidade = item["quantidade"]
    quantidades.append(quantidade)

# Criar gráfico de linha e salvar como imagem PNG
plt.figure(figsize=(10, 6))
plt.plot(modelos, quantidades, marker='o', linestyle='-', color='blue')
plt.title("Vendas por Modelo de Carro (Gráfico de Linha)")
plt.xlabel("Modelos")
plt.ylabel("Quantidade Vendida")
plt.xticks(rotation=90)
plt.tight_layout()
plt.grid(True)
plt.savefig("exemplo_graficos/grafico_linha_vendas.png")
plt.close()


janela = tk.Tk()
janela.title("Gráfico de Linha - Vendas de Carros")

imagem = tk.PhotoImage(file="exemplo_graficos/grafico_linha_vendas.png")
label = tk.Label(janela, image=imagem)
label.pack(padx=10, pady=10)

janela.mainloop()