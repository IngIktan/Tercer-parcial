# Daniel Alejandro Flores Sepulveda
# Este programa crea un archivo de entrada de prueba para el algoritmo de Polyphase Sort.

def create_large_test_file(filename):
    # Crea un archivo con números desordenados para pruebas
    with open(filename, 'w') as f:
        f.write("64\n")
        f.write("34\n")
        f.write("25\n")
        f.write("12\n")
        f.write("22\n")
        f.write("11\n")
        f.write("90\n")
        f.write("33\n")
        f.write("76\n")
        f.write("45\n")
        f.write("67\n")
        f.write("23\n")

# Ejemplo de uso:
test_file = "large_unsorted_input.txt"
create_large_test_file(test_file)
