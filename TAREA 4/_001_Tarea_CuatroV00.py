# Daniel Alejandro Flores Sepulveda
# Este programa implementa el algoritmo de Dijkstra y muestra su funcionamiento paso a paso en la consola y gráficamente.

import heapq  # Importa el módulo heapq para usar colas de prioridad
import networkx as nx  # Importa NetworkX para crear y visualizar grafos
import matplotlib.pyplot as plt  # Importa matplotlib para la visualización gráfica

class Graph:
    def __init__(self, vertices):
        # Inicializa un grafo con un número dado de vértices
        self.V = vertices  # Número de vértices
        self.graph = [[0] * vertices for _ in range(vertices)]  # Matriz de adyacencia
        self.edges = []  # Lista de aristas

    def add_edge(self, u, v, weight):
        # Agrega una arista con un peso dado entre dos vértices u y v
        self.graph[u][v] = weight  # Establece el peso de la arista en la matriz de adyacencia
        self.graph[v][u] = weight  # Como el grafo es no dirigido, también establece el peso en la dirección opuesta
        self.edges.append((u, v, weight))  # Agrega la arista a la lista de aristas

    def prim_mst(self):
        # Implementa el algoritmo de Prim para encontrar el árbol de expansión mínima (MST)
        key = [float('inf')] * self.V  # Inicializa las claves con infinito
        parent = [None] * self.V  # Inicializa el array de padres
        key[0] = 0  # La clave del primer vértice es 0 para asegurarse de que se elija primero
        min_heap = [(0, 0)]  # Cola de prioridad para seleccionar el vértice con la clave mínima
        in_mst = [False] * self.V  # Array para rastrear los vértices incluidos en el MST
        mst_edges = []  # Lista para almacenar las aristas del MST

        while min_heap:
            weight, u = heapq.heappop(min_heap)  # Selecciona el vértice con la clave mínima
            in_mst[u] = True  # Marca el vértice como incluido en el MST

            for v in range(self.V):
                if self.graph[u][v] > 0 and not in_mst[v] and key[v] > self.graph[u][v]:
                    # Si hay una arista válida y el vértice no está en el MST y la clave es mayor que el peso de la arista
                    key[v] = self.graph[u][v]  # Actualiza la clave
                    heapq.heappush(min_heap, (key[v], v))  # Agrega el vértice a la cola de prioridad
                    parent[v] = u  # Establece el padre del vértice

        for i in range(1, self.V):
            # Construye la lista de aristas del MST a partir del array de padres
            mst_edges.append((parent[i], i, self.graph[i][parent[i]]))

        return mst_edges  # Devuelve la lista de aristas del MST

    def plot_graph(self, mst_edges):
        # Visualiza el grafo original y el MST
        G = nx.Graph()  # Crea un grafo vacío
        for u, v, weight in self.edges:
            # Agrega todas las aristas del grafo original
            G.add_edge(u, v, weight=weight)

        pos = nx.spring_layout(G)  # Posiciona los nodos usando el layout de resorte
        nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=15)
        # Dibuja el grafo original
        labels = nx.get_edge_attributes(G, 'weight')  # Obtiene los pesos de las aristas
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)  # Dibuja los pesos de las aristas

        mst = nx.Graph()  # Crea un grafo vacío para el MST
        for u, v, weight in mst_edges:
            # Agrega las aristas del MST
            mst.add_edge(u, v, weight=weight)

        nx.draw(mst, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=15, edge_color='red')
        # Dibuja el MST en rojo
        plt.show()  # Muestra el gráfico

# Crear el grafo y agregar las aristas
g = Graph(5)
g.add_edge(0, 1, 2)
g.add_edge(0, 3, 6)
g.add_edge(1, 2, 3)
g.add_edge(1, 3, 8)
g.add_edge(1, 4, 5)
g.add_edge(2, 4, 7)
g.add_edge(3, 4, 9)

mst_edges = g.prim_mst()  # Encuentra el MST usando el algoritmo de Prim
g.plot_graph(mst_edges)  # Visualiza el grafo y el MST
