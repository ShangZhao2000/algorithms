class Vertex:
    def __init__(self, ID):
        self.id = ID
        self.adj = []
    def add_edge(self, v, w):
        self.adj.append((v, w))
    
class Graph:
    def __init__(self, V):
        self.size = V
        self.vertices = [None for _ in range(V)]
        self.edges = []
    def add_vertex(self, ID):
        self.vertices[ID] = Vertex(ID)
    def add_edge(self, u, v, w):
        self.edges.append((u, v, w))
        self.vertices[u].add_edge(v, w)

def floyd_warshall(weighted_graph):
    distances = [[float("inf") for _ in range(weighted_graph.size)] for __ in range(weighted_graph.size)]
    for u, v, w in edges:
        distances[u][v] = w
    for k in range(weighted_graph.size):
        for i in range(weighted_graph.size):
            for j in range(weighted_graph.size):
                if distances[i][k] + distances[k][j] < distances[i][j]:
                    distances[i][j] = distances[i][k] + distances[k][j]
    return distances