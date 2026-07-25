import heapq

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 5)],
    'C': [('D', 1)],
    'D': []
}

def ucs(start, goal):
    frontier = [(0, start, [start])]
    visited = set()

    while frontier:
        cost, node, path = heapq.heappop(frontier)

        if node == goal:
            return path, cost

        if node not in visited:
            visited.add(node)

            for neighbor, edge_cost in graph[node]:
                heapq.heappush(
                    frontier,
                    (cost + edge_cost, neighbor, path + [neighbor])
                )

    return None, float('inf')

path, cost = ucs('A', 'D')

print("Path:", path)
print("Cost:", cost)
