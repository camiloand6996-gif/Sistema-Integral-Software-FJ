from entidades import Entidad, Cliente
from servicios import Servicio, ServicioSala
from excepciones import ErrorReserva, registrar_evento, registrar_error


# Clase Reserva
class Reserva(Entidad):

    def __init__(self, identificador, cliente, servicio, duracion):

        super().__init__(identificador)

        self.__cliente = cliente
        self.__servicio = servicio
        self.__duracion = duracion
        self.__estado = "Pendiente"

        self.validar()

        registrar_evento(
            f"Reserva {identificador} creada correctamente."
        )

    # Validar los datos de la reserva
    def validar(self):

        if not isinstance(self.__cliente, Cliente):
            raise ErrorReserva("El cliente no es valido.")

        if not isinstance(self.__servicio, Servicio):
            raise ErrorReserva("El servicio no es valido.")

        if (
            isinstance(self.__duracion, bool)
            or not isinstance(self.__duracion, (int, float))
            or self.__duracion <= 0
        ):
            raise ErrorReserva("La duracion debe ser mayor que cero.")

        return True

    # Consultar el estado de la reserva
    @property
    def estado(self):
        return self.__estado

    @property
    def cliente(self):
        return self.__cliente

    @property
    def servicio(self):
        return self.__servicio

    @property
    def duracion(self):
        return self.__duracion

    # Confirmar reserva
    def confirmar(self):

        try:
            if self.__estado != "Pendiente":
                raise ErrorReserva(
                    "Solamente se pueden confirmar reservas pendientes."
                )

            self.__estado = "Confirmada"

            registrar_evento(
                f"Reserva {self.identificador} confirmada."
            )

            return True

        except ErrorReserva as error:
            registrar_error(str(error))
            raise

    # Cancelar reserva
    def cancelar(self):

        try:
            if self.__estado != "Pendiente":
                raise ErrorReserva(
                    "Solamente se pueden cancelar reservas pendientes."
                )

            self.__estado = "Cancelada"

            registrar_evento(
                f"Reserva {self.identificador} cancelada."
            )

            return True

        except ErrorReserva as error:
            registrar_error(str(error))
            raise

    # Procesar reserva y calcular costo
    def procesar(self, impuesto=0, descuento=0):

        try:
            if self.__estado != "Confirmada":
                raise ErrorReserva(
                    "La reserva debe estar confirmada para procesarse."
                )

            costo = self.__servicio.calcular_costo(
                self.__duracion,
                impuesto,
                descuento
            )

            registrar_evento(
                f"Reserva {self.identificador} procesada. "
                f"Costo total: ${costo}"
            )

            return costo

        except ErrorReserva:
            raise

        except Exception as error:
            registrar_error(
                f"Error al procesar reserva {self.identificador}: {error}"
            )
            raise ErrorReserva(
                "No fue posible procesar la reserva."
            ) from error

    # Mostrar informacion de la reserva
    def mostrar_informacion(self):

        return (
            f"\nReserva: {self.identificador}"
            f"\nCliente: {self.__cliente.nombre}"
            f"\nServicio: {self.__servicio.nombre}"
            f"\nDuracion: {self.__duracion} horas"
            f"\nEstado: {self.__estado}"
        )


# Prueba del modulo
if __name__ == "__main__":

    try:
        # Crear cliente
        cliente = Cliente(
            "1001",
            "Carlos Perez",
            "carlos@gmail.com",
            "3001234567"
        )

        # Crear servicio
        servicio = ServicioSala(
            "S01",
            "Sala de reuniones",
            50000
        )

        # Crear reserva
        reserva = Reserva(
            "R001",
            cliente,
            servicio,
            2
        )

        print("Reserva creada correctamente.")
        print(reserva.mostrar_informacion())

        # Confirmar reserva
        reserva.confirmar()

        print("\nReserva confirmada.")

        # Procesar reserva
        costo = reserva.procesar(impuesto=19)

        print(f"\nCosto total de la reserva: ${costo:,.2f}")

        print("\nPrueba de reservas finalizada correctamente.")

    except ErrorReserva as error:
        registrar_error(f"Error en la prueba de reservas: {error}")
        print(f"Error en la prueba: {error}")

    except Exception as error:
        registrar_error(f"Error inesperado en la prueba: {error}")
        raise ErrorReserva(
            "No fue posible ejecutar la prueba de reservas."
        ) from error
        

    
        
        
