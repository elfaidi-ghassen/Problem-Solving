import sys, os
from collections import deque
if os.path.exists("input.txt"):
    sys.stdin = open("input.txt")

n, m = map(int, input().split())
MAX = 10**4
visited = [False] * MAX
to_visit = deque([n])
levels = 0
while to_visit:
    level_size = len(to_visit)
    while level_size > 0:
        node = to_visit.popleft()
        if node == m:
            to_visit.clear()
            break
        
        for neighbor in (node - 1, node * 2):
            if neighbor <= MAX and not visited[neighbor - 1] and neighbor >= 1:
                visited[neighbor - 1] = True
                to_visit.append(neighbor)
        level_size -= 1
    levels += 1

print(levels - 1)