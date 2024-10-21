import pandas as pd

# Lendo o arquivo CSV da Microatividade 1
df = pd.read_csv('Online_Retail.csv', sep=';', engine='python', encoding='latin1')

# Criando um subconjunto de dados com 3 colunas: 'ID', 'Date', 'Calories'
subconjunto = df[['CustomerID', 'InvoiceDate', 'Country']]

# Exibindo o subconjunto de dados
print(subconjunto)