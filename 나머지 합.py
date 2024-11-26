n, m = map(int, input().split())
num = list(map(int, input().split()))
cnt = 0

def dfs(index, sum, depth):
    global cnt
    
    if depth == 0:
        print(sum)
        if sum % m == 0:
            cnt += 1
        return
    if index >= n:
        return
    dfs(index+1, sum+num[i], depth-1)
        
    
for i in range(1, n+1):
    for j in range(n):
        dfs(j, 0, i)
print(cnt)