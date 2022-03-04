class Vertex:
    def __init__(self, ID):
        self.id = ID
        self.adj = []
    def add_edge(self, v):
        self.adj.append(v)
    
class Graph:
    def __init__(self, V):
        self.size = V
        self.vertices = [None for _ in range(V)]
    def add_vertex(self, ID):
        self.vertices[ID] = Vertex(ID)

from collections import deque        
def topological_sort(dag):
    in_degree = [0 for _ in range(dag.size)]
    for vertex in dag.vertices:
        for neighbour in vertex.adj:
            in_degree[neighbour.id] += 1
    queue = deque()
    for i in range(len(in_degree)):
        if in_degree[i] == 0:
            queue.append(dag.vertices[i])
    res = []
    while queue:
        curr = queue.popleft()
        res.append(curr)
        for vertex in curr.adj:
            in_degree[vertex.id] -= 1
            if in_degree[vertex.id] == 0:
                queue.append(vertex)
    return res