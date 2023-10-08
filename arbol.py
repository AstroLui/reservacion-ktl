class Empleado:
    def __init__(self, hotel, nombre, posicion, salario, fechaContratacion):
        self.hotel = hotel
        self.nombre = nombre
        self.posicion = posicion
        self.salario = salario
        self.fechaContratacion = fechaContratacion

    def get_hotel(self):
        return self.hotel

    def get_nombre(self):
        return self.nombre

    def get_posicion(self):
        return self.posicion

    def get_salario(self):
        return self.salario

    def get_fecha_contratacion(self):
        return self.fechaContratacion
    
    def print_empleado(self):
        print(f"Nombre: {self.nombre}")
        print(f"Posición: {self.posicion}")
        print(f"Salario: {self.salario}")
        print(f"Fecha de contratación: {self.fechaContratacion}")


class NodoArbol:
    def __init__(self, objeto):
        # "dato" puede ser de cualquier tipo, incluso un objeto si se sobrescriben los operadores de comparación
        self.valor = objeto
        self.izquierda = None
        self.derecha = None
    
    def get_dato(self):
        return self.dato

    def get_izquierda(self):
        return self.izquierda

    def get_derecha(self):
        return self.derecha


class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = NodoArbol(valor)
        else:
            self._insertar_recursivo(valor, self.raiz)

    def _insertar_recursivo(self, valor, nodo_actual):
        if valor.salario < nodo_actual.valor.salario:
            if nodo_actual.izquierda is None:
                nodo_actual.izquierda = NodoArbol(valor)
            else:
                self._insertar_recursivo(valor, nodo_actual.izquierda)
        elif valor.salario > nodo_actual.valor.salario:
            if nodo_actual.derecha is None:
                nodo_actual.derecha = NodoArbol(valor)
        else:
            self._insertar_recursivo(valor, nodo_actual.derecha)

    def eliminar(self, valor):
        self.raiz = self._eliminar_recursivo(valor, self.raiz)

    def _eliminar_recursivo(self, valor, nodo_actual):
        if nodo_actual is None:
            return None
        if valor.salario < nodo_actual.valor.salario:
            nodo_actual.izquierda = self._eliminar_recursivo(valor, nodo_actual.izquierda)
        elif valor > nodo_actual.valor:
            nodo_actual.derecha = self._eliminar_recursivo(valor, nodo_actual.derecha)
        else:
            if nodo_actual.izquierda is None:
                return nodo_actual.derecha
            elif nodo_actual.derecha is None:
                return nodo_actual.izquierda
            else:
                sucesor = self._encontrar_minimo(nodo_actual.derecha)
                nodo_actual.valor = sucesor.valor
                nodo_actual.derecha = self._eliminar_recursivo(sucesor.valor, nodo_actual.derecha)
        return nodo_actual

    def _encontrar_minimo(self, nodo_actual):
        if nodo_actual.izquierda is None:
            return nodo_actual
        return self._encontrar_minimo(nodo_actual.izquierda)

    def modificar(self, valor_viejo, valor_nuevo):
        self.eliminar(valor_viejo)
        self.insertar(valor_nuevo)

    def consultar(self, valor):
        return self._consultar_recursivo(valor, self.raiz)

    def _consultar_recursivo(self, valor, nodo_actual):
        if nodo_actual is None or nodo_actual.valor == valor:
            return nodo_actual
        if valor.salario < nodo_actual.valor.salario:
            return self._consultar_recursivo(valor,nodo_actual.izquierda)
        return self._consultar_recursivo(valor, nodo_actual.derecha)

    def inorden(self):
        self._inorden_recursivo(self.raiz)
    
    def _inorden_recursivo(self, nodo_actual):
        if nodo_actual is not None:
            self._inorden_recursivo(nodo_actual.izquierda)
            nodo_actual.valor.print_empleado
            self._inorden_recursivo(nodo_actual.derecha)
    
    def preorden(self):
        self._preorden_recursivo(self.raiz)
    
    def _preorden_recursivo(self, nodo_actual):
        if nodo_actual is not None:
            nodo_actual.valor.print_empleado
            self._preorden_recursivo(nodo_actual.izquierda)
            self._preorden_recursivo(nodo_actual.derecha)
    
    def postorden(self):
        self._postorden_recursivo(self.raiz)
    
    def _postorden_recursivo(self, nodo_actual):
        if nodo_actual is not None:
            self._postorden_recursivo(nodo_actual.izquierda)
            self._postorden_recursivo(nodo_actual.derecha)
            nodo_actual.valor.print_empleado
    
    def empty(self):
        if self.raiz is None:
            return True
        return False
