import pandas as pd
import numpy as np

# imprime as primeiras linhas
# imprime informações sobre as colunas e tipos de dados
def ler_esquema_original(df):
    print(df.head())  
    print(df.info())  
    print(df.describe())  



# o Dataframe é passado como parâmetro da função e verifica a coluna e modifica pelo "valor passado"
def preencher_campos_vazios(df, coluna, valor):

    df[coluna] = df[coluna].fillna(valor)
    return df



#Descreve quais linhas com Células nulas e retorna esses dados
def verificar_linhas_nulas(df):
    
    return df[df.isnull().any(axis=1)]