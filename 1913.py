#달팽이

n = int(input())
m = int(input())
y, x = 0, 0
num = n*n
dir = [[1, 0],[0, 1],[-1, 0],[0, -1]]
d = 0
cy, cx = 0, 0
map = [[0 for _ in range(n)] for _ in range(n)]

# while num != 0:
#     if num == m:
#         cy, cx = y, x

#     map[y][x] = num
#     num -= 1
#     if y + dir[d][0] < 0 or x + dir[d][1] < 0 or y + dir[d][0] >= n or x + dir[d][1] >= n:
#         d = (d+1)%4        
#     elif map[y + dir[d][0]][x + dir[d][1]] != 0:
#         d = (d+1)%4                
#     y += dir[d][0]
#     x += dir[d][1]
# for i in map:
#     for j in i:
#         print(j, end=' ')
#     print()
# print(cy+1, cx+1)

#다른 풀이

map = [[0 for _ in range(n)] for _ in range(n)]
d = 0
y, x = -1, 0
cy, cx = 0, 0
num = n*n + 1

for i in range(n*2, 1, -1):
    for j in range(i//2):
        y += dir[d][0]
        x += dir[d][1]
        num -= 1
        map[y][x] = num
    d = (d+1)%4
for i in map:
    print(*i)