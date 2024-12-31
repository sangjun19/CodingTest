# i 번째 학생까지 고려했을떄
# j: 축구팀에 이미 선택된 인원
# k: 야구팀에 이미 선택된 인원
n = int(input())
stu = []

for _ in range(n):
    a, b = map(int, input().split())
    stu.append([a, b])

# stu.sort(key=lambda x: (-x[0], -x[1]))

dp = [[[0] * 10 for _ in range(12)] for _ in range(n + 1)]

for i in range(1,  n + 1):
    for j in range(12):
        for k in range(10):
            dp[i][j][k] = dp[i - 1][j][k]
            if j > 0:
                dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j - 1][k] + stu[i - 1][0])
            if k > 0:
                dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j][k - 1] + stu[i - 1][1])

print(dp[n][11][9])