n, m = map(int, input().split())
visited = [0] * (n+1)
list = []

def dfs():
    if len(list) == m:
        print(' '.join(map(str, list)))
        return
    for i in range(1, n+1):
        if visited[i] == 1: continue
        visited[i] = 1
        list.append(i)
        dfs()
        list.pop()
        visited[i] = 0
dfs()
    