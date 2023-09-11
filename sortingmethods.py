
#Tipo de Ordenamiento:
#
#1. MergeSort: Ordenamiento de costo total por un rango de Fechas
#
def mergesort_RangoFechas_ASC(arr):
    if len(arr) > 1:
        mid = len(arr)//2

        L = arr[:mid]
        R = arr[mid:]

        mergesort_RangoFechas_ASC(L)
        mergesort_RangoFechas_ASC(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i].getCostoTotal() <= R[j].getCostoTotal():
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    
    return arr

def mergesort_RangoFechas_DESC(arr):
    if len(arr) > 1:
        mid = len(arr)//2

        L = arr[:mid]
        R = arr[mid:]

        mergesort_RangoFechas_DESC(L,)
        mergesort_RangoFechas_DESC(R,)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i].getCostoTotal() >= R[j].getCostoTotal():
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    
    return arr

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

def quickSort_Multiple_ASC(arr, criterio1, criterio2):
    if len(arr) <= 1:
        return arr
    smaller, larger, pi= __particion_Multiple_ASC(arr, criterio1, criterio2)
    return quickSort_Multiple_ASC(smaller, criterio1, criterio2) + [pi] + quickSort_Multiple_ASC(larger,criterio1, criterio2)

def __particion_Multiple_ASC(arr, criterio1, criterio2):
    pivot = arr[len(arr) // 2]
    smaller = []
    larger = []
    for item in arr:
        if getattr(item.habitacion, criterios[criterio1]) < getattr(pivot.habitacion, criterios[criterio1] ) and getattr(item.habitacion, criterios[criterio2])< getattr(pivot.habitacion, criterios[criterio2]):
            smaller.append(item)

        elif getattr(item.habitacion, criterios[criterio1]) > getattr(pivot.habitacion, criterios[criterio1] ) and getattr(item.habitacion, criterios[criterio2]) > getattr(pivot.habitacion, criterios[criterio2]):
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
    n = len(arr)

    for i in range(n//2-1, -1, -1):
        __heapify_Duracion_ASC(arr, n, i)

    for i in range(n-1, 0, -1):
        (arr[i], arr[0]) = (arr[0], arr[i])
        __heapify_Duracion_ASC(arr, i, 0)
    
    return arr

def __heapify_Duracion_ASC(arr, n, i):
    largerst = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i].getDuracion() < arr[l].getDuracion():
        largerst = l
    
    if r < n and arr[largerst].getDuracion() < arr[r].getDuracion():
        largerst = r

    if largerst != i:
        (arr[i], arr[largerst]) = (arr[largerst], arr[i])
    
        __heapify_Duracion_ASC(arr, n, largerst)

def heapSort_Duracion_DESC(arr):
    n = len(arr)

    for i in range(n//2-1, -1, -1):
        __heapify_Duracion_DESC(arr, n, i)
    
    for i in range(n-1, 0, -1):
        (arr[i], arr[0]) = (arr[0], arr[i])
        __heapify_Duracion_DESC(arr, i, 0)
    
    return arr

def __heapify_Duracion_DESC(arr, n, i):
    largerst = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i].getDuracion() > arr[l].getDuracion():
        largerst = l
    
    if r < n and arr[largerst].getDuracion() > arr[r].getDuracion():
        largerst = r

    if largerst != i:
        (arr[i], arr[largerst]) = (arr[largerst], arr[i])
    
        __heapify_Duracion_DESC(arr, n, largerst)

#
#4. Shellsort: Ordenamiento del cliente segun el numero de reservaciones que tenga
#
def shellsort_NoReservaciones_DESC(arr):
    n = len(arr) 
    gap = n // 2
    while gap > 0: 
        for i in range(gap, n): 
            temp = arr[i]
            j = i
            while  j >= gap and arr[j - gap].getTotalReservaciones() < temp.getTotalReservaciones(): 
                arr[j] = arr[j - gap]
                j -= gap  
            arr[j] = temp 
        gap //= 2
    
    return arr

def shellsort_NoReservaciones_ASC(arr):
    n = len(arr) 
    gap = n // 2
    while gap > 0: 
        for i in range(gap, n): 
            temp = arr[i]
            j = i
            while  j >= gap and arr[j - gap].getTotalReservaciones() > temp.getTotalReservaciones(): 
                arr[j] = arr[j - gap]
                j -= gap  
            arr[j] = temp 
        gap //= 2
    
    return arr
