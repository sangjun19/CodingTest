n, k = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

a1, a2 = 0, 0
for i in range(1, k):
    a2 += 1
    if a1 < a2:
        a1 += 1
        a2 = 0
        
# print(a1, a2)

cnt = 0
for i in range(n):
    for j in range(n):
        if arr[i][j] == n * n - a1:
            if cnt == a2:
                print(i + 1, j + 1)
                exit(0)
            cnt += 1