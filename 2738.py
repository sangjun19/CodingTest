x, y = map(int, input().split())
num = []
for i in range(x*2):
        num.append(list(map(int, input().split())))
for i in range(x):
    for j in range(y):
        num[i][j] += num[i+x][j]
        print(num[i][j],end=' ')
    print()