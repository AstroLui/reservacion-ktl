import random
from datetime import date, datetime
import json

# Almacena todas las reservas activas en la aplicación (tempDB)
reservas = []

# Almacena todas las habitaciones activas de la aplicación (tempDB)
habitaciones = []

class  Habitacion:

    def __init__(self, id, tipo, capacidad, precio):
        self.id = id
        self.tipo = tipo
        self.capacidad = capacidad
        self.precio = precio

    def info(self):
        """
        Devuelve le información del objeto de forma imprimible por consola.
        """ 
        return "{: <10} {: <16} {: <3}".format(self.id, self.tipo, self.capacidad)
    
    def getId(self):
        return self.id
    
    def getTipo(self):
        return self.tipo
    
    def getCapacidad(self):
        return self.capacidad
    
    def getPrecio(self):
        return self.precio

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
        self.costoTotal = self.duracion.days * self.habitacion.getPrecio()

    def info(self):
        """
        Devuelve le información del objeto de forma imprimible por consola.
        """ 
        return "ID: {:0>5}\n Nombres: {}\n Habitacion: {}\n Entrada: {}\n Salida: {}\n Duración: {} días\n\n TOTAL: {}$".format(self.id, self.nombre, self.habitacion.getId(), self.fechaEntrada.strftime("%A %d. %B %Y"), self.fechaSalida.strftime("%A %d. %B %Y"), self.duracion.days, self.costoTotal)

    def infoLineal(self):
        """
        Devuelve le información del objeto de forma imprimible por consola.
        """ 
        return "ID: {:0>5}, Nombres: {}, Habitacion: {}, Entrada: {}, Salida: {}, Duración: {} días, TOTAL: {}$".format(self.id, self.nombre, self.habitacion.getId(), self.fechaEntrada.strftime("%d/%m/%y"), self.fechaSalida.strftime("%d/%m/%y"), self.duracion.days, self.costoTotal)

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
    
    def getCostoTotal(self):
        return self.costoTotal

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

def cargarHabitaciones():
    with open('./db_habitaciones.json', 'r') as db:
        dbJSON = json.load(db)

    for habitacion in dbJSON:
        id = habitacion["id"]
        tipo = habitacion["tipo"]
        capacidad = habitacion["capacidad"]
        precio = habitacion["precio"]
        
        habitacion = Habitacion(id, tipo, capacidad, precio)
        # Se agrega la cuenta a la tempDB
        habitaciones.append(habitacion)
    return

def cargarReservas():
    with open('./db_reserva.json', 'r') as db:
        dbJSON = json.load(db)

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
    cargarHabitaciones()
    while True:
        print('\nMENU PRINCIPAL')
        print('___')
        print('0. Cargar Seed')
        print('1. Crear Reserva')
        print('10. Ver todas las reservas')
        opcion = int(input('Seleccione una opción: '))
        match opcion:
            case 0:
                cargarReservas()
            case 1:
                crearReserva()
            case 10:
                verReserervas()

main()