
#Tipo de Ordenamiento:
# 
#1. MergeSort: Ordenamiento de costo total por un rango de Fechas
#  
def mergesort_RangoFechas_ASC(arr): 
    if len(arr) > 1: 
        mid = len(arr)//2

        #La listas `L` y `R` almacenaran los elemento de la lista `arr` que ayudaran
        # a organizar la lista `arr`
        L = arr[:mid]   # `L` almacenara los elementos del lado izquierdo hasta la mitad de la lista `arr`
        R = arr[mid:]   # `R` almacenara los elementos de la mitad hasta el lado derecho de la lista `arr`

        #Llamada recursiva que dividira `L`
        mergesort_RangoFechas_ASC(L)

        #Llamada recursiva que dividira `R`
        mergesort_RangoFechas_ASC(R)

        #Inicializacion de los indices que se usaran para las listas `arr`, `L` y `R`
        i = j = k = 0

        #Ciclo que comparar quien es el menor de los elementos que contiene las lista `L` y `R`
        # y los almacenara nuevamente en la lista `arr`, este ciclo finalizara cuando cualquiera 
        # de las dos listas `L` y `R` termine de recorreser por complento 
        while i < len(L) and j < len(R):
            if L[i].getCostoTotal() <= R[j].getCostoTotal():
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        #En el caso de que la lista `R` fue el primero en recorrese por completo, este ciclo
        # almacenara en la lista `arr` los elementos restantes de la lista `L`, y finalizara cuando 
        # `L` se recorra por completo
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
    
        #En el caso de que la lista `L` fue el primero en recorrese por completo, este ciclo
        # almacena en la lista `arr` los elementos restantes de la lista `R`, y finalizara cuando
        # `R` se recorra por completo
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def mergesort_RangoFechas_DESC(arr): 
    if len(arr) > 1: 
        mid = len(arr)//2

        #La listas `L` y `R` almacenaran los elemento de la lista `arr` que ayudaran
        # a organizar la lista `arr`
        L = arr[:mid]   # `L` almacenara los elementos del lado izquierdo hasta la mitad de la lista `arr`
        R = arr[mid:]   # `R` almacenara los elementos de la mitad hasta el lado derecho de la lista `arr`

        #Llamada recursiva que dividira `L`
        mergesort_RangoFechas_DESC(L)
        
        #Llamada recursiva que dividira `R`
        mergesort_RangoFechas_DESC(R)

        #Inicializacion de los indices que se usaran para las listas `arr`, `L` y `R`
        i = j = k = 0

        #Ciclo que comparar quien es el menor de los elementos que contiene las lista `L` y `R`
        # y los almacenara nuevamente en la lista `arr`, este ciclo finalizara cuando cualquiera 
        # de las dos listas `L` y `R` termine de recorreser por complento 
        while i < len(L) and j < len(R):
            if L[i].getCostoTotal() >= R[j].getCostoTotal():
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        #En el caso de que la lista `R` fue el primero en recorrese por completo, este ciclo
        # almacenara en la lista `arr` los elementos restantes de la lista `L`, y finalizara cuando 
        # `L` se recorra por completo
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        #En el caso de que la lista `L` fue el primero en recorrese por completo, este ciclo
        # almacena en la lista `arr` los elementos restantes de la lista `R`, y finalizara cuando
        # `R` se recorra por completo
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

#
#
#2. Quicksort: Ordenamiento Multiple
#

criterios= ["capacidad","fechaEntrada","id"]

def quickSort_NoMultiple_ASC(arr, low, high, criterio):
    if low < high:
        pi = __particion_NoMultiple_ASC(arr, low, high, criterio)
        quickSort_NoMultiple_ASC(arr, low, pi-1, criterio)
        quickSort_NoMultiple_ASC(arr, pi+1, high, criterio)
    return arr

def __particion_NoMultiple_ASC(arr, low, high, criterio):
    i = low - 1

    if criterio == 0 or criterio == 2:
        pivot = getattr(arr[high].habitacion, criterios[criterio])
        for j in range(low, high):
            if getattr(arr[j].habitacion,criterios[criterio]) <=  pivot:
                i +=1
                (arr[i], arr[j]) = (arr[j], arr[i])
        i = i + 1
        (arr[i], arr[high]) = (arr[high], arr[i])
        return i
    else:
        pivot = getattr(arr[high], criterios[criterio])
        for j in range(low, high):
            if getattr(arr[j],criterios[criterio]) <=  pivot:
                i +=1
                (arr[i], arr[j]) = (arr[j], arr[i])
        i = i + 1
        (arr[i], arr[high]) = (arr[high], arr[i])
        return i

def quickSort_NoMultiple_DESC(arr, low, high, criterio):
    if low < high:
        pi = __particion_NoMultiple_DESC(arr, low, high, criterio)
        quickSort_NoMultiple_DESC(arr, low, pi-1, criterio)
        quickSort_NoMultiple_DESC(arr, pi+1, high, criterio)
    return arr

def __particion_NoMultiple_DESC(arr, low, high, criterio):
    i = low - 1
    
    if criterio == 0 or criterio == 2:
        pivot = getattr(arr[high].habitacion, criterios[criterio])
        for j in range(low, high):
            if getattr(arr[j].habitacion,criterios[criterio]) >=  pivot:
                i +=1
                (arr[i], arr[j]) = (arr[j], arr[i])
        i = i + 1
        (arr[i], arr[high]) = (arr[high], arr[i])
        return i
    else:
        pivot = getattr(arr[high], criterios[criterio])
        for j in range(low, high):
            if getattr(arr[j],criterios[criterio]) >=  pivot:
                i +=1
                (arr[i], arr[j]) = (arr[j], arr[i])
        i = i + 1
        (arr[i], arr[high]) = (arr[high], arr[i])
        return i

def quickSort_Multiple_ASC(arr):
    if len(arr) <= 1:
        return arr
    smaller, larger, pi= __particion_Multiple_ASC(arr)
    return quickSort_Multiple_ASC(smaller) + [pi] + quickSort_Multiple_ASC(larger)

def __particion_Multiple_ASC(arr):
    pivot = arr[len(arr) // 2]
    smaller = []
    larger = []
    for item in arr:
        if item.getDuracion() < pivot.getDuracion() and item.getCostoTotal() < pivot.getCostoTotal():
            smaller.append(item)

        elif item.getDuracion() > pivot.getDuracion() and item.getCostoTotal() > pivot.getCostoTotal():
            larger.append(item)

    return smaller, larger, pivot

def quickSort_Multiple_DESC(arr):
    if len(arr) <= 1:
        return arr
    smaller, larger, pi= __particion_Multiple_DESC(arr)
    return quickSort_Multiple_DESC(smaller) + [pi] + quickSort_Multiple_DESC(larger)

def __particion_Multiple_DESC(arr):
    pivot = arr[len(arr) // 2]
    smaller = []
    larger = []
    for item in arr:
        if item.getDuracion() > pivot.getDuracion() and item.getCostoTotal() > pivot.getCostoTotal():
            smaller.append(item)

        elif item.getDuracion() < pivot.getDuracion() and item.getCostoTotal() < pivot.getCostoTotal():
            larger.append(item)

    return smaller, larger, pivot
#
#3. Heapsort: Ordenamiento segun su duracion de reserva
#
def heapSort_Duracion_ASC(arr):
    """
        La funcion `heapSort_Duracion_ASC` ordena de forma ascendente una lista tomando
        como criterio de ordenamiento la duracion de la reservar

        :param arr: El parametro `arr` representa la lista que se desea ordenar
    """
    # Inicializamos `n` almacenando la longitud de la lista
    n = len(arr)

    #Ciclo que construye el arbol binario y lo ordena 
    # de mayor a menor
    for i in range(n//2-1, -1, -1):
        __heapify_Duracion_ASC(arr, n, i)
    
    for i in range(n-1, 0, -1):
        (arr[i], arr[0]) = (arr[0], arr[i])
        __heapify_Duracion_ASC(arr, i, 0)
    
    return arr

def __heapify_Duracion_ASC(arr, n, i):
    """
    La función `__heapify_Duracion_ASC` compara los elementos de la lista de para ordenarlos de forma
    ascendente
    
    :param arr: el parametro `arr` es una lista que contiene elementos que es necesario reorganizarlo
    :param n: el parametro "n" representa el tamaño de la lista `arr` o el número de elementos en la lista `arr`
    :param i: el parametro "i" representa el índice del nodo actual
    """

    #Inicializamos los indices de los nodos
    largerst = i   # Indice para el nodo principal
    l = 2 * i + 1   # Indice de los nodos izquierdas 
    r = 2 * i + 2   # Indice de las nodos derechas

    # Condicion que compara si son mayores los nodos secundario 
    # de la izquierda con el nodo principal
    if l < n and arr[i].getDuracion() < arr[l].getDuracion():
        largerst = l
    
    # Condicion que compara si son mayores los nodos secundario 
    # de la derecha con el nodo principal
    if r < n and arr[largerst].getDuracion() < arr[r].getDuracion():
        largerst = r

    # Condicion que cambia la variable `largerst` si es necesario
    if largerst != i:
        (arr[i], arr[largerst]) = (arr[largerst], arr[i])
        
        __heapify_Duracion_ASC(arr, n, largerst)

def heapSort_Duracion_DESC(arr):
    """
        La funcion `heapSort_Duracion_DESC` ordena de forma descendente una lista tomando
        como criterio de ordenamiento la duracion de la reservar
        
        :param arr: El parametro `arr` representa la lista que se desea ordenar
    """
    # Inicializamos `n` almacenando la longitud de la lista
    n = len(arr)

    #Ciclo que construye el arbol binario y lo ordena 
    # de menor a mayor
    for i in range(n//2-1, -1, -1):
        __heapify_Duracion_DESC(arr, n, i)
    
    # Ciclo que extrae los elementos uno a uno y los 
    # almacena nuevamente en `arr` de forma ordenada
    for i in range(n-1, 0, -1):
        (arr[i], arr[0]) = (arr[0], arr[i])
        __heapify_Duracion_DESC(arr, i, 0)
    
    return arr

def __heapify_Duracion_DESC(arr, n, i):
    """
    La función `__heapify_Duracion_DESC` compara los elementos de la lista de para ordenarlos de forma
    descendente
    
    :param arr: el parametro `arr` es una lista que contiene elementos que es necesario reorganizarlo
    :param n: el parametro "n" representa el tamaño de la lista `arr` o el número de elementos en la lista `arr`
    :param i: el parametro "i" representa el índice del nodo actual
    """
    #Inicializamos los indices de los nodos
    largerst = i   # Indice para el nodo principal
    l = 2 * i + 1   # Indice de los nodos izquierdas 
    r = 2 * i + 2   # Indice de las nodos derechas

     # Condicion que compara si son menores los nodos secundario 
    # de la izquierda con el nodo principal
    if l < n and arr[i].getDuracion() > arr[l].getDuracion():
        largerst = l
    
    # Condicion que compara si son menores los nodos secundario 
    # de la derecha con el nodo principal
    if r < n and arr[largerst].getDuracion() > arr[r].getDuracion():
        largerst = r

     # Condicion que cambia la variable `largerst` si es necesario
    if largerst != i:
        (arr[i], arr[largerst]) = (arr[largerst], arr[i])
    
        __heapify_Duracion_DESC(arr, n, largerst)

#
#4. Shellsort: Ordenamiento del cliente segun el numero de reservaciones que tenga
#
def shellsort_NoReservaciones_DESC(arr):
    """
        La funcion `shellsort_NoReservaciones_DESC` ordena de forma descendiente una lista
        tomando como criterio el numero de reservaciones 

        :param arr: El parametro `arr` representa la lista que se quiere ordenar
    """
    
    n = len(arr)    #Almacenamos el tamaño de la lista
    
    gap = n // 2    #Inicializamos el tamaño de espacio 

    # Realiza una clasificación de inserción con espacios usando la variable `gap`.
    # Los primeros elementos del espacio a[0..gap-1] ya están en el espacio
    # orden sigue añadiendo un elemento más hasta completar el array
    # está ordenado por espacios
    while gap > 0: 
        for i in range(gap, n): 

            # Agregamos arr[i] a los elementos que han sido ordenados por espacios
            # guardamos arr[i] en una variable temporal `temp` y hacemos un agujero en la posición i
            temp = arr[i]
            
            # Desplazar elementos anteriores ordenados por espacios hasta encontrar 
            # la ubicación correcta para arr[i]
            j = i
            while  j >= gap and arr[j - gap].getTotalReservaciones() < temp.getTotalReservaciones(): 
                arr[j] = arr[j - gap]
                j -= gap  

            # Colcamos temp en la arr[i] en su ubicación correcta
            arr[j] = temp 
        gap //= 2
    
    return arr

def shellsort_NoReservaciones_ASC(arr):
    """
        La funcion `shellsort_NoReservaciones_DESC` ordena de forma descendiente una lista
        tomando como criterio el numero de reservaciones 

        :param arr: El parametro `arr` representa la lista que se quiere ordenar
    """
    n = len(arr)    #Almacenamos el tamaño de la lista
    
    gap = n // 2    #Inicializamos el tamaño de espacio 

    # Realiza una clasificación de inserción con espacios usando la variable `gap`.
    # Los primeros elementos del espacio a[0..gap-1] ya están en el espacio
    # orden sigue añadiendo un elemento más hasta completar el array
    # está ordenado por espacios
    while gap > 0: 
        for i in range(gap, n):

            # Agregamos arr[i] a los elementos que han sido ordenados por espacios
            # guardamos arr[i] en una variable temporal `temp` y hacemos un agujero en la posición i
            temp = arr[i]

            # Desplazar elementos anteriores ordenados por espacios hasta encontrar 
            # la ubicación correcta para arr[i]
            j = i
            while  j >= gap and arr[j - gap].getTotalReservaciones() > temp.getTotalReservaciones(): 
                arr[j] = arr[j - gap]
                j -= gap  
                
            #Colcamos temp en la arr[i] en su ubicación correcta
            arr[j] = temp 
        gap //= 2
    
    return arr
