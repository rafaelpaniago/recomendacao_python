import pandas as pd
import sqlite3

with open(r'C:\Users\comercial-10\Desktop\RP\TESTE\archive_ec\data.csv', encoding='utf-8', errors='ignore') as file:
    content = file.read()

# Usando o StringIO para ler o csv e armazenar num dataframe

from io import StringIO
csv_data = StringIO(content)

df_base = pd.read_csv(csv_data)
print(df_base.tail())
