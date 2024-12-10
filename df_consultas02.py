import pandas as pd
import sqlite3

conn = sqlite3.connect('db_df_base.db')

# CONSULTA 03 -> MÉDIA DO VALOR TOTAL DE VENDA POR PAÍS

# consulta03 = """
#     select nome_pais, avg(quantidade * preco_unidade) as media_vendas
#     from table_df_base
#     group by nome_pais
#     order by media_vendas desc
# """

# con03_df = pd.read_sql_query(consulta03, conn)
# print(con03_df)

#----------------------------------------------------

# CONSULTA 04 -> FATURAMENTO MENSAL

consulta04 = """
    select strftime('%Y-%m', data_fatura) as mes_ano, sum(quantidade * preco_unidade) as faturamento_mensal
    from table_df_base
    group by mes_ano
    order by faturamento_mensal desc
"""

con04_df = pd.read_sql_query(consulta04, conn)
print(con04_df)