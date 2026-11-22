from abc import ABC, abstractmethod
from excepciones import ErrorCliente


# Clase abstracta general
class Entidad(ABC):

    def __init__(self, identificador):
        self._identificador = identificador

    @property
    def identificador(self):
        return self._identificador

    @abstractmethod
    def validar(self):
        """Metodo que deben implementar las clases derivadas."""
        pass


# Clase Cliente
class Cliente(Entidad):

    def __init__(self, identificador, nombre, correo, telefono):

        super().__init__(identificador)

        self.__nombre = nombre
        self.__correo = correo
        self.__telefono = telefono

        self.validar()

    # Validacion de los datos del cliente
    def validar(self):

        if not isinstance(self.identificador, str) or not self.identificador.strip():
            raise ErrorCliente("El identificador del cliente es obligatorio.")

        if not isinstance(self.__nombre, str) or len(self.__nombre.strip()) < 3:
            raise ErrorCliente("El nombre debe tener al menos 3 caracteres.")

        if (
            not isinstance(self.__correo, str)
            or self.__correo.count("@") != 1
            or " " in self.__correo
            or "." not in self.__correo.split("@")[-1]
        ):
            raise ErrorCliente("El correo electronico no es valido.")
    

        if not isinstance(self.__telefono, str) or not self.__telefono.isdigit():
            raise ErrorCliente("El telefono debe contener solamente numeros.")

        if not 7 <= len(self.__telefono) <= 15:
            raise ErrorCliente("El telefono debe tener entre 7 y 15 digitos.")

        return True

    # Consultar datos del cliente
    @property
    def nombre(self):
        return self.__nombre

    @property
    def correo(self):
        return self.__correo

    @property
    def telefono(self):
        return self.__telefono

    # Mostrar informacion del cliente
    def mostrar_informacion(self):

        return (
            f"Identificacion: {self.identificador}\n"
            f"Nombre: {self.__nombre}\n"
            f"Correo: {self.__correo}\n"
            f"Telefono: {self.__telefono}"
        )


# Prueba del modulo
if __name__ == "__main__":

    try:
        cliente = Cliente(
            "1001",
            "Carlos Perez",
            "carlos@gmail.com",
            "3001234567"
        )

        print("Cliente registrado correctamente.")
        print(cliente.mostrar_informacion())

    except ErrorCliente as error:
        print(f"Error al registrar cliente: {error}")
