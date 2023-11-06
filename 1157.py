str = input().lower()
alpha = list(set(str))
cnt = []

for i in alpha:
    count = str.count(i)
    cnt.append(count)

if cnt.count(max(cnt)) > 1:
    print("?")
else:
    print(alpha[cnt.index(max(cnt))].upper())