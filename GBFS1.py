import heapq

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}

heuristic = {
    'A': 6,
    'B': 4,
    'C': 5,
    'D': 3,
    'E': 1,
    'F': 2,
    'G': 0
}

def gbfs(start, goal):
    queue = [(heuristic[start], start)]
    visited = []

    while queue:
        _, node = heapq.heappop(queue)

        if node not in visited:
            visited.append(node)

            if node == goal:
                return visited

            for neighbour in graph[node]:
                heapq.heappush(queue, (heuristic[neighbour], neighbour))

    return None

path = gbfs('A', 'G')

print("GBFS Traversal:")
print(" -> ".join(path))
