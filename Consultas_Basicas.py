import psycopg2

class DB(object):
    
    def __init__(self) -> None:
        self.conexion_DB()
        #self.seleccionar_todos_los_registros()
        #self.seleccionar_un_registro()
        self.seleccionar_varios_registros()

    def conexion_DB(self):
        self.my_connection = psycopg2.connect(user="postgres",
        password="admin",
        host = "127.0.0.1",
        port = "5432",
        database = "teste_db")

    def seleccionar_todos_los_registros(self):
        try:
            with self.my_connection:
                with self.my_connection.cursor()  as self.my_cursor:
                    sentencia = "SELECT * FROM persona"
                    self.my_cursor.execute(sentencia)
                    registros = self.my_cursor.fetchall()
                    print(registros)
        except Exception as e:
            print(f"Ha ocurrido un error : {e}")
        finally:
            self.my_connection.close()
            self.my_cursor.close()
    
    def seleccionar_un_registro(self):
        try:
            with self.my_connection:
                with self.my_connection.cursor()  as self.my_cursor:
                    sentencia = "SELECT * FROM persona WHERE id_persona = %s" #Parametro posicional o placeholder
                    id_persona = 1
                    self.my_cursor.execute(sentencia,(id_persona,))
                    registros = self.my_cursor.fetchone()
                    print(registros)
        except Exception as e:
            print(f"Ha ocurrido un error : {e}")
        finally:
            self.my_connection.close()
            self.my_cursor.close()
    
    def seleccionar_varios_registros(self):
        try:
            with self.my_connection:
                with self.my_connection.cursor()  as self.my_cursor:
                    sentencia = "SELECT * FROM persona WHERE id_persona IN %s"
                    #entrada = input("Proporciona los ids a buscar separado por comas : ")
                    #llaves_primarias = (tuple(entrada.slipt(",")),)
                    llaves_primarias = ((1,2,3,4),) 
                    self.my_cursor.execute(sentencia,llaves_primarias)
                    registros = self.my_cursor.fetchall()
                    for registro in registros:
                        print(registro)

        except Exception as e:
            print(f"Ha ocurrido un error : {e}")
        finally:
            self.my_connection.close()
            self.my_cursor.close()

app = DB()
