def solution(n, bans):
    answer = ''
    bans.sort()
    cnt = 0
    for word in bans:
        temp = list(word)
        temp.reverse()
        index = 1
        arr = []
        result = 0
        for w in temp:
            result += index*(ord(w)-97)
            index *= 26
        arr.append(result)
        
        if result <= n:
            cnt += 1
    n -= cnt
    while n >= 26:
        answer += chr(n//26 + 97)
        n = n % 26
    
    return answer