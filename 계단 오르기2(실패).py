n = int(input())
arr = list(map(int, input().split()))
dp = [[0] * 4 for _ in range(n + 1)]
for i in range(2, n + 1, 2):
    dp[i][0] = arr[i - 1]
dp[1][1] = arr[0]

for i in range(2, n + 1):
    for j in range(1, 4):
        dp[i][j] = max(dp[i - 1][j - 1], dp[i - 2][j]) + arr[i - 1]
        
print(max(dp[n]))