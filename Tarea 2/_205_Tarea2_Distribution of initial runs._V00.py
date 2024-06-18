# Daniel Alejandro Flores Sepulveda
# Este programa distribuye datos de entrada en varios archivos ordenados iniciales (runs).

import os

def distribute_initial_runs(input_file, num_runs):
    # Abre el archivo de entrada para lectura
    with open(input_file, 'r') as f:
        lines = f.readlines()  # Lee todas las líneas del archivo
        lines = [int(line.strip()) for line in lines]  # Convierte las líneas a enteros
        
        # Divide las líneas en bloques (runs) y los ordena
        runs = [lines[i::num_runs] for i in range(num_runs)]
        for i, run in enumerate(runs):
            run.sort()  # Ordena cada bloque (run)
            with open(f"run_{i}.txt", 'w') as out:
                for num in run:
                    out.write(f"{num}\n")  # Escribe los números ordenados en un archivo

# Ejemplo de uso:
input_file = "unsorted_input.txt"  # Asegúrate de que este archivo exista
num_runs = 3  # Número de bloques (runs) iniciales

distribute_initial_runs(input_file, num_runs)

# Verifica el contenido de los archivos creados
for i in range(num_runs):
    with open(f"run_{i}.txt", 'r') as f:
        print(f"Contenido de run_{i}.txt:")
        print(f.read())
