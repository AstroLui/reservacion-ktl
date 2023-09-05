import random
from datetime import date, datetime

# Almacena todas las cuentas activas en la aplicación (tempDB)
reservas = []

class Reservas:
    """
    Encapsula la información y las operaciones de cada cuenta.
    
    Cada cuenta tiene una clave especial que le permite al propietario validar operaciones.
    Esta clave se almacena en forma de hash, tal que no quede registro de la clave original en texto plano.

    Nótese ninguna de la operaciones realiza validación directamente, sino que se deja de parte del programador.
    """
    ultID = 1

    def __init__(self,
                 nombre: str,
                 idn: str,
                 correo: str,
                 telf: str,
                 fechaEntrada: str,
                 fechaSalida: str
                 ):
        """
        Construye los objetos de la clase Cuenta.
        
        :param nombre: Nombre del propietario de la :class:`Cuenta`
        :param cedula: C.I. del propietario :class:`Cuenta`
        :param clave_especial: La clave que se usará para autorizar operaciones
        :param balance_inicial: El balance inicial de la cuenta en centavos
        :raises ValueError: cuando el balance inicial es menor a 1.00
        """

        self.id = random.randint(0, 99999) #Agregar la funcion random de Math
        self.nombre = nombre
        self.idn = idn
        self.correo = correo
        self.telf = telf
        self.fechaReserve = datetime.now #Guardad la fecha actual
        self.fechaEntrada = fechaEntrada
        self.fechaSalida = fechaSalida
        self.balance = balance_inicial

    def __reserv__(self):
        """Devuelve le información del objeto de forma legible""" 
        return "Cuenta(numero={:0>4}, nombre={}, ci={}, balance={})".format(self.numero, self.nombre, self.cedula, format_centavos(self.balance))

def abrircuenta():
    """Recibe los datos del monto con el que se va a aperturar la cuenta"""
    
    ci = input("Indique la C.I. del propietario o la propietaria ")
    if esta_ci_registrada(ci):
        print_err("Ya hay una cuenta con esta C.I. registrada")
        return

    nombre = input("Indique el nombre del propietario o la propietaria de la cuenta: ").strip()
    clave = input_nuevaclave()

    # Captura el monto que se desea depositar en la apertura de la cuenta.
    balance = input_monto("Indique el balance inicial de la cuenta")

    # Crea un nuevo objeto de la clase Cuenta con el balance inicial capturado anteriormente
    c = Cuenta(nombre, ci, clave, balance)

    # Se agrega la cuenta a la tempDB
    cuentas[c.numero] = c

    # Detalla el estado de la operación y el balance de la cuenta relacionada.
    print_info("Nueva cuenta creada:", c)

    return c


