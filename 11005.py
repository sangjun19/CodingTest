n, b = map(int, input().split())
ary = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
result = []
while n != 0:
    result.append(ary[n%b])
    n //= b
result.reverse()
for s in result:
    print(s,end='')