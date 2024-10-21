import pandas as pd

# Lendo o arquivo CSV
df = pd.read_csv('Online_Retail.csv', sep=';', engine='python', encoding='latin1')

# Exibindo informações gerais sobre o conjunto de dados
print("Informações gerais sobre o conjunto de dados:")
df.info()