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

import heapq
def minimum_spanning_tree(weighted_graph):
    min_heap = [(0, weighted_graph.vertices[0].id)]
    included = [False for _ in range(weighted_graph.size)]
    dist = [float("inf") for _ in range(weighted_graph.size)]
    pred = [None for _ in range(weighted_graph.size)]
    included[weighted_graph.vertices[0].id] = True
    dist[weighted_graph.vertices[0].id] = 0
    mst = Graph(weighted_graph.size)
    while min_heap:
        curr_node = weighted_graph.vertices[heappop(min_heap)[1]]
        mst.add_vertex(curr_node.id)
        if pred[curr_node.id] is not None:
            mst.vertices[curr_node.id].add_edge(mst.vertices[pred[curr_node.id]], dist[curr_node.id])
            mst.vertices[pred[curr_node.id]].add_edge(mst.vertices[curr_node.id], dist[curr_node.id])
        included[curr_node.id] = True
        for neighbour, weight in curr_node.adj:
            if not included[neighbour.id] and weight < dist[neighbour.id]:
                heappush((weight, neighbour.id))
                dist[neighbour.id] = weight
                pred[neighbour.id] = curr_node.id 
    return mst
