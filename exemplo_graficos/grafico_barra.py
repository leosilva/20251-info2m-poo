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


# Criar o gráfico e salvar como imagem PNG
plt.figure(figsize=(10, 8))
# plt.barh(modelos, quantidades, color="skyblue") # grafico de barras horizontal
plt.bar(modelos, quantidades, color="skyblue") # grafico de barras vertical
plt.ylabel("Modelos")
plt.xlabel("Quantidade Vendida")
plt.title("Vendas por Modelo de Carro")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("exemplo_graficos/grafico_vendas.png")
plt.close()

janela = tk.Tk()
janela.title("Gráfico de Vendas - Concessionária")

imagem = tk.PhotoImage(file="exemplo_graficos/grafico_vendas.png")

label_imagem = tk.Label(janela, image=imagem)
label_imagem.pack(padx=10, pady=10)

janela.mainloop()