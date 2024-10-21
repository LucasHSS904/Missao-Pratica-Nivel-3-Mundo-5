import pandas as pd

# Leia o arquivo CSV, adicione separador e encoding, se necessário
df = pd.read_csv('Online_Retail.csv', sep=';', encoding='utf-8', engine='python')

# Verifique as informações gerais
print(df.info())

# Exiba as primeiras e últimas linhas
print(df.head())
print(df.tail())

#Criar uma cópia do conjunto de dados:
df_copy = df.copy()

#Substituir valores nulos na coluna 'Calories' por 0:
df_copy['Country'].fillna(0, inplace=True)
print(df_copy)

#Substituir valores nulos na coluna 'Date' por '1900/01/01':
df_copy['InvoiceDate'].fillna('1900/01/01', inplace=True)
print(df_copy)

#Transformar a coluna 'Date' para datetime:
df_copy['InvoiceDate'] = pd.to_datetime(df_copy['InvoiceDate'], errors='coerce', format='%Y/%m/%d')
print(df_copy)

#Lidar com o erro de data '20201226':
df_copy['InvoiceDate'] = df_copy['InvoiceDate'].replace('20201226', pd.NaT)
df_copy['InvoiceDate'] = pd.to_datetime(df_copy['InvoiceDate'], errors='coerce')
print(df_copy)

#Remover registros com valores nulos na coluna 'Date':
df_cleaned = df_copy.dropna(subset=['InvoiceDate'])
print(df_cleaned)