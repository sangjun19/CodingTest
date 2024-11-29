n = int(input())
dp = [[0 for _ in range(n + 1)] for _ in range(101)]
energy = [0]
happy = [0]
energy += list(map(int, input().split()))
happy += list(map(int, input().split()))

for i in range(1, 101):  # 에너지 범위
    for j in range(1, n + 1):  # 아이템 인덱스
        if energy[j] <= i:  # 현재 아이템을 포함할 수 있는 경우
            dp[i][j] = max(dp[i][j - 1], happy[j] + dp[i - energy[j]][j - 1])
        else:  # 포함할 수 없는 경우
            dp[i][j] = dp[i][j - 1]

print(dp[100][n])  # 최대 체력이 99인 경우의 최적 값 출력
