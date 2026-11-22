from abc import abstractmethod
from entidades import Entidad
from excepciones import ErrorServicio


# Clase abstracta Servicio
class Servicio(Entidad):

    def __init__(self, identificador, nombre, precio_base):
        super().__init__(identificador)
        self._nombre = nombre
        self._precio_base = precio_base
        self.validar()

    @property
    def nombre(self):
        return self._nombre

    @property
    def precio_base(self):
        return self._precio_base

    def validar(self):
        if not isinstance(self._nombre, str) or not self._nombre.strip():
            raise ErrorServicio("El nombre del servicio es obligatorio.")

        if (
            isinstance(self._precio_base, bool)
            or not isinstance(self._precio_base, (int, float))
            or self._precio_base <= 0
        ):
            raise ErrorServicio("El precio debe ser mayor que cero.")

        return True

    @abstractmethod
    def calcular_costo(self, duracion, impuesto=0, descuento=0):
        pass

    @abstractmethod
    def describir(self):
        pass


# Servicio 1: Reserva de salas
class ServicioSala(Servicio):

    def validar(self):
        super().validar()

    def calcular_costo(self, duracion, impuesto=0, descuento=0):
        if not isinstance(duracion, (int, float)) or isinstance(duracion, bool) or duracion <= 0:
            raise ErrorServicio("La duracion de la sala debe ser mayor que cero.")

        if not 0 <= impuesto <= 100 or not 0 <= descuento <= 100:
            raise ErrorServicio("El impuesto y descuento deben estar entre 0 y 100.")

        subtotal = self.precio_base * duracion
        subtotal -= subtotal * descuento / 100
        return round(subtotal + subtotal * impuesto / 100, 2)

    def describir(self):
        return f"Reserva de sala: {self.nombre}. Precio por hora: ${self.precio_base}"


# Servicio 2: Alquiler de equipos
class ServicioEquipo(Servicio):

    def validar(self):
        super().validar()

    def calcular_costo(self, duracion, impuesto=0, descuento=0):
        if not isinstance(duracion, (int, float)) or isinstance(duracion, bool) or duracion <= 0:
            raise ErrorServicio("La duracion del alquiler debe ser mayor que cero.")

        if not 0 <= impuesto <= 100 or not 0 <= descuento <= 100:
            raise ErrorServicio("El impuesto y descuento deben estar entre 0 y 100.")

        subtotal = self.precio_base * duracion
        subtotal -= subtotal * descuento / 100
        return round(subtotal + subtotal * impuesto / 100, 2)

    def describir(self):
        return f"Alquiler de equipo: {self.nombre}. Precio por hora: ${self.precio_base}"


# Servicio 3: Asesorias especializadas
class ServicioAsesoria(Servicio):

    def validar(self):
        super().validar()

    def calcular_costo(self, duracion, impuesto=0, descuento=0):
        if not isinstance(duracion, (int, float)) or isinstance(duracion, bool) or duracion <= 0:
            raise ErrorServicio("La duracion de la asesoria debe ser mayor que cero.")

        if not 0 <= impuesto <= 100 or not 0 <= descuento <= 100:
            raise ErrorServicio("El impuesto y descuento deben estar entre 0 y 100.")

        subtotal = self.precio_base * duracion
        subtotal -= subtotal * descuento / 100
        return round(subtotal + subtotal * impuesto / 100, 2)

    def describir(self):
        return f"Asesoria especializada: {self.nombre}. Precio por hora: ${self.precio_base}"


# Prueba del modulo
if __name__ == "__main__":

    try:
        sala = ServicioSala("S01", "Sala de reuniones", 50000)
        equipo = ServicioEquipo("E01", "Computador portatil", 20000)
        asesoria = ServicioAsesoria("A01", "Asesoria de software", 80000)

        servicios = [sala, equipo, asesoria]

        for servicio in servicios:
            print("\n" + servicio.describir())
            print("Costo por 2 horas:", servicio.calcular_costo(2))

        print("\nTodos los servicios funcionan correctamente.")

    except ErrorServicio as error:
        print("Error en el servicio:", error)
