def canChooseOdd(ls, x):
    # x is the number of elements you must choose
    odd = list(filter(lambda x : x % 2 == 1, ls))
    even = list(filter(lambda x : x % 2 == 0, ls))
    while True:
        for i in range(len(odd)):
            sum = 0
            nb = 0  
            
            for j in range(i, len(odd)):
                if nb < x:
                    sum += odd[j]
                    nb += 1
                
                if nb == x:
                    # print("here1")
                    if sum % 2 == 1:
                        return True
                    else:
                        continue
                if sum % 2 == 1:
                    if nb == x:
                        return True
                    other_sum = 0
                    other_nb = 0
                    for k in range(len(even)):
                        sum += even[k]
                        other_sum += even[k]
                        nb += 1
                        other_nb += 1
                        if nb == x:
                            return True
                    sum -= other_sum
                    nb -= other_nb
        return False
def programTest():
    t = int(input()) # between 1 and 100
    for i in range(t):
        n, x = list(map(int, input().split()))
        ls = list(map(int, input().split()))
        print("YES" if canChooseOdd(ls, x) else "NO")
 
programTest()
