graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}

visited = []

def dfs(node):
    if node not in visited:
        visited.append(node)
        for next_node in graph[node]:
            dfs(next_node)

start = 'A'
dfs(start)

print("DFS Traversal:")
print(" -> ".join(visited))
