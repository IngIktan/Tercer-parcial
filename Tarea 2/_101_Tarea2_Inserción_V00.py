# Daniel Alejandro Flores Sepulveda
# Este programa implementa el algoritmo de ordenación por inserción (Insertion Sort)

def insertion_sort(arr):
    n = len(arr)  # Obtiene la longitud del arreglo
    for i in range(1, n):  # Itera sobre el arreglo desde el segundo elemento hasta el final
        key = arr[i]  # Selecciona el elemento actual como la clave a insertar en su posición correcta
        j = i - 1  # Inicializa un índice para comparar con el elemento anterior
        while j >= 0 and key < arr[j]:  # Mientras haya elementos mayores que la clave
            arr[j + 1] = arr[j]  # Desplaza los elementos mayores hacia la derecha
            j -= 1  # Reduce el índice para seguir comparando hacia atrás
        arr[j + 1] = key  # Inserta la clave en la posición correcta

def print_array(arr):
    for i in range(len(arr)):  # Itera sobre el arreglo
        print(arr[i], end=" ")  # Imprime cada elemento separado por espacio
    print()  # Imprime una nueva línea al final

def main():
    arr = [12, 11, 13, 5, 6]  # Define un arreglo desordenado
    print("Array original:")
    print_array(arr)  # Imprime el arreglo original
    
    insertion_sort(arr)  # Llama a la función de ordenación por inserción
    
    print("Array ordenado por Insertion Sort:")
    print_array(arr)  # Imprime el arreglo ordenado

if __name__ == "__main__":
    main()  # Llama a la función principal si el script se ejecuta como programa principal
