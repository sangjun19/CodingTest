n = int(input())
num = [0 for i in range(n)]
for i in range(n):
    a, b = map(int, input().split())
    num[i] = a+b
for i in range(n):
    print(num[i])