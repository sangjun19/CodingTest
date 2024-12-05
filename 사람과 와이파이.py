n, k = map(int, input().split())
people = set(map(int, input().split()))
people = list(people)
people.sort()
total = 0
dif = []
for i in range(len(people) - 1):
    temp = abs(people[i + 1] - people[i])
    total += temp
    dif.append(temp)
dif.sort()
dif.reverse()
key = min(k - 1, len(dif))
for i in range(key):
    total -= dif[i]
    
print(total)
# 1 3 6 7 9 = 2 + 3 + 1 + 2 = 8