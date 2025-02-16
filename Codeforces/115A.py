import sys, os
from collections import deque
if os.path.exists("input.txt"):
    sys.stdin = open("input.txt")
    
    
n = int(input())

# graph = [[]] * n
graph = [[] for _ in range(n)]
leaders = []
for i in range(1, n + 1):
    manager = int(input())
    if manager != -1:
        graph[manager - 1].append(i)
    else:
        leaders.append(i)

mx = 0
for leader in leaders:
    to_visit = deque()
    to_visit.append(leader)
    visited = set([leader])
    res = 0
    while to_visit:
        level_length = len(to_visit)
        while level_length > 0:
            n = to_visit.popleft()
            for neighbor in graph[n - 1]:
                if neighbor not in visited:
                    to_visit.append(neighbor)
                    visited.add(neighbor)
            level_length -= 1
        res += 1
    mx = max(mx, res)
    if res > mx:
        mx = res
print(mx)
