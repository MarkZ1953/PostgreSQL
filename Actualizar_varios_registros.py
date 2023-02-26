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
                    sentencia = "UPDATE persona SET nombre=%s,apellido=%s,email = %s WHERE id_persona=%s"
                    valores = (
                        ("David Felipe","Castro","castrolopez.davidfelipe@gmail.com",1),
                        ("Ivonne","Gutierrez","ivonneg@gmail.com",2),
                        ("Juan Pablo","Gonzales","pablog@gmail.com",3)
                    )
                    cursor.executemany(sentencia,valores)
                    registros_actualizados = cursor.rowcount
                    print(f"Registros Actualizados : {registros_actualizados}")
        except Exception as e:
            print(f"Ha ocurrido un error : {e}")
        finally:
            self.my_connection.close()

DB()