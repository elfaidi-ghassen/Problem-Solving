# problem from urionlinejudge.com.br

import os, sys

if os.path.exists("input.txt"):
    sys.stdin = open("input.txt")

t = int(input())
already_seen = []

def dfs(starting_node):
        group = [starting_node]
        stack = []
        stack.append(starting_node)
        while stack:
            node = stack.pop()
            neighbors = graph[node] if node in graph else []
            for n in neighbors:
                if n not in already_seen:
                    group.append(n)
                    already_seen.append(n)
        return group

for i in range(t):
    n, m = list(map(int, input().split()))
    print(f"Case #{i + 1}:")
    graph = {}
    for j in range(m):
        n1, n2 = input().split()
        if n1 not in graph:
            graph[n1] = []
        
        if n2 not in graph:
            graph[n2] = []
        
        graph[n1].append(n2)
        graph[n2].append(n1)

    component_groups = []
    
    for char in map(chr, range(97, 97 + n)):
        if char in already_seen:
            continue
        group = dfs(char)
        component_groups.append(group)

    for group in component_groups:
        print(", ".join(sorted(group)) + ",")
    print(len(component_groups), "connected components")
    already_seen.clear()