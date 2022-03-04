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

def minimum_spanning_tree(weighted_graph):
    parent = [-1 for _ in range(weighted_graph.size)]
    mst = Graph(weighted_graph.size)
    mst.vertices = weighted_graph.vertices[:]
    def find(u):
        if parent[u] < 0:
            return u
        parent[u] = find(parent[u])
        return parent[u]
    def union(u, v):
        r1 = find(u)
        r2 = find(v)
        if r1 != r2:
            if -parent[r1] > -parent[r2]:
                parent[r2] = r1
            else:
                parent[r1] = r2
            return True
        else:
            return False
    for u, v, w in sorted(weighted_graph.edges, key=lambda x: x[2]):
        if union(u, v):
            mst.add_edge(u, v, w)
    return mst