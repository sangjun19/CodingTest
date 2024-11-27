# 구현 방법
# 1. 상태 정의
    # DP 배열을 3차원으로 정의:
    # dp[y][x][mask]: (y, x) 위치에서 mask 상태로 도달할 수 있는 경로의 수.
    # mask: 비트마스크로 표현된 아이템 수집 상태.
    # mask = 0110이면 4개의 아이템 중 2번과 3번 아이템을 수집한 상태.
# 2. 초기화
    # 시작점에서 아무 아이템도 수집하지 않은 상태로 시작:
    # dp[0][0][0] = 1
# 3. 점화식
    # 각 위치 (y, x)에서 오른쪽 (0, 1) 또는 아래쪽 (1, 0)으로 이동.
    # 이동하려는 위치 (ny, nx)가:
    # 장애물(wall)에 속해 있으면 스킵.
    # 아이템(item_map) 위치라면, 비트마스크 상태를 업데이트.
    # new_mask = mask | (1 << 아이템의 인덱스)
    # 가능한 경우의 수를 누적:
    # dp[ny][nx][new_mask] += dp[y][x][mask]
# 4. 결과 계산
    # 우측 하단 (n-1, m-1)에서 모든 아이템을 수집한 상태 mask = (1 << a) - 1의 값을 출력:
    # dp[n-1][m-1][(1 << a) - 1] % MOD
# 5. 입력 및 출력
# 입력:
    # 표 크기: n, m
    # 아이템 개수: a, 장애물 개수: b
    # a개의 아이템 위치
    # b개의 장애물 위치
# 출력:
    # 가능한 경로의 수를 
    # 10^9 + 7 로 나눈 나머지.

# dfs로 풀어 시간초과가 발생

# result = 0

# def dfs(y, x, n, m, item, wall, visited, count):
#     global result
#     if y == n - 1 and x == m - 1 and count == len(item):
#         result += 1
#         # print(visited)
#         return
#     for dy, dx in [(0, 1), (1, 0)]:
#         ny, nx = y + dy, x + dx
#         if 0 <= ny < n and 0 <= nx < m and (ny, nx) not in wall and (ny, nx) not in visited:
#             visited.append((ny, nx))
#             if (ny, nx) in item:
#                 dfs(ny, nx, n, m, item, wall, visited, count + 1)
#             else:
#                 dfs(ny, nx, n, m, item, wall, visited, count)
#             visited.pop()

# def main():
#     n, m, r, c = map(int, input().split())
#     item = []
#     wall = []
#     for i in range(r):
#         a, b = map(int, input().split())
#         item.append((a - 1, b - 1))
#     for i in range(c):
#         a, b = map(int, input().split())
#         wall.append((a - 1, b - 1))
#     dfs(0, 0, n, m, item, wall, [], 0)
#     print(result % 1000000007)

# if __name__ == "__main__":
#     main()

def dp(n, m, item, wall):
    ret = [[[0 for _ in range(1 << len(item))] for _ in range(m)] for _ in range(n)]
    ret[0][0][0] = 1
    
    for y in range(n):
        for x in range(m):
            for mask in range(1 << len(item)):
                if ret[y][x][mask] == 0:
                    continue
                for dy, dx in [(0, 1), (1, 0)]:
                    ny, nx = y + dy, x + dx
                    if ny < n and nx < m and (ny, nx) not in wall:
                        new_mask = mask
                        if (ny, nx) in item:
                            new_mask |= 1 << item.index((ny, nx)) # 몇 번째 아이템인지 찾아서 비트마스크로 표현
                        ret[ny][nx][new_mask] += ret[y][x][mask] # 가능한 경우의 수를 누적
                        
    return ret[n - 1][m - 1][(1 << len(item)) - 1] % 1000000007
    
def main():
    n, m, r, c = map(int, input().split())
    item = []
    wall = []
    for i in range(r):
        a, b = map(int, input().split())
        item.append((a - 1, b - 1))
    for i in range(c):
        a, b = map(int, input().split())
        wall.append((a - 1, b - 1))
    print(dp(n, m, item, wall))

if __name__ == "__main__":
    main()