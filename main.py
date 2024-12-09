import pandas as pd
import sqlite3

with open(r'C:\Users\comercial-10\Desktop\RP\TESTE\archive_ec\data.csv', encoding='utf-8', errors='ignore') as file:
    content = file.read()

# Usando o StringIO para ler o csv e armazenar num dataframe

from io import StringIO
csv_data = StringIO(content)

df_base = pd.read_csv(csv_data)

# Ajustar nome das colunas

df_base = df_base.rename(columns={'InvoiceNo':'numero_fatura'})
df_base = df_base.rename(columns={'StockCode':'codigo_estoque'})
df_base = df_base.rename(columns={'Description':'descricao'})
df_base = df_base.rename(columns={'Quantity':'quantidade'})
df_base = df_base.rename(columns={'InvoiceDate':'data_fatura'})
df_base = df_base.rename(columns={'UnitPrice':'preco_unidade'})
df_base = df_base.rename(columns={'CustomerID':'id_cliente'})
df_base = df_base.rename(columns={'Country':'nome_pais'})

# Ajustar o tipo de dado

# Isso aqui encontra os valores nulos e transforma em zero. Em seguida muda o tipo de dado para inteiro e depois object.
df_base['id_cliente'] = df_base['id_cliente'].fillna(0).astype('int').astype('object')




