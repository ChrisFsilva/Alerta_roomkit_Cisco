import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import customtkinter as ctk
import tkinter as tk

# ======= Configuração inicial do CustomTkinter =======
ctk.set_appearance_mode("dark")  # ou "light"
ctk.set_default_color_theme("blue")

# ======= Janela principal =======
root = ctk.CTk()
root.title("Painéis de Chamados")
root.geometry("1920x1080")
root.configure(fg_color="#3c3c3c")

# ======= Carrega os dados inicialmente =======
df = pd.read_csv('db_analise_ficticio.csv')
df['Data'] = pd.to_datetime(df['Data'], format='%m-%d-%y %H-%M-%S')

df_concluido = df[df['Status'] == 'Concluído']
df_aberto = df[df['Status'] == 'Aberto'].sort_values(by='Data')
df_concluido['MesAno'] = df_concluido['Data'].dt.strftime('%m-%Y')
chamados_por_mes = df_concluido.groupby('MesAno').size()

# ======= Painel 1: Chamados em aberto =======

frame_painel1 = ctk.CTkFrame(root, width=275, height=815, corner_radius=10)
frame_painel1.place(relx=0.10, rely=0.05)
ctk.CTkLabel(frame_painel1, 
             text="Solicitando atendimento", 
             font=("Arial", 16, "bold")
             ).pack(pady=10)

canvas1 = tk.Canvas(frame_painel1, 
                    bg='#515151', 
                    width=220, 
                    height=815, 
                    highlightthickness=0)

scrollbar1 = tk.Scrollbar(frame_painel1, 
                          orient='vertical', 
                          command=canvas1.yview)

scrollable_frame1 = ctk.CTkFrame(canvas1, 
                                 fg_color="#515151")

scrollable_frame1.bind("<Configure>", lambda e: canvas1.configure(scrollregion=canvas1.bbox("all")))
canvas1.create_window((0, 0), 
                      window=scrollable_frame1, 
                      anchor="nw")
canvas1.configure(yscrollcommand=scrollbar1.set)
canvas1.pack(side="left", 
             fill="both", 
             expand=True)
scrollbar1.pack(side="right", fill="y")

for _, row in df_aberto.iterrows():
    card = ctk.CTkFrame(scrollable_frame1, fg_color="#ff5c5c", corner_radius=10)
    card.pack(pady=5, padx=10, fill="x")
    ctk.CTkLabel(card, 
                 text=f"Unidade: {row['Unidade']}", 
                 anchor='w', 
                 text_color="black"
                 ).pack(anchor='w', 
                        padx=10)
    
    ctk.CTkLabel(card, 
                 text=f"Sala: {row['Sala']}", 
                 anchor='w', 
                 text_color="black"
                 ).pack(anchor='w', 
                        padx=10)
    
    ctk.CTkLabel(card, 
                 text=f"Problema: {row['Problema']}", 
                 anchor='w', 
                 text_color="black"
                 ).pack(anchor='w', 
                        padx=10)
    
    ctk.CTkLabel(card, 
                 text=f"Data: {row['Data'].strftime('%d/%m/%Y %H:%M')}", 
                 anchor='w', text_color="black"
                 ).pack(anchor='w', 
                        padx=10)

# ======= Painel 2: Gráfico de chamados concluídos por mês =======

frame_painel2 = ctk.CTkFrame(root, width=1000, height=600)
frame_painel2.place(relx=0.25, rely=0.05)

fig, ax = plt.subplots(figsize=(10, 5.8))
ax.bar(chamados_por_mes.index, chamados_por_mes.values, color='gold')
ax.set_title('Chamados Concluídos por Mês', color="white", weight="bold", pad=13)
ax.set_xlabel('Mês/Ano', color="white")
ax.set_ylabel('Quantidade', color="white")
ax.set_facecolor('#515151')
fig.patch.set_facecolor('#515151')
ax.yaxis.grid(True, color='#515151', linestyle='--', linewidth=0.3)
ax.xaxis.grid(False)
plt.setp(ax.get_xticklabels(), rotation=45, color="white")

canvas_fig = FigureCanvasTkAgg(fig, master=frame_painel2)
canvas_fig.draw()
canvas_fig.get_tk_widget().pack(fill='both', expand=True)

# ======= Painel 3: Chamados Pendentes com rolagem horizontal =======
painel3 = ctk.CTkFrame(root, width=1000, height=300, corner_radius=10, fg_color="black")
painel3.place(relx=0.25, rely=0.65)

ctk.CTkLabel(painel3, text="Chamados em atendimento", 
             font=("Arial", 16, "bold"),
             corner_radius=6, 
             text_color="white"
             ).pack(pady=(10, 5))

canvas3 = tk.Canvas(painel3, bg="#515151", width=1000, height=200, highlightthickness=0)
scrollbar_x = tk.Scrollbar(painel3, orient='horizontal', command=canvas3.xview)
scrollable_frame3 = ctk.CTkFrame(canvas3, fg_color="#515151")

scrollable_frame3.bind("<Configure>", lambda e: canvas3.configure(scrollregion=canvas3.bbox("all")))
canvas3.create_window((0, 0), window=scrollable_frame3, anchor="nw")
canvas3.configure(xscrollcommand=scrollbar_x.set)
canvas3.pack(side="top", fill="both", expand=True)
scrollbar_x.pack(side="bottom", fill="x")

pendentes = df[df['Status'].str.lower() == 'pendente'].sort_values(by='Data')
for row in pendentes.itertuples():
    card = ctk.CTkFrame(scrollable_frame3, fg_color="#FFD700", corner_radius=10)
    card.pack(side='left', padx=10, pady=10)

    ctk.CTkLabel(card, 
                 text=f"Unidade: {row.Unidade}", 
                 anchor='w', 
                 text_color="black"
                 ).pack(anchor="w", 
                        padx=10)
    
    ctk.CTkLabel(card, 
                 text=f"Sala: {row.Sala}", 
                 anchor='w', 
                 text_color="black"
                 ).pack(anchor="w", 
                        padx=10)
    
    ctk.CTkLabel(card, 
                 text=f"Problema: {row.Problema}", 
                 anchor='w', 
                 text_color="black"
                 ).pack(anchor="w", 
                        padx=10)
    
    ctk.CTkLabel(card, 
                 text=f"Data: {row.Data.strftime('%d/%m/%Y %H:%M')}", 
                 anchor='w', 
                 text_color="black"
                 ).pack(anchor="w", 
                        padx=10)

# ======= Função de atualização automática =======

def atualizar_dados():
    global df_aberto, df_concluido, chamados_por_mes

    try:
        df_novo = pd.read_csv('db_analise_ficticio.csv')
        df_novo['Data'] = pd.to_datetime(df_novo['Data'], format='%m-%d-%y %H-%M-%S')

        df_aberto = df_novo[df_novo['Status'] == 'Aberto'].sort_values(by='Data')
        df_concluido = df_novo[df_novo['Status'] == 'Concluído']
        df_concluido['MesAno'] = df_concluido['Data'].dt.strftime('%m-%Y')
        chamados_por_mes = df_concluido.groupby('MesAno').size()
        pendentes = df_novo[df_novo['Status'].str.lower() == 'pendente'].sort_values(by='Data')

        # Atualiza painel 1
        for widget in scrollable_frame1.winfo_children():
            widget.destroy()
        for _, row in df_aberto.iterrows():
            card = ctk.CTkFrame(scrollable_frame1, fg_color="#ff5c5c", corner_radius=10)
            card.pack(pady=5, padx=10, fill="x")
            ctk.CTkLabel(card, 
                         text=f"Unidade: {row['Unidade']}", 
                         anchor='w', 
                         text_color="black"
                         ).pack(anchor='w', 
                                padx=10)
            
            ctk.CTkLabel(card, 
                         text=f"Sala: {row['Sala']}", 
                         anchor='w', 
                         text_color="black"
                         ).pack(anchor='w', 
                                padx=10)
            
            ctk.CTkLabel(card, 
                         text=f"Problema: {row['Problema']}", 
                         anchor='w', 
                         text_color="black"
                         ).pack(anchor='w', 
                                padx=10)
            
            ctk.CTkLabel(card, 
                         text=f"Data: {row['Data'].strftime('%d/%m/%Y %H:%M')}", 
                         anchor='w', 
                         text_color="black"
                         ).pack(anchor='w', 
                                padx=10)

        # Atualiza gráfico (painel 2)
        
        ax.clear()
        ax.bar(chamados_por_mes.index, chamados_por_mes.values, color='gold')
        ax.set_title('Chamados Concluídos por Mês', color="white", weight="bold", pad=13)
        ax.set_xlabel('Mês/Ano', color="white")
        ax.set_ylabel('Quantidade', color="white")
        ax.set_facecolor('#515151')
        fig.patch.set_facecolor('#515151')
        ax.yaxis.grid(True, color='#515151', linestyle='--', linewidth=0.3)
        ax.xaxis.grid(False)
        plt.setp(ax.get_xticklabels(), rotation=45, color="white")
        canvas_fig.draw()

        # Atualiza painel 3
        for widget in scrollable_frame3.winfo_children():
            widget.destroy()
        for row in pendentes.itertuples():
            card = ctk.CTkFrame(scrollable_frame3, fg_color="#FFD700", corner_radius=10)
            card.pack(side='left', padx=10, pady=10)
            ctk.CTkLabel(card, 
                         text=f"Unidade: {row.Unidade}", 
                         anchor='w', 
                         text_color="black"
                         ).pack(anchor="w", 
                                padx=10)
            
            ctk.CTkLabel(card, 
                         text=f"Sala: {row.Sala}", 
                         anchor='w', 
                         text_color="black"
                         ).pack(anchor="w", 
                                padx=10)
            
            ctk.CTkLabel(card, 
                         text=f"Problema: {row.Problema}", 
                         anchor='w', 
                         text_color="black"
                         ).pack(anchor="w", 
                                padx=10)
            
            ctk.CTkLabel(card, 
                         text=f"Data: {row.Data.strftime('%d/%m/%Y %H:%M')}", 
                         anchor='w', 
                         text_color="black"
                         ).pack(anchor="w", 
                                padx=10)

    except Exception as e:
        print(f"Erro ao atualizar dados: {e}")

    root.after(30000, atualizar_dados)  # Atualiza novamente em 30 segundos

# ======= Inicia a primeira atualização programada =======
root.after(1000, atualizar_dados)

# ======= Mainloop =======
root.mainloop()
