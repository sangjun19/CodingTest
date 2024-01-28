n, m = map(int, input().split())
chess = []
for i in range(n):
    chess.append(input())

answer1 = [[_ for _ in range(m)]for _ in range(n)]
answer2 = [[_ for _ in range(m)]for _ in range(n)]
for i in range(n):
    for j in range(m):
        if i%2 == j%2:
            answer1[i][j] = "B"
            answer2[i][j] = "W"
        else:
            answer1[i][j] = "W"
            answer2[i][j] = "B"
result = []

for i in range(n-7):
    for j in range(m-7):
        check1 = 0
        check2 = 0
        for k in range(i, i+8):
            for l in range(j, j+8):
                if chess[k][l] != answer1[k][l]: check1 += 1
                if chess[k][l] != answer2[k][l]: check2 += 1
        result.append(check1)
        result.append(check2)
             
print(min(result))