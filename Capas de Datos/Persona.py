from Manejo_Logging import log

class Persona:
    def __init__(self,id_persona = None,nombre = None,apellido = None,email = None) -> None:
        self._id_persona = id_persona
        self._nombre = nombre
        self._apellido = apellido
        self._email = email
    
    def __str__(self) -> str:
        return f"""
            Id Persona : {self._id_persona},Nombre: {self._nombre},
            Apellido: {self._apellido}, Email: {self._email}
        """

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self,apellido):
        self._apellido = apellido
    
if __name__ == "__main__":
    persona1 = Persona(1,"Felipe","Castro","castrolopez.davidfelipe@gmail.com")
    log.debug(persona1)
    persona1 = Persona