import pandas as pd

# Lendo o arquivo CSV
df = pd.read_csv('Online_Retail.csv', sep=';', engine='python', encoding='latin1')

# Exibindo as primeiras 10 linhas
print("Primeiras 10 linhas:")
print(df.head(10))

# Exibindo as últimas 10 linhas
print("\nÚltimas 10 linhas:")
print(df.tail(10))