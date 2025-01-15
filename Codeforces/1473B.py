def lcm(s, t):
    
    if s == t:
        return s
    x = len(s)
    y = len(t)
    s1 = s
    t1 = t
    x1 = x
    y1 = y
    while x1 != y1:
        if x1 > y1:
            y1 += y
            t1  = t1 + t
        if y1 > x1:
            x1 += x
            s1 = s1 + s
    if s1 == t1:
        return s1
    return -1
            
    
 
def testing():
    n = int(input())
    for _ in range(n):
        s = input()
        t = input()
        print(lcm(s, t))
 
testing()
 
