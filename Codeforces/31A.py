n = int(input())
ls = list(map(int, input().split()))


def solutions():
    for i in range(len(ls)):
        for j in range(len(ls)):
            for k in range(j + 1, len(ls)):
                if i == j or i == k:
                    continue
                if ls[i] == ls[j] + ls[k]:
                    print(i + 1, j + 1, k + 1)
                    return
    print(-1)

solutions()