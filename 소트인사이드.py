num = input()
list = []
for n in num:
    list.append(int(n))
list.sort()
list.reverse()
for n in list:
    print(n,end='')