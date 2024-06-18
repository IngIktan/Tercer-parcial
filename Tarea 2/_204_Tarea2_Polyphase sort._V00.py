# Daniel Alejandro Flores Sepulveda
# Este programa implementa una versión simplificada del algoritmo de Polyphase Sort para ordenar grandes conjuntos de datos utilizando múltiples fases.

import heapq
import os

def split_file(input_file, num_initial_runs):
    # Abre el archivo de entrada para lectura
    with open(input_file, 'r') as f:
        lines = f.readlines()  # Lee todas las líneas del archivo
        lines = [int(line.strip()) for line in lines]  # Convierte las líneas a enteros
        
        # Divide las líneas en bloques iniciales y los ordena
        runs = [lines[i::num_initial_runs] for i in range(num_initial_runs)]
        for i, run in enumerate(runs):
            run.sort()
            with open(f"run_{i}.txt", 'w') as out:
                for num in run:
                    out.write(f"{num}\n")

def polyphase_merge(runs, output_file):
    # Abre todos los archivos de "runs" para lectura
    run_files = [open(f"run_{i}.txt", 'r') for i in range(runs)]
    
    # Abre el archivo de salida para escritura
    with open(output_file, 'w') as out:
        heap = []
        
        # Lee la primera línea de cada archivo de "run"
        for i, file in enumerate(run_files):
            line = file.readline().strip()
            if line:
                num = int(line)
                heapq.heappush(heap, (num, i))  # Agrega el número y el índice del archivo al heap
        
        # Mientras haya elementos en el heap
        while heap:
            smallest_num, run_idx = heapq.heappop(heap)  # Obtiene el menor elemento del heap
            out.write(f"{smallest_num}\n")  # Escribe el número en el archivo de salida
            
            next_line = run_files[run_idx].readline().strip()  # Lee la siguiente línea del archivo correspondiente
            if next_line:
                next_num = int(next_line)
                heapq.heappush(heap, (next_num, run_idx))  # Agrega el siguiente número al heap
    
    # Cierra todos los archivos de "runs"
    for file in run_files:
        file.close()

    # Elimina los archivos temporales de "runs"
    for i in range(runs):
        os.remove(f"run_{i}.txt")

# Ejemplo de uso:
input_file = "large_unsorted_input.txt"  # Asegúrate de que este archivo exista
num_initial_runs = 3  # Número de "runs" iniciales
output_file = "sorted_output.txt"

# Divide el archivo de entrada en "runs" iniciales
split_file(input_file, num_initial_runs)

# Fusiona los "runs" utilizando Polyphase Sort
polyphase_merge(num_initial_runs, output_file)
