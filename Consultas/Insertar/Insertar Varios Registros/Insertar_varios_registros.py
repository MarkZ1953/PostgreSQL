import psycopg2

class DB:
    def __init__(self) -> None:
        self.conexion_DB()
        self.fetch_all()
    
    def conexion_DB(self):
        self.my_connection = psycopg2.connect(user="postgres",
        password="admin",
        host = "127.0.0.1",
        port = "5432",
        database = "teste_db")
    
    def fetch_all(self):
        try:
            with self.my_connection:
                with self.my_connection.cursor() as cursor:
                    sentencia = "INSERT INTO persona (nombre,apellido,email) VALUES(%s,%s,%s)"
                    valores = [
                        ('Marcos', 'Cantu', 'mcantu@mail.com'),
                        ('Angel', 'Quintana', 'aquintana@mail.com'),
                        ('Maria', 'Gonzalez', 'mgonzalez@mail.com')
                    ]
                    cursor.executemany(sentencia,valores)
                    registros_insertados = cursor.rowcount
                    print(f"Registros Insertados : {registros_insertados}")
        except Exception as e:
            print(f"Ha ocurrido un error : {e}")
        finally:
            self.my_connection.close()

DB()