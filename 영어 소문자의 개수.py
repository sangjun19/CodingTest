n = int(input())
alpha = map(str, input().split())
alpha = list(alpha)
hash = {}
for s in alpha:
    if s.isupper() or not s.isalpha():
        break
    if s in hash:
        hash[s] += 1
    else:
        hash[s] = 1
        
hash = dict(sorted(hash.items()))
for k, v in hash.items():
    print( k + " : " + str(v))