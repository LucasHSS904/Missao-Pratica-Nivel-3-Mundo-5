import pandas as pd

# Lendo o arquivo CSV
df = pd.read_csv('Online_Retail.csv', sep=';', engine='python', encoding='latin1')

# Configurando o número máximo de linhas a serem exibidas
pd.set_option('display.max_rows', 9999)

# Exibindo o conjunto de dados completo
print(df.to_string())