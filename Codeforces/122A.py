def is_lucky(n):
    while n > 0:
        k = n % 10
        n = n // 10
        if not(k == 4 or k == 7):
            return False
    return True
 
        
 
def almost_lucky(n):
    if is_lucky(n):
        return True
    for i in range(4, n // 2 + 1):
        if n % i == 0 and is_lucky(i):
            return True
    return False
 
 
print("YES" if almost_lucky(int(input())) else "NO")
