import pandas as pd

# Ler o CSV
def ler_csv():
    arquivo = r"C:\Users\Renan\Desktop\Banco-de-Dados-II-utilizando-Pandas-em-Python\base_dados\PDA_Lista_Instituicoes_Ensino_Superior_do_Brasil_EMEC (1).csv"
    df = pd.read_csv(arquivo, sep=None, engine='python', encoding='utf-8')
    return df



