from main import df_base
import pandas as pd

# EXPLORAÇÃO
print(df_base.info()) # Exibe informações gerais do DF.
print(df_base.dtypes) # Exibe o tipo de dados das colunas.
print(df_base.head()) # Exibe n linhas iniciais do dataframe.
print(df_base.tail()) # Exibe n linhas finais do dataframe.
print(df_base.shape) # Tupla com número de linhas e colunas.
print(df_base.columns) # Nomes de todas as colunas do dataframe.
print(df_base.index) # Linha inicial, final e o tipo do índice.

# ANÁLISE BÁSICA
print(df_base.nunique()) # Número de valores únicos em cada coluna.
print(df_base['descricao'].unique()) # Valores únicos de uma coluna específica.
print(df_base['descricao'].value_counts()) # Conta a frequência de cada valor na coluna.
print(df_base.describe()) # Estatísticas descritivas colunas numéricas
print(df_base['quantidade'].mean()) # Calcula a média dos valores da coluna.
print(df_base['quantidade'].median()) # Calcula a mediana dos valores.
print(df_base['quantidade'].std()) # Calcula o desvio padrão.
print(df_base['quantidade'].sum()) # Soma valores de uma coluna.
print(df_base.corr()) # Retorna correlação entre colunas numéricas.

# FILTROS BÁSICOS
print(df_base[df_base['quantidade'] > 50]) # Filtra linhas com base numa condição.
print(df_base.sort_values(by='preco_unidade', ascending=False)) # Ordena com base em uma coluna.

# REMOVER VALORES AUSENTES
df_base= df_base.dropna() # Atualiza o DF para não ter valores ausentes, nulos.
df_base['descricao'] = df_base['descricao'].fillna(0) # Troca os valores nulos por zero.


# 4