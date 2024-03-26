n = int(input())
bridge = []
for i in range(n):
    a, b = map(int, input().split())
    bridge.append([a, b])
for b in bridge: #5*4*3/3*2*1 = 10
    sum = 1
    sum2 = 1
    for i in range(b[0]):
        sum *= b[0]
        b[0] -= 1
        sum2 *= b[1]
        b[1] -= 1
    print(sum2//sum)