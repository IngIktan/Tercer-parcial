# Daniel Alejandro Flores Sepulveda
# Este programa crea archivos de entrada de prueba para el algoritmo de Balanced Multiway Merging.

def create_test_files():
    with open("file1.txt", 'w') as f1:
        f1.write("1\n")
        f1.write("4\n")
        f1.write("7\n")
    
    with open("file2.txt", 'w') as f2:
        f2.write("2\n")
        f2.write("5\n")
        f2.write("8\n")
    
    with open("file3.txt", 'w') as f3:
        f3.write("3\n")
        f3.write("6\n")
        f3.write("9\n")

# Ejemplo de uso:
create_test_files()
