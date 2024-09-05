import sys
input = sys.stdin.readline


def getMinPossibleLength(string):
    length = len(string)
    pi = [0]*(length)
    j = 0

    for i in range(1, length):
        while j > 0 and string[i] != string[j]:
            j = pi[j - 1]

        if string[i] == string[j]:
            j += 1
            pi[i] = j

    return L - pi[-1]


if __name__ == '__main__':
    L = int(input())
    screen = str(input().rstrip())

    minPossibleLength = getMinPossibleLength(screen)
    print(minPossibleLength)