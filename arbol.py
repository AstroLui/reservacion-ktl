class Empleado:
    def __init__(self,hotel, id, name, position, salary, date_of_recruitment):
        self.hotel = hotel
        self.name = name
        self.id = id
        self.position = position
        self.salary = salary
        self.date_of_recruitment = date_of_recruitment
        self.left = None
        self.right = None
    
    def print_empleado(self):
        print(f"Nombre: {self.name}")
        print(f"Cédula: {self.id}")
        print(f"Posición: {self.position}")
        print(f"Salario: {self.salary}")
        print(f"Fecha de reclutamiento: {self.date_of_recruitment}")

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, empleado):
        if self.root is None:
            self.root = empleado
            print("Empleado creado satisfactoriamente!")
        else:
            self._insert(empleado, self.root)

    def _insert(self, empleado, current_node):
        if empleado.id < current_node.id:
            if current_node.left is None:
                current_node.left = empleado
                print("Empleado creado satisfactoriamente!")
            else:
                self._insert(empleado, current_node.left)
        elif empleado.id > current_node.id:
            if current_node.right is None:
                current_node.right = empleado
                print("Empleado creado satisfactoriamente!")
            else:
                self._insert(empleado, current_node.right)
        else:
            print("Empleado ya existente!")

    def search(self, id):
        if self.root is None:
            return None
        else:
            return self._search(id, self.root)

    def _search(self, id, current_node):
        if current_node is None:
            return None
        elif current_node.id == id:
            return current_node
        elif id < current_node.id:
            return self._search(id, current_node.left)
        else:
            return self._search(id, current_node.right)
    
    def delete(self, id):
        if self.root is None:
            return None
        else:
            self.root = self._delete(id, self.root)

    def _delete(self, id, current_node):
        if current_node is None:
            return None
        elif id < current_node.id:
            current_node.left = self._delete(id, current_node.left)
        elif id > current_node.id:
            current_node.right = self._delete(id, current_node.right)
        else:
            if current_node.left is None:
                return current_node.right
            elif current_node.right is None:
                return current_node.left
            else:
                min_node = self._find_min_node(current_node.right)
                current_node.id = min_node.id
                current_node.name = min_node.name
                current_node.position = min_node.position
                current_node.salary = min_node.salary
                current_node.date_of_recruitment = min_node.date_of_recruitment
                current_node.right = self._delete(min_node.id, current_node.right)
        return current_node

    def _find_min_node(self, current_node):
        while current_node.left is not None:
            current_node = current_node.left
        return current_node
    
    def print_in_order(self):
        if self.root is not None:
            self._print_in_order(self.root)

    def _print_in_order(self, current_node):
        if current_node is not None:
            self._print_in_order(current_node.left)
            current_node.print_empleado()
            self._print_in_order(current_node.right)

    def print_pre_order(self):
        if self.root is not None:
            self._print_pre_order(self.root)

    def _print_pre_order(self, current_node):
        if current_node is not None:
            current_node.print_empleado()
            self._print_pre_order(current_node.left)
            self._print_pre_order(current_node.right)

    def print_post_order(self):
        if self.root is not None:
            self._print_post_order(self.root)

    def _print_post_order(self, current_node):
        if current_node is not None:
            self._print_post_order(current_node.left)
            self._print_post_order(current_node.right)
            current_node.print_empleado()
    
    def print_ordered_by_attribute(self, attribute):
        if self.root is not None:
            empleados = []
            self._get_empleados_in_order(self.root, empleados, attribute)
            for empleado in empleados:
                empleado.print_empleado()

    def _get_empleados_in_order(self, current_node, empleados, attribute):
        if current_node is not None:
            self._get_empleados_in_order(current_node.left, empleados, attribute)
            empleados.append(current_node)
            self._get_empleados_in_order(current_node.right, empleados, attribute)
        if attribute == "name":
            #Usamos la funcion sort de las listas para ordenar los empleados
            #Especificando el parametro key que define una funcion especial para el ordenamiento
            #En este caso, se ordena por el atributo name, usando una funcion lambda para declarar
            #una función anónima que toma instancias de empleados y devuelve el valor de su atributo name
            empleados.sort(key=lambda x: x.name)
        elif attribute == "id":
            empleados.sort(key=lambda x: x.id)
        elif attribute == "position":
            empleados.sort(key=lambda x: x.position)
        elif attribute == "salary":
            empleados.sort(key=lambda x: x.salary)
        elif attribute == "date_of_recruitment":
            empleados.sort(key=lambda x: x.date_of_recruitment)
    
    def empty(self):
        return self.root is None

def fecha(fecha):
    # Separa la cadena de texto separando cada valor en su variable
    dia, mes, ano = fecha.split("/")

    # Se convierte en el texto en numero
    try:
        dia = int(dia)
        mes = int(mes)
        ano = int(ano)
    except ValueError:
        Accion("Error", "La fecha solo admite el formato dd/mm/aaaa").guardar()
        print('\n( X ) La fecha solo admite el formato dd/mm/aaaa')
    # Crea el objeto del tipo Fecha
    fechaObjeto = date(ano, mes, dia)

    Accion("Operacion", "Se creo el objeto de la fecha {}".format(fecha)).guardar()
  
    # Retorna el objeto
    return fechaObjeto

def create_empleado():
    hotel= input("Nombre del hotel: ")
    name = input("ENombre del empleado: ")
    id = int(input("Cédula: "))
    position = input("Posición: ")
    salary = float(input("Salario: "))
    date_of_recruitment = fecha(input("Fecha de contratación (dd/mm/aaaa): "))
    empleado = Empleado(hotel, id, name, position, salary, date_of_recruitment)
    return empleado


def print_menu():
    print("1. Crear Empleado")
    print("2. Eliminar Empleado")
    print("3. Buscar Empleado")
    print("4. Modificar Empleado")
    print("5. Listar todos los Empleados")
    print("6. Listar todos los Empleados ordenardos por atributo")
    print("7. Salir")

