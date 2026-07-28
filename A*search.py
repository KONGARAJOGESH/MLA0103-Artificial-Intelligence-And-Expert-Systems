import heapq

network = {
    'S': [('A', 3), ('B', 4)],
    'A': [('C', 2), ('D', 6)],
    'B': [('D', 3), ('E', 5)],
    'C': [('G', 4)],
    'D': [('G', 2)],
    'E': [('G', 1)],
    'G': []
}

h = {
    'S': 6,
    'A': 5,
    'B': 4,
    'C': 3,
    'D': 2,
    'E': 1,
    'G': 0
}

def a_star(source, destination):
    open_list = [(h[source], source)]
    g_cost = {source: 0}
    previous = {source: None}

    while open_list:
        _, current = heapq.heappop(open_list)

        if current == destination:
            route = []
            while current:
                route.append(current)
                current = previous[current]
            return route[::-1], g_cost[destination]

        for nxt, distance in network[current]:
            temp_cost = g_cost[current] + distance

            if nxt not in g_cost or temp_cost < g_cost[nxt]:
                g_cost[nxt] = temp_cost
                f_cost = temp_cost + h[nxt]
                heapq.heappush(open_list, (f_cost, nxt))
                previous[nxt] = current

    return [], -1

route, cost = a_star('S', 'G')

if route:
    print("Shortest Path:", " -> ".join(route))
    print("Total Cost:", cost)
else:
    print("Goal node not reachable.")
