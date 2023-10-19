str = input()
num = [-1 for _ in range(26)]
for i in range(len(str)):
    if num[ord(str[i])-97]==-1: num[ord(str[i])-97] = i
for n in num:
    print(n,end=' ')