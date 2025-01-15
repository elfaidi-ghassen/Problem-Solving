beautiful = set()
k = 1
while True:
    n = (2 ** k - 1) * (2 ** (k - 1))
    if n <= 10**5:
        beautiful.add(n)
    else:
        break
    k += 1
 
 
def beautifulDivisor(n):
    div = [i for i in range(1, n // 2 + 1) if n % i == 0 and i in beautiful]
    if n in beautiful:
        div.append(n)
    return max(div)
 
 
def test():
    n = int(input())
    print(beautifulDivisor(n))
    
test()
