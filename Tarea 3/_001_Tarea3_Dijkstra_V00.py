# Daniel Alejandro Flores Sepulveda
# Este programa implementa el algoritmo de Dijkstra y muestra su funcionamiento paso a paso en la consola y gráficamente.

import heapq
import matplotlib.pyplot as plt
import networkx as nx

def dijkstra(graph, start):
    # Inicializa las estructuras de datos
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    path = {vertex: None for vertex in graph}
    
    step = 1  # Paso inicial
    
    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        
        # Muestra el estado del heap y las distancias en cada paso
        print(f"Paso {step}:")
        print(f"  Nodo actual: {current_vertex}")
        print(f"  Distancia actual: {current_distance}")
        print(f"  Heap: {priority_queue}")
        print(f"  Distancias: {distances}")
        step += 1
        
        if current_distance > distances[current_vertex]:
            continue
        
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
                path[neighbor] = current_vertex
    
    return distances, path

def print_path(path, start, end):
    # Reconstruye el camino más corto
    reverse_path = []
    current = end
    while current is not None:
        reverse_path.append(current)
        current = path[current]
    
    print("Camino más corto:", " -> ".join(reversed(reverse_path)))
    return list(reversed(reverse_path))

def visualize_graph(graph, path=None):
    G = nx.Graph()
    
    for node, edges in graph.items():
        for neighbor, weight in edges.items():
            G.add_edge(node, neighbor, weight=weight)
    
    pos = nx.spring_layout(G)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=700, font_size=15)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=12)
    
    if path:
        path_edges = list(zip(path, path[1:]))
        nx.draw(G, pos, edgelist=path_edges, edge_color='r', width=2)
    
    plt.show()

# Ejemplo de uso
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start_node = 'A'
end_node = 'D'
distances, path = dijkstra(graph, start_node)
print(f"Distancias desde el nodo {start_node}: {distances}")
shortest_path = print_path(path, start_node, end_node)

# Visualizar el grafo y el camino más corto
visualize_graph(graph, shortest_path)
