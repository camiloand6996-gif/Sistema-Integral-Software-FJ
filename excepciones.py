import logging


# Configuración del archivo de registros
logging.basicConfig(
    filename="registros.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)


# Excepción general del sistema
class ErrorSistema(Exception):
    """Clase base para los errores del sistema."""
    pass


# Error al registrar un cliente
class ErrorCliente(ErrorSistema):
    """Se genera cuando hay problemas con un cliente."""
    pass


# Error relacionado con los servicios
class ErrorServicio(ErrorSistema):
    """Se genera cuando un servicio no es válido."""
    pass


# Error relacionado con las reservas
class ErrorReserva(ErrorSistema):
    """Se genera cuando una reserva presenta problemas."""
    pass


# Error por datos inválidos
class ErrorDatos(ErrorSistema):
    """Se genera cuando los datos ingresados son incorrectos."""
    pass


# Función para registrar errores
def registrar_error(mensaje):
    logging.error(mensaje)


# Función para registrar eventos
def registrar_evento(mensaje):
    logging.info(mensaje)


# Mensaje de comprobación
if __name__ == "__main__":
    registrar_evento("Sistema Software FJ iniciado.")
    print("Módulo de excepciones funcionando correctamente.")
