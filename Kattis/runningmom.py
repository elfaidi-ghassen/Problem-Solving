from collections import deque
import sys, os
if os.path.exists("input.txt"):
    sys.stdin = open("input.txt")

n = int(input())
graph = {}
for _ in range(n):
    src, dest = input().split()
    if src not in graph:
        graph[src] = []
    graph[src].append(dest)

cities = []
while True:
    try:
        city = input()
        cities.append(city)
    except EOFError:
        break
def dfs(node, graph, seen, recursion_stack):
    seen.add(node)
    if node not in graph:
        return False
    recursion_stack.add(node)
    for neighbor in graph[node]:
        if neighbor in seen and neighbor in recursion_stack:
            return True
        if neighbor not in seen:
            result = dfs(neighbor, graph, seen, recursion_stack)
            if result:
                return True
    recursion_stack.remove(node)
    return False


# def dfs(city, graph, seen, recursion_stack):
    # seen.add(city)
    # if city not in graph:
    #     return False
    # recursion_stack.add(city)
    # for neighbor in graph[city]:
    #     if neighbor in seen and neighbor in recursion_stack:
    #         return True
    #     elif neighbor not in seen:
    #         result = dfs(neighbor, graph, recursion_stack, seen)
    #         if result:
    #             return True
    # recursion_stack.remove(city)
    # return False

for city in cities:
    seen = set()
    if dfs(city, graph, seen, set()):
        print(f"{city} safe")
    else:
        print(f"{city} trapped")

