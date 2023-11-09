#4, 9,25,81
#2, 3, 5, 9, 17, 33
#0, 1, 2, 3,  4,  5
s = 2
c = 1
n = int(input())
for i in range(n):
    s += c
    c *= 2
print(s*s)