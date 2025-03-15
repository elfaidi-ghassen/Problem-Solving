from collections import deque 
import sys, os 

if os.path.exists("input.txt"): 
    sys.stdin = open("input.txt") 

t = int(input())

count = [0, 0]
def is_bipartite(start, graph, color, visited):
    count[0] = 1
    count[1] = 0
    color[start] = 0
    to_visit = deque()
    to_visit.appendleft(start)
    visited[start] = True
    is_valid = True
    while to_visit:
        first = to_visit.pop()
        for neighbor in graph[first]:
            if visited[neighbor] and color[first] == color[neighbor]:
                is_valid = False
            if not visited[neighbor]:
                color[neighbor] = 1 - color[first]
                count[color[neighbor]] += 1
                to_visit.appendleft(neighbor)
                visited[neighbor] = True
    return is_valid

for _ in range(t):
    _ = input()
    n = int(input())
    graph = [[] for _ in range(n)]
    for i in range(n):
        nb, *enemies = map(int, input().split())
        if nb == 0:
            continue
        for enemy in enemies:
            if enemy > n:
                continue
            graph[i].append(enemy - 1)
            if i not in graph[enemy - 1]:
                graph[enemy - 1].append(i)

    total = 0
    visited = [False] * n
    for i in range(n):
        if visited[i]:
            continue
        color = [-1] * n
        v = is_bipartite(i, graph, color, visited)
        if v:
            total += max(count[0], count[1])
    print(total)