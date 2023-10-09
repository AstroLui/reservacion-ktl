class Empleado:
    def __init__(self, hotel, cedula, nombre, posicion, salario, fechaContratacion):
        self.hotel = hotel
        self.cedula = cedula
        self.nombre = nombre
        self.posicion = posicion
        self.salario = salario
        self.fechaContratacion = fechaContratacion
    
    def print_empleado(self):
        print()
        print(f"{self.nombre}")
        print(f"Cédula: {self.cedula}")
        print(f"Posición: {self.posicion}")
        print(f"Salario: {self.salario}")
        print(f"Fecha de contratación: {self.fechaContratacion}")
        

#Estructura para poder almacenar los empleados en el arbol binario
class NodoArbol:
    def __init__(self, objeto):
        self.valor = objeto
        self.izquierda = None
        self.derecha = None

#Esta estructura es la que se utilizará para almacenar los empleados de cada hotel
class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = NodoArbol(valor)
        else:
            self._insertar_recursivo(valor, self.raiz)

    def _insertar_recursivo(self, valor, nodo_actual):
        if valor.nombre < nodo_actual.valor.nombre:
            if nodo_actual.izquierda is None:
                nodo_actual.izquierda = NodoArbol(valor)
            else:
                self._insertar_recursivo(valor, nodo_actual.izquierda)
        elif valor.nombre > nodo_actual.valor.nombre:
            if nodo_actual.derecha is None:
                nodo_actual.derecha = NodoArbol(valor)
        else:
            self._insertar_recursivo(valor, nodo_actual.derecha)

    def eliminar(self, valor):
        self.raiz = self._eliminar_recursivo(valor, self.raiz)

    def _eliminar_recursivo(self, nombre, nodo_actual):
        if nodo_actual is None:
            return None
        if nombre < nodo_actual.valor.nombre:
            nodo_actual.izquierda = self._eliminar_recursivo(nombre, nodo_actual.izquierda)
        elif nombre > nodo_actual.valor.nombre:
            nodo_actual.derecha = self._eliminar_recursivo(nombre, nodo_actual.derecha)
        else:
            if nodo_actual.izquierda is None:
                return nodo_actual.derecha
            elif nodo_actual.derecha is None:
                return nodo_actual.izquierda
            else:
                sucesor = self._encontrar_minimo(nodo_actual.derecha)
                nodo_actual.valor = sucesor.valor
                nodo_actual.derecha = self._eliminar_recursivo(sucesor.valor.nombre, nodo_actual.derecha)
        return nodo_actual

    def _encontrar_minimo(self, nodo_actual):
        if nodo_actual.izquierda is None:
            return nodo_actual
        return self._encontrar_minimo(nodo_actual.izquierda)

    def modificar(self, nombre, valor_nuevo):
        nodo = self.consultar(nombre)
        if nodo:
            nodo.valor = valor_nuevo
            print("\nEmpleado modificado exitosamente")

    def consultar(self, nombre):
        return self._consultar_recursivo(nombre, self.raiz)

    def _consultar_recursivo(self, nombre, nodo_actual):
        if nodo_actual is None or nodo_actual.valor.nombre == nombre:
            return nodo_actual
        if nombre < nodo_actual.valor.nombre:
            return self._consultar_recursivo(nombre,nodo_actual.izquierda)
        return self._consultar_recursivo(nombre, nodo_actual.derecha)

    def inorden(self):
        self._inorden_recursivo(self.raiz)
    
    def _inorden_recursivo(self, nodo_actual):
        if nodo_actual is not None:
            self._inorden_recursivo(nodo_actual.izquierda)
            nodo_actual.valor.print_empleado()
            self._inorden_recursivo(nodo_actual.derecha)
    
    def preorden(self):
        self._preorden_recursivo(self.raiz)
    
    def _preorden_recursivo(self, nodo_actual):
        if nodo_actual is not None:
            nodo_actual.valor.print_empleado()
            self._preorden_recursivo(nodo_actual.izquierda)
            self._preorden_recursivo(nodo_actual.derecha)
    
    def postorden(self):
        self._postorden_recursivo(self.raiz)
    
    def _postorden_recursivo(self, nodo_actual):
        if nodo_actual is not None:
            self._postorden_recursivo(nodo_actual.izquierda)
            self._postorden_recursivo(nodo_actual.derecha)
            nodo_actual.valor.print_empleado()
    
    def empty(self):
        if self.raiz is None:
            return True
        return False