import psycopg2

class DB:
    def __init__(self) -> None:
        self.conexion_DB()
        self.delete()
    
    def conexion_DB(self):
        self.my_connection = psycopg2.connect(user="postgres",
        password="admin",
        host = "127.0.0.1",
        port = "5432",
        database = "teste_db")
    
    def delete(self):
        try:
            with self.my_connection:
                with self.my_connection.cursor() as cursor:
                    sentencia = "DELETE FROM persona WHERE id_persona IN %s"
                    entrada = input("Proporciona el id_persona a eliminar (separados por coma) : ")
                    valores = (tuple(entrada.split(",")),)
                    cursor.execute(sentencia,valores)
                    registros_eliminados = cursor.rowcount
                    print(f"Registros Eliminados : {registros_eliminados}")
        except Exception as e:
            print(f"Ha ocurrido un error : {e}")
        finally:
            self.my_connection.close()

DB()