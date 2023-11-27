n, m = map(int, input().split())
chess = []
for i in range(n):
    chess.append(input())
check = 0
for i in range(n-1):
    for j in range(n-1):
        if chess[i][j] == chess[i][j+1] or chess[i][j] == chess[i+1][j]:
            check += 1
for j in range(n-1):
    if chess[n-1][j] == chess[n-1][j+1] or chess[i][j] == chess[i-1][j]:
        check += 1
print(check)