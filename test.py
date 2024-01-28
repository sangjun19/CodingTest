nums = [1, 2, 2, 3, 3]
answer = []
for n in nums:
    if n in answer:
        answer.remove(n)
    else:
        answer.append(n)
print(answer)

nums = [2, 4, 2, 3, 3]
result = 0
for n in nums:
    result ^= n  # XOR 연산 수행

# XOR 연산을 통해 남은 결과가 중복되지 않는 요소가 됨
print(result)
