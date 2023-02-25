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
            with self.my_connection.cursor() as cursor:
                sentencia = "SELECT * FROM persona WHERE id_persona IN %s"
                # llaves_primarias = ((1,2,3),)
                entrada = input("Proporciona los Ids a buscar : ")
                llaves_primarias = (tuple(entrada.split(",")),)
                cursor.execute(sentencia,llaves_primarias)
                registros = cursor.fetchall()
                for registro in registros:
                    print(registro)

        except Exception as e:
            print(f"Ha ocurrido un error : {e}")
        finally:
            self.my_connection.close()

DB()