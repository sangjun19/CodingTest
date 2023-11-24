n, m = map(int, input().split())
for i in range(n):
    chess = list(map(int, input().split()))
check = 0
for i in range(n-1):
    for j in range(n-1):
        if chess[i][j] != chess[i][j+1] or chess[i][j] != chess[i+1][j]:
            check += 1   
for j in range(n-1):
    if chess[i][j] != chess[i][j+1] or chess[i][j] != chess[i-1][j]:
        check += 1
print(check)