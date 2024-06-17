import heapq
import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0] * vertices for _ in range(vertices)]
        self.edges = []

    def add_edge(self, u, v, weight):
        self.graph[u][v] = weight
        self.graph[v][u] = weight
        self.edges.append((u, v, weight))

    def prim_mst(self):
        key = [float('inf')] * self.V
        parent = [None] * self.V
        key[0] = 0
        min_heap = [(0, 0)]  # (key, vertex)
        in_mst = [False] * self.V
        mst_edges = []

        while min_heap:
            weight, u = heapq.heappop(min_heap)
            in_mst[u] = True

            for v in range(self.V):
                if self.graph[u][v] > 0 and not in_mst[v] and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    heapq.heappush(min_heap, (key[v], v))
                    parent[v] = u

        for i in range(1, self.V):
            mst_edges.append((parent[i], i, self.graph[i][parent[i]]))

        return mst_edges

    def plot_graph(self, mst_edges):
        G = nx.Graph()
        for u, v, weight in self.edges:
            G.add_edge(u, v, weight=weight)

        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=15)
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

        mst = nx.Graph()
        for u, v, weight in mst_edges:
            mst.add_edge(u, v, weight=weight)

        nx.draw(mst, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=15, edge_color='red')
        plt.show()

# Crear el grafo y agregar las aristas
g = Graph(5)
g.add_edge(0, 1, 2)
g.add_edge(0, 3, 6)
g.add_edge(1, 2, 3)
g.add_edge(1, 3, 8)
g.add_edge(1, 4, 5)
g.add_edge(2, 4, 7)
g.add_edge(3, 4, 9)

mst_edges = g.prim_mst()
g.plot_graph(mst_edges)
