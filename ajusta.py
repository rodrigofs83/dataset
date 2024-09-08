import pandas as pd
#from sklearn.preprocessing import StandardScaler, LabelEncoder

# Passo 1: Ler o arquivo CSV
df = pd.read_csv('ionosphere_data.csv')

# Exibir o dataframe original
print("DataFrame original:")
print(df)

# Passo 2: Trocar as colunas de índice 0 e 10
#colunas = df.columns.tolist()  # Converter as colunas em uma lista
#colunas[0], colunas[1] = colunas[1], colunas[0]  # Trocar as colunas
datasets = pd.read_csv('ionosphere_data.csv',header=None, skiprows=1)
# Passo 2: Trocar as colunas de índice 0 e 10
colunas = datasets.columns.tolist()  # Converter as colunas em uma lista
colunas[0], colunas[34] = colunas[34], colunas[0]  # Trocar as colunas
#label_encoder = LabelEncoder()
#colunas[0] = label_encoder.fit_transform(colunas[0])
# Reorganizar o dataframe com as colunas trocadas
datasets= datasets[colunas]
# Remover espaços em branco de todo o DataFrame (se houver)
#datasets = datasets.dropna(axis=1, how='any')
# Reorganizar o dataframe com as colunas trocadas
df = datasets 

# Exibir o dataframe após a troca
print("\nDataFrame após a troca das colunas 0 e 10:")

print(datasets)
#print(datasets)
# Passo 3: (Opcional) Salvar o dataframe modificado em um novo arquivo CSV
df.to_csv('ionosphere_data1.csv', index=False)
