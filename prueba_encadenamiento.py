from entidades import Cliente
from servicios import ServicioSala
from reservas import Reserva
from excepciones import ErrorReserva

try:
    cliente = Cliente("1001", "Carlos Perez", "carlos@gmail.com", "3001234567")
    servicio = ServicioSala("S01", "Sala de reuniones", 50000)

    reserva = Reserva("R010", cliente, servicio, 2)
    reserva.confirmar()

    reserva.procesar(impuesto=150)

except ErrorReserva as error:
    print("Excepcion personalizada:", error)
    print("Error original:", error.__cause__)
    print("Tipo del error original:", type(error.__cause__).__name__)