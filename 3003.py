chess = [1, 1, 2, 2, 2, 8]
num = list(map(int, input().split()))
for i in range(6):
    chess[i] -= num[i]
    print(chess[i],end=' ')