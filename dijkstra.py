import heapq
def dijkstra(graph, vertex):
    heap = [(0, vertex)]
    distances = {}
    for i in graph:
        distances[i] = float('inf')
    distances[vertex] = 0
    while heap:
        curr_vertex = heapq.heappop(heap)[1]
        for i in graph[curr_vertex]:
            if i[1] + distances[curr_vertex] < distances[i[0]]:
                distances[i[0]] = i[1] + distances[curr_vertex]
                heapq.heappush(heap, (distances[i[0]], i[0]))
    return distances
            


graph = {
        'A': [('B', 10), ('C', 3)],
        'C': [('D', 2)],
        'D': [('E', 10)],
        'E': [],
        'B': [('C', 3), ('D', 2)]
    }

graph2 = {
        'A': [('B', 10), ('C', 3)],
        'C': [('D', 2)],
        'D': [('E', 10)],
        'E': [('A', 7)],
        'B': [('C', 3), ('D', 2)]
    }
print(dijkstra(graph2, 'D'))