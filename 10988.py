str = input()
check = 1
for i in range(len(str)//2):
    if str[i] != str[len(str)-i-1]:
        check = 0
        break
print(check)