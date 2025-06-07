import psycopg2 

def conectar():
    
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="ensino_superior",
            user="postgres",
            password="@renan123"
        )
        print("Conexão realizada com sucesso!")
        return conn
    except psycopg2.Error as e:
        print(f"Erro ao conectar: {e}")
        return None
    
if __name__ == "__main__":
    conectar()