# Daniel Alejandro Flores Sepulveda
# Este programa implementa el algoritmo de ordenación por selección (Selection Sort)

def selection_sort(arr):
    n = len(arr)  # Obtiene la longitud del arreglo
    for i in range(n):  # Itera sobre el arreglo
        min_idx = i  # Supone que el primer elemento no ordenado es el mínimo
        for j in range(i + 1, n):  # Itera sobre el resto del arreglo
            if arr[j] < arr[min_idx]:  # Encuentra el mínimo elemento restante
                min_idx = j  # Actualiza el índice del mínimo encontrado
        arr[i], arr[min_idx] = arr[min_idx], arr[i]  # Intercambia el elemento actual con el mínimo encontrado

def print_array(arr):
    for i in range(len(arr)):  # Itera sobre el arreglo
        print(arr[i], end=" ")  # Imprime cada elemento separado por espacio
    print()  # Imprime una nueva línea al final

def main():
    arr = [64, 25, 12, 22, 11]  # Define un arreglo desordenado
    print("Array original:")
    print_array(arr)  # Imprime el arreglo original
    
    selection_sort(arr)  # Llama a la función de ordenación por selección
    
    print("Array ordenado por Selection Sort:")
    print_array(arr)  # Imprime el arreglo ordenado

if __name__ == "__main__":
    main()  # Llama a la función principal si el script se ejecuta como programa principal
