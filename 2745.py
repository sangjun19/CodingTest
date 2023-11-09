N, b = input().split()
ary = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

N = N[::-1] #reverse
result = 0

for i,n in enumerate(N):
    result += (int(b)**i)*(ary.index(n))
print(result)