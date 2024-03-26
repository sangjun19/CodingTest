def check(c):
    for i in range(c):
        if (chess[c] == chess[i]) or (c-i == abs(chess[c] - chess[i])):
            return False
    return True

def find(d):
    global result
    
    if d == n:
        result += 1
        return
    
    for i in range(n):
        if visited[i] == False:
            chess[d] = i
            
            if check(d):
                visited[i] = True
                find(d + 1)
                visited[i] = False
                

n = int(input())
chess = [0] * n
visited = [False] * n
result = 0

find(0)
print(result)