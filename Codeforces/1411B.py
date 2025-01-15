def is_fair(nb):
    k = nb
    while k > 0:
        right = k % 10
        k = k // 10
        if right != 0 and nb % right != 0:
            return False
    return True
 
t = int(input())
for i in range(t):
    n = int(input())
 
    k = n
    while True:
        if is_fair(k):
            print(k)
            break
        k += 1
