def dfs(y, x, fy, fx, arr, visited):
    visited.append((y, x))
    if y == fy and x == fx:
        return 1
    for dy, dx in [[1, 0], [0, 1]]:
        ny, nx = y + dy, x + dx
        if 0 <= ny < fy + 1 and 0 <= nx < fx + 1:
            if arr[ny][nx] == 1 and (ny, nx) not in visited:
                if dfs(ny, nx, fy, fx, arr, visited):
                    return 1
    return 0

def main():
    n, m = map(int, input().split())
    arr = []
    for i in range(n):
        arr.append(list(map(int, input().split())))
    print(dfs(0, 0, n - 1, m - 1, arr, []))
    

if __name__ == "__main__":
    main()