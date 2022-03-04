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
    def add_vertex(self, ID):
        self.vertices[ID] = Vertex(ID)

def topological_sort(dag):

    def dfs(vertex):
        for neighbour in vertex.adj:
            if not visited[neighbour.id]:
                visited[neighbour.id] = True
                dfs(neighbour)
        order.append(vertex.id)

    visited = [False for _ in range(dag.size)]
    order = []
    for vertex in dag.vertices:
        if not visited[vertex.id]:
            visited[vertex.id] = True
            dfs(vertex)
    return order[::-1]