import psycopg2

def get_connection():
    try:
        connection = psycopg2.connect(
            host="localhost",
            user="postgres",
            password="admin",
            database="Restaurante"
        )
        return connection
    except Exception as e:
        print(f"Error de conexión: {e}")
        return None


