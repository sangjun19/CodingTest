n = int(input())
num = 666
cnt = 1
while True:
    if n == cnt:
        print(num)
        break
    num += 1
    s = str(num)
    if "666" in s:
        cnt += 1