# Daniel Alejandro Flores Sepulveda
# Este programa implementa el algoritmo de RadixSort

def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n  # Arreglo de salida
    count = [0] * 10  # Arreglo para contar las ocurrencias de cada dígito
    
    # Contar la cantidad de cada dígito en exp
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1
    
    # Cambiar count[i] para que ahora contenga la posición real de este dígito en output[]
    for i in range(1, 10):
        count[i] += count[i - 1]
    
    # Construir el arreglo de salida
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1
    
    # Copiar los elementos ordenados en el arreglo original
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    max_value = max(arr)  # Encuentra el valor máximo en el arreglo
    exp = 1  # Inicializa el exponente
    
    while max_value // exp > 0:
        counting_sort(arr, exp)  # Llama a counting_sort para ordenar según el dígito actual
        exp *= 10  # Incrementa el exponente para pasar al siguiente dígito

def main():
    arr = [170, 45, 75, 90, 802, 24, 2, 66]
    print("Array original:")
    print(arr)
    
    radix_sort(arr)
    
    print("Array ordenado por RadixSort:")
    print(arr)

if __name__ == "__main__":
    main()
