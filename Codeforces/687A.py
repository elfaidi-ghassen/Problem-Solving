from collections import deque 
import sys, os 

if os.path.exists("input.txt"): 
    sys.stdin = open("input.txt") 

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = {}
def is_bipatite(graph):
    for node in range(1, n + 1):
        if node in visited:
            continue
        to_visit = deque()
        to_visit.append(node)
        visited[node] = 0
        while to_visit:
            first = to_visit.popleft()
            for node in graph[first]:
                if node in visited:
                    if visited[first] == visited[node]:
                        return False
                else:
                    visited[node] = 1 - visited[first]
                    to_visit.append(node)
    return True

if not is_bipatite(graph):
    print(-1)
else:
    first_group = [node for node in visited if visited[node] == 1]
    second_group = [node for node in visited if visited[node] == 0]
    print(len(first_group))
    print(" ".join(map(str, first_group)))
    print(len(second_group))
    print(" ".join(map(str, second_group)))
