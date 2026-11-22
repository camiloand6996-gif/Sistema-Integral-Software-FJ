from entidades import Cliente
from servicios import (
    ServicioSala,
    ServicioEquipo,
    ServicioAsesoria
)
from reservas import Reserva
from excepciones import (
    ErrorCliente,
    ErrorServicio,
    ErrorReserva,
    registrar_evento,
    registrar_error
)


# Listas internas del sistema
clientes = []
servicios = []
reservas = []


# Funcion para registrar clientes
def registrar_cliente(identificador, nombre, correo, telefono):

    try:
        cliente = Cliente(
            identificador,
            nombre,
            correo,
            telefono
        )

        clientes.append(cliente)

        registrar_evento(
            f"Cliente {nombre} registrado correctamente."
        )

        print(f"Cliente {nombre} registrado correctamente.")

    except ErrorCliente as error:
        registrar_error(f"Error de cliente: {error}")
        print(f"Error al registrar cliente: {error}")


# Funcion para registrar servicios
def registrar_servicio(servicio):

    try:
        servicios.append(servicio)

        registrar_evento(
            f"Servicio {servicio.nombre} registrado."
        )

        print(f"Servicio {servicio.nombre} registrado correctamente.")

    except ErrorServicio as error:
        registrar_error(f"Error de servicio: {error}")
        print(f"Error al registrar servicio: {error}")


# Funcion para crear reservas
def crear_reserva(identificador, cliente, servicio, duracion):

    try:
        reserva = Reserva(
            identificador,
            cliente,
            servicio,
            duracion
        )

        reservas.append(reserva)

        print(f"Reserva {identificador} creada correctamente.")

        return reserva

    except ErrorReserva as error:
        registrar_error(f"Error de reserva: {error}")
        print(f"Error al crear reserva: {error}")
        return None


def ejecutar_sistema():

    print("=" * 55)
    print(" SISTEMA INTEGRAL DE GESTION - SOFTWARE FJ ")
    print("=" * 55)

    try:

        # OPERACION 1: Registrar cliente valido
        print("\nOPERACION 1")
        registrar_cliente(
            "1001",
            "Carlos Perez",
            "carlos@gmail.com",
            "3001234567"
        )

        # OPERACION 2: Registrar otro cliente
        print("\nOPERACION 2")
        registrar_cliente(
            "1002",
            "Maria Rodriguez",
            "maria@gmail.com",
            "3101234567"
        )

        # OPERACION 3: Intentar registrar cliente invalido
        print("\nOPERACION 3")
        registrar_cliente(
            "1003",
            "Ana",
            "correo_invalido",
            "abc123"
        )

        # OPERACION 4: Crear servicio de sala
        print("\nOPERACION 4")
        sala = ServicioSala(
            "S01",
            "Sala de reuniones",
            50000
        )
        registrar_servicio(sala)

        # OPERACION 5: Crear servicio de equipos
        print("\nOPERACION 5")
        equipo = ServicioEquipo(
            "E01",
            "Computador portatil",
            20000
        )
        registrar_servicio(equipo)

        # OPERACION 6: Crear servicio de asesoria
        print("\nOPERACION 6")
        asesoria = ServicioAsesoria(
            "A01",
            "Asesoria de software",
            80000
        )
        registrar_servicio(asesoria)

        # OPERACION 7: Intentar crear servicio invalido
        print("\nOPERACION 7")

        try:
            servicio_invalido = ServicioSala(
                "S02",
                "Sala invalida",
                -5000
            )
            registrar_servicio(servicio_invalido)

        except ErrorServicio as error:
            registrar_error(
                f"Servicio rechazado: {error}"
            )
            print(f"Servicio rechazado: {error}")

        # OPERACION 8: Crear reserva correcta
        print("\nOPERACION 8")

        reserva1 = crear_reserva(
            "R001",
            clientes[1],
            sala,
            2
        )

        if reserva1:
            reserva1.confirmar()
            costo = reserva1.procesar(impuesto=19)
            print(f"Costo de la reserva: ${costo:,.2f}")

        # OPERACION 9: Intentar crear reserva invalida
        print("\nOPERACION 9")

        crear_reserva(
            "R002",
            clientes[0],
            equipo,
            -3
        )

        # OPERACION 10: Crear y cancelar reserva
        print("\nOPERACION 10")

        reserva2 = crear_reserva(
            "R003",
            clientes[1],
            asesoria,
            1
        )

        if reserva2:
            reserva2.cancelar()
            print("Reserva cancelada correctamente.")

        # Resumen del sistema
        print("\n" + "=" * 55)
        print(" RESUMEN GENERAL DEL SISTEMA ")
        print("=" * 55)

        print(f"Clientes registrados: {len(clientes)}")
        print(f"Servicios registrados: {len(servicios)}")
        print(f"Reservas creadas: {len(reservas)}")

        registrar_evento(
            "Ejecucion de las 10 operaciones finalizada."
        )

    except Exception as error:

        registrar_error(
            f"Error general del sistema: {error}"
        )

        print(f"Error general: {error}")

    else:
        print("\nEl sistema termino las operaciones correctamente.")

    finally:
        print("\nProceso de ejecucion finalizado.")
        registrar_evento("Finalizacion del programa principal.")


# Inicio del programa
if __name__ == "__main__":
    ejecutar_sistema()
