a, b, c, d, e, f = map(int, input().split())
small = min(a, d)
while True:
    if small % a == 0 and small % d == 0:
        break
    small += 1
print(small)