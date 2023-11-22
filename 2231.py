n = int(input())
b = 0
for i in range(n):
    s = 0
    for j in str(i):
        s += int(j)
    if i + s == n:
        print(i)
        b = 1
        break
if b == 0: print(0)