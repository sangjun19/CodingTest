n, k = map(int, input().split())
num = list(map(int, input().split()))
print(sorted(num)[n-k])