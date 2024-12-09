import pandas as pd
import sqlite3

conn = sqlite3.connect('db_df_base.db')

consulta01 = """
    select * from table_df_base
    limit 12
"""

con01_df = pd.read_sql_query(consulta01, conn)
print(con01_df)