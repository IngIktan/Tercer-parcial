# Daniel Alejandro Flores Sepulveda
# Este programa implementa el algoritmo de Kruskal para encontrar el Árbol de Expansión Mínima (MST) y lo visualiza gráficamente.

import networkx as nx  # Importa NetworkX para crear y visualizar grafos
import matplotlib.pyplot as plt  # Importa matplotlib para la visualización gráfica

class Graph:
    def __init__(self, vertices):
        # Inicializa un grafo con un número dado de vértices
        self.V = vertices  # Número de vértices
        self.graph = []  # Lista de aristas

    def add_edge(self, u, v, w):
        # Agrega una arista con un peso dado entre dos vértices u y v
        self.graph.append([u, v, w])

    def find(self, parent, i):
        # Encuentra el conjunto de un elemento i (usando compresión de ruta)
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        # Une dos subconjuntos x e y según el rango
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)

        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_y] = root_x
            rank[root_x] += 1

    def kruskal(self):
        # Implementa el algoritmo de Kruskal para encontrar el MST
        result = []  # Esta lista almacenará el MST final
        i, e = 0, 0  # Variables para recorrer las aristas y contar las aristas del MST
        self.graph = sorted(self.graph, key=lambda item: item[2])  # Ordena las aristas por peso

        parent = []  # Lista para almacenar el subconjunto de cada vértice
        rank = []  # Lista para almacenar el rango de cada subconjunto

        for node in range(self.V):
            # Inicializa cada vértice para que sea su propio padre (subconjunto) y rango 0
            parent.append(node)
            rank.append(0)

        while e < self.V - 1:
            # Continúa hasta que el MST tenga V-1 aristas
            u, v, w = self.graph[i]  # Selecciona la arista de menor peso
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:
                # Si los vértices u y v no están en el mismo subconjunto, inclúyelos en el MST
                e = e + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)

            # Dibuja el grafo después de agregar cada arista al MST
            self.draw_graph(result)

        return result

    def draw_graph(self, result):
        # Visualiza el grafo original y el MST
        G = nx.Graph()  # Crea un grafo vacío
        for edge in self.graph:
            # Agrega todas las aristas del grafo original
            G.add_edge(edge[0], edge[1], weight=edge[2])

        pos = nx.spring_layout(G)  # Posiciona los nodos usando el layout de resorte
        plt.figure()
        nx.draw(G, pos, with_labels=True)
        # Dibuja el grafo original
        nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): f"{w}" for u, v, w in self.graph})
        # Dibuja los pesos de las aristas
        nx.draw_networkx_edges(G, pos, edgelist=result, edge_color='r', width=2)
        # Dibuja el MST en rojo
        plt.show()  # Muestra el gráfico

# Crear el grafo y agregar las aristas
g = Graph(4)
g.add_edge(0, 1, 10)
g.add_edge(0, 2, 6)
g.add_edge(0, 3, 5)
g.add_edge(1, 3, 15)
g.add_edge(2, 3, 4)

print("Edges in the constructed MST")
result = g.kruskal()  # Encuentra el MST usando el algoritmo de Kruskal
for u, v, weight in result:
    print(f"{u} -- {v} == {weight}")  # Imprime las aristas del MST
