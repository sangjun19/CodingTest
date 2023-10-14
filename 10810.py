n, m = map(int, input().split())
b = [0 for _ in range(n)]
for x in range(m):
    i, j, k = map(int, input().split())
    for y in range(i-1,j):
        b[y] = k
for x in b:
    print(x, end=' ')