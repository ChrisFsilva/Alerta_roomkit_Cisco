import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

# ======= Carregar os dados =======
df = pd.read_csv('db_analise_ficticio.csv')
df['Data'] = pd.to_datetime(df['Data'], format='%m-%d-%y %H-%M-%S')

# ======= Filtrar os dados =======
df_aberto = df[df['Status'] == 'Em aberto']
df_concluido = df[df['Status'] == 'Concluído']

# Agrupar por mes/ano para o gráfico
df_concluido['MesAno'] = df_concluido['Data'].dt.strftime('%m-%Y')
chamados_por_mes = df_concluido.groupby('MesAno').size()

# ======= Criar a figura com GridSpec =======
fig = plt.figure(figsize=(16, 9), facecolor='white')
gs = gridspec.GridSpec(100, 100, figure=fig)  # Grid 100x100 para proporções flexíveis

# ======= Painel 1 Tabela lateral =======
ax1 = fig.add_subplot(gs[5:95, 0:30])
ax1.set_facecolor('#e0ffe0')
#ax1.axis('off')

# Garantir consistência do status
df_aberto = df[df['Status'] == 'Aberto']

# Garantir que o campo 'Data' está em datetime
df_aberto['Data'] = pd.to_datetime(df_aberto['Data'], errors='coerce')
df_aberto = df_aberto.sort_values('Data')

# Verifica se há dados
if df_aberto.empty:
    ax1.text(0.5, 0.5, "Nenhum chamado em aberto", ha='center', va='center', fontsize=12, color='gray')
else:
    y_position = 1.0
    card_spacing = 0.14  # Tamanho vertical entre os cards

    for _, row in df_aberto.iterrows():
        unidade = row.get('Unidade', 'N/A')
        sala = row.get('Sala', 'N/A')
        problema = row.get('Problema', 'N/A')
        data = row['Data']
        data_str = data.strftime('%d/%m/%Y %H:%M') if pd.notnull(data) else 'Data inválida'

        texto_card = (
            f"📍 Unidade: {unidade}\n"
            f"🛠 Sala: {sala}\n"
            f"❗ Problema: {problema}\n"
            f"📅 Data: {data_str}"
        )

        ax1.text(
            0.02, y_position, texto_card,
            verticalalignment='top',
            fontsize=9,
            bbox=dict(boxstyle="round,pad=0.5", facecolor='lightgreen', edgecolor='green'),
            fontfamily='monospace'
        )

        y_position -= card_spacing


# Texto com os dados em aberto
# texto = '\n'.join(f"{row['Data'].strftime('%m-%d-%y %H:%M:%S')} - {row['Status']}" for _, row in df_aberto.iterrows())
# ax1.text(0, 1, f"Chamados em aberto:\n\n{texto}", verticalalignment='top', fontsize=9, color='black')

# ======= Painel 2 Grafico =======
ax2 = fig.add_subplot(gs[0:65, 35:100])  # 65% altura, 65% largura
ax2.set_facecolor('white')
chamados_por_mes.plot(kind='bar', ax=ax2, color='black')

# Customizacoes
ax2.set_title('Chamados Concluídos por Mês')
ax2.set_xlabel('Mês/Ano')
ax2.set_ylabel('Quantidade de Chamados')
ax2.set_xticklabels(ax2.get_xticklabels(), rotation=45)
ax2.tick_params(axis='y')
ax2.grid(False)

# ======= Painel 3 – Futuro conteúdo =======
ax3 = fig.add_subplot(gs[70:100, 35:100])  # 30% altura, 65% largura
ax3.set_facecolor('#f0f0f0')
ax3.set_title('Painel 3 (Reservado)', fontsize=10)
#x3.axis('off')

# ======= 7. Ajustar layout e exibir =======
plt.tight_layout()
plt.show()