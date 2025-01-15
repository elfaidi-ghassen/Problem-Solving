def up(nch):
    return "".join(list(map(lambda c : ("0" if c == "9" else str(int(c) + 1)), nch)))
def to_right(nch):
    if len(nch) == 1:
        return nch
    return nch[-1] + nch[:-1]
 
def getCode(nch, n):
    min_num = nch
    for i in range(10):
        nch = up(nch)
        min1 = nch
        nch1 = nch
        for _ in range(n):
            nch1 = to_right(nch1)
            if int(nch1) < int(min1):
                min1 = nch1
        if min1 < min_num:
            min_num = min1
    return min_num
 
 
def test():
    n = int(input())
    nch = input()
    print(getCode(nch, n))
test()
