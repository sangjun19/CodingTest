n = int(input())
money = []
coin = [25, 10, 5, 1]
for i in range(n):
    money.append(int(input()))
for i in money:
    for j in coin:
        print(f"{i//j} ",end='')
        i %= j
    print()
