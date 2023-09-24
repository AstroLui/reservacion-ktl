from datetime import date, datetime
import os

class Accion:
    def __init__(self, tipo, mensaje):
        self.date = datetime.now()
        self.tipo = tipo.upper()
        self.mensaje = mensaje

    def info(self):
        """
        Devuelve le información del objeto de forma imprimible por consola.
        """ 
        return "{} | {} - {}\n".format(self.date.strftime("%d/%m/%y %H:%M:%S"), self.tipo, self.mensaje)
    
    def guardar(self):
        # Usamos una pila para almacenar las acciones
        pila = []
        # Agregamos la nueva acción a la pila
        if not os.path.exists("log.txt"):
            open("log.txt", "x").close

        else:
            with open("log.txt", "r") as f:
                for linea in f:
                    print(linea)
                    pila.insert(0, linea)

            with open("log.txt", "a") as f:
                pila.append(self)
                # Recorremos la pila y guardamos cada acción en el archivo
                while pila:
                    accion = pila.pop()
                    print(type(accion))
                    if type(accion) == str:
                        f.write("{}".format(accion))
                    else:
                        f.write("{} | {} - {}\n".format(accion.date.strftime("%d/%m/%y %H:%M:%S"), accion.tipo, accion.mensaje))
