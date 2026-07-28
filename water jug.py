from collections import deque

cap = (10, 7, 5)
start = (10, 0, 0)
goal = (5, 5, 0)

q = deque([(start, [start])])
seen = set()

while q:
    state, path = q.popleft()

    if state == goal:
        print("Solution:")
        for x in path:
            print(x)
        break

    if state in seen:
        continue

    seen.add(state)

    for i in range(3):
        for j in range(3):
            if i != j:
                s = list(state)
                move = min(s[i], cap[j]-s[j])
                s[i] -= move
                s[j] += move
                new = tuple(s)

                if new not in seen:
                    q.append((new, path+[new]))
else:
    print("No Solution")
