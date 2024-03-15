s = input()
arr = set()
for i in range(len(s)):
    tmp = ""
    for j in range(i, len(s)):
        tmp += s[j]
        arr.add(tmp)
print(len(arr))
