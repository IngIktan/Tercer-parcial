# Daniel Alejandro Flores Sepulveda
# Este programa implementa el algoritmo de Straight Merging para combinar dos archivos ordenados en uno nuevo.

def straight_merge(file1, file2, output_file):
    # Abre los archivos de entrada y salida
    with open(file1, 'r') as f1, open(file2, 'r') as f2, open(output_file, 'w') as out:
        # Lee la primera línea de cada archivo
        line1 = f1.readline().strip()
        line2 = f2.readline().strip()
        
        # Comienza a comparar y combinar las líneas de los archivos
        while line1 and line2:
            num1 = int(line1)
            num2 = int(line2)
            
            # Compara los números y escribe el menor en el archivo de salida
            if num1 <= num2:
                out.write(f"{num1}\n")
                line1 = f1.readline().strip()  # Lee la siguiente línea de file1
            else:
                out.write(f"{num2}\n")
                line2 = f2.readline().strip()  # Lee la siguiente línea de file2
        
        # Si queda alguna línea en file1, escríbela en el archivo de salida
        while line1:
            out.write(f"{line1}\n")
            line1 = f1.readline().strip()
        
        # Si queda alguna línea en file2, escríbela en el archivo de salida
        while line2:
            out.write(f"{line2}\n")
            line2 = f2.readline().strip()

# Ejemplo de uso:
file1 = "file1.txt"
file2 = "file2.txt"
output_file = "sorted_output.txt"

straight_merge(file1, file2, output_file)
