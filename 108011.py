n, m = map(int, input().split())
num = list(range(1,n+1))
for x in range(m):
    i, j = map(int, input().split()) 
    temp = num.copy()
    for y in range(i-1,j):
        temp[i+j-2-y] = num[y] 
    num = temp.copy()
for n in num:
    print(n,end=' ')