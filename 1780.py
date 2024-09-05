import sys

# 1. 입력받기 
n = int(input())
paper = []
for i in range(n):
    paper.append(list(map(int,sys.stdin.readline().split())))

# 종이 종류 RESULT 
result = {-1:0, 0:0,1:0}

# 2. 종이의 종류(-1, 0, 1)와 다르면 분할 
def divided(row,col,n):
    curr = paper[row][col] # 종이의 시작 

    for i in range(row, row+n):
        for j in range(col, col+n):
            # 현재 종이 종류와 다르다면 
            if paper[i][j] != curr:
                # 종이 1/3로 분할 (ex. n == 9 , n = 9 -> 3 -> 1 )
                next = n//3
                # 종이를 같은 크기의 종이 9개로 자르므로 
                divided(row, col, next) # 1번째 block (0,0)
                divided(row, col+next, next) # 2번째 block (0,1)
                divided(row, col+(next*2), next) # 3번째 block (0,2)
                divided(row+next, col, next) # 4번째 block (1,0)
                divided(row+next, col+next, next) # 5번째 block (1,1)
                divided(row+next, col+(next*2), next) # 6번째 block (1,2)
                divided(row+(next*2), col, next) # 7번째 block (1,0)
                divided(row+(next*2), col+next, next) # 8번째 block (1,1)
                divided(row+(next*2), col+(next*2), next) # 9번째 block (1,2)
                return 

    # 3. 종이 종류에 따라 count 
    result[curr] +=1 
    return 


divided(0,0,n)

# 4. 결과 return 
for i in result.values():
    print(i)