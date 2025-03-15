from collections import deque
import sys, os
if os.path.exists("input.txt"):
    sys.stdin = open("input.txt")


def is_bipartite(graph):
    to_visit = deque()
    color = [None] * n
    for i in range(n):
        if color[i] == None:
            color[i] = 0
            to_visit.appendleft(i)
            while to_visit:
                first = to_visit.pop()
                for neighbor in graph[first]:
                    if color[neighbor] == color[first]:
                        return False
                    if color[neighbor] == None:
                        color[neighbor] = 1 - color[first]
                        to_visit.appendleft(neighbor)
    return True

while True:
    n = int(input())
    if n == 0:
        break
    m = int(input())
    graph = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    if is_bipartite(graph):
        print("BICOLORABLE.")
    else:
        print("NOT BICOLORABLE.")
