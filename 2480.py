x, y, z = map(int, input().split())
if x == y and y == z: print(10000+1000*x)
elif x != y and y != z and x != z: print(max(x, y, z)*100)
else:
    if x != z: print(1000+100*y)
    else: print(1000+100*x)