def main():
    n, m = map(int, input().split())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))
    q = []
    visited = []
    q.append((0, 0))
    visited.append((0, 0))
    arr[0][0] = 0
    
    while q:
        y, x = q.pop(0)
        if y == n - 1 and x == m - 1:
            # for a in arr:
            #     print(*a)
            print(arr[y][x])
            return
        for dy, dx in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            ny, nx = y + dy, x + dx
            if 0 <= ny < n and 0 <= nx < m and (ny, nx) not in visited and arr[ny][nx] == 1:
                arr[ny][nx] = arr[y][x] + 1
                visited.append((ny, nx))
                q.append((ny, nx))    
    print(-1)

if __name__ == "__main__":
    main()