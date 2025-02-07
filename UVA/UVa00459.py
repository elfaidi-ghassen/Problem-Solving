import sys, os
from collections import defaultdict

if os.path.exists("input.txt"):
    sys.stdin = open("input.txt")

t = int(input())
input()

def dfs(v):
    visited.add(v)
    for n in graph[v]:
        if n not in visited:
            dfs(n)

result = []
for _ in range(t):
    graph = defaultdict(list)
    largest = input()
    while True:
        try:
            line = input()
        except:
            break
        if line == "":
            break
        first, second = line
        
        graph[first].append(second)
        graph[second].append(first)
    visited = set()
    counter = 0
    for node in [chr(k) for k in range(65, ord(largest) + 1)]:
        if node not in graph:
            counter += 1
            continue
        if node in visited:
            continue
        counter += 1
        dfs(node)
    result.append(counter)
print("\n\n".join(map(str,result)))