jug1 = 0
jug2 = 0

CAP1 = 11
CAP2 = 9

while True:
    print("\n------ Water Jug Puzzle ------")
    print("11L Jug:", jug1, "L")
    print("9L Jug :", jug2, "L")

    if jug1 == 8:
        print("\n🎉 Congratulations! Goal achieved.")
        break

    print("\n1. Fill 11L Jug")
    print("2. Fill 9L Jug")
    print("3. Empty 11L Jug")
    print("4. Empty 9L Jug")
    print("5. Pour 11L -> 9L")
    print("6. Pour 9L -> 11L")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        jug1 = CAP1

    elif choice == 2:
        jug2 = CAP2

    elif choice == 3:
        jug1 = 0

    elif choice == 4:
        jug2 = 0

    elif choice == 5:
        transfer = min(jug1, CAP2 - jug2)
        jug1 -= transfer
        jug2 += transfer

    elif choice == 6:
        transfer = min(jug2, CAP1 - jug1)
        jug2 -= transfer
        jug1 += transfer

    elif choice == 7:
        print("Game Over")
        break

    else:
        print("Invalid Choice")
