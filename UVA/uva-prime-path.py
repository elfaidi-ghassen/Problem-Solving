from collections import deque
from math import sqrt
import sys, os
if os.path.exists("input.txt"):
    sys.stdin = open("input.txt")

n = int(input())
all_primes = []

def is_prime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

primes = set()
for i in range(1000,10000):
    if is_prime(i):
        primes.add(i)

def generate_next(n):
    s = str(n)
    def generate_at_index(i, out):
        start = 1 if i == 0 else 0
        for k in range(start, 10):
            if str(k) == s[i]:
                continue
            cpy = int(s[ : i] + str(k) + s[i + 1 : ])
            if cpy in primes:
                out.append(cpy)
    out = []
    generate_at_index(0, out)
    generate_at_index(1, out)
    generate_at_index(2, out)
    generate_at_index(3, out)
    return out

def bfs(start, end):
    to_visit = deque([start])
    visited = set([start])
    count = 0
    while to_visit:
        size = len(to_visit)
        count += 1
        while size > 0:
            head = to_visit.popleft()
            if head == end:
                return count
            for node in generate_next(head):
                if node not in visited:
                    to_visit.append(node)
                    visited.add(node)
            
            size -= 1
    return -1


for _ in range(n):
    start, end = map(int, input().split())
    result = bfs(start, end)
    if result == -1:
        print("Impossible")
    else:
        print(result - 1)