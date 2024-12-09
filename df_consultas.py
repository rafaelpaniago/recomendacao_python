import pandas as pd
import sqlite3

conn = sqlite3.connect('db_df_base.db')


# CONSULTA 01 -> 10 PRODUTOS MAIS VENDIDOS

# consulta01 = """
#     select descricao, sum(quantidade) as total_vendido
#     from table_df_base
#     group by descricao
#     order by total_vendido DESC
#     limit 10
# """

# con01_df = pd.read_sql_query(consulta01, conn)
# print(con01_df)


#----------------------------------------------------

# CONSULTA 02 -> PAÍS COM MAIOR NÚMERO DE CLIENTES

consulta02 = """
    select nome_pais, count(distinct id_cliente) as total_clientes_unicos
    from table_df_base
    group by nome_pais
    order by total_clientes_unicos desc
    limit 10
"""

con02_df = pd.read_sql_query(consulta02, conn)
print(con02_df)