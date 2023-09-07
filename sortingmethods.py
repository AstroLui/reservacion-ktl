
#Tipo de Ordenamiento:
# 
#1. MergeSort
#

def mergesortRangoASC(arr): 
    if len(arr) > 1: 
        mid = len(arr)//2

        L = arr[:mid]
        R = arr[mid:]

        mergesortRangoASC(L,)
        mergesortRangoASC(R,)

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

def mergesortRangoDESC(arr): 
    if len(arr) > 1: 
        mid = len(arr)//2

        L = arr[:mid]
        R = arr[mid:]

        mergesortRangoDESC(L,)
        mergesortRangoDESC(R,)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] >= R[j]:
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

#
#2. Quicksort
#
def quickSort(arr, low, high):

    if low < high:
        pi = __particion(arr, low, high)
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)


def __particion(arr, low, high):
    pivot = arr[high] 
    i = low - 1
    for j in range(low, high):
        if arr[j] <=  pivot:
            i +=1
            (arr[i], arr[j]) = (arr[j], arr[i])
    i = i + 1
    (arr[i], arr[high]) = (arr[high], arr[i])
    return i

#
#3. Heapsort
#

def heapSortDuracionASC(arr):
    n = len(arr)

    for i in range(n//2-1, -1, -1):
        __heapifyASC(arr, n, i)
    
    for i in range(n-1, 0, -1):
        (arr[i], arr[0]) = (arr[0], arr[i])
        __heapifyASC(arr, i, 0)

def __heapifyASC(arr, n, i):
    largerst = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i].getDuracion() < arr[l].getDuracion():
        largerst = l
    
    if r < n and arr[largerst].getDuracion() < arr[r].getDuracion():
        largerst = r

    if largerst != i:
        (arr[i], arr[largerst]) = (arr[largerst], arr[i])
    
        __heapifyASC(arr, n, largerst)

def heapSortDuracionDESC(arr):
    n = len(arr)

    for i in range(n//2-1, -1, -1):
        __heapify(arr, n, i)
    
    for i in range(n-1, 0, -1):
        (arr[i], arr[0]) = (arr[0], arr[i])
        __heapify(arr, i, 0)

def __heapify(arr, n, i):
    largerst = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i].getDuracion() > arr[l].getDuracion():
        largerst = l
    
    if r < n and arr[largerst].getDuracion() > arr[r].getDuracion():
        largerst = r

    if largerst != i:
        (arr[i], arr[largerst]) = (arr[largerst], arr[i])
    
        __heapify(arr, n, largerst)

#
#4. Shellsort
#

def shellsortPrecioHabDESC(arr):
    n = len(arr) 
    gap = n // 2
    while gap > 0: 
        for i in range(gap, n): 
            temp = arr[i]
            j = i
            while  j >= gap and arr[j - gap].getPrecio() < temp.getPrecio(): 
                arr[j] = arr[j - gap]
                j -= gap  
            arr[j] = temp 
        gap //= 2

def shellsortPrecioHabASC(arr):
    n = len(arr) 
    gap = n // 2
    while gap > 0: 
        for i in range(gap, n): 
            temp = arr[i]
            j = i
            while  j >= gap and arr[j - gap].getPrecio() > temp.getPrecio(): 
                arr[j] = arr[j - gap]
                j -= gap  
            arr[j] = temp 
        gap //= 2
