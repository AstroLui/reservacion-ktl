import random
from datetime import date, datetime
import json
import sys

# Almacena todas las reservas activas en la aplicación (tempDB)
reservas = []

# Almacena todas las habitaciones activas de la aplicación (tempDB)
habitaciones = []

class  Habitacion:

    def __init__(self, id, tipo, capacidad):
        self.id = id
        self.tipo = tipo
        self.capacidad = capacidad

    def info(self):
        """
        Devuelve le información del objeto de forma imprimible por consola.
        """ 
        return "{: <10} {: <16} {: <3}".format(self.id, self.tipo, self.capacidad)
    
    def getId(self):
        return self.id

class Reserva:
    """
    Encapsula la información y las operaciones de cada cuenta.
    """

    def __init__(self, nombre: str, idn: str, correo: str, telf: str, habitacion, fechaEntrada, fechaSalida):
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

    def info(self):
        """
        Devuelve le información del objeto de forma imprimible por consola.
        """ 
        return "ID: {:0>5}\n Nombres: {}\n Habitacion: {}\n Entrada: {}\n Salida: {}\n Duración: {} días".format(self.id, self.nombre, self.habitacion.getId(), self.fechaEntrada.strftime("%A %d. %B %Y"), self.fechaSalida.strftime("%A %d. %B %Y"), self.duracion.days)

    def infoLineal(self):
        """
        Devuelve le información del objeto de forma imprimible por consola.
        """ 
        return "ID: {:0>5}, Nombres: {}, Habitacion: {}, Entrada: {}, Salida: {}, Duración: {} días".format(self.id, self.nombre, self.habitacion.getId(), self.fechaEntrada.strftime("%d/%m/%y"), self.fechaSalida.strftime("%d/%m/%y"), self.duracion.days)

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

def cargarConfig():
    with open('./config.json', 'r') as f:
        DOC = json.load(f)
        global default 
        default = DOC[0]["default"]
        global ruta_habs
        ruta_habs = DOC[0]["seed_rooms"]
        global ruta_reserv
        ruta_reserv = DOC[0]["seed_reserv"]
        global hotel
        hotel = DOC[0]["name_hotel"]

def cargarHabitaciones():
    with open(ruta_habs, 'r') as f:
        dbJSON = json.load(f)

    for habitacion in dbJSON:
        id = habitacion["id"]
        tipo = habitacion["tipo"]
        capacidad = habitacion["capacidad"]
        
        habitacion = Habitacion(id, tipo, capacidad)
        # Se agrega la cuenta a la tempDB
        habitaciones.append(habitacion)

    return

def cargarReservas():
    with open(ruta_reserv, 'r') as f:
        dbJSON = json.load(f)

    for reserva in dbJSON:
        cliente = reserva["cliente"]
        nombre = cliente["nombre"]
        idn = cliente["idn"]
        correo = cliente["correo"]
        telf = cliente["telf"]
        habitacion = reserva["habitacion"]
        habitacionId = habitacion["id"]

        for habitacionI in habitaciones:
            if habitacionI.getId() == habitacionId:
                habitacionId = habitacionI

        fechaEntrada = fecha(habitacion["fechaEntrada"])
        fechaSalida = fecha(habitacion["fechaSalida"])
        
        # Crea un nuevo objeto de la clase Cuenta con el balance inicial capturado anteriormente
        reserva = Reserva(nombre, idn, correo, telf, habitacionId, fechaEntrada, fechaSalida)

        # Se agrega la cuenta a la tempDB0
        reservas.append(reserva)

    print('\n!!! Archivo cargado exitosamente')
    #print(data)
    return

def seleccionarHabitacion(fechaEntrada, fechaSalida):
    print('\n_________')
    print('HABITACIONES DISPONIBLES')
    print('{: <6}  {: <10} {: <16} {: <3}'.format('Opción', 'Habitación', 'Tipo', 'Capacidad')) 
    i = 0
    habitacionesNoDisponibles = []
    for reserva in reservas:
        if reserva.getFechaEntrada() < fechaEntrada or reserva.getFechaSalida() < fechaSalida:
            habitacionesNoDisponibles.append(reserva.getHabitacion())
    
    habitacionesDiponibles = [x for x in habitaciones if x not in habitacionesNoDisponibles]

    for hab  in habitacionesDiponibles:
        print("{: >2}.    ".format(i),hab.info())
        i += 1
    print('‾‾‾‾‾‾‾‾‾')

    index = int(input('Seleccione una habitacion: '))

    habitacionSeleccionada = habitacionesDiponibles[index]
    return habitacionSeleccionada

def crearReserva():
    """
    Recibe los datos del monto con el que se va a aperturar la cuenta
    """
    print('')
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

    print('\n_________')
    # Detalla el estado de la operación y el balance de la cuenta relacionada.
    print("RESERVA:\n",reserva.info())
    print('‾‾‾‾‾‾‾‾‾')

    print('\n!!! Reserva realizada exitosamente')

    return

def verReserervas():
    print('\n_________')
    i = 1
    for reserva in reservas:
        print("RESERVA", i , ': ', reserva.infoLineal())
        i += 1
    print('‾‾‾‾‾‾‾‾‾')
    return

def main():
    cargarConfig()
    cargarHabitaciones()
    while True:
        print('\nMENU PRINCIPAL ' + hotel)
        print('___')
        print('0. Cargar Seed')
        print('1. Crear Reserva')
        print('10. Ver todas las reservas')
        print('20. Ver todas las reservas')
        opcion = int(input('Seleccione una opción: '))
        match opcion:
            case 0:
                cargarReservas()
            case 1:
                crearReserva()
            case 10:
                verReserervas()
            case 20:
                sys.exit()

main()