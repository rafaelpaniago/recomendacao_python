from main import df_base
import pandas as pd





















































# EXPLORAÇÃO DE DADOS
# Exibir informações gerais do df_base
print(df_base.info())

# Exibir tipo de dados das colunas.
print(df_base.dtypes)

# Exibe n linhas iniciais do dataframe.
print(df_base.head())

# Exibe n linhas finais do dataframe.
print(df_base.tail())

# Tupla com número de linhas e colunas.
print(df_base.shape)

# Nomes de todas as colunas do dataframe.
print(df_base.columns)

# Linha inicial, final e o tipo do índice.
print(df_base.index)

# ---- ANÁLISE BÁSICA

# Número de valores únicos em cada coluna.
print(df_base.nunique())

# Valores únicos de uma coluna específica.
print(df_base['descricao'].unique())

# Conta a frequência de cada valor na coluna.
print(df_base['descricao'].value_counts())

# Estatísticas descritivas colunas numéricas
print(df_base.describe())

# Calcula a média dos valores da coluna.
print(df_base['quantidade'].mean())

# Calcula a mediana dos valores.
print(df_base['quantidade'].median())

# Calcula o desvio padrão.
print(df_base['quantidade'].std())

# Soma valores de uma coluna.
print(df_base['quantidade'].sum())

# Retorna correlação entre colunas numéricas.
print(df_base.corr())

# ---- FILTROS BÁSICOS

# Filtra linhas com base em uma condição.
print(df_base[df_base['quantidade'] > 50])

# Ordena o dataframe com base em uma coluna.
print(df_base.sort_values(by='preco_unidade', ascending=False))

# ---- REMOVER VALORES AUSENTES (not available)

# Atualiza o dataframe para não ter valores ausentes, nulos.
df_base = df_base.dropna()

# Troca valores nulos por outro valor
df_base['descricao'] = df_base['descricao'].fillna(0)