def bfs(graph, vertex1, vertex2):
    queue = [[vertex1, [vertex1]]]
    visited = set()
    while queue:
        curr_vertex, path = queue.pop(0)
        visited.add(curr_vertex)
        for i in graph[curr_vertex]:
            if i not in visited:
                if i==vertex2:
                    path.append(i)
                    return path
                else:
                    queue.append([i, path+[i]])




graph={
    'lava': set(['sharks', 'piranhas']),
    'sharks': set(['lava', 'bees', 'lasers']),
    'piranhas': set(['lava', 'crocodiles']),
    'bees': set(['sharks']),
    'lasers': set(['sharks', 'crocodiles']),
    'crocodiles': set(['piranhas', 'lasers'])
  }

print(bfs(graph, 'crocodiles', 'bees'))