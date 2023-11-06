alpha = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
num = input()
time = 0
for n in num:
    for i in range(0,8):
        if n in alpha[i]:
            time+=i+3
print(time)