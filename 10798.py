str = [input() for _ in range(5)]
for i in range(15):
    for j in range(5):
        if len(str[j])<=i: continue

        print(str[j][i], end='')