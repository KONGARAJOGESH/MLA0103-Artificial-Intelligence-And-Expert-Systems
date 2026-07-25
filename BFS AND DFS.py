graph = {
    10: [20, 30],
    20: [40, 50],
    30: [60],
    40: [],
    50: [70],
    60: [],
    70: []
}

def bfs(start):
    visited = []
    queue = [start]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            queue.extend(graph[node])
    print("BFS:", visited)

def dfs(node, visited):
    if node not in visited:
        visited.append(node)
        for neighbor in graph[node]:
            dfs(neighbor, visited)

visited = []
bfs(10)
dfs(10, visited)
print("DFS:", visited)
