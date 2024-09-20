def main():
    n, m = map(int, input().split())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))
    q = []
    q.append((0, 0))
    while q:
        y, x = q.pop(0)
        if y == n - 1 and x == m - 1:
            print(1)
            return
        for dy, dx in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            ny, nx = y + dy, x + dx
            if 0 <= ny < n and 0 <= nx < m and arr[ny][nx] == 1:
                arr[ny][nx] = 0
                q.append((ny, nx))
    print(0)
        
if __name__ == "__main__":
    main()
    