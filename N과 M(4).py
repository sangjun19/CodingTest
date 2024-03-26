n, m = map(int, input().split())
visited = [0] * (n+1)
list = []

def dfs(num):
    if len(list) == m:
        print(' '.join(map(str, list)))
        return
    for i in range(1, n+1):
        if num > i: continue
        visited[i] = 1
        list.append(i)
        dfs(i)
        list.pop()
        visited[i] = 0
dfs(-1)
