import pandas as pd
from funcoesNormativas import verificar_linhas_nulas,ler_esquema_original

df = pd.read_csv(r"C:\\Users\\kevyn\\OneDrive\\Área de Trabalho\\Pandas\\PDA_Lista_Instituicoes_Ensino_Superior_do_Brasil_EMEC (1).csv")

print(ler_esquema_original(df))
#print(verificar_linhas_nulas(df))





























#Identificação do esquema original
#Tratamento de dados não-conformes (nulos, inconsistentes)
#Popular um banco relacional com um esquema mais elaborado (tentem normalizar a base)
#Desmembramento do esquema (ocorrências de endereços podem ser armazenadas em tabelas à parte)
#Padronização de dados (separar dados de endereços em colunas)
#Identificação de sinônimos com completude distinta de informação (conforme o exemplo dado em sala da cefaleia e dor de cabeça)