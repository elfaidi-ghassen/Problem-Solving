import math


def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
primes =  []
for i in range(2, 1000 + 1):
    if is_prime(i):
        primes.append(i)
# print(primes)

def isGoldBach(n):
    for i in range(len(primes) - 1):
        if primes[i] > n:
            return False
        
        if primes[i] + primes[i + 1] == n:
            # print(primes[i], "+", primes[i + 1], "+ 1 =", primes[i] + primes[i + 1] + 1)
            return True
    return False
n, k = list(map(int, input().split()))
count = 0

for m in range(2, n + 1):
    if isGoldBach(m - 1) and m in primes:
        # print(m)
        count += 1

print("YES" if count >= k else "NO")
# print(count)
