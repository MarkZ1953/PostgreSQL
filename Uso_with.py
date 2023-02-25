import psycopg2

class DB:
    def __init__(self) -> None:
        self.conexion_DB()
        self.uso_with()

    def conexion_DB(self):
        self.my_connection = psycopg2.connect(user="postgres",
        password="admin",
        host = "127.0.0.1",
        port = "5432",
        database = "teste_db")
    
    def uso_with(self):
        try:
            with self.my_connection.cursor() as cursor:
                sentencia = "SELECT * FROM persona"
                cursor.execute(sentencia)
                registros = cursor.fetchall()
                print(registros)
        except Exception as e:
            print(f"Ha ocurrido un error : {e}")
        finally:
            self.my_connection.close()

DB()