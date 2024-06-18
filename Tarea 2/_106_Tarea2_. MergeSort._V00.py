# Daniel Alejandro Flores Sepulveda
# Este programa implementa el algoritmo de MergeSort

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Encuentra el punto medio del arreglo
        L = arr[:mid]  # Divide el arreglo en mitades izquierda y derecha
        R = arr[mid:]
        
        merge_sort(L)  # Ordena la mitad izquierda
        merge_sort(R)  # Ordena la mitad derecha
        
        i = j = k = 0
        
        # Combina las dos mitades ordenadas
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        
        # Añade los elementos restantes de L, si los hay
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        
        # Añade los elementos restantes de R, si los hay
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def main():
    arr = [12, 11, 13, 5, 6, 7]
    print("Array original:")
    print(arr)
    
    merge_sort(arr)
    
    print("Array ordenado por MergeSort:")
    print(arr)

if __name__ == "__main__":
    main()
