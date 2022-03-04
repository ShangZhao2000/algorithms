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

def bellman_ford(weighted_graph, source):
    dist = [float("inf") for _ in range(weighted_graph.size)]
    pred = [None for _ in range(weighted_graph.size)]
    dist[source] = 0
    for _ in range(weighted_graph.size - 1):
        for u, v, w in weighted_graph.edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                pred[v] = u
    for u, v, w in weighted_graph.edges:
        if dist[u] + w < dist[v]:
            return False
    return dist, pred