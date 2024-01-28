#bfs 활용
def solution(maps):
    n = len(maps)
    m = len(maps[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 동, 남, 서, 북

    queue = []
    queue.append((0, 0, 1))
    maps[0][0] = 0

    while queue:
        y, x, dist = queue.pop(0)

        if y == n - 1 and x == m - 1:
            return dist

        for dx, dy in directions:
            ny, nx = y + dy, x + dx
            if 0 <= ny < n and 0 <= nx < m and maps[ny][nx] == 1:
                queue.append((ny, nx, dist + 1))
                maps[ny][nx] = 0

    return -1 