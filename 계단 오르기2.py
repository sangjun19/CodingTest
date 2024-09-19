n = int(input())
arr = list(map(int, input().split()))
dp = [[0] * 4 for _ in range(n + 1)]
for i in range(2, n + 1, 2):
    dp[i][0] = arr[i - 1] + dp[i - 2][0]
dp[1][1] = arr[0]

for i in range(2, n + 1):
    for j in range(1, 4):
        if dp[i - 1][j - 1] == 0 and dp[i - 2][j] == 0:
            continue
        dp[i][j] = max(dp[i - 1][j - 1], dp[i - 2][j]) + arr[i - 1]
        
# for d in dp:
#     print(*d)
        
print(max(dp[n]))