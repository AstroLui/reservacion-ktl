class Nodo: 
    def __init__(self, value):
        self.Value = value
        self.Height = 1 
        self.Left = None
        self.Right= None

class Factura: 
    def __init__(self, Reserva, NumeroF): 
        self.Reserva= Reserva
        self.Estado = 'Pendiente'
        self.NumeroF = NumeroF 
    
    def InfoFactura(self): 
        print('\n++ FACTURA No.{} del {} ++'.format(self.NumeroF, self.Reserva.hotel))
        print(' - Nombre y Apellido del Cliente: {}'.format(self.Reserva.usuario.nombre))
        print(' - IDN del Cliente: {}'.format(self.Reserva.usuario.idn))
        print(' - Metodo de Pago: {}'.format(self.Reserva.metodoPago))
        print(' - Estado de Pago: {}'.format(self.Estado))

        print('=======================================================================')
        print('ID de la Reservacion     Tipo de habitacion    Duracion     Costo Total')
        print("{:^22} {:^22} {:^10} {:>10}$".format(self.Reserva.id, self.Reserva.habitacion.tipo, self.Reserva.duracion.days, self.Reserva.costoTotal))
        print('=======================================================================')

    def InfoFacturaLineal(self):
        return "FACTURA No. {}, ID de la Reserva: {}, Nombre del Cliente: {}, Costo Total de la Reserva: {}$, Metodo de Pago: {}, Estado de Pago: {}".format(
        self.NumeroF, self.Reserva.id, self.Reserva.usuario.nombre, self.Reserva.costoTotal, self.Reserva.metodoPago, self.Estado)
    
class AVL: 
    def __init__(self): 
        self.Root = None
    
    def Add(self, value): 
       self.Root = self.__Adding__(self.Root, value)

    def __Adding__(self, current_nodo, value):
        if current_nodo is None: 
            return Nodo(value) 
        
        if value.NumeroF < current_nodo.Value.NumeroF: 
            current_nodo.Left = self.__Adding__(current_nodo.Left, value)
        elif value.NumeroF > current_nodo.Value.NumeroF: 
            current_nodo.Right = self.__Adding__(current_nodo.Right, value)
        else: 
            return current_nodo
        
        current_nodo.Height= 1 + max(self.__Height__(current_nodo.Left), self.__Height__(current_nodo.Right))

        Fe = self.__FactorEquilibrio__(current_nodo)

        if Fe > 1 and value.NumeroF < current_nodo.Left.Value.NumeroF: 
            return self.__RotateRight__(current_nodo)
        if Fe < -1 and value.NumeroF > current_nodo.Right.Value.NumeroF: 
            return self.__RotateLeft__(current_nodo)
        if Fe > 1 and value.NumeroF > current_nodo.Left.Value.NumeroF: 
            current_nodo.Left = self.__RotateLeft__(current_nodo.Left)
            return self.__RotateRight__(current_nodo)
        if Fe < -1 and value.NumeroF < current_nodo.Left.Value.NumeroF: 
            current_nodo.Right = self.__RotateRight__(current_nodo.Left)
            return self.__RotateLeft__(current_nodo)
        
        return current_nodo
    
    __criterios = ["idn", "costoTotal", "hotel", "NumeroF"]
    def Search(self, value, i):
        self.__Searching__(self.Root, value, i)
        
    def __Searching__(self, Nodo, value, i):
        if Nodo is not None:
            if i == 0:  
                if getattr(Nodo.Value.Reserva.usuario, self.__criterios[i]) == value:
                    Nodo.Value.InfoFactura() 
                if Nodo.Left is not None:
                    self.__Searching__(Nodo.Left, value, i)
                if Nodo.Right is not None: 
                    self.__Searching__(Nodo.Right, value, i)
            elif i == 1: 
                if getattr(Nodo.Value.Reserva, self.__criterios[i]) >= value:
                    Nodo.Value.InfoFactura() 
                if Nodo.Left is not None:
                    self.__Searching__(Nodo.Left, value, i)
                if Nodo.Right is not None: 
                    self.__Searching__(Nodo.Right, value, i)
            elif i == 2:
                if getattr(Nodo.Value.Reserva, self.__criterios[i]) == value:
                    Nodo.Value.InfoFactura() 
                if Nodo.Left is not None:
                    self.__Searching__(Nodo.Left, value, i)
                if Nodo.Right is not None: 
                    self.__Searching__(Nodo.Right, value, i)
            else:
                if getattr(Nodo.Value, self.__criterios[i]) == value:
                    Nodo.Value.InfoFactura() 
                if Nodo.Left is not None:
                    self.__Searching__(Nodo.Left, value, i)
                if Nodo.Right is not None: 
                    self.__Searching__(Nodo.Right, value, i)

    def SearchLineal(self, value, i, arbol):
        self.__SearchingLineal__(self.Root, value, i, arbol)
        
    def __SearchingLineal__(self, Nodo, value, i, arbol):
        if Nodo is not None:
            arbol.Add(Nodo.Value)
            if i == 0:  
                if getattr(Nodo.Value.Reserva.usuario, self.__criterios[i]) == value:
                    print(Nodo.Value.InfoFacturaLineal()) 
                if Nodo.Left is not None:
                    self.__SearchingLineal__(Nodo.Left, value, i, arbol)
                if Nodo.Right is not None: 
                    self.__SearchingLineal__(Nodo.Right, value, i, arbol)
            elif i == 1: 
                if getattr(Nodo.Value.Reserva, self.__criterios[i]) >= value:
                    print(Nodo.Value.InfoFacturaLineal()) 
                if Nodo.Left is not None:
                    self.__SearchingLineal__(Nodo.Left, value, i, arbol)
                if Nodo.Right is not None: 
                    self.__SearchingLineal__(Nodo.Right, value, i, arbol)
            elif i == 2:
                if getattr(Nodo.Value.Reserva, self.__criterios[i]) == value:
                    print(Nodo.Value.InfoFacturaLineal()) 
                if Nodo.Left is not None:
                    self.__SearchingLineal__(Nodo.Left, value, i, arbol)
                if Nodo.Right is not None: 
                    self.__SearchingLineal__(Nodo.Right, value, i, arbol)
            else:
                if getattr(Nodo.Value, self.__criterios[i]) == value:
                    print(Nodo.Value.InfoFacturaLineal()) 
                if Nodo.Left is not None:
                    self.__SearchingLineal__(Nodo.Left, value, i, arbol)
                if Nodo.Right is not None: 
                    self.__SearchingLineal__(Nodo.Right, value, i, arbol)

    def Delete(self, value):
        i = Factura(self.Root.Value, value-1)
        self.Root = self.__Deleting__(self.Root, i)
    
    def __Deleting__(self, Nodo, i): 
        if Nodo is None: 
            return Nodo
        if  Nodo.Value.NumeroF > i.NumeroF: 
            Nodo.Left = self.__Deleting__(Nodo.Left, i)
        elif Nodo.Value.NumeroF < i.NumeroF: 
            Nodo.Right = self.__Deleting__(Nodo.Right, i)
        else: 
            if Nodo.Left is None or Nodo.Right is None: 
                temp = None
                if temp == Nodo.Left: 
                    temp = Nodo.Right
                else:
                    temp = Nodo.Left
                
                if temp is None:
                    Nodo = None
                else: 
                    Nodo = temp
            else:
                temp = self.__Predecesor__(Nodo.Left)
                Nodo.Value = temp.Value
                Nodo.Left = self.__Deleting__(Nodo.Left, temp.Value)
        
        if Nodo is None: 
            return Nodo
        
        Nodo.Height = max(self.__Height__(Nodo.Left), self.__Height__(Nodo.Right)) + 1

        Fe = self.__FactorEquilibrio__(Nodo)
        if Fe > 1 and self.__FactorEquilibrio__(Nodo.Left) >= 0:
            return self.__RotateRight__(Nodo)
        if Fe < -1 and self.__FactorEquilibrio__(Nodo.Right) <= 0: 
            return self.__RotateLeft__(Nodo)  
        if Fe > 1 and self.__FactorEquilibrio__(Nodo.Left) < 0: 
            Nodo.Left = self.__RotateLeft__(Nodo.Left)
            return self.__RotateRight__(Nodo)
        if Fe < -1 and self.__FactorEquilibrio__(Nodo.Right) > 0:
            Nodo.Right = self.__RotateRight__(Nodo.Right)
            return self.__RotateLeft__(Nodo)
        
        return Nodo


    def __RotateRight__(self, Nodo):
        new_root = Nodo.Left
        temp = new_root.Right

        new_root.Right = Nodo
        Nodo.Left = temp

        Nodo.Height = max(self.__Height__(Nodo.Left), self.__Height__(Nodo.Right)) + 1
        new_root.Height = max(self.__Height__(new_root.Left), self.__Height__(new_root.Right)) + 1

        return new_root
    
    def __RotateLeft__(self, Nodo): 
        new_root = Nodo.Right
        temp = new_root.Left

        new_root.Left= Nodo
        Nodo.Right = temp

        Nodo.Height = max(self.__Height__(Nodo.Left), self.__Height__(Nodo.Right)) + 1
        new_root.Height = max(self.__Height__(new_root.Left), self.__Height__(new_root.Right)) + 1

        return new_root

    def __Height__(self, Nodo): 
        if Nodo is None: 
            return 0
        return Nodo.Height

    def __FactorEquilibrio__(self, Nodo):
        if Nodo is None: 
            return 0
        return self.__Height__(Nodo.Left) - self.__Height__(Nodo.Right)

    def __Predecesor__(self, Nodo): 
        Current_Nodo = Nodo
        while Current_Nodo.Right != None: 
            Current_Nodo = Current_Nodo.Right
        
        return Current_Nodo
    
    def Show(self):
        self.__Showing__(self.Root)
    
    def __Showing__(self, nodo_actual):
        if nodo_actual is not None:
            self.__Showing__(nodo_actual.Left)
            print(nodo_actual.Value.InfoFacturaLineal())
            self.__Showing__(nodo_actual.Right)

    def __SearchingR__(self, Nodo, value):
        if Nodo is not None: 
            if getattr(Nodo.Value, "NumeroF") == value:
                return Nodo 
            if Nodo.Left is not None:
                return self.__SearchingR__(Nodo.Left, value)
            if Nodo.Right is not None: 
                return self.__SearchingR__(Nodo.Right, value)
        return Nodo
    
    def Pay(self, limit):
        print('\n_________')
        self.Show()
        
        numero = int(input('Seleccion el numero de factura que desea pagar: '))
        if numero > limit: 
            raise ValueError
        self.Search(numero, 3)
        Temp = self.__SearchingR__(self.Root, numero)
        if (Temp.Value.Reserva.getCostoTotal() != 0):
            costo = int(input('Ingrese el monto del costo: '))
            if costo <= Temp.Value.Reserva.getCostoTotal():
                Temp.Value.Reserva.setCostoTotal(costo)
                print("Monto ingresado correctamente!!")
            else:
                raise ValueError

        else: 
            print('Ya la reserva ha sido cancelada')
        if(Temp.Value.Reserva.getCostoTotal() == 0):
            Temp.Value.Estado = 'Cancelado'

def heightAVL(root):
    if root is None:
        return 0
    
    return 1 + max(heightAVL(root.Left), heightAVL(root.Right))