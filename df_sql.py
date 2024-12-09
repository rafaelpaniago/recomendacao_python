from main import df_base
import sqlite3

conn = sqlite3.connect('db_df_base.db')
df_base.to_sql('table_df_base', conn, index=False, if_exists='replace')