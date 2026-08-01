from queue import PriorityQueue

# Goal State
goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

# Start State (Solvable)
start = (1, 2, 3,
         4, 0, 6,
         7, 5, 8)

# Heuristic Function (Misplaced Tiles)
def heuristic(state):
    h = 0
    for i in range(9):
        if state[i] != 0 and state[i] != goal[i]:
            h += 1
    return h

# Generate Neighbor States
def neighbors(state):
    result = []
    blank = state.index(0)

    row = blank // 3
    col = blank % 3

    moves = [(-1,0),(1,0),(0,-1),(0,1)]

    for dr, dc in moves:
        nr = row + dr
        nc = col + dc

        if 0 <= nr < 3 and 0 <= nc < 3:
            newblank = nr*3 + nc

            temp = list(state)
            temp[blank], temp[newblank] = temp[newblank], temp[blank]

            result.append(tuple(temp))

    return result

# Print Puzzle
def print_board(state):
    for i in range(0,9,3):
        for j in range(3):
            if state[i+j] == 0:
                print("_", end=" ")
            else:
                print(state[i+j], end=" ")
        print()
    print()

# A* Search
def solve():
    pq = PriorityQueue()

    pq.put((heuristic(start), 0, start))

    parent = {}
    parent[start] = None

    cost = {}
    cost[start] = 0

    while not pq.empty():

        f, g, current = pq.get()

        if current == goal:

            path = []

            while current is not None:
                path.append(current)
                current = parent[current]

            path.reverse()

            print("\nPuzzle Solved Successfully!")
            print("Total Moves =", len(path)-1)

            step = 0

            for state in path:
                print("Step", step)
                print_board(state)
                step += 1

            return

        for nxt in neighbors(current):

            newcost = g + 1

            if nxt not in cost or newcost < cost[nxt]:
                cost[nxt] = newcost
                priority = newcost + heuristic(nxt)

                pq.put((priority, newcost, nxt))
                parent[nxt] = current

    print("No Solution Found")

# Main
solve()
