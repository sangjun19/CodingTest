num = [list(map(int, input().split())) for _ in range(9)]
max = 0
x, y = 0, 0
for i in range(9):
    for j in range(9):
        if max <= num[i][j]:
            max = num[i][j]
            x = i
            y = j
print(max)
print(x+1, y+1)