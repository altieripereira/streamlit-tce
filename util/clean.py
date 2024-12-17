import pandas as pd

# Carregar o arquivo CSV
df = df_data = pd.read_csv("datasets/despesa_2024.csv", encoding="cp1252", encoding_errors='ignore', sep=';')
df_limpo = df.dropna()

df_limpo = df.head(3000)

df_limpo.to_csv('despesa_2024_clear.csv', encoding="cp1252", index=False)

print("Arquivo reduzido salvo com sucesso!")
