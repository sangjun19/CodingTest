n, m = map(int, input().split())
num = list(range(1, n+1))
for i in range(m):
    a, b = map(int, input().split())
    a-=1
    b-=1
    temp = num[a]
    num[a] = num[b] 
    num[b] = temp
for i in num:
    print(i,end=' ')