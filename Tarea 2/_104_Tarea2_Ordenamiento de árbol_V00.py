# Daniel Alejandro Flores Sepulveda
# Este programa implementa el algoritmo de ordenamiento de árbol (Tree Sort)

class TreeNode:
    def __init__(self, key):
        self.left = None  # Nodo izquierdo inicialmente vacío
        self.right = None  # Nodo derecho inicialmente vacío
        self.val = key  # Valor del nodo

class BinarySearchTree:
    def __init__(self):
        self.root = None  # Inicializa el árbol binario como vacío
    
    def insert(self, key):
        if self.root is None:  # Si el árbol está vacío
            self.root = TreeNode(key)  # Crea un nuevo nodo como raíz
        else:
            self._insert_recursive(self.root, key)  # Llama a la función recursiva para insertar
    
    def _insert_recursive(self, node, key):
        if key < node.val:  # Si la clave es menor que el valor del nodo actual
            if node.left is None:  # Si no hay nodo izquierdo
                node.left = TreeNode(key)  # Crea un nuevo nodo izquierdo
            else:
                self._insert_recursive(node.left, key)  # Llama recursivamente con el nodo izquierdo
        else:  # Si la clave es mayor o igual al valor del nodo actual
            if node.right is None:  # Si no hay nodo derecho
                node.right = TreeNode(key)  # Crea un nuevo nodo derecho
            else:
                self._insert_recursive(node.right, key)  # Llama recursivamente con el nodo derecho
    
    def inorder_traversal(self):
        result = []  # Lista para almacenar el recorrido inorder
        self._inorder_recursive(self.root, result)  # Llama a la función recursiva de recorrido inorder
        return result  # Retorna el resultado del recorrido inorder
    
    def _inorder_recursive(self, node, result):
        if node:  # Si el nodo no es None
            self._inorder_recursive(node.left, result)  # Recorre recursivamente el nodo izquierdo
            result.append(node.val)  # Agrega el valor del nodo al resultado
            self._inorder_recursive(node.right, result)  # Recorre recursivamente el nodo derecho

def tree_sort(arr):
    bst = BinarySearchTree()  # Crea un nuevo árbol binario de búsqueda
    for elem in arr:  # Itera sobre cada elemento del arreglo
        bst.insert(elem)  # Inserta cada elemento en el árbol binario
    return bst.inorder_traversal()  # Retorna el arreglo ordenado mediante recorrido inorder

def main():
    arr = [12, 4, 5, 6, 2, 3, 8, 1]  # Define un arreglo desordenado
    print("Array original:")
    print(arr)  # Imprime el arreglo original
    
    sorted_arr = tree_sort(arr)  # Llama a la función de ordenamiento de árbol
    
    print("Array ordenado por Tree Sort:")
    print(sorted_arr)  # Imprime el arreglo ordenado

if __name__ == "__main__":
    main()  # Llama a la función principal si el script se ejecuta como programa principal
