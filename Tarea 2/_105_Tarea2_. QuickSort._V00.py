# Daniel Alejandro Flores Sepulveda
# Este programa implementa el algoritmo de QuickSort

def partition(arr, low, high):
    pivot = arr[high]  # Escoge el último elemento como pivote
    i = low - 1  # Índice del menor elemento
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Intercambia elementos
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Coloca el pivote en su posición correcta
    return i + 1  # Retorna el índice del pivote

def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)  # Divide el arreglo y encuentra el pivote
        quick_sort(arr, low, pi - 1)  # Ordena los elementos antes del pivote
        quick_sort(arr, pi + 1, high)  # Ordena los elementos después del pivote

def main():
    arr = [10, 7, 8, 9, 1, 5]
    n = len(arr)
    print("Array original:")
    print(arr)
    
    quick_sort(arr, 0, n - 1)
    
    print("Array ordenado por QuickSort:")
    print(arr)

if __name__ == "__main__":
    main()
