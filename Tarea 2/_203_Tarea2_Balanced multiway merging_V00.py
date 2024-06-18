# Daniel Alejandro Flores Sepulveda
# Este programa implementa el algoritmo de Balanced Multiway Merging para combinar múltiples archivos ordenados en uno nuevo.

import heapq

def balanced_multiway_merge(files, output_file):
    # Abre todos los archivos de entrada para lectura
    file_handles = [open(file, 'r') for file in files]
    
    # Abre el archivo de salida para escritura
    with open(output_file, 'w') as out:
        heap = []  # Utilizamos un heap (montón) para encontrar el menor elemento entre todos los archivos
        for file_handle in file_handles:
            line = file_handle.readline().strip()  # Lee la primera línea de cada archivo
            if line:  # Si la línea no está vacía
                num = int(line)  # Convierte la línea en un número entero
                heapq.heappush(heap, (num, file_handle))  # Agrega el número y el manejador del archivo al heap
        
        # Mientras haya elementos en el heap
        while heap:
            smallest_num, smallest_file_handle = heapq.heappop(heap)  # Obtiene el menor elemento del heap
            out.write(f"{smallest_num}\n")  # Escribe el número en el archivo de salida
            
            next_line = smallest_file_handle.readline().strip()  # Lee la siguiente línea del archivo correspondiente
            if next_line:  # Si la línea no está vacía
                next_num = int(next_line)  # Convierte la línea en un número entero
                heapq.heappush(heap, (next_num, smallest_file_handle))  # Agrega el número y el manejador del archivo al heap
    
    # Cierra todos los archivos de entrada
    for file_handle in file_handles:
        file_handle.close()

# Ejemplo de uso:
files = ["file1.txt", "file2.txt", "file3.txt"]  # Asegúrate de que estos archivos existan y estén ordenados
output_file = "sorted_output.txt"

balanced_multiway_merge(files, output_file)
