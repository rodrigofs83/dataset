import pandas as pd

# Passo 1: Ler o arquivo CSV
df = pd.read_csv('data.csv')

# Exibir o dataframe original
print("DataFrame original:")
print(df)

# Passo 2: Trocar as colunas de índice 0 e 10
colunas = df.columns.tolist()  # Converter as colunas em uma lista
colunas[0], colunas[1] = colunas[1], colunas[0]  # Trocar as colunas

# Reorganizar o dataframe com as colunas trocadas
df = df[colunas]

# Exibir o dataframe após a troca
print("\nDataFrame após a troca das colunas 0 e 10:")
print(df)

# Passo 3: (Opcional) Salvar o dataframe modificado em um novo arquivo CSV
df.to_csv('data1.csv', index=False)
