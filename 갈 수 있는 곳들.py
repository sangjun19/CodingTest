def main():
    n, k = map(int, input().split())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))
    q = []
    for _ in range(k):
        a, b = map(int, input().split())
        arr[a - 1][b - 1] = 1
        q.append((a - 1, b - 1))
    cnt = 0
    while q:
        y, x = q.pop(0)
        # print(y, x)
        # if arr[y][x] == 1:
        #     continue        
        cnt += 1
        for dy, dx in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            ny, nx = y + dy, x + dx
            if 0 <= ny < n and 0 <= nx < n and arr[ny][nx] == 0:            
                arr[ny][nx] = 1
                q.append((ny, nx))
    print(cnt)
    
if __name__ == "__main__":
    main()