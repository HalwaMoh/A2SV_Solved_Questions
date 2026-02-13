matrix = []
for i in range(5):
    row = list(map(int, input().split()))
    matrix.append(row)

for i in range(5):
    for j in range(5):
        if matrix[i][j] == 1:
            one_row = i + 1  
            one_col = j + 1

moves = abs(one_row - 3) + abs(one_col - 3)

print(moves)
