import heapq
import math
tree = {
    'A': {'B': 5, 'C': 1},
    'B': {'A': 5, 'C': 2, 'D': 1},
    'C': {'A': 1, 'B': 2, 'D': 4, 'E': 8},
    'D': {'B': 1, 'C': 4, 'E': 3, 'F': 6},
    'E': {'C': 8, 'D': 3},
    'F': {'D': 6}
}


def init_distance(graph, root):
    distance = {root: 0}
    for node in graph:
        if node != root:
            distance[node] = math.inf
    return distance


def dijkstra(graph, root):
    pq = []
    heapq.heappush(pq, (0, root))
    seen = set()
    # seen.add(root)
    parent = {root: None}
    distance = init_distance(graph, root)
    while len(pq) > 0:
        pair = heapq.heappop(pq)
        dist = pair[0]
        vertex = pair[1]
        seen.add(vertex)
        nodes = graph[vertex].keys()
        for node in nodes:
            if node not in seen:
                if (dist + graph[vertex][node]) < distance[node]:
                    heapq.heappush(pq, (dist + graph[vertex][node], node))
                    parent[node] = vertex
                    distance[node] = dist + graph[vertex][node]
    return parent, distance


parents, distance = dijkstra(tree, 'A')
print(parents)
print(distance)