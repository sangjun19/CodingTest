people = 0

def dfs(y, x, arr):    
    global people
    people += 1
    arr[y][x] = 0    
    # for a in arr:
    #     print(*a)
    # print()
    for dy, dx in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
        ny, nx = y + dy, x + dx
        if 0 <= ny < len(arr) and 0 <= nx < len(arr[0]):
            if arr[ny][nx] == 1:               
                dfs(ny, nx, arr)
    return 

def main():
    global people
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(list(map(int, input().split())))
    
    cnt = 0
    town = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1:
                people = 0
                dfs(i, j, arr)
                town.append(people)
                cnt += 1
    
    print(cnt)
    town.sort()
    for t in town:
        print(t)
    
    
if __name__ == "__main__":
    main()