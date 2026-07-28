import heapq

graph = {
    'A': [('B', 2), ('C', 4)],
    'B': [('D', 3)],
    'C': [('D', 1), ('E', 5)],
    'D': [('G', 2)],
    'E': [('G', 1)],
    'G': []
}

h = {'A': 5, 'B': 3, 'C': 4, 'D': 2, 'E': 1, 'G': 0}

def astar(start, goal):
    pq = [(0, start)]
    cost = {start: 0}
    path = {start: None}

    while pq:
        _, node = heapq.heappop(pq)

        if node == goal:
            result = []
            while node:
                result.append(node)
                node = path[node]
            return result[::-1], cost[goal]

        for nxt, w in graph[node]:
            new = cost[node] + w
            if nxt not in cost or new < cost[nxt]:
                cost[nxt] = new
                path[nxt] = node
                heapq.heappush(pq, (new + h[nxt], nxt))

start = 'A'
goal = 'G'

route, total = astar(start, goal)
print("Shortest Path:", " -> ".join(route))
print("Total Cost:", total)
