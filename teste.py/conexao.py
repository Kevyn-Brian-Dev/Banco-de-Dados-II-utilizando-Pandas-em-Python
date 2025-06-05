import psycopg2 


def conectar():
    
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="meu_banco_de_dados",
            user="meu_usuario",
            password="minha_senha"
        )
        return conn
    except psycopg2.Error as e:
        print(f"Erro ao conectar: {e}")
        return None