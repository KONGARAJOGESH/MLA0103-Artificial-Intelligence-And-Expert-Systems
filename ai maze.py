maze = [
    list("##########"),
    list("#S     # #"),
    list("# ### ## #"),
    list("#   #    #"),
    list("### #### #"),
    list("#      # #"),
    list("# #### # #"),
    list("#    #   E"),
    list("##########")
]

for i in range(len(maze)):
    for j in range(len(maze[i])):
        if maze[i][j] == "S":
            x, y = i, j

while True:
    for row in maze:
        print("".join(row))

    print("\nUse W = Up, S = Down, A = Left, D = Right")
    move = input("Enter move: ").lower()

    nx, ny = x, y

    if move == "w":
        nx -= 1
    elif move == "s":
        nx += 1
    elif move == "a":
        ny -= 1
    elif move == "d":
        ny += 1
    else:
        print("Invalid move!\n")
        continue

    if maze[nx][ny] == "#":
        print("You hit a wall!\n")
        continue

    if maze[nx][ny] == "E":
        print("\n🎉 Congratulations! You reached the goal!")
        break

    maze[x][y] = " "
    x, y = nx, ny
    maze[x][y] = "S"

    print()
