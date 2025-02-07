import sys, os

if os.path.exists("input.txt"):
    sys.stdin = open("input.txt")


def dfs(n):
    to_visit = []
    to_visit.append(n)
    visited[n] = True
    while to_visit:
        k = to_visit.pop()
        for node in graph[k]:
            if not visited[node]:
                visited[node] = True
                to_visit.append(node)


n, m = map(int, input().split())

graph = [[] for _ in range(n)]

visited = [False] * n
for _ in range(m):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)

dfs(0)
non_visited = []
for i in range(n):
    if not visited[i]:
        non_visited.append(i)

if len(non_visited) > 0:
    for n in sorted(non_visited):
        print(n + 1)
else:
    print("Connected")