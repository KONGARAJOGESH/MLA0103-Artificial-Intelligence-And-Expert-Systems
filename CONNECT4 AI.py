ROWS = 6
COLS = 7

board = [["." for _ in range(COLS)] for _ in range(ROWS)]

def display():
    print("\n")
    for row in board:
        print(" ".join(row))
    print("1 2 3 4 5 6 7")

def drop(col, player):
    for row in range(ROWS - 1, -1, -1):
        if board[row][col] == ".":
            board[row][col] = player
            return True
    return False

def check(player):

    for r in range(ROWS):
        for c in range(COLS - 3):
            if all(board[r][c+i] == player for i in range(4)):
                return True
   for r in range(ROWS - 3):
        for c in range(COLS):
            if all(board[r+i][c] == player for i in range(4)):
                return True


    for r in range(ROWS - 3):
        for c in range(COLS - 3):
            if all(board[r+i][c+i] == player for i in range(4)):
                return True

    for r in range(3, ROWS):
        for c in range(COLS - 3):
            if all(board[r-i][c+i] == player for i in range(4)):
                return True

    return False

player = "X"

while True:
    display()

    try:
        col = int(input(f"Player {player}, Enter column (1-7): ")) - 1
    except:
        print("Enter a valid number.")
        continue

    if col < 0 or col >= COLS:
        print("Invalid column!")
        continue

    if not drop(col, player):
        print("Column Full!")
        continue

    if check(player):
        display()
        print("\nCongratulations!")
        print("Player", player, "Wins!")
        break

    player = "O" if player == "X" else "X"
