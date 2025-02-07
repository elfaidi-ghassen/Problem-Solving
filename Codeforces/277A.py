import sys, os

if os.path.exists("input.txt"):
    sys.stdin = open("input.txt")


def get_neighbors(i):
    neighbors = []
    my_languages = graph[i]
    
    for node_index in range(n):
        if node_index == i:
            continue
        
        their_languages = graph[node_index]
        for l in my_languages:
            if l in their_languages:
                neighbors.append(node_index)
    return neighbors


def bfs(i):
    visited.add(i)
    for node in get_neighbors(i):
        if node not in visited:
            bfs(node)

graph = []
visited = set()
n, m = map(int, input().split())
for _ in range(n):
    _, *languages = map(int, input().split())
    graph.append(languages)

counter = 0
no_language = True
for i in range(n):
    if len(graph[i]) == 0:
        counter += 1
    elif i not in visited:
        bfs(i)
        counter += 1
        no_language = False

if no_language:
    print(counter)
else:
    print(counter - 1)