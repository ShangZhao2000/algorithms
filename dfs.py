def dfs(graph, vertex1, vertex2, visited=[]):
    visited.append(vertex1)
    if vertex1==vertex2:
        return visited
    else:
        for i in graph[vertex1]:
            if i not in visited:
                v=dfs(graph, i, vertex2, visited)
                if v!=[]:
                    return v
        return []    

graph={
    'lava': set(['sharks', 'piranhas']),
    'sharks': set(['lava', 'bees', 'lasers']),
    'piranhas': set(['lava', 'crocodiles']),
    'bees': set(['sharks']),
    'lasers': set(['sharks', 'crocodiles']),
    'crocodiles': set(['piranhas', 'lasers'])
  }


print(dfs(graph, 'lava', 'lasers'))
