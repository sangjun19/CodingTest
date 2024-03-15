n = int(input())
name = []
for i in range(n):
    a, n = input().split()
    name.append([int(a), n])
#name.sort(key = lambda x : x[0])
for s in sorted(name, key = lambda x : x[0]):
    print(s[0],s[1])