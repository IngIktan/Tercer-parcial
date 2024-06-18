# Daniel Alejandro Flores Sepulveda
# Este programa implementa el algoritmo de Natural Merging para ordenar un archivo de entrada.

def natural_merge(input_file, output_file):
    # Abre el archivo de entrada para lectura y el archivo de salida para escritura
    with open(input_file, 'r') as f, open(output_file, 'w') as out:
        lines = f.readlines()  # Lee todas las líneas del archivo de entrada
        n = len(lines)  # Obtiene el número de líneas
        if n <= 1:
            out.writelines(lines)  # Si el archivo tiene una línea o menos, escríbelas directamente
            return
        
        current_run = []  # Lista para almacenar el "run" actual
        previous_num = None  # Variable para almacenar el número anterior leído
        run_started = False  # Indicador de si se ha iniciado un nuevo "run"
        
        # Itera sobre cada línea del archivo
        for line in lines:
            num = int(line.strip())  # Convierte la línea en un número entero
            
            if previous_num is None or num >= previous_num:
                current_run.append(line)  # Agrega la línea al "run" actual si está ordenado o es el primero
                run_started = True  # Marca que se ha iniciado el "run"
            else:
                if run_started:
                    out.writelines(current_run)  # Escribe el "run" actual en el archivo de salida
                    current_run = [line]  # Inicia un nuevo "run" con la línea actual
                else:
                    out.write(line)  # Escribe la línea si no se ha iniciado ningún "run"
                
                run_started = False  # Reinicia el indicador de "run" iniciado
            
            previous_num = num  # Actualiza el número anterior con el número actual
        
        if run_started:
            out.writelines(current_run)  # Escribe el último "run" si no se ha escrito

# Ejemplo de uso:
input_file = "unsorted_input.txt"  # Asegúrate de que este archivo exista y tenga contenido
output_file = "sorted_output.txt"

natural_merge(input_file, output_file)
