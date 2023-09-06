import random
from datetime import date, datetime
import json

# Almacena todas las reservas activas en la aplicación (tempDB)
reservas = []

# Almacena todas las habitaciones activas de la aplicación (tempDB)
habitaciones = []

class Reserva:
    """
    Encapsula la información y las operaciones de cada cuenta.
    """

    def __init__(self, nombre: str, idn: str, correo: str, telf: str, habitacion: str, fechaEntrada, fechaSalida):
        """
        Construye los objetos de la clase Reserva.
        
        :param id: identificador unico de la :class:`Reserva`
        """

        self.id = verificarID()
        self.nombre = nombre
        self.idn = idn
        self.correo = correo
        self.telf = telf
        self.fechaReserva = datetime.now
        self.habitacion = habitacion
        self.fechaEntrada = fechaEntrada
        self.fechaSalida = fechaSalida
        self.duracion = fechaSalida - fechaEntrada

    def reserva(self):
        """
        Devuelve le información del objeto de forma imprimible por consola.
        """ 
        return "ID: {:0<4}, Nombres: {}, Habitacion: {},Entrada: {}, Salida: {}".format(self.id, self.nombre, self.habitacion, self.fechaEntrada, self.fechaSalida)

    def getId(self):
        return self.id

    def getNombre(self):
        return self.nombre

    def getFechaReserva(self):
        return self.fechaReserva

    def getHabitacion(self):
        return self.habitacion

    def getFechaEntrada(self):
        return self.fechaEntrada

    def getFechaSalida(self):
        return self.fechaSalida
    
    def getDuracion(self):
        return self.duracion
    

def verificarID():
    id = random.randint(0, 99999)
    for reserva in reservas:
        if reserva.getId() == id:
            verificarID()
    return id

def fecha(fecha):
    dia, mes, ano = fecha.split("/")
    dia = int(dia)
    mes = int(mes)
    ano = int(ano)
    fechaObjeto = date(ano, mes, dia)
    return fechaObjeto

def cargarArchivo():
    with open('./db_reserva.json', 'r') as f:
        dbJSON = json.load(f)

    for reserva in dbJSON:
        cliente = reserva["cliente"]
        nombre = cliente["nombre"]
        idn = cliente["idn"]
        correo = cliente["correo"]
        telf = cliente["telf"]
        habitacion = reserva["habitacion"]
        habitacionId = habitacion["id"]
        fechaEntrada = fecha(habitacion["fechaEntrada"])
        fechaSalida = fecha(habitacion["fechaSalida"])
        
        # Crea un nuevo objeto de la clase Cuenta con el balance inicial capturado anteriormente
        reserva = Reserva(nombre, idn, correo, telf, habitacionId, fechaEntrada, fechaSalida)

        # Se agrega la cuenta a la tempDB
        reservas.append(reserva)

    print('\n!!! Archivo cargado exitosamente \n')
    #print(data)
    return


def seleccionarHabitacion(fechaEntrada, fechaSalida):
    #print(fechaEntrada, fechaSalida)
    print('Seleccione la habitacion que desea')
    #verificarhabitacion

def crearReserva():
    """
    Recibe los datos del monto con el que se va a aperturar la cuenta
    """
    
    nombre = input("Indique su nombre: ")
    idn = int(input("Indique su número de cédula: "))
    correo = input("Indique su correo electrónico: ")
    telf = input("Indique su número telefónico: ")
    fechaEntrada = fecha(input("Indique la fecha de entrada (DD/MM/AAAA): "))
    fechaSalida = fecha(input("Indique la fecha de salida (DD/MM/AAAA): "))

    habitacion = seleccionarHabitacion(fechaEntrada, fechaSalida)

    # Crea un nuevo objeto de la clase Cuenta con el balance inicial capturado anteriormente
    reserva = Reserva(nombre, idn, correo, telf, habitacion, fechaEntrada, fechaSalida)

    # Se agrega la cuenta a la tempDB
    reservas.append(reserva)

    # Detalla el estado de la operación y el balance de la cuenta relacionada.
    print("RESERVA: ", reserva.reserva())

    return reservas

def verReserervas():
    print('\n___')
    i = 0
    for reserva in reservas:
        print("RESERVA", i , ': ', reserva.reserva())
        i += 1
    print('---')
    return

def main():
    while True:
        print('\nMENU PRINCIPAL')
        print('___')
        print('0. Cargar Seed')
        print('1. Crear Reserva')
        print('10. Ver todas las reservas')
        opcion = int(input('Seleccione una opción: '))
        match opcion:
            case 0:
                cargarArchivo()
            case 1:
                crearReserva()
            case 10:
                verReserervas()

main()