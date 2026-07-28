j10 = 10
j7 = 0
j4 = 0

print("Initial State:", (j10, j7, j4))

def pour(a, b, ca, cb):
    move = min(a, cb-b)
    a -= move
    b += move
    return a, b

j10, j7 = pour(j10, j7, 10, 7)
print((j10, j7, j4))

j7, j4 = pour(j7, j4, 7, 4)
print((j10, j7, j4))

j4 = 0
print((j10, j7, j4))

j7, j4 = pour(j7, j4, 7, 4)
print((j10, j7, j4))

j10, j7 = pour(j10, j7, 10, 7)
print((j10, j7, j4))

print("Goal Achieved:", (j10, j7, j4))
