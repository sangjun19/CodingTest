dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]


def BFS(r, c):
    # Q를 초기화
    Q = []
    Q.append((r, c))
    dist[r][c] = 1
    # Q에 요소가 존재할때까지만 돌 것(빈 컨테이너가 되면 멈춰버린다)
    while Q:
        curr_r, curr_c = Q.pop(0)
        # 4방향탐색
        for i in range(4):
            nr = curr_r + dr[i]
            nc = curr_c + dc[i]
            # 범위를 벗어나면 다른방향 탐색
            if nr < 0 or nr >= N or nc < 0 or nc >= N: continue
            # 갈 수 없는 자리거나 이미 방문한 경우
            if arr[nr][nc] == 0 or dist[nr][nc] != 0: continue

            Q.append((nr, nc))
            dist[nr][nc] = dist[curr_r][curr_c] + 1


N = int(input())
arr = [list(map(int, input())) for _ in range(N)]  # 행의 길이만큼 만들어준다
dist = [[0]*N for _ in range(N)]
# 입력이 끝났으면 처음 시작 위치 찾기
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1 and dist[i][j] == 0:
            BFS(i, j)

for d in dist: # 이 부분을 프린트해서 찍어봅니다!
    print(*d)

# 7
# 0000011
# 0000000
# 0011100
# 0010111
# 0110010
# 0011100
# 0000000