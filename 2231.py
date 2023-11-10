n = int(input())
s = 0
for i in range(n):
    s = 0
    for j in str(i):
        s += int(j)
    if i + s == n:
        print(i)
        s = 1
        break
if s == 0: print(0)