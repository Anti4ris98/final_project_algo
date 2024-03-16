import heapq

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for _ in range(vertices)]
    
    def add_edge(self, src, dest, weight):
        self.graph[src].append((dest, weight))

def dijkstra(graph, start_vertex):
    distances = [float('inf')] * graph.V
    distances[start_vertex] = 0
    priority_queue = [(0, start_vertex)]
    
    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        
        if current_distance > distances[current_vertex]:
            continue
        
        for neighbor, weight in graph.graph[current_vertex]:
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

# Приклад використання
graph = Graph(5) # Припустимо, що у нас є граф з 5 вершинами
graph.add_edge(0, 1, 4)
graph.add_edge(0, 2, 1)
graph.add_edge(2, 1, 2)
graph.add_edge(1, 3, 1)
graph.add_edge(2, 3, 5)
graph.add_edge(3, 4, 3)

start_vertex = 0
distances = dijkstra(graph, start_vertex)
print(f"Найкоротші шляхи від вершини {start_vertex} до інших: {distances}")
