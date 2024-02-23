n = int(input())
m = int(input())
dir = [[-1, 0],[0, 1],[1, 0],[0, -1]]
s = 1
i = j = n/2
while s != m:
    for i in range(4):
        