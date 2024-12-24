n = int(input())
arr =[]
for _ in range(n):
    arr.append(int(input()))

maxW = 0

for i in range(n):
    maxW = max(maxW, arr[i] * (n - i))

print(maxW)