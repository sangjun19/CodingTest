n = int(input())
str = []
for i in range(n):
    str.append(input())
str = list(set(str))
str.sort(key = lambda x : (len(x), x))
for s in str:
    print(s)