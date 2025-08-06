import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import ttk

# ======= 1. Carrega os dados =======
df = pd.read_csv('db_analise_ficticio.csv')

# Converte coluna de data
df['Data'] = pd.to_datetime(df['Data'], format='%m-%d-%y %H-%M-%S')

# Filtra os dados
df_concluido = df[df['Status'] == 'Concluído']
df_aberto = df[df['Status'] == 'Aberto'].sort_values(by='Data')

# Agrupa os concluídos por mês
df_concluido['MesAno'] = df_concluido['Data'].dt.strftime('%m-%Y')
chamados_por_mes = df_concluido.groupby('MesAno').size()

# ======= 2. Interface principal =======
root = tk.Tk()
root.title("Painéis de Chamados")
root.geometry("1920x1080")  # Define o tamanho da janela principal
root.configure(bg="white")

# ======= Painel 1: Chamados em aberto (com scroll) =======
frame_painel1 = tk.Frame(root, width=200, height=900, bg='white')
frame_painel1.place(relx=0.10, rely=0.05)  # Posição e tamanho relativo

# Adiciona um canvas e scrollbar para rolagem
canvas = tk.Canvas(frame_painel1, bg='white', width=200, height=900)
scrollbar = ttk.Scrollbar(frame_painel1, orient='vertical', command=canvas.yview)
scrollable_frame = tk.Frame(canvas, bg='white')

# Configura o canvas para usar a barra de rolagem
scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# Adiciona um "card" verde para cada chamado em aberto
for _, row in df_aberto.iterrows():
    card = tk.Frame(scrollable_frame, bg='lightgreen', bd=2, relief='solid', padx=5, pady=5)
    card.pack(pady=5, fill='x', expand=True)

    unidade = tk.Label(card, text=f"Unidade: {row['Unidade']}", bg='lightgreen', anchor='w')
    sala = tk.Label(card, text=f"Sala: {row['Sala']}", bg='lightgreen', anchor='w')
    problema = tk.Label(card, text=f"Problema: {row['Problema']}", bg='lightgreen', anchor='w')
    data = tk.Label(card, text=f"Data: {row['Data'].strftime('%d/%m/%Y %H:%M')}", bg='lightgreen', anchor='w')

    unidade.pack(anchor='w')
    sala.pack(anchor='w')
    problema.pack(anchor='w')
    data.pack(anchor='w')

# ======= Painel 2: Gráfico de barras dos concluídos =======
frame_painel2 = tk.Frame(root, width=100, height=500, bg='white')
frame_painel2.place(relx=0.25, rely=0.05)

fig, ax = plt.subplots(figsize=(14, 6))

# Adiciona apenas a grid lateral (eixo Y)
ax.yaxis.grid(True, color='gold', linestyle='--', linewidth=0.5)
ax.xaxis.grid(False)  # Desativa a grid no eixo X

ax.bar(chamados_por_mes.index, chamados_por_mes.values, color='black')
ax.set_title('Chamados Concluídos por Mês')
ax.set_xlabel('Mês/Ano')
ax.set_ylabel('Quantidade')
ax.set_facecolor('white')
fig.patch.set_facecolor('white')
plt.xticks(rotation=45)

# ======= Painel 3 - Chamados Pendentes com rolagem horizontal =======

# Criação do frame externo (Painel 3)
painel3 = tk.Frame(root, width=780, height=455, bg='white')
painel3.place(relx=0.30, rely=0.78)  # posicionado abaixo do painel 2

# Canvas e scrollbar horizontal
canvas_painel3 = tk.Canvas(painel3, bg='white', width=1200, height=150) # Tamanho do quadro
scrollbar_x = tk.Scrollbar(painel3, orient='horizontal', command=canvas_painel3.xview) # Barra de rolagem do quadro
canvas_painel3.configure(xscrollcommand=scrollbar_x.set)
scrollable_frame3 = tk.Frame(canvas_painel3, bg='white')

# Configura o canvas para usar a barra de rolagem
scrollable_frame3.bind(
    "<Configure>",
    lambda e: canvas_painel3.configure(scrollregion=canvas_painel3.bbox("all"))
)

canvas_window = canvas_painel3.create_window((0, 0), window=scrollable_frame3, anchor="nw")
canvas.configure(xscrollcommand=scrollbar.set)

canvas_painel3.pack(side="top", fill="both", expand=True)
scrollbar_x.pack(side="bottom", fill="x")

# === Inserção dos cards com status "pendente"
pendentes = df[df['Status'].str.lower() == 'pendente']  # Filtro

# Ordena por data/hora mais antiga
pendentes = pendentes.sort_values(by='Data')

for index, row in pendentes.iterrows():
    card = tk.Frame(scrollable_frame3, bg='gold', bd=2, relief='solid', padx=10, pady=5)
    card.pack(side='left', padx=10, pady=10)

    # Exibe informações
    tk.Label(card, text=f"Unidade: {row['Unidade']}", bg='gold', anchor='w').pack()
    tk.Label(card, text=f"Sala: {row['Sala']}", bg='gold', anchor='w').pack()
    tk.Label(card, text=f"Problema: {row['Problema']}", bg='gold', anchor='w').pack()
    tk.Label(card, text=f"Data: {row['Data']}", bg='gold', anchor='w').pack()

# Embeda o gráfico no Tkinter
canvas_fig = FigureCanvasTkAgg(fig, master=frame_painel2)
canvas_fig.draw()
canvas_fig.get_tk_widget().pack(fill='both', expand=True)
root.mainloop()