from collections import deque
def bipartition(graph):
    def component(root):
        vertex_dist = {root:0}
        queue = deque([(root, 0)])
        pred = {root:None}
        while queue:
            curr_vertex, dist = queue.popleft()
            for neighbour in graph[curr_vertex]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append((neighbour, dist + 1))
                    pred[neighbour] = curr_vertex
                elif vertex_dist[neighbour] % 2 == dist % 2:
                    curr_v_path, neighbour_path = [curr_vertex], [neighbour]
                    curr = curr_vertex
                    while curr != root:
                        curr_v_path.append(pred[curr])
                        curr = pred[curr]
                    v_path_set = set(curr_v_path)
                    curr = neighbour
                    while curr != root:
                        if pred[curr] in v_path_set:
                            break
                        else:
                            neighbour_path.append(pred[curr])
                            curr = pred[curr]
                    return (curr_v_path[:vertex_dist[curr_vertex] - vertex_dist[pred[curr]] + 1] + neighbour_path[::-1], False)
        return (set(i for i in vertex_dist if vertex_dist[i] % 2 == 0), set(i for i in vertex_dist if vertex_dist[i] % 2 == 1), True)
    visited = set()
    A, B = set(), set()
    for u in graph:
        if u not in visited:
            visited.add(u)
            contents, bipartite = component(u)
            if bipartite:
                A, B = A.union(contents[0]), B.union(contents[1])
            else:
                return contents
    return (A, B)