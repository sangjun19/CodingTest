def adjacent(x): 
    for i in range(x):
        if row[x] == row[i] or abs(row[x]-row[i]) == x-i: #가로와 대각선에 겹치는 것이 있나 확인
            return False
    return True

def dfs(x):
    global result

    if x == N: # N개 만큼 확인했을대
        result += 1
        print(row)
    else:
        for i in range(N):
            row[x] = i
            if adjacent(x): # 겹치는게 없으면
                dfs(x+1)



N = int(input())
row = [0] * N
result = 0

dfs(0)
print(result)