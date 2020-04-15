tree = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D', 'E'],
    'D': ['B', 'C', 'E', 'F'],
    'E': ['C', 'D'],
    'F': ['D']
}


def bfs(graph, root):
    queue = []
    queue.append(root)
    seen = set()
    seen.add(root)
    parent = {root : None}
    while len(queue) > 0:
        vertex = queue.pop(0)
        nodes = graph[vertex]
        for node in nodes:
            if node not in seen:
                queue.append(node)
                seen.add(node)
                parent[node] = vertex
        print(vertex)
    return parent


parents = bfs(tree,'A')
for key in parents:
    print(key, parents[key])
