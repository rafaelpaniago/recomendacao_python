## Importar DF do arquivo main
from main import df_base

df_base_new = df_base.dropna()
print(df_base_new.info())

# O dataframe sem valores nulos é df_base_new

