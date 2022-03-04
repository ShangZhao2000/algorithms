"""Takes as input n, the number of nodes from 1 to n and incompatibilities, a list of lists of 2 elements which cannot be 
grouped together. Returns 2 lists representing a grouping of the nodes such that no incompatible nodes are in the same group,
False if this cannot be achieved.
"""
from collections import deque
from collections import defaultdict
def bipartite_matching(n, incompatibilities):
    node_colour = {}
    graph = defaultdict(list)
    for u, v in incompatibilities:
        graph[u].append(v)
        graph[v].append(u)
    for node in range(1, n + 1):
        if node not in node_colour:
            node_colour[node] = 0
            queue = deque([node])
            while queue:
                curr = queue.popleft()
                for neighbour in graph[curr]:
                    if neighbour not in node_colour:
                        node_colour[neighbour] = node_colour[curr] ^ 1
                    elif node_colour[neighbour] != node_colour[curr] ^ 1:
                        return False
    return [i for i in node_colour if node_colour[i] == 0], [i for i in node_colour if node_colour[i] == 1]