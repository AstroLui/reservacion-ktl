import random
#Tipo de Ordenamiento:
# 
#1. Ordenamiento MergeSort
#
# La primera sub-lista ira desde [l....m] y la nombramos como L(left)
# La segunda sub-lista ira desde [m+1....r] y la nombramos como R(right)
def Merge(arr, l, m, r):
    """
    La funcion Merge toma un lista, las divide en dos sub-lista, y luego las fusiona de forma ordenada
    
    :param arr: Es la lista que debe de ser ordenada
    :param l: Representa el indice inicial de la sub-lista que deben fusionarse 
    :param m: Representa el indice medio de la lista `arr`, se utiliza para dividir la lista en dos sub-lista
    :param r: Representa el indice del ultimo elemento de la sub-lista que deben fusionarse
    """

    # Las expresiones `n1 = m - l + 1` y `n2 = r - m` calculan los tamaños de las dos sub-lista
    # que se fusionarán, 
    n1 = m - l + 1      # `n1` para la sub-lista `L`
    n2 = r - m          # `n2` para la sub-lista `R`

    #Inicializacion de las dos sub-lista 
    L=[0] * (n1)  
    R=[0] * (n2)    

    # Copiamos los elementos de la lista `arr` en las sub-listas, para la sub-lista `L` se copiaran los elementos 
    # que estan antes de la mitad de la lista y para `R` los elementos que vienen despues de la mitad
    for i in range(0, n1):
        L[i] = arr[i + l] 

    for j in range(0, n2): 
        R[j] = arr[m + 1 +j]

    #Fusionamos las sub-lista y convertir nuevamente `arr[l..r]` ordenada

    i = 0   # Índice inicial de la sub-lista `L`
    j = 0   # Índice inicial de la sub-lista `R`
    k = l   # Índice inicial de la lista fusionado `arr`

    # Se evalua cual de los elementos de las sub-listas `L` y `R` son menores,  
    # y se le asigna al `arr`, hasta que alguna de las sub-listas se termine de recorrer
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i +=1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    
    # Si la sub-lista `R` termino primero de recorrer, se le asignara a `arr`
    # los demas elementos faltantes de la sub-lista `L`
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    
    # En caso contrario, se le asignara a `arr` los demas elementos faltantes de la
    # sub-lista `R`
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def mergeSort(arr, l, r):
    """
    La función mergeSort implementa el algoritmo Merge para ordenar una lista en orden ascendente
    
    :param arr: Es la lista que debe de ser ordenada
    :param l: Representa el índice izquierdo del subarreglo que debe ordenarse
    :param r: Representa el índice derecho del subarreglo que debe ordenarse
    """
    
    if l < r:
        # La expresión `m = l + (r-l)//2` está calculando el índice medio de la lista `arr` en orden
        # para dividirlo en dos subarreglos. Es equivalente a `m = (l + r) // 2`, pero usando `l + (r-l)//2`
        # en lugar de `(l+r)//2` ayuda a evitar el desbordamiento de enteros cuando se trata de valores grandes de `l`
        # y `r`.
        m = l + (r-l)//2
        
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        Merge(arr, l, m, r) 


def MergeSort(arr): 
    if len(arr) > 1: 
        mid = len(arr)//2

        L = arr[:mid]
        R = arr[mid:]

        MergeSort(L)
        MergeSort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
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

"""
arr = [random.randint(1, 20) for i in range(1)]
for i in range(len(arr)):
    print("%d" % arr[i],end=" ")
print()

temp = arr
n = len(arr)
MergeSort(temp)
mergeSort(arr, 0, n-1)

print("Vector Ordenado por mergeSort")
for i in range(len(arr)):
    print("%d" % arr[i],end=" ")
print()
print("Vector Ordenado por MergeSort")
for i in range(len(temp)):
    print("%d" % temp[i],end=" ")
"""

#2. Quicksort

def particion(arr, low, high):
    """
    La función `particion` toma una lista `arr`, un índice inicial `low` y un índice del ultimo elemento `high`, y
    divide la lista en función de un elemento pivote.
    
    :param arr: El parámetro "arr" es una lista de elementos que deben particionarse
    :param low: El parámetro "low" representa el índice inicial de la lista que necesita
     ser dividido
    :param high: El parámetro "high" representa el índice del último elemento de la lista "arr"
    :return: el índice del elemento pivote después de particionar la lista.
    """
    pivot = arr[high]  #Usaremos de pivote el utimo elemento de la lista `arr`

    # Puntero para elemento mayor
    i = low - 1

    # Recorremos todos los elementos, comparando cada elemento
    # con el pivote
    for j in range(low, high):
        if arr[j] <=  pivot:

            # Si se encuentra un elemento más pequeño que el pivote
            # intercambiarlo con el elemento mayor señalado por i
            i +=1

            # Intercambiamos el elemento i con elemento en j
            (arr[i], arr[j]) = (arr[j], arr[i])
    i = i + 1
    # Intercambiar el elemento pivote con el elemento mayor especificado por i
    (arr[i], arr[high]) = (arr[high], arr[i])
    
    # Devuelve la posición desde donde se realiza la partición
    return i


def quickSort(arr, low, high):
    """
    La funcion recursiva `quickSort`, implemente la funcion `particion` para realizar distintas particiones
    alrededor de un pivote, para ordenar de manera ascendente los elementos de una lista
    
    :param arr: La lista de entrada que debe ordenarse
    :param low: Representa el índice inicial del lista que debe ser ordenado
    :param high: Representa el índice del último elemento de la lista
     eso necesita ser ordenado
    """
    if low < high:

        # Encuentra un elemento pivote tal que
        # elemento más pequeño que el pivote está a la izquierda
        # elemento mayor que el pivote está a la derecha
        pi = particion(arr, low, high)

        # Llamada recursiva a la izquierda de pivote
        quickSort(arr, low, pi-1)

        #LLamada recursiva a la derecha del pivote
        quickSort(arr, pi+1, high)

arr = [random.randint(1, 20) for i in range(10)]
n = len(arr)
quickSort(arr, 0, n-1)
for i in range(len(arr)):
    print("%d" % arr[i],end=" ")

#3. Heapsort
def heapify(arr, n, i):
    largerst = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largerst = l
    
    if r < n and arr[largerst] < arr[r]:
        largerst = r

    if largerst != i:
        (arr[i], arr[largerst]) = (arr[largerst], arr[i])
    
        heapify(arr, n, largerst)

def heapSort(arr):
    n = len(arr)

    for i in range(n//2-1, -1, -1):
        heapify(arr, n, i)
    
    for i in range(n-1, 0, -1):
        (arr[i], arr[0]) = (arr[0], arr[i])
        heapify(arr, i, 0)

#heapSort(arr)


#4. Shellsort
def shellsort(arr):
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i 
            while j >= gap and arr[j-gap] > temp:
                arr[j] = arr[j-gap]
                j -= gap
            
            arr[j] = temp
        gap //= 2

arr = [ 12, 34, 54, 2, 3]
#shellsort(arr)
