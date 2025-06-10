import pandas as pd

# Carregando os dados
df_tratado = pd.read_csv(r"C:\\Users\\Renan\\Desktop\\Banco-de-Dados-II-utilizando-Pandas-em-Python\\base_dados\\df_auxiliar.csv")

# Menu
def menu():
    while True:
        print("\n==== MENU - ANÁLISE DE INSTITUIÇÕES DE ENSINO ====")
        print("1 - Ver valores nulos por coluna")
        print("2 - Listar instituições Extintas")
        print("3 - Listar instituições Em Atividade")
        print("4 - Contagem por estado (UF)")
        print("5 - Total por situação (Em Atividade, Extinta)")
        print("6 - Buscar IES por sigla")
        print("7 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("\n Valores nulos por coluna:\n")
            print(df_tratado.isnull().sum())

        elif opcao == "2":
            print("\n Instituições extintas:\n")
            print(df_tratado[df_tratado['SITUACAO_IES'] == 'Extinta'][['NOME_DA_IES', 'UF', 'MUNICIPIO']].head(10))

        elif opcao == "3":
            print("\n Instituições Em Atividade:\n")
            print(df_tratado[df_tratado['SITUACAO_IES'] == 'Em Atividade'][['NOME_DA_IES', 'UF', 'MUNICIPIO']].head(10))
            
        elif opcao == "4":
            print("\n Quantidade de IES por estado (UF) :\n")
            df_filtrado_uf = df_tratado[df_tratado['UF'] != 'NÃO INFORMADO']
            print(df_filtrado_uf['UF'].value_counts())

        elif opcao == "5":
            print("\n Total por situação institucional:\n")
            print(df_tratado['SITUACAO_IES'].value_counts())

        elif opcao == "6":
            sigla = input("Digite a sigla da instituição: ").strip().upper()
            resultado = df_tratado[df_tratado['SIGLA'] == sigla]
            if resultado.empty:
                print(f"\nNenhuma instituição encontrada com a sigla '{sigla}'\n")
            else:
                print(f"\nInstituições com a sigla '{sigla}':\n")
                print(resultado[['NOME_DA_IES', 'UF', 'MUNICIPIO']])

        elif opcao == "7":
            print("Saindo...")
            break

        else:
            print("Opção inválida, tente novamente.")

# Executar menu
if __name__ == "__main__":
    menu()
