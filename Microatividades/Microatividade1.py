import pandas as pd
df = pd.read_csv('Online_Retail.csv', sep=';', engine='python', encoding='latin1')
print(df.head())