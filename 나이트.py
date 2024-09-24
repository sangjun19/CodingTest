def main():
    n = int(input())
    r1, c1, r2, c2 = list(map(int, input().split()))
    arr = [[0] * n for _ in range(n)]
    q = []
    visited = []
    q.append((r1 - 1, c1 - 1))
    while q:
        y, x = q.pop(0)
        value = arr[y][x]
        if y == r2 - 1 and x == c2 - 1:
            print(value)
            return
        for dy, dx in ((-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)):
            ny, nx = y + dy, x + dx
            if 0 <= ny < n and 0 <= nx < n and (ny, nx) not in visited:
                arr[ny][nx] = value + 1
                visited.append((ny, nx))
                q.append((ny, nx))
    print(-1)
    
if __name__ == "__main__":
    main()