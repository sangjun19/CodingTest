def main():
    n, k = map(int, input().split())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))
    r, c = map(int, input().split())
    r -= 1
    c -= 1
    
    for _ in range(k):
        num = arr[r][c]
        q = []
        visited = []
        q.append((r, c))
        visited.append((r, c))
        max_num = 0
        while q:
            y, x = q.pop(0)     
            # print(y, x)       
            if arr[y][x] >= max_num and arr[y][x] < num:                
                if max_num == arr[y][x]:
                    if y < r:
                        r, c = y, x
                    elif x < c and y == r:
                        r, c = y, x
                else:
                    r, c = y, x
                max_num = arr[y][x]
                
            for dy, dx in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                ny, nx = y + dy, x + dx
                if 0 <= ny < n and 0 <= nx < n and (ny, nx) not in visited and arr[ny][nx] < num:
                    q.append((ny, nx))
                    visited.append((ny, nx))
                            
    print(r + 1, c + 1)
        

if __name__ == "__main__":
    main()