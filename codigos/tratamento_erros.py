import pandas as pd
import leitura_csv as lc

# Carrega o arquivo CSV
df = lc.ler_csv() 

# Colunas categóricas (Strings)
colunas_texto = ['SIGLA', 'CATEGORIA_DA_IES', 'ORGANIZACAO_ACADEMICA', 'SITUACAO_IES', 'NOME_DA_IES', 'MUNICIPIO', 'UF']
for coluna in colunas_texto:
    df[coluna] = df[coluna].replace('', pd.NA).fillna('N/I').str.strip().str.upper()

# Colunas booleanas
booleanas = ['COMUNITARIA', 'CONFESSIONAL', 'FILANTROPICA']
for coluna in booleanas:
    df[coluna] = df[coluna].replace('', pd.NA)  # apenas marca como nulo se vazio
    df[coluna] = df[coluna].map({'S': True, 'N': False, pd.NA: False})  # ou mantenha pd.NA se quiser diferenciar

# Colunas numéricas
colunas_numericas = ['CODIGO_DA_IES', 'CODIGO_MUNICIPIO_IBGE']
for coluna in colunas_numericas:
    df[coluna] = pd.to_numeric(df[coluna], errors='coerce').fillna(-1).astype(int)  # usa -1 como "valor inválido"

# CONVERSÃO DE CAMPOS BOOLEANOS
df['COMUNITARIA'] = df['COMUNITARIA'].map({'S': True, 'N': False})
df['CONFESSIONAL'] = df['CONFESSIONAL'].map({'S': True, 'N': False})
df['FILANTROPICA'] = df['FILANTROPICA'].map({'S': True, 'N': False})

# EXIBIÇÃO FINAL PARA VERIFICAÇÃO
print(df.head())

