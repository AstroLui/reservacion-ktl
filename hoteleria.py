import random
from datetime import date, datetime

# Almacena todas las cuentas activas en la aplicación (tempDB)
reservas = []

class Reserva:
    """
    Encapsula la información y las operaciones de cada cuenta.
    """

    def __init__(self,
                 nombre: str,
                 idn: str,
                 correo: str,
                 telf: str,
                 fechaEntrada: str,
                 fechaSalida: str
                 ):
        """
        Construye los objetos de la clase Reserva.
        
        :param id: identificador unico de la :class:`Reserva`
        """

        self.id = random.randint(0, 99999) #Agregar la funcion random de Math
        self.nombre = nombre
        self.idn = idn
        self.correo = correo
        self.telf = telf
        self.fechaReserve = datetime.now #Guardad la fecha actual
        self.fechaEntrada = fechaEntrada
        self.fechaSalida = fechaSalida

    def __reserv__(self):
        """
        Devuelve le información del objeto de forma imprimible por consola.
        """ 
        return "(ID: {:0>4}, Nombres: {}, Habitacion: {},Entrada: {}, Salida: {})".format(self.id, self.nombre, self.habitacion, self.fechaEntrada, self.fechaSalidaß)

def crearReserva():
    """
    Recibe los datos del monto con el que se va a aperturar la cuenta
    """
    
    idn = input("Indique la C.I. del propietario o la propietaria ")
    if verificarHabitacion(habitacion, fecha ):
        print("La habitacion se encuentra reservada para la fecha ", fechaEntrada, "/", fechaSalida)
        return

    # Crea un nuevo objeto de la clase Cuenta con el balance inicial capturado anteriormente
    reserva = Reserva(nombre, idn, correo, telf, fechaEntrada, fechaSalida)

    # Se agrega la cuenta a la tempDB
    reservas[len(reservas) + 1] = reserva

    # Detalla el estado de la operación y el balance de la cuenta relacionada.
    print("RESERVA: ", reservas)

    return reservas


