import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carregar banco de dados
df = pd.read_csv('db_analise_ficticio.csv')

# Converte a coluna 'Data' para datetime (formato MM-dd-aa HH-mm-SS)
df['Data'] = pd.to_datetime(df['Data'], format='%m-%d-%y %H-%M-%S')

# Filtra apenas os chamados com status 'Concluido'
df_concluido = df[df['Status'] == 'Concluído']

# Cria uma nova coluna 'MesAno' no formato 'MM-YYYY' para agrupar por mês
df_concluido['MesAno'] = df_concluido['Data'].dt.strftime('%m-%Y')

# Agrupa e conta os chamados concluídos por mês
chamados_por_mes = df_concluido.groupby('MesAno').size()

# Plota o gráfico
plt.figure(figsize=(10, 6))
chamados_por_mes.plot(kind='bar')
plt.title('Chamados Concluídos por Mês')
plt.xlabel('Mês/Ano')
plt.ylabel('Quantidade de Chamados')
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(False)

plt.show()

