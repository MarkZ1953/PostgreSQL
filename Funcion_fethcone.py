import psycopg2

class DB:
    def __init__(self) -> None:
        self.conexion_DB()
        self.fetch_one()

    def conexion_DB(self):
        self.my_connection = psycopg2.connect(user="postgres",
        password="admin",
        host = "127.0.0.1",
        port = "5432",
        database = "teste_db")
    
    def fetch_one(self):
        try:
            with self.my_connection.cursor() as cursor:
                sentencia = "SELECT * FROM persona WHERE id_persona = %s"
                # id_persona = input("Ingrese el valor de Id_persona : ") 
                #No es necesario convertir el valor obtenido atravez de consola en un entero, este parametro admite string
                id_persona = 2
                cursor.execute(sentencia,(id_persona,))
                registros = cursor.fetchone()
                print(registros)
        except Exception as e:
            print(f"Ha ocurrido un error : {e}")
        finally:
            self.my_connection.close()

DB()