# El archivo `gestionreservaciones` es para la clase de la lista entrelazada tipo Cola
# sobre la reservaciones de cada hotel

class Nodo: 
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class Cola: 
    def __init__(self):
        self.frente = None
        self.fin = None 

    def __Empty__(self): 
        return self.frente is None
    
    def Add(self, valor): 
        nodo_nuevo = Nodo(valor)
        if self.__Empty__():
            self.frente = nodo_nuevo
        else: 
            self.fin.siguiente= nodo_nuevo
        self.fin = nodo_nuevo
    
    def Delete(self): 
        if self.__Empty__():
            return None
        else: 
            valor_eliminado = self.frente.valor
            self.frente = self.frente.siguiente
            if self.frente == None: 
                self.fin = None
            return valor_eliminado

    def ViewList(self):
        if self.__Empty__() is False:
            self.__AuxView__(self.frente)

    def __AuxView__(self, nodo):
        if nodo is not None: 
            print(nodo.valor.usuario)
            self.__AuxView__(nodo.siguiente)
