number = list(range(1,31))
for i in range(28):
    number.remove(int(input()))
print(min(number))
print(max(number))