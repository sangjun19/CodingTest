n, k = map(int, input().split())
arr = [[0, 0]]
vMax = [[0 for _ in range(k + 1)] for _ in range(n + 1)]

for i in range(n):
    x, y = map(int, input().split())
    arr.append([x, y])

for i in range(1, n + 1):
    for j in range(1, k + 1):
        w, v = arr[i][0], arr[i][1]
        if w <= j:
            vMax[i][j] = max(vMax[i - 1][j], v + vMax[i - 1][j - w])
        else:
            vMax[i][j] = vMax[i - 1][j]

print(vMax[n][k])